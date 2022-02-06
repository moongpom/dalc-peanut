from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Image
# Create your views here.
def index(request):
    return render(request,"index.html")

def imageUpload(request):
    if request.method == 'POST': 
        image_form = ImageForm(request.POST,request.FILES)
        image_form.save()
        #return redirect("colorPicker",image_form.id)
        return redirect("index")
    else:
        image_form = ImageForm()
        return render(request,'imageUpload.html',{'form':ImageForm})