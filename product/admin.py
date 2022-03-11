# from email.mime import image
# from tkinter import Image
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from . import models
from .models import Category
# Register your models here.
# admin.site.register(models.Category)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(models.Brand)
admin.site.register(models.Product)
admin.site.register(models.Image)
