from django.shortcuts import render
from django.http import JsonResponse

from apps.carList.models import CarAll

def carListView(request):
    cars=CarAll.objects.all()
    data_result=list(cars.values())
    return JsonResponse(data_result,safe=False)

def carDetailsView(request,pk):
    car=CarAll.objects.get(pk=pk)
    data={
        "name":car.name,
        "describtion":car.describtion
    }
    #data=list(car.values())
    return JsonResponse(data)