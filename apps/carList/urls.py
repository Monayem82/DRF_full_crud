from django.urls import path,include
from apps.carList import views

urlpatterns = [
    path('',views.carListView),
    path('<int:pk>',views.carDetailsView),
]
