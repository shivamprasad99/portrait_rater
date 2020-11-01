from django.http import HttpResponse
from django.shortcuts import render,redirect
from . forms import *
from . import urls
from . import predict
import os

def portrait_image_view(request):
    for obj in Portrait.objects.all():
        print(obj)
    if request.method == 'POST':
        form = PortraitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            pobj = Portrait.objects.get(name=form.cleaned_data['name'])
            mssg = str(predict.predict_image(pobj.portrait_img.path))
            os.remove(pobj.portrait_img.path)
            Portrait.objects.filter(name=form.cleaned_data['name']).delete()
            return HttpResponse(mssg)
    else:
        form = PortraitForm()
    return render(request,'index.html',{'form':form})

def success(request):
    return HttpResponse('Successfully uploaded')

