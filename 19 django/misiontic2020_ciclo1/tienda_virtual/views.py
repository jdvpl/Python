from django.shortcuts import render
from . import forms

# Create your views here.
def home(request):
    return render(request, 'tienda_virtual/index.html')

def carrito(request):
    productos = [
        {"nombre":'tarrito de agua','costo':2000,'cantidad':5}
    ]
    parameters = {'productos':  productos}
    return render(request, 'tienda_virtual/carrito_compras.html', parameters)

def historial(request):
    historial = [
        {"nombre":'tarrito de agua','costo':2000,'cantidad':5}

    ]
    parameters = {'historial':  historial}
    return render(request, 'tienda_virtual/historial.html', parameters)

def productos(request):
    frm_agregar = forms.agregar_producto()
    parameters = {'frm_agregar' :  frm_agregar}
    return render(request, 'tienda_virtual/lista_productos.html', parameters)

def pagos(request):
    frm_pago = forms.pagar_carrito()
    parameters = {'frm_pago' :  frm_pago}
    return render(request, 'tienda_virtual/pagar.html', parameters)

