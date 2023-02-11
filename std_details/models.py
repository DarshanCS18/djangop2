from django.db import models

# Create your models here.
class Studentmd_details(models.Model):
    Std_Id= models.CharField(max_length=260,primary_key= True)
    Name= models.CharField(max_length=260)
    Age= models.PositiveIntegerField()
    Gender= models.CharField(max_length=100)
    Phone= models.PositiveSmallIntegerField()
    Email=models.EmailField()