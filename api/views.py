from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
@api_view(['GET'])
def apioverview(request):
    api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}


    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all().order_by('-id')
    serilizer = TaskSerializer(tasks, many=True)
    return Response(serilizer.data)


@api_view(['GET'])
def taskdetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serilizer = TaskSerializer(tasks, many=False)
    return Response(serilizer.data)

@api_view(['POST'])
def taskcreate(request):
    serilizer = TaskSerializer(data=request.data)
    
    if serilizer.is_valid():
        serilizer.save()
    return Response(serilizer.data)

@api_view(['POST'])
def taskupdate(request, pk):
    tasks = Task.objects.get(id=pk)
    serilizer = TaskSerializer(instance=tasks, data=request.data)
    
    if serilizer.is_valid():
        serilizer.save()
    return Response(serilizer.data)

@api_view(['DELETE'])
def taskdelete(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return Response('item deleted')