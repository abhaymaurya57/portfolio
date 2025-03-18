from django.shortcuts import render
from abhay.models import Comment
from abhay.models import Contact

from django.shortcuts import get_object_or_404
from django.contrib import messages
import mysql.connector
# from dateti  me import datetime
# Create your views here.

# def (request):
#     return render(request,'')
conn=mysql.connector.connect(host="localhost",user="root",password="Admin",database="comment")
# cont=mysql.connector.connect(host="localhost",user="root",password="Admin",database="contact")

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

def login(request):
    return render(request,"login.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')     #data ko la rahe hai html se
        number = request.POST.get('number')
        email = request.POST.get('email')
        whatsapp = request.POST.get('whatsapp')

        
        try:
            cursor = conn.cursor()
            query="insert into contact values('{}','{}','{}','{}')".format(name,number,email,whatsapp)
            cursor.execute(query)
            conn.commit()

            contact = Contact(name=name,email=email,phone=number,whatsapp=whatsapp)    #object
            contact.save()
            
            yes="your messege is succusfuly send"
            return render(request,'contact.html',{'yes': yes})
        except:
            return HttpResponse(f"Database error")
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
        # conn=mysql.connector.connect(host="localhost",user="root",password="Admin",database="comment")
        try:
            cursor = conn.cursor()
            query="insert into users values('{}','{}','{}','{}')".format(name,number,email,feedback)
            cursor.execute(query)
            conn.commit()


            comment = Comment(name=name,email=email,phone=number,feedback=feedback)    #object
            comment.save()

            com="your messege is succusfuly send"
            return render(request,'comment.html',{'com': com})
        except:
            return HttpResponse("error")
    return render(request,'comment.html')



from django.http import HttpResponse
def upload(request): 
    if request.method == 'POST':
        userid = request.POST.get('userid')     #data ko la rahe hai html se
        password = request.POST.get('password')

        if not userid or not password:
            return render(request, 'login.html', {'error': 'Both fields are required'})
        
        try:
            db = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='Admin',
                        database='comment'
                        )
            cur = db.cursor()
            query = "SELECT * FROM login WHERE userid = %s AND password = %s"
            cur.execute(query, (userid, password))
            user = cur.fetchone()

            if user:
                query = "SELECT * FROM comment.contact "
                curso = db.cursor()
                curso.execute(query)
                rows = curso.fetchall()

                query = "SELECT * FROM comment.users"
                cursor = db.cursor()
                cursor.execute(query)
                uses = cursor.fetchall()
                return render(request, 'upload.html', {'rows': rows,'uses':uses})
            else:
                return render(request, 'login.html', {'error': 'Invalid userid or password'})

        except mysql.connector.Error as err:
            return HttpResponse(f"Database error: {err}")
    return render(request, 'login.html')
    
            