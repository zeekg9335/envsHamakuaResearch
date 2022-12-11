from django.db import models

# Create your models here.
class Hamakua_Data(models.Model):
    basin=models.CharField(max_length=999)
    taxonomicResolution=models.CharField(max_length=100)
    specieCount= models.IntegerField()
    class Meta:
        db_table= 'Hamakua_Data'

class Hamakua_After_Disking(models.Model):
    basin=models.CharField(max_length=999)
    taxonomicResolution=models.CharField(max_length=100)
    specieCount= models.IntegerField()
    class Meta:
        db_table= 'Hamakua_After_Disking'
