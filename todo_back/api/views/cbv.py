from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Task, TaskList
from api.serializers import TaskSerializer, TaskListSerializer
from rest_framework.permissions import IsAuthenticated


class Tasklists(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        tasklists = TaskList.objects.all()
        serializer = TaskListSerializer(tasklists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TasklistDetail(APIView):

    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        tasklist = self.get_object(pk)
        serializer = TaskListSerializer(tasklist)
        return Response(serializer.data)

    def put(self, request, pk):
        tasklist = self.get_object(pk)
        serializer = TaskListSerializer(instance=tasklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        tasklist = self.get_object(pk)
        tasklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Tasks(APIView):
    def get_tasklist(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        tasklist = self.get_tasklist(pk)
        result = []
        tasks = Task.objects.all()
        for task in tasks:
            if tasklist == task.task_list:
                result.append(task)
        serializer = TaskSerializer(result, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        tasklist = self.get_tasklist(pk)
        request.data[4] = tasklist
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskDetail(APIView):

    def get_task(self, pk):
        try:
            return Task.objects.get(id=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_task(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_task(pk)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        task = self.get_task(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
