from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from .forms import FileData
from  imageapp.models import File
from imageapp.functions import handle_uploaded_file  
from pdf2image import convert_from_path
import os


from pdf2image import convert_from_path
import glob,os
import os, subprocess

# Create your views here.
def index(request):
    form=FileData()
    if request.method == 'POST':  
        form = FileData(request.POST, request.FILES)  
        if form.is_valid():
            form.save()  
            
            # return HttpResponse("File uploaded successfuly") 
    context={'form':form}
    return render(request,'imageapp/index.html', context)


def convert_data(request):
    pdf_dir =r"G:\\invoice\\media\\upload\\"  #Enter the path to the uploaded pdf
   
    os.chdir(pdf_dir)

    for pdf_file in glob.glob(os.path.join(pdf_dir, "*.pdf")):
        pages = convert_from_path(pdf_file, 500)
        for page in pages:
            c=1
            page.save(pdf_file[:-4]+str(c)+".jpg", 'JPEG')
            c=c+1
    b=os.listdir(r"G:\\invoice\\media\\upload\\") #accessing the folder in which the images are stored
    d=b[1]
    print(d)

    data={"key": "value", "image":d}
    return JsonResponse(data)  #sending the json response to the ajax call in index.html
