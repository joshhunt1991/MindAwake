from django.shortcuts import render

# Create your views here.


def gallery(request):
    """ renders the index page template """

    return render(request, 'gallery/gallery.html')


def viewTattoo(request, pk):
    """ renders the index page template """

    return render(request, 'gallery/tattoo.html')


def addTattoo(request):
    """ renders the index page template """

    return render(request, 'gallery/add-tattoo.html')
