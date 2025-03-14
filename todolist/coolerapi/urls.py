from django.urls import path
from . views import (TaskerListCreate,TaskerRetrieveUpdateDelete,
TaskListCreate,TaskRetrieveUpdateDelete)

urlpatterns = [
    #taskers crud
    path('taskers', TaskerListCreate.as_view() , name='tasker-list-create'),
    path('taskers/<int:pk>', TaskerRetrieveUpdateDelete.as_view() , name='tasker-RetrieveUpdateDelete'),
    # task crud
    path('tasks', TaskListCreate.as_view() , name='task-list-create'),
    path('tasks/<int:pk>', TaskRetrieveUpdateDelete.as_view() , name='task-RetrieveUpdateDelete'),
]