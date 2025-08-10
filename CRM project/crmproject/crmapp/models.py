from django.db import models

# Create your models here.
class Customers(models.Model):
    image=models.ImageField(upload_to='pictures/')
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username = models.CharField(max_length=150, null=True, blank=True)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=50)
    address=models.TextField(max_length=100)
    city=models.CharField(max_length=100)
    customer_info=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
