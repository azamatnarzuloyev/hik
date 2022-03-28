# from email.mime import image
# from tkinter import Image
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from product.calculator import Doller
from . import models
from .models import Category, Status
# Register your models here.

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(models.Brand)
admin.site.register(Status)
admin.site.register(Doller)

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


