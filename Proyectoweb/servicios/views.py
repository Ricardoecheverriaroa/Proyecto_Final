from django.shortcuts import render

from servicios.models import servicios

# Create your views here.

def serv(request):
    serv=servicios.objects.all()
    
    return render(request, "servicios/servicios.html", {"serv": serv})