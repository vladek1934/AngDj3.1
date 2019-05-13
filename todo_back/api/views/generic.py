from rest_framework import generics
from rest_framework import permissions
from api.models import TaskList
from api.serializers import TaskListSerializer2


class Tasklists(generics.ListCreateAPIView):

    def get_queryset(self):
        return TaskList.objects.filter(created_by=self.request.user)

    def get_serializer_class(self):
        return TaskListSerializer2

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TasklistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TaskListSerializer2
    queryset = TaskList.objects.all()
