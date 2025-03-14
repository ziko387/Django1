from rest_framework import generics
from cooler.models import Task ,Taskers
from.serializers import TaskersSerializer,TaskSerializer
# Create your views here.


#crud operations for the taskers
#listening and creating
class TaskerListCreate(generics.ListCreateAPIView):
    queryset = Taskers.objects.all()
    serializer_class = TaskersSerializer


##updating and deleting
class TaskerRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
      queryset = Task.objects.all()
      serializer_class = TaskSerializer

# crud operation for task
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


##updating and deleting
class TaskRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

