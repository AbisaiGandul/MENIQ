from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = request.POST

        if User.objects.filter(username = form['username']).exists():
            return render(request, 'register.html', {'error_message': 'Ya existe un usuario con este nombre'})
        else:
            new_user = User.objects.create_user(first_name =form['first_name'], last_name=form['last_name'], username= form['username'], email = form['email'], password = form['password'])
            login(request, new_user)
            return redirect('/index/', {'user' : new_user.username})
    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        form = request.POST
        user = authenticate(username = form['username'], password = form['password'])
        if user is not None:
            login(request, user)
            return redirect('/index/', {'user': user.username})
        else:
            return render(request, 'login.html', {'error_message': 'Usuario o contrsena incorrectos'})
    return render(request, 'login.html')

def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            logout(request)
            return redirect('/login/')
        return render(request, 'index.html') 
    return redirect('/login/')