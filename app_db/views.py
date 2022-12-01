from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Example

def show(request):
    return(HttpResponse('Hello !'))

def index(request): #priklad jak predavat promenne do html template
    template = loader.get_template('app_db/index.html')
    context = {
        "test" : "LALALA",
        "name" : "Lera"
    }
    return HttpResponse(template.render(context, request))

def index_(request): #druhy zpusob jak rendrovat pouzitim promennych
    template = loader.get_template('app_db/index.html')
    context = {
        "test" : "LALALA",
        "name" : "KAKKAKKA a"
    }
    return render(request, 'app_db/index.html',context)

def db(request):
    #a = Example.objects.create(integer_fielad = 10,char_fiald = 'My name')
    a = Example.objects.get(id = 1)
    return HttpResponse('<h1>Helllo</h1>  {} -- {} '.format(a.integer_fielad, a.char_fiald))



