
from rest_framework import serializers
from . import models

class StatuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields= "__all__"
    def validate_name(self, data):
        if models.Status.objects.filter(name__iexact=data.strip()).exists():
            raise serializers.ValidationError("This category already exists!")
        return data

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = models.Brand
   



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.CharField(read_only=True)
    children = serializers.SerializerMethodField()
    class Meta:
        depth = 1
        model = models.Category
        fields = ("id",'name','slug','children','rasm', 'product_count')
        read_only = True
    def get_children(self, obj):
        return CategorySerializer(obj.get_children(), many=True).data

    def validate_name(self, data):
        if models.Category.objects.filter(name__iexact=data.strip()).exists():
            raise serializers.ValidationError("This category already exists!")
        return data
 
       


class CategorySerializerMini(CategorySerializer):
    class Meta(CategorySerializer.Meta):
        fields = ['id',"name",'slug']


class ProductListMini(serializers.ModelSerializer):
    categories = CategorySerializerMini(read_only=True)
    image = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

  
 
    class Meta:
        model = models.Product
        fields = (
            "id",
            "name",
            "slug",
            'mgpiksel',
            'status',
            'categories',
            "price",
            "image",
            "image_count",   
        )
    def get_status(self, obj):
        objects = obj.status.all()
        data = [(status.slug) for status in objects]
        return data


        extra_kwargs = {"price": {"read_only": True}}


    def get_image(self, obj):
        host = self.context.get("request")
        image = obj.image
        host_name = host.get_host()

        is_secure = "https://" if host.is_secure() else "http://"

        if image:
            return is_secure + host_name + image
        return None



class ProductDetailSerializerMini(ProductListMini):
    class Meta(ProductListMini.Meta):
        fields = [
            "slug",
            "name",
        ]

class CategoryProductSerializer(serializers.ModelSerializer):
    products = ProductListMini(read_only=True, many=True)
    class Meta:
        model = models.Category
        fields = ("products")


class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductListMini(read_only=True, many=True)
    class Meta:
        model = models.Category
        fields = ("id", "name", "products")



    


class ProductListCreate(serializers.ModelSerializer):
    colors = serializers.JSONField(required=False)
    images = ImageSerializer(required=False, read_only=True, many=True)
    status = serializers.SerializerMethodField(read_only=True)
    brand = BrandSerializer(read_only=True)
    slug = serializers.ReadOnlyField()

    market_price =serializers.IntegerField(read_only=True)
    categories = CategorySerializerMini(read_only=True)
    class Meta:
        model = models.Product
        fields = (
            "id",
            "slug",
            "name",
            'mgpiksel',
            "categories",
            'status',
            "description",
            "brand",
            'market_price',
            "colors",
            "price",
            "available",
            "images",
            'texttitle',
            'text',
        )
        extra_kwargs = {"price": {"read_only": True}}

    # def get_status(self, obj):
    #     objects = obj.status.all()
    #     data = [(status.slug) for status in objects]
    #     return data

class BannerAdSerializer(serializers.ModelSerializer):
    product = ProductListMini(read_only=True)
    """
    Fields:
        title, slug, product, active, url, @link
    """

    class Meta:
        model = models.BannerAd
        fields = [
            "title",
            "slug",
            "product",
            "image",
            "active",
            "show_prices",
            "order",
      
        ]
        extra_kwargs = {
            "image": {"read_only": True},
            "order": {"read_only": True},
         
        }

    def validate(self, data):
        request = self.context.get("request").data
        errors = []
        # if not request.get("image"):
        #     errors.append("Image is required!")
        if not request.get("product"):
            errors.append("Product is required!")
        if errors:
            raise serializers.ValidationError(errors)

        return super().validate(data)

