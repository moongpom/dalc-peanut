from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to="mediaForm/",blank=False,null=False)
