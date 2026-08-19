from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = request.POST
        user = User.objects.create_user(username= form['username'], email = form['email'], password = form['password'])
        return render(request, 'index.html', {'user' : user.username})
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')