from django.db import models

# Create your models here.
class StudentsModel(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=60)
    smark=models.FloatField()
    saddr=models.CharField(max_length=250)