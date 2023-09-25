from django.shortcuts import render
from app.forms import *
from django.core.mail import send_mail

from django.http import HttpResponse

# Create your views here.
def registration(request):
    UFO=UserForm()
    PFO=ProfileForm()
    d={'UFO':UFO,'PFO':PFO}
    if(request.method=='POST' and request.FILES):
        UFDO=UserForm(request.POST)
        PFDO=ProfileForm(request.POST,request.FILES)
        if(UFDO.is_valid() and PFDO.is_valid()):
            MUFDO=UFDO.save(commit=False)
            MUFDO.set_password(UFDO.cleaned_data['password'])
            MUFDO.save()
            MPFDO=PFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            send_mail('registration',
                             'Thank you, you have registered successfully',
                             'vasanthareddya9@gmail.ocm',
                             [MUFDO.email],
                             fail_silently=False)
            return HttpResponse('registration successfully')

    return render(request,'registration.html',d)