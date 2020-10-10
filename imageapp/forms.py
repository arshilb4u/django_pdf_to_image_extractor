from django.forms import ModelForm
from .models import *

class FileData(ModelForm):
    class Meta:
        model=File
        
        fields='__all__'