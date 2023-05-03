from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}


    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            USO=ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            USO.set_password=pw
            USO.save()


            PFO=pfd.save(commit=False)
            PFO.username=USO
            PFO.save()
            

            

            return HttpResponse('Registration is Successfully completed')
        else:
            return HttpResponse('data is not valid')
    return render(request,'registration.html',d)
