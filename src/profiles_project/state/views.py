from django.shortcuts import render
from .models import Task
from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from rest_framework.exceptions import NotAcceptable
# Create your views here.


class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.state == "d":
            raise NotAcceptable("You can't be able to update this object") 

        return super(TaskView, self).update(request, *args, **kwargs)   

 