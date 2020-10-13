from django.shortcuts import render,HttpResponse

# Create your views here.

def Holamundo(request):
    return HttpResponse("Hola mundo con DJANGO")