from django.shortcuts import render

# Create your views here.
def datos_entrega(request):
    return render(request, 'datos_entrega.html' )
