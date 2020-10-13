from django.shortcuts import render,HttpResponse

# Create your views here.
def HolaMundo(request):
    return HttpResponse("Hola insectos")
