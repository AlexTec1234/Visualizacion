from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def inicio(request):
    template=loader.get_template('prindex.html')
    #llama y retorna al html para devolver la vitsa
    return HttpResponse(template.render())
def sensores(request):
    template=loader.get_template('sensores.html')
    #llama y retorna al html para devolver la vitsa
    return HttpResponse(template.render())
def menu(request):
    # Aquí puedes agregar lógica adicional si es necesario
    return render(request, 'menu.html', {})
def graficas(request):
    template=loader.get_template('graficas.html')
    #llama y retorna al html para devolver la vitsa
    return HttpResponse(template.render())