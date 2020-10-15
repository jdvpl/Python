from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
layout="""

"""
footer="""

"""
def index(request):
    hmtl="""
    <ul>
    """
    year=2021
    while year <=2050:
        hmtl+=f"<li>{year}</li>"
        year+=1

    hmtl+="</ul>"
    return render(request,'index.html')
def HolaMundo(request):
    return render(request,'hola_mundo.html')
def Pagina(request,redirigir=0):
    if redirigir==1:
        return redirect('contacto',nombre="lucifer",apellido="satanas")
    
    return render(request,'pagina.html')
def contacto(request,nombre="juan",apellido="suarez"):
    html=f"""
        
        
    """
    if nombre and apellido:
        html+=f"<center><h2>Pagina de contacto de {nombre} {apellido}</h2></center>"
    else:
        html+=f"<center><h2>Pagina de contacto</h2></center>"
    html+="<p>Creado por Juan Daniel Suarez</p>"
    return HttpResponse(layout+html+footer)
