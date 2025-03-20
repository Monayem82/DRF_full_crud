from django.shortcuts import render,redirect
from django.http import JsonResponse

from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from apps.carList.models import CarAll
from apps.carList.serializers import CarAllSerializer

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


stripe.api_key=settings.STRIPE_SECRET_KEY
# Payment with stripe
@csrf_exempt
def create_checkout_session(request):
    if request.method=="POST":
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {'name': 'Test Product'},
                            'unit_amount': 2000,  # 20.00 USD
                        },
                        'quantity': 2,
                    },
                ],
                mode='payment',
                success_url="http://localhost:8000/carlist/payment-success",
                cancel_url="http://localhost:8000/payment-cancel/",
            )
            return redirect(session.url)
        except:
            raise('<h1>Invalid</h1>')
    
    return render(request,'stripe/stripe.html')

def payment_success(request):
    return render(request, "stripe/payment-success.html")



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