from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Producto

# Create your views here.
@login_required
def producto(request):
    #select * from productos;
    productos   = Producto.objects.all()

    producto = Producto.objects.get(id=1)

    print(productos)
    context = {
        'productos': productos,
        'usuario': 'Israel',
        'producto1': producto,
        'title': 'Productos::',
    }

    return render(request,"productos.html",context)

def producto_id(request,valor):
    print(valor)
    return render(request,"productos.html",{})