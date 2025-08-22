from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Process
from .serializers import ProcessSerializer

@api_view(['POST'])
def receive_process(request):
    serializer = ProcessSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Data saved"})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def latest_processes(request):
    processes = Process.objects.order_by('-timestamp')[:50]
    serializer = ProcessSerializer(processes, many=True)
    return Response(serializer.data)
