from django.shortcuts import render, redirect
from .models import Category, Tattoo

# Create your views here.


def gallery(request):

    category = request.GET.get('category')
    if category is None:
        tattoos = Tattoo.objects.all()
    else:
        tattoos = Tattoo.objects.filter(category__name__contains=category)

    categories = Category.objects.all()

    context = {'categories': categories, 'tattoos': tattoos}

    return render(request, 'gallery/gallery.html', context)


def viewTattoo(request, pk):

    tattoo = Tattoo.objects.get(id=pk)

    return render(request, 'gallery/tattoo.html', {'tattoo': tattoo})


def addTattoo(request):

    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        tattoo = Tattoo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )

        return redirect('gallery')

    context = {'categories': categories}

    return render(request, 'gallery/add-tattoo.html', context)
