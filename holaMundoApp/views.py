from django.shortcuts import render,HttpResponse, redirect
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here controladores.
@login_required
def hola(request):
    return HttpResponse("""
                        <h1>Hola desde otro metodo</h1>
                        <p>Esto es un parrafo desde django</p>
                        """)
def index(request):
    
    context = {
    "nombre": "Julio",
    "apellido": "Palma",
    "flanes": ["flan1", "flan2", "flan3"],
    "title":"HOME::"
    }
    return render(request,"index.html",context)

def acerca(request):
    context = {
        "title":"ABOUT::"
    }
    return render(request,"about.html",context)

def login(request):
    #get -> mostrar el html
    if request.method == "GET":
        gato ={"title":"Login 2"}
        return render(request,"login2.html",gato)
    
    #post ->capturar datos desde el html
    if request.method == "POST":
        print(request.POST)
        print(request.POST["email"])
        print(request.POST["password"])
        email = request.POST["email"]
        password = request.POST["password"]
    
        request.session["email"] = email

        #uso de sesion

        return redirect("/")

@login_required
def registro(request):
    if request.method == "POST":
        username=request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(username,email , password)
        
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]

        user.save()#inserta o actualiza
    return redirect("/login")




