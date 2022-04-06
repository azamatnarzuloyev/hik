# from email.mime import image
# from tkinter import Image
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models
from .models import Category, CategoryStatus
# Register your models here.

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(models.Brand)
admin.site.register(CategoryStatus)

class GalleryInlines(admin.TabularInline):
    model = models.Image
    max_num = 6

@admin.register(models.Product)
class ProductsModelAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        'image_tag',

      
    ]

    inlines = [
        GalleryInlines
    ]

    # list_editable = [
    #     'available'
    # ]

    # list_filter = [
    #     'available'
    # ]

    search_fields = [
        "name",
       
      
     
    ]

@admin.register(models.Doller)
class DollersModelAdmin(admin.ModelAdmin):
    list_display = [
     'kurs' 
    ]
