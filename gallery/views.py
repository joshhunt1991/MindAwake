from django.shortcuts import render

# Create your views here.


def gallery(request):
    """ renders the index page template """

    return render(request, 'gallery/gallery.html')
