from django.shortcuts import render

# Create your views here.

# def (request):
#     return render(request,'')

def  base(request):
    return render(request,'base.html')

# def  home(request):
#     return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def skill(request):
    return render(request,'skill.html')


def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')

def contact(request):
    return render(request,'contact.html')