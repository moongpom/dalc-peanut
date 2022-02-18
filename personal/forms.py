from tkinter import Widget
from django import forms
from .models import ImageData
#from .widgets import PreviewFileWidget
class ImageForm(forms.ModelForm): 
    class Meta:  
        model = ImageData
        fields = ['image']

class ColorForm1(forms.ModelForm): 
    class Meta:  
        model = ImageData
        fields = ['c1','c2']
class ColorForm2(forms.ModelForm): 
    class Meta:  
        model = ImageData
        fields = ['c3','c4']
class ColorForm3(forms.ModelForm): 
    class Meta:  
        model = ImageData
        fields = ['c5','c6']
class ColorForm4(forms.ModelForm):
    class Meta:  
        model = ImageData
        fields = ['c7','c8']