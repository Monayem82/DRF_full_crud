from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from apps.carList.models import CarAll
from apps.carList.serializers import CarAllSerializer


#----------------manual way------------
# def carListView(request):
#     # cars=CarAll.objects.all()
#     # data_result=list(cars.values())
#     # return JsonResponse(data_result,safe=False)
#     return 

@api_view(['GET'])
def carListView(request):
    if request.method=="GET":
        cars=CarAll.objects.all()
        serializer=CarAllSerializer(cars,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def carDetailsView(request,pk):
    car=CarAll.objects.get(pk=pk)
    data={
        "name":car.name,
        "describtion":car.describtion
    }
    #data=list(car.values())
    return JsonResponse(data)