from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def signup(request):
    return render(request, 'main/signup.html')    

def signin(request):
    return render(request, 'main/signin.html')

def verifycode(request):
    return render(request, 'main/verifycode.html')

def verify(request):
    return redirect('main_index')

def result(request):
    return render(request, 'main/result.html')
