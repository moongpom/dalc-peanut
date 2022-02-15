from tkinter import Widget
from django import forms
from .models import ImageData
#from .widgets import PreviewFileWidget
class ImageForm(forms.ModelForm): # 장고에서 제공해주는 forms를 상수로 받아옴 
    class Meta:  
        model = ImageData
        fields = ['image']