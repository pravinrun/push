
from django.urls import path
from .views import UserListView, TaskListView, AddUserView, AddTaskView, ExportToExcel

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('add_user/', AddUserView.as_view(), name='add_user'),
    path('add_task/', AddTaskView.as_view(), name='add_task'),
    path('export/', ExportToExcel.as_view(), name='export_to_excel'),
]