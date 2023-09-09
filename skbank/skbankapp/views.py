from django.contrib import auth, messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def demo(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'Button.html')
        else:
            messages.info(request, "invalid credentials")
            return redirect('skbankapp/login')
    return render(request, "login.html")


def devolep(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if username == "" or password == "":
            messages.error(request, 'Please fill all required fields')
            return redirect('skbankapp/register')
        elif password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect('skbankapp/register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name)
                user.save()
                return redirect('skbankapp/login')
            print("user created")
        else:
            print("password not matching")
            messages.info(request, "password not matching")
            return redirect('skbankapp/register')
        return redirect('/')
    return render(request, "register.html")


def message_form(request):
    messages.success(request, 'Form submission successful')


def logout(request):
    auth.logout(request)
    return redirect('/')
