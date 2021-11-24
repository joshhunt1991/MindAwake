from django.shortcuts import render
from .models import Category, Tattoo

# Create your views here.


def gallery(request):    
    """ renders the index page template """
    categories = Category.objects.all()
    tattoos = Tattoo.objects.all()
    context = {'categories':categories, 'tattoos':tattoos}

    return render(request, 'gallery/gallery.html', context)


def viewTattoo(request, pk):
    """ renders the index page template """

    return render(request, 'gallery/tattoo.html')


def addTattoo(request):
    """ renders the index page template """

    return render(request, 'gallery/add-tattoo.html')
