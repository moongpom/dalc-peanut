from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to="mediaForm/",blank=False,null=False)
    upload_date=models.DateTimeField()
    sessionData = models.CharField(max_length=1000)

class ColorPicker(models.Model):
    #색상선택후 값을 (200,200,200) 형식으로 받아올거라 가정하고 CharField로 필드 생성
    
    #M1. 하지만 [200,200,200] 배열 형식으로 각데이터를 받는다면?
    #M2-1. 또, 만약 선택한 색상들을 getlist로 하나의 리스트로 받아올 수 있다면  필드를 이렇게 많이 만들필요가 있나?
    #   https://citylock77.tistory.com/83
    #M2-2. 아니면 이중배열?
    #M3.ArrayField 고려해보기
    #M4. 이건 폼으로 만들지 말고 하는건?
    c1 = models.CharField(max_length=200)
    c2 = models.CharField(max_length=200)
    c3 = models.CharField(max_length=200)
    c4 = models.CharField(max_length=200)
    c5 = models.CharField(max_length=200)
    c6 = models.CharField(max_length=200)
    c7 = models.CharField(max_length=200)
    c8 = models.CharField(max_length=200)

