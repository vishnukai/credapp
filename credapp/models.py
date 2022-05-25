from django.db import models

# Create your models here.
class productdetails(models.Model):
    pname=models.CharField(max_length=255)
    desc=models.TextField()
    qty=models.IntegerField()
    price=models.IntegerField()
