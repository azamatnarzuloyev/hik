
from django.db import models
from product.models import CategoryStatus, Category
# Create your models here.



class Children(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "productfilter"
        ordering = ["pk", "name"]

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(Children, self).save(*args, **kwargs)

class FIlterProduct(models.Model):
    categories = models.ManyToManyField(Category, blank=True)
    categorystatuses = models.ManyToManyField(CategoryStatus, blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    childrens= models.ManyToManyField(Children)

    def __str__(self):
        return self.name
    



