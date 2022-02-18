from django.db import models

# Create your models here.

class ImageData(models.Model):
    image = models.ImageField(upload_to="mediaForm/",blank=False,null=False)
    upload_date=models.DateTimeField(blank=True,null=True)
    sessionData = models.CharField(max_length=1000)
    c1 = models.CharField(max_length=200,blank=True,null=True)
    c2 = models.CharField(max_length=200,blank=True,null=True)
    c3 = models.CharField(max_length=200,blank=True,null=True)
    c4 = models.CharField(max_length=200,blank=True,null=True)
    c5 = models.CharField(max_length=200,blank=True,null=True)
    c6 = models.CharField(max_length=200,blank=True,null=True)
    c7 = models.CharField(max_length=200,blank=True,null=True)
    c8 = models.CharField(max_length=200,blank=True,null=True)

