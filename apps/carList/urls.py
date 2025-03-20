from django.urls import path,include
from apps.carList import views

urlpatterns = [
    path('',views.carListView),
    path('<int:pk>',views.carDetailsView),
    path('stripe/',views.create_checkout_session,name="create-session-cheakout"),
    path("payment-success/", views.payment_success, name="payment_success"),
]
