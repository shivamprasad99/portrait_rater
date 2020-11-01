from django.http import HttpResponse
from django.shortcuts import render,redirect
from . forms import *
from . import urls
import os
import time

def portrait_image_view(request):
    for obj in Portrait.objects.all():
        print(obj)
    if request.method == 'POST':
        form = PortraitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            pobj = Portrait.objects.get(name=form.cleaned_data['name'])
            f = open('path.txt','w')
            f.write(pobj.portrait_img.path)
            f.close()
            os.system('python predict.py')
            f = open('result.txt','r')
            mssg = f.read()
            f.close()
            os.remove(pobj.portrait_img.path)
            Portrait.objects.filter(name=form.cleaned_data['name']).delete()
            return HttpResponse(mssg)
            return HttpResponse('fuck')
    else:
        form = PortraitForm()
    return render(request,'index.html',{'form':form})

def success(request):
    return HttpResponse('Successfully uploaded')

