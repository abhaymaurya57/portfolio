
# from dateti  me import datetime
# Create your views here.

# def (request):
#     return render(request,'')
from django.shortcuts import render
from django.http import HttpResponse
from abhay.models import Comment, Contact
import mysql.connector

# Establishing MySQL Connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Admin',
    database='comment'
)

cursor = conn.cursor()


def base(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'about.html')


def skill(request):
    return render(request, 'skill.html')


def signin(request):
    return render(request, 'signin.html')


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, "login.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        whatsapp = request.POST.get('whatsapp')

        try:
            query = "INSERT INTO contact (name, number, email, whatsapp) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, number, email, whatsapp))
            conn.commit()

            # Save using Django ORM
            contact = Contact(name=name, email=email, phone=number, whatsapp=whatsapp)
            contact.save()

            return render(request, 'contact.html', {'yes': "Your message was successfully sent."})
        except mysql.connector.Error as err:
            return HttpResponse(f"Database error: {err}")

    return render(request, 'contact.html')


def comment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')

        try:
            query = "INSERT INTO users (name, number, email, feedback) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, number, email, feedback))
            conn.commit()

            # Save using Django ORM
            comment = Comment(name=name, email=email, phone=number, feedback=feedback)
            comment.save()

            return render(request, 'comment.html', {'com': "Your message was successfully sent."})
        except mysql.connector.Error as err:
            return HttpResponse(f"Database error: {err}")

    return render(request, 'comment.html')


def upload(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        password = request.POST.get('password')

        if not userid or not password:
            return render(request, 'login.html', {'error': 'Both fields are required'})

        try:
            query = "SELECT * FROM login WHERE userid = %s AND password = %s"
            cursor.execute(query, (userid, password))
            user = cursor.fetchone()

            if user:
                cursor.execute("SELECT * FROM contact")
                rows = cursor.fetchall()

                cursor.execute("SELECT * FROM users")
                users = cursor.fetchall()

                return render(request, 'upload.html', {'rows': rows, 'uses': users})
            else:
                return render(request, 'login.html', {'error': 'Invalid userid or password'})

        except mysql.connector.Error as err:
            return HttpResponse(f"Database error: {err}")

    return render(request, 'login.html')
