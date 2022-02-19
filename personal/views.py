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
            print(request.session.session_key)
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
            
            print("request.POST['color0']",request.POST.getlist('color')[0])
            print("request.POST['color1']",request.POST.getlist('color')[1])
            image.c1=request.POST.getlist('color')[0]
            image.c2=request.POST.getlist('color')[1]
            image.save()
            return redirect("colorSelect2",imageId)
        else : 
            return render(request,"colorSelect.html",{'imageContents':image,'imageId':imageId})
#colorselct.html이 굳이 여러개여야 할까? 그냥 하나로 하고서 view에서만 여러개 나눠서 조정해주면 되지않나?
def colorSelect2(request,imageId):
    print(imageId)
    image=ImageData.objects.get(id= imageId)

    if image.sessionData != request.session.session_key :
        return render(request,"index.html",{'err':1})
        
    else :
        if request.method == "POST":
            print("request.POST['color0']",request.POST.getlist('color'))
            print("request.POST['color0']",request.POST.getlist('color')[0])
            print("request.POST['color1']",request.POST.getlist('color')[1])
            image.c3=request.POST.getlist('color')[0]
            image.c4=request.POST.getlist('color')[1]
            image.save()
            return redirect("colorSelect3",imageId)
        else : 
            return render(request,"colorSelect.html",{'imageContents':image,'imageId':imageId})

def colorSelect3(request,imageId):
    print(imageId)
    image=ImageData.objects.get(id= imageId)

    if image.sessionData != request.session.session_key :
        return render(request,"index.html",{'err':1})
        
    else :
        if request.method == "POST":
            print("request.POST['color0']",request.POST.getlist('color')[0])
            print("request.POST['color1']",request.POST.getlist('color')[1])
            image.c5=request.POST.getlist('color')[0]
            image.c6=request.POST.getlist('color')[1]
            image.save()
            return redirect("colorSelect4",imageId)
        else : 
            return render(request,"colorSelect.html",{'imageContents':image,'imageId':imageId})

def colorSelect4(request,imageId):
    print(imageId)
    image=ImageData.objects.get(id= imageId)

    if image.sessionData != request.session.session_key :
        return render(request,"index.html",{'err':1})
        
    else :
        if request.method == "POST":
            print("request.POST['color0']",request.POST.getlist('color')[0])
            print("request.POST['color1']",request.POST.getlist('color')[1])
            image.c7=request.POST.getlist('color')[0]
            image.c8=request.POST.getlist('color')[1]
            image.save()
            return redirect("loading",imageId)
        else : 
            return render(request,"colorSelect.html",{'imageContents':image,'imageId':imageId})
'''
def colorSelect(request):
    return render(request, "colorSelect.html")
'''


def loading(request,imageId):
    # 머신러닝 돌리는 중에 loading 창이 떠야 함
    image=ImageData.objects.get(id= imageId)
    rgbList=[]
    rgbResult=[] #머신러닝으로 최종으로 보낼 이중리스트
    rgbList.append(image.c1)
    rgbList.append(image.c2)
    rgbList.append(image.c3)
    rgbList.append(image.c4)
    rgbList.append(image.c5)
    rgbList.append(image.c6)
    rgbList.append(image.c7)
    rgbList.append(image.c8)

    
    for value in rgbList:
        value = value.lstrip('rgb(')
        value = value.rstrip(')')
        #print(i)
        color = value.strip().split(',')
        color_list=[] #각리스트
        for i in color :
            color_list.append(int(i))

        #print(type(color_list[0]))
        print(color_list)
        rgbResult.append(color_list)
        
    print("=========",rgbResult,"==========")
    
    return render(request, "loading.html")

def result(request):
    # 머신러닝에서 받아온 데이터를 여기에 뽑아주기
    return render(request,"result.html")
