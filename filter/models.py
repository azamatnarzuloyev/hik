from audioop import findfactor
from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField
from product.models import CategoryStatus, Category
# Create your models here.
from mptt.models import  TreeForeignKey


class Children(models.Model):
    name = models.CharField(max_length=50)
  


class FIlterProduct(models.Model):
    categories = TreeForeignKey(
        Category,
        related_name='productcategory',
        on_delete=models.CASCADE,blank=True, null=True
    )
    categorystatuses = models.ManyToManyField(CategoryStatus, blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    childrens= models.ManyToManyField(Children)
    



