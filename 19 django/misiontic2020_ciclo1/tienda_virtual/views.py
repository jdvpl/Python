from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def home(request):
    return render(request, 'tienda_virtual/index.html')

