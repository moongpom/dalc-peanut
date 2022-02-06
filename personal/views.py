from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Image
from django.utils import timezone
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
            imgForm.sessionData = request.session
            print("세션확인 --")
            print(imgForm.sessionData)
#만약 model에 있는 필드를 다 담아줬다면  그냥 바로 저장해줘도 됨
            imgForm.save()
            #return redirect("detailPage",book.id)
            return redirect("index")
    else:
        image_form = ImageForm()
        return render(request,'imageUpload.html',{'form':ImageForm})