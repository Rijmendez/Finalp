from django.shortcuts import render

# Create your views here.
def Menu(request):
    return render(request, 'page/Menu.html')

def consulta(request):
    return render(request, 'consulta.html')

def producto (request) :
    return render(request, 'producto.html')

def Factura (request) :
    return render(request, 'page/Facturacion.html')