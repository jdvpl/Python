from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    hmtl="""
    <h1>Inicio</h1>
    <p>años hasta el 2050</p>
    <ul>
    """
    year=2021
    while year

    hmtl+="</ul>"
    return HttpResponse(hmtl)
def HolaMundo(request):
    html="""
        <h1> Hola insectos</h1>
        <h3>Hola Soy Juan Daniel Suarez</h3>"""
    return HttpResponse(html)
def Pagina(request):
    html="""
        <h2>Django</h2>
        <p>Creado por Juan Daniel Suarez</p>
    """
    return HttpResponse(html)
