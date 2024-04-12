from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic import View
from .models import User, Task
from .forms import UserForm, TaskForm
import openpyxl

class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        paginator = Paginator(users, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'user_list.html', {'page_obj': page_obj})
    
class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        paginator = Paginator(tasks, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'task_list.html', {'page_obj': page_obj})

class AddUserView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'add_user.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        return render(request, 'add_user.html', {'form': form})
    
class AddTaskView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'add_task.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, 'add_task.html', {'form': form})

class ExportToExcel(View):
    def get(self, request):
        users = User.objects.all()
        tasks = Task.objects.all()

        wb = openpyxl.Workbook()
        user_sheet = wb.active
        user_sheet.title = 'Users'
        user_sheet.append(['ID', 'Name', 'Email', 'Mobile'])

        for user in users:
            user_sheet.append([user.id,  user.name,  user.email,  user.mobile])

        task_sheet = wb.create_sheet(title='Tasks')
        task_sheet.append(['ID', 'User', 'Task Detail',])
        task_sheet.append(['ID', 'User', 'Task Detail', 'Task Type'])
        for task in tasks:
            task_sheet.append([task.id, task.user.name, task.task_detail, task.task_type])

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=my_data.xlsx'
        wb.save(response)
        return response