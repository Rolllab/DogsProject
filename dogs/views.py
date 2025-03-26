from django.shortcuts import render

from dogs.models import Breed, Dog


def index(request):
    context = {
        'objects_list': Breed.objects.all()[:3],
        'title': 'Питомник - Главная'
    }
    return render(request, 'dogs/index.html', context)


def breeds_list_view(request):
    context = {
        'objects_list': Breed.objects.all(),
        'title': 'Питомник - Все наши породы'
    }
    return render(request, 'dogs/breeds.html', context)


def breed_dogs_list_view(request, pk):
    breed_item = Breed.objects.get(pk=pk)
    context = {
        'objects_list': Dog.objects.filter(breed_id=pk),
        'title': f'Собаки породы - {breed_item.name}',
        'breed_pk': breed_item.pk
    }
    return render(request, 'dogs/dogs.html', context)

def dogs_list_view(request):
    context = {
        'object': Dog.objects.all(),
        'title': 'Питомник - Все наши собаки'
    }
    return render(request, 'dogs/dogs.html', context)
