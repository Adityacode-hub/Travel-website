from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from account.models import Public
from django .contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
       
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if Public.objects.filter(username=username).exists():
                print('Username taken')
                return render(request, 'register.html', {'error_message': 'Username already taken'})
            elif Public.objects.filter(email=email).exists():
                print('Email taken')
                return render(request, 'register.html', {'error_message': 'Email already taken'})
            else:
                public = Public.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password1  
                )
                public.save()
                print('User registered successfully')
                return redirect('/')  
        else:
            
            return render(request, 'register.html', {'error_message': 'Passwords do not match'})

    # Render the registration form template for GET requests
    return render(request, 'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        public=Public.objects.filter(username=username,password=password)#it will return the queryset matched with the specified attributes
        if len(public)==0:
            loginError="INVALID USERNAME OR PASSWORD"
            res=render(request,'login.html', {'loginError':loginError}) #here we have passed loginerror in the dictionary
        else:
            """login success we want to sustain the data until the logout then we make the session variables"""
            request.session['username']=public[0].username
            request.session['username']=public[0].username
            res=HttpResponseRedirect("")
            return res
    else:
        res=render(request,'login.html')
        return res
