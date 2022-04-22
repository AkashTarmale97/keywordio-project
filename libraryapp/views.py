from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import admin_login
from .models import AddBook
import mysql.connector as sql

# Create your views here.

def registration(request):
    return render(request,'registration.html')
def login(request):
    return render(request,'login.html')   
def dashborad(request):
    return render(request,'dashborad.html')  
def update(request):
    return render(request,'update.html') 
def addbook(request):
    return render(request,'addbook.html') 
def deletebook(request):
    return render(request,'delete.html') 

fname=''
email=''
password=''
# Create your views here.

def signaction(request):
    global fname,email,password
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="root123",database='Lab')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="fname":
                fname=value
            if key=="email":
                email=value
            if key=="password":
                password=value
        
        c="insert into auth Values('{}','{}','{}')".format(fname,email,password)
        cursor.execute(c)
        m.commit()
        #return render(request,"login.html")
    return render(request,'registration.html')
email=''
password=''
# Create your views here.

def loginaction(request):
    global email,password
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="root123",database='Lab')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                email=value
            if key=="password":
                password=value
        
        c="select email,password from auth where email='{}' and password='{}'".format(email,password)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"dashborad.html")

    return render(request,'login.html')


id=""
bn=""
sub=""
aut=""


def addbook(request):
    global id,bn,sub,aut
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="root123",database='Lab')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="id":
                id=value
            if key=="bn":
                bn=value
            if key=="sub":
                sub=value
            if key=="aut":
                aut=value           
       
        c="insert into addbook Values('{}','{}','{}','{}')".format(id,bn,sub,aut)
        cursor.execute(c)
        m.commit()

    return render(request,"addbook.html")

id=""
bn=""
sub=""
aut=""
       
def updatebook(request):
    global id,bn,sub,aut
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="root123",database='Lab')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="id":
                id=value
           
            if key=="bn":
                bn=value
            if key=="sub":
                sub=value
            if key=="aut":
                aut=value
           
        
        c="update addbook set bn='{}',sub='{}',aut='{}' where id='{}'".format(bn,sub,aut,id)
        cursor.execute(c)
        m.commit()


    return render(request,"dashborad.html")







id=""
def deletedata(request):
    global id
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="root123",database='Lab')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="id":
                id=value
        c="delete * from addbook where id='{}'".format(id)
        cursor.execute(c)
        m.commit()
     
    return redirect("dashborad.html") 