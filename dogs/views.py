from django.shortcuts import render

from dogs.models import Bread, Dog

def index(request):
    context = {
        'object_list': Bread.objects.all()[:3],
        'title': 'Питомник - Главная'
    }
    return render(request, 'dogs/index.html', context)
