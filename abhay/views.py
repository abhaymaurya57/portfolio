from django.shortcuts import render
from abhay.models import Comment
from django.shortcuts import get_object_or_404
from django.contrib import messages
import mysql.connector
# from dateti  me import datetime
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


                           # mysql
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
def comment(request):
    if request.method=='POST':
        name = request.POST.get('name')     #data ko la rahe hai html se
        number = request.POST.get('number')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        # comment = Comment(name=name,email=email,phone=phone,feedback=feedback)    #object
        conn=mysql.connector.connect(host="localhost",user="root",password="Admin",database="comment")

        cursor = conn.cursor()
        query="insert into users values('{}','{}','{}','{}')".format(name,number,email,feedback)
        cursor.execute(query)
        conn.commit()


        comment = Comment(name=name,email=email,phone=number,feedback=feedback)    #object
        comment.save()
    return render(request,'comment.html')
