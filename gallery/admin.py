from django.contrib import admin

# Register your models here.

from .models import Tattoo, Category

admin.site.register(Category)
admin.site.register(Tattoo)
