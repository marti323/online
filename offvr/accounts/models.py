from django.db import models

# Create your models here.


class Customer(models.Model):
    name=maodels.CharField(max_longth=200,null=True)
    phone=maodels.CharField(max_longth=200,null=True)
    email=maodels.CharField(max_longth=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null= True)
    