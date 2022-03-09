# from email.mime import image
# from tkinter import Image
from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Brand)
admin.site.register(models.Product)
# admin.site.register(Image)