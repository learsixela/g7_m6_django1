from django.shortcuts import render,HttpResponse, redirect
#from django.http import HttpResponse
# Create your views here controladores.

def hola(request):
    return HttpResponse("""
                        <h1>Hola desde otro metodo</h1>
                        <p>Esto es un parrafo desde django</p>
                        """)
def index(request):
    context = {
    "nombre": "Julio",
    "apellido": "Palma",
    "flanes": ["flan1", "flan2", "flan3"]
    }
    return render(request,"index.html",context)

def login(request):
    #get -> mostrar el html
    if request.method == "GET":
        return render(request,"login.html")
    
    #post ->capturar datos desde el html
    if request.method == "POST":
        print(request.POST)
        print(request.POST["email"])
        print(request.POST["password"])
        email = request.POST["email"]
        password = request.POST["password"]
        #crear un objeto y asignar los valores
        #crear el registro en la base datos
            #objeto.save()
        return redirect("/")



    #http://127.0.0.1:8000/login/?email=a%40a.cl&password=admin1234
