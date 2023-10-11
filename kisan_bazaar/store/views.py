from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def about(request):
    context = {}
    return render(request, 'store/about.html', context)

def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)

def signin(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return render(request, "store/store.html")
        
        else:
            messages.error(request, "Bad credentials")
            return redirect('/signup')

    return render(request, 'store/signin.html', context)

def signup(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, "You have registered successfully!")
        return redirect('/signin')
    return render(request, 'store/signup.html', context)

def signout(request):
    logout(request)
    return redirect('/')