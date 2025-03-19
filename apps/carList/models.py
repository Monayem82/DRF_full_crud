from django.db import models

class CarAll(models.Model):
    name =models.CharField(max_length=50)
    describtion=models.TextField(max_length=250)
    is_active=models.BooleanField(default=False)
    created_to=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
