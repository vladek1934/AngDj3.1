from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import Task, TaskList
from api.serializers import TaskSerializer, TaskListSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
def Tasklists(request):
    if IsAuthenticated:
        if request.method == 'GET':
            tasklists = TaskList.objects.all()
            serializer = TaskListSerializer(tasklists, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            serializer = TaskListSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def TasklistDetail(request, pk):
    try:
        tasklist = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskListSerializer(tasklist)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskListSerializer(instance=tasklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        tasklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
