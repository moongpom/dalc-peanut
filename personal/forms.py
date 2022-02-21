
from django import forms
from .models import ImageData
#from .widgets import PreviewFileWidget
class ImageForm(forms.ModelForm): 
    class Meta:  
        model = ImageData
        fields = ['image']
