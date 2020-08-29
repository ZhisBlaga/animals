from django.shortcuts import render
from shelter.models import Animal
from django.template import loader
from django.http.response import HttpResponse
# Create your views here.



def main_page(request):
    template = loader.get_template('shelter/index.html')
    animals = Animal.objects.all()
    data = {
        "title": "Главная",
        "animals": animals,
    }
    return HttpResponse(template.render(data, request))


def about(request):
    template = loader.get_template('shelter/about.html')
    data = {
        "title": "О нас",
        
    }
    return HttpResponse(template.render(data, request))


