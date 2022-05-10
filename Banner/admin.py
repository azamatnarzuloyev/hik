from django.contrib import admin
from .models import RasmAdd, RasmImages


class GalleryInlines(admin.TabularInline):
    model = RasmImages
    max_num = 10


@admin.register(RasmAdd)
class ProductsModelAdmin(admin.ModelAdmin):
    list_display = [
        "name", 
        'image_tag',

      
    ]

    inlines = [
        GalleryInlines
    ]
   


    search_fields = [
        "name", 
     
    ]