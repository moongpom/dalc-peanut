from django.shortcuts import render,redirect,get_object_or_404
from .forms import ImageForm
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
            return redirect("colorSelect",imgForm.id)
    else:
        image_form = ImageForm()
        return render(request,'imageUpload.html',{'form':ImageForm})


def colorSelect(request,imageId):
    image = get_object_or_404(ImageData,pk=imageId) 
    print("session확인 image session 정보 : " + image.sessionData + "현재 세션 정보 " +request.session.session_key)
    if image.sessionData != request.session.session_key :

          return render(request,"index.html",{'err':1})
    # # 세가지 숫자 조합 (0~256까지) 이중리스트로 8개 생성  
    # #사진 어케 넘겨줌? \
    colorList=[]
    for _ in range(8):
        line=[]
        for _ in range(3):
            line.append(random.randrange(257) )
        colorList.append(line)
    return render(request,"colorSelect.html",{'imageContents':image})
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
