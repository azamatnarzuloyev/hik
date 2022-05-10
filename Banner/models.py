
from distutils.command.upload import upload
from django.db import models
from django.utils.html import format_html
# Create your models here.
class RasmAdd(models.Model):
    name = models.CharField(max_length=50)

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

        

class RasmImages(models.Model):
    product = models.ForeignKey(
        "Banner.RasmAdd", models.CASCADE, null=True, related_name="images"
    )
    image = models.ImageField(upload_to="banneradd", blank=False, null=True)