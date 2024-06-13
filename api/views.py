from django.shortcuts import render
from django.http import JsonResponse
import rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import TaskSerializer
from api.models import Task

# Create your views here.
@api_view(['GET'])
def apiOverView(request):

    api_urls = {
        "LOL": 'lol'
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializers = TaskSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Task.objects.get(id=pk)
    serializers = TaskSerializer(instance = tasks, data=request.data)

    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def taskUpdate(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return Response('Item successfully delete')