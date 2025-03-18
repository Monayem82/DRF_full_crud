
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carlist/',include('apps.carList.urls')),
    path('api/',include('apps.api.urls')),
]
