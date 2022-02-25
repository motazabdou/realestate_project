from django.shortcuts import render, redirect

def register(request):
    """ Render register template"""
    return render(request, 'accounts/register.html')


def login(request):
    """ Render login template"""
    return render(request, 'accounts/login.html')


def logout(request):
    """ Redirect to index page"""
    return redirect('index')


def dashboard(request):
    """ Render dashboard template"""
    return render(request, 'accounts/dashboard.html')
