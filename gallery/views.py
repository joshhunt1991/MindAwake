rom django.shortcuts import render

# Create your views here.


def index(request):
    """ renders the index page template """

    return render(request, 'gallery/gallery.html')
