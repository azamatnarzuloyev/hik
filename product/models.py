from django.db import models
from django.utils.text import slugify
import random, string
from django.utils import timezone
from django.urls import reverse
from PIL import Image as image
from io import  BytesIO
from django.core.files.base import ContentFile
import os.path
from ckeditor.fields import RichTextField
from mptt.models import  TreeForeignKey, MPTTModel
# Create your models here.
from django.utils.html import format_html

class Doller(models.Model):
    kurs = models.IntegerField()


def MakeThumb(instance, thubm_size=((400, 400))):
    img = image.open(instance)
    img.thumbnail(thubm_size, image.ANTIALIAS)

    thumb_name, thumb_extension = os.path.splitext(instance.name)
    thumb_extension = thumb_extension.lower()

    thumb_filename = thumb_name + thumb_extension

    if thumb_extension in [".jpg", ".jpeg"]:
        FTYPE = "JPEG"
    elif thumb_extension == ".gif":
        FTYPE = "GIF"
    elif thumb_extension == ".png":
        FTYPE = "PNG"
    else:
        return False  


    temp_thumb = BytesIO()
    img.save(temp_thumb, FTYPE)
    temp_thumb.seek(0)


    data = {
        "name": thumb_filename,
        "content": ContentFile(temp_thumb.read()),
        "save": False,
    }
    temp_thumb.close()

    return data

    return True


class Category(MPTTModel):
    """
    name, @products
    """
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, editable=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    rasm = models.ImageField(upload_to='media/category',null=True, blank=True )
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
    )
    @property
    def product_count(self):
        return self.products.count()

    class MPTTMeta:
        order_insertion_by = ["name"]
        ordering = ['pk', 'name']
    def __str__(self):
        return self.name

    @classmethod
    def make_slug(cls, name):
        slug = slugify(name, allow_unicode=False)
        letters = string.ascii_letters + string.digits

        while cls.objects.filter(slug=slug).exists():
            slug = slugify(
                name + "-" + "".join(random.choices(letters, k=6)), allow_unicode=False
            )
        return slug

    @property
    def products(self):
        return Product.objects.filter(categories=self.pk).all()

    def save(self, *args, **kwargs):
        self.name = self.name.title() if self.name else self.name
        self.slug = self.make_slug(self.name)

        super().save(*args, **kwargs)


class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True, primary_key=True)
    icon = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title() if self.name else self.name
        super().save(*args, **kwargs)
        

class Image(models.Model):
    product = models.ForeignKey(
        "product.Product", models.CASCADE, null=True, related_name="images"
    )
    image = models.ImageField(upload_to="products", blank=False, null=True)

    
class CategoryStatus(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    slug = models.SlugField(unique=True, null=True, editable=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)

   

    class Meta:
        verbose_name_plural = "CategoryStatuses"
        ordering = ["pk", "name"]

    def __str__(self):
        return self.name


    @classmethod
    def make_slug(cls, name):
        slug = slugify(name, allow_unicode=False)
        letters = string.ascii_letters + string.digits

        while cls.objects.filter(slug=slug).exists():
            slug = slugify(
                name + "-" + "".join(random.choices(letters, k=6)), allow_unicode=False
            )
        return slug


    def save(self, *args, **kwargs):
        self.name = self.name.title() if self.name else self.name
        self.slug = self.make_slug(self.name)

        super().save(*args, **kwargs)

class Productallfilter(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "filter"
        ordering = ["pk", "name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(Productallfilter, self).save(*args, **kwargs)


class Product(models.Model):
  
    mgpiksel = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(unique=True, editable=False, null=False, blank=True)
    categories = TreeForeignKey(
        Category,
        related_name='product_category',
        on_delete=models.CASCADE,
    )
    productallfilter = models.ManyToManyField(Productallfilter)
    categorystatuses = models.ManyToManyField(CategoryStatus, blank=True)
    quantit = models.IntegerField(default=1, null=False, blank=True)
    description = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brand, models.CASCADE, blank=True, null=True)
    price = models.IntegerField()
    active = models.BooleanField(default=True)
    available = models.BooleanField(default=True)
    texttitle = RichTextField()
    text = RichTextField()
    

    @property
    def image(self):
        obj = self.images.first()
        if obj and obj.image:
            return obj.image.url
        return None
    def image_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 2px;' src='{}'>".format(self.image))
    @property
    def image_count(self):
        return self.images.all().count()

    @property
    def url(self):
        return reverse("products_detail", kwargs={"slug": self.slug})

    @property
    def has_banner_ad(self):
        if self.banner_ad:
            return True
        return False

    @classmethod
    def make_slug(cls, name):
        slug = slugify(name, allow_unicode=False)
        letters = string.ascii_letters + string.digits

        while cls.objects.filter(slug=slug).exists():
            slug = slugify(
                name + "-" + "".join(random.choices(letters, k=6)), allow_unicode=False
            )
        return slug

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.strip()
        if not self.slug:
            self.slug = self.make_slug(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-pk", "name"]
        




class deal(models.Model):
    product = models.OneToOneField(Product, models.CASCADE, verbose_name="deal")
    start = models.DateTimeField(null=True, blank=True, default=timezone.now)
    end = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class BannerAd(models.Model):
    __original_image_name = None

    def __init__(self, *args, **kwargs):
        super(BannerAd, self).__init__(*args, **kwargs)
        self.__original_image_name = self.image.name

    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.CharField(max_length=200, editable=False)
    product = models.OneToOneField(
        Product, models.CASCADE, null=True, blank=True, related_name="banner_ad"
    )
    active = models.BooleanField(default=True, blank=False, null=False)
    show_prices = models.BooleanField(default=True, blank=False, null=False)
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="banners", blank=False, null=True)
    thumbnail = models.ImageField(
        upload_to="banners/thumbnails/", blank=False, null=True
    )
    description = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.make_slug(self.title)

        if not self.order:
            last_banner = BannerAd.objects.order_by("-order", "title").first()
            if last_banner and last_banner.order:
                self.order = last_banner.order + 1

        image = self.image
        if self.pk:
            self.make_thumbnail(self.pk, self.image)
        else:
            self.thumbnail.save(**MakeThumb(self.image))
        super().save(*args, **kwargs)

    @classmethod
    def make_thumbnail(cls, pk, image):
        instance = cls.objects.get(pk=pk)
        if instance.image != image:
            instance.thumbnail.save(**MakeThumb(instance.image))
        return None

    @classmethod
    def make_slug(cls, name):
        slug = slugify(name, allow_unicode=False)
        letters = string.ascii_letters + string.digits

        while cls.objects.filter(slug=slug).exists():
            slug = slugify(
                name + "-" + "".join(random.choices(letters, k=6)), allow_unicode=False
            )
        return slug

    @property
    def link(self):
        if self.product:
            return self.product.url
        elif self.url:
            return self.url
        return None

    class Meta:
        ordering = ["order", "title"]
