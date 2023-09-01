from django.urls import path
from tasks.views import get_list

urlpatterns = [
    path('', get_list, name='list')
]

from django.urls import path
from tasks.views import get_list, create_task, update_task, delete_task

urlpatterns = [
    path('', get_list, name='index'),
    path('create', create_task, name='create'),
    path('update/<int:id>', update_task, name='update'),
    path('delete/<int:id>', delete_task, name='delete')
]