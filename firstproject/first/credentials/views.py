from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        U=request.POST['username']
        P=request.POST['password']
        U=auth.authenticate(username=U,password=P)
        if U is not None:
            auth.login(request,U)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,'login.html')



def register(request):
    if request.method=='POST':
        userid=request.POST['username']
        fname=request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email_id']
        pa1 = request.POST['password']
        pa2 = request.POST['password1']
        if pa1==pa2:
            if User.objects.filter(username=userid).exists():
                messages.info(request,'user name already exist')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email id already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=userid, first_name=fname, last_name=lname, email=email,
                                                password=pa1)
                user.save();
                return redirect('login')
                print("user created")
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


