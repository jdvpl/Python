from django.shortcuts import render,HttpResponse

# Create your views here.
layout="""
<h2>Sitio web con Django | Juan Daniel Suarez</h2>
<hr/>

<ul>
    <li><a href="/">Inicio</a></li>
    <li><a href="/hola-mundo">Hola Mundo</a></li>
    <li><a href="/pagina-prueba">Pagina</a></li>
    <li><a href="/contacto">Contacto</a></li>
</ul>
<hr/>
"""
footer="""
<hr/>
<center><h2>Contacto</h2></center>
<hr/>
<b>Nombre: </b> <p>Juan Daniel Suarez</p>
<b>Telefono: </b> <p>3209188638</p>
<b>Email: </b> <p>juanda554242@gmail.com</p>
"""
def index(request):
    hmtl="""
    <h1>Inicio</h1>
    <p>años hasta el 2050</p>
    <ul>
    """
    year=2021
    while year <=2050:
        hmtl+=f"<li>{year}</li>"
        year+=1

    hmtl+="</ul>"
    return HttpResponse(layout+hmtl+footer)
def HolaMundo(request):
    html="""
        <h1> Hola insectos</h1>
        <h3>Hola Soy Juan Daniel Suarez</h3>"""
    return HttpResponse(layout+html+footer)
def Pagina(request):
    html="""
        <h2>Django</h2>
        <p>Creado por Juan Daniel Suarez</p>
    """
    return HttpResponse(layout+html+footer)
def contacto(request,nombre="juan",apellido="suarez"):
    html=f"""
        
        
    """
    if nombre and apellido:
        html+=f"<center><h2>Pagina de contacto de {nombre} {apellido}</h2></center>"
    else:
        html+=f"<center><h2>Pagina de contacto</h2></center>"
    html+="<p>Creado por Juan Daniel Suarez</p>"
    return HttpResponse(layout+html+footer)
