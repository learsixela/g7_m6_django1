from django.shortcuts import render, HttpResponse

# Create your views here.
def mascotas(request):
    return HttpResponse("""
            <h2>Esto es mi mascota</h2>
            <p>mis mascotas son 3 perritos</p>
            <img src="" alt="Zoe">
            <img src="" alt="Ayun">
            <img src="" alt="Negrito">
                        """)

def mascotas2(request):
    return render(request,"index.html")