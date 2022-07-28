from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.cache import cache_control
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    return render(request,'landing.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.method == 'POST':
       email = request.POST['email']
       password = request.POST['pass']
       print(email,password)
       if email=="" or password == "":
           print("fail1")
           return JsonResponse(
               {'success':False
               },
               safe=False
           )
    
    return render(request,'login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        sname = request.POST.get('secondname')
        phone = request.POST.get('phone')
        email =  request.POST.get('email')
        password =  request.POST.get('password1')
        print("first name-"+fname)
        print("second name -"+sname)
        print("Phone-"+str(phone))
        print("email-"+email)
        print("password-"+password)
    
    return render(request,'register.html')