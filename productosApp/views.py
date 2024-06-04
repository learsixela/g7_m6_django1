from django.shortcuts import render
from .models import Producto

# Create your views here.
def producto(request):
    #select * from productos;
    productos   = Producto.objects.all()

    producto = Producto.objects.get(id=1)

    print(productos)
    context = {
        'productos': productos,
        'usuario': 'Israel',
        'producto1': producto
    }

    return render(request,"productos.html",context)

def producto_id(request,valor):
    print(valor)
    return render(request,"productos.html",{})