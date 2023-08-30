from django.urls import path
from tasks.views import get_list

urlpatterns = [
    path('', get_list, name='list')
]