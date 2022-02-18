from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import ImageData
from django.utils import timezone
import random
# Create your views here.
def index(request):

    return render(request,"index.html")

def imageUpload(request):
    print("진행1 --")
    if request.method == 'POST': 
        image_form = ImageForm(request.POST,request.FILES)
        print("진행2 --")
        if image_form.is_valid():
            imgForm = image_form.save(commit = False)
            imgForm.upload_date = timezone.now() 
            imgForm.sessionData = request.session.session_key
            print("세션확인 --")
            print(imgForm.sessionData)
            #만약 model에 있는 필드를 다 담아줬다면  그냥 바로 저장해줘도 됨
            imgForm.save()
            return redirect("colorSelect1",imgForm.id)
    else:
        image_form = ImageForm()
        return render(request,'imageUpload.html',{'form':image_form})

def colorSelect1(request,imageId):
    print(imageId)
    image=ImageData.objects.get(id= imageId)

    if image.sessionData != request.session.session_key :
        return render(request,"index.html",{'err':1})
        
    else :
        if request.method == "POST":
            print("request.POST['color0']",request.POST.getlist('color'))
            print("request.POST['color1']",request.POST.getlist('color'))
            image.c1=request.POST['color']
            image.c2=request.POST['color']
            image.save()
            return redirect("colorSelect2",imageId)
        else : 
            return render(request,"colorSelect1.html",{'imageContents':image,'imageId':imageId})
       

def colorSelect2(request,imageId):
    print(imageId)
    image=ImageData.objects.get(id= imageId)
    color_form=ColorForm1(instance=image)
    print("이거 이상핮ㄴ데? ",color_form)

    if image.sessionData != request.session.session_key :
        return render(request,"index.html",{'err':1})
        
    else :
        if request.method == "POST":
            color_form = ColorForm1(request.POST, instance = image)
            print("제발조 ㅁ돼라 --")
            color_form.save()
            return redirect("colorSelect3",imageId)
        else : return render(request,"colorSelect2.html",{'imageContents':image,'form':color_form,'imageId':imageId}) 
    
def colorSelect3(request,imageId):
    print(imageId)
    image = get_object_or_404(ImageData,pk=imageId) 
    print("session확인 image session 정보 : " + image.sessionData + "현재 세션 정보 " +request.session.session_key)
    if request.method == 'GET': 
        print("진행2 --")
       
        color_form = ColorForm2(instance=image)
        print("진행3 --")
        if image.sessionData != request.session.session_key :
            print("진행4 --")
            return render(request,"index.html",{'err':1})
        
        else :
            print("진행5 --")
            return render(request,"colorSelect2.html",{'imageContents':image,'form':color_form,'imageId':imageId})
       
    else : 
        
        color_form = ColorForm1(request.POST,request.FILES)
        print("진행1 --")
        color_form.save()
        return redirect("colorSelect3",imageId)

'''
def colorSelect(request):
    return render(request, "colorSelect.html")
'''


def loading(request):
    # 머신러닝 돌리는 중에 loading 창이 떠야 함
    return render(request, "loading.html")

def result(request):
    # 머신러닝에서 받아온 데이터를 여기에 뽑아주기
    return render(request,"result.html")
