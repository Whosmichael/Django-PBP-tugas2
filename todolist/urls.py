from django.urls import path
from todolist.views import create_task
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import show_todolist
from todolist.views import update_task
from todolist.views import delete_task
from todolist.views import show_json, get_todolist_json, add_todolist_ajax
from todolist.views import create_task_json   


app_name = 'todolist'

urlpatterns = [  
    path('',show_todolist, name='show_todolist'),
    path('login/',login_user, name='login_user'),
    path('logout/',logout_user, name='logout_user'),
    path('register/',register, name='register'),
    path('create-task/',create_task, name='create_task'),
    path('logout/',logout_user, name='logout_user'),
    path('update-task/<int:id>', update_task, name='update_task'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('json/', show_json, name='show_json'),
    path('add/', create_task_json, name='create_task_json'),
    path('json/', get_todolist_json , name='get_todolist_json'),
    path('add/', add_todolist_ajax , name='add_todolist_ajax'),
]
