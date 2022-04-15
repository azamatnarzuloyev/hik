

from django.shortcuts import  get_object_or_404
from .paginations import CustomPagination
from rest_framework import generics, response, status, views, permissions
from . import serializers
from . import models

from .utils import (

    buildImage,
)
from rest_framework import filters ,pagination
import datetime
from django.core.mail import send_mail
import threading, json
from rest_framework import generics
from django_filters import rest_framework as fil



class ProductFilter(fil.FilterSet):
    min_price = fil.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = fil.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = models.Product
        fields = ['name','categories__slug','brand','categorystatuses__name','productallfilter__name' , 'mgpiksel',]



class DollerViews(generics.ListAPIView):
    serializer_class = serializers.DOllerSerializers
    queryset  = models.Doller.objects.all()


class TopProducts(generics.ListAPIView):
    serializer_class = serializers.ProductListMini
   
    def get_queryset(self):
        queryset = models.Product.objects.filter(available=True).order_by("?")[:20]
        return queryset


class ProductListCreate(generics.ListAPIView):
    serializer_class = serializers.ProductListCreate
    queryset = models.Product.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    lookup_field = "slug"
 
    filter_backends = (fil.DjangoFilterBackend,)
    filterset_class = ProductFilter
    pagination_class = CustomPagination
    # search_fields = ('name', 'categories__name')
    # ordering_fields = ('name', 'categories__name')
   
    
    def get(self, request, *args, **kwargs):
        self.serializer_class = serializers.ProductListMini
        return super().get(request, *args, **kwargs)
      
  


class ProductDetail(generics.RetrieveAPIView):
    serializer_class = serializers.ProductListCreate
    queryset = models.Product.objects.all()
    lookup_field = "slug"
    filter_backends = (fil.DjangoFilterBackend,)
    filterset_class = ProductFilter
    
    
class ProductSearch(generics.ListAPIView):
    serializer_class = serializers.ProductListCreate
    queryset = models.Product.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "categories__slug"]
    lookup_field = "slug"
   



class CategoryListCreate(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.filter(level=0)
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
class CategoryDetail(generics.ListAPIView):
    serializer_class = serializers.CategoryDetailSerializer
    queryset = models.Category.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    lookup_field = ("slug")
    # filter_backends = (fil.DjangoFilterBackend,)
    # filterset_class = ProductFilter
    # ordering = ['pk', 'name']
   

    # def put(self, request, *args, **kwargs):
    #     self.serializer_class = serializers.CategorySerializer
    #     return super().put(request, *args, **kwargs)


class BannerAdListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.BannerAdSerializer

    def perform_create(self, serializer):
        image = self.request.data.get("image", None)
        fileImage = self.request.FILES.get("image", None)

        product = get_object_or_404(
            models.Product, slug=self.request.data.get("product", {}).get("slug")
        )

        if not fileImage and image is not None:
            serializer.save(
                product=product,
                image=buildImage(image, "banner_%s" % self.request.data.get("title")),
            )
        else:
            serializer.save(product=product, image=fileImage)

    def get_queryset(self):
        queryset = models.BannerAd.objects.filter(active=True)

        # if self.request.user.is_authenticated and self.request.user.has_perms:
        #     return queryset.all()
        # return queryset.filter(active=True)


class BannerAdsDetail(generics.RetrieveUpdateDestroyAPIView, BannerAdListCreate):
    lookup_field = "product__slug"
    lookup_url_kwarg = "slug"

    def get(self, request, slug, *args, **kwargs):
        banner_ad = self.get_queryset().filter(product__slug=slug).first()

        product = get_object_or_404(models.Product, slug=slug)

        serialize = serializers.ProductListMini(product)
        serialize.context["request"] = request

        data = {
            **self.get_serializer(banner_ad).data,
            "vacant": False if banner_ad else True,
            "product": serialize.data,
        }

        return response.Response(data=data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        banner = self.queryset.filter(product__slug=self.slug).first()

        if banner:
            return super().update(request, *args, **kwargs)

        return super().create(self, request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        banner = self.get_object()
        image = self.request.data.get("image", None)
        fileImage = self.request.FILES.get("image", None)

        if not fileImage and image is not None:
            banner.image = buildImage(
                image, "banner_%s" % self.request.data.get("title")
            )
            banner.save()

        serializer = self.serializer_class(banner)
        serializer.context["request"] = request

        return super().patch(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.patch(request, *args, **kwargs)


class BannerAdsReOrder(views.APIView):
    queryset = models.BannerAd.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data

        if data and data is not None:
            for i in data:
                banner = models.BannerAd.objects.filter(slug=i.get("slug")).first()
                banner.order = i.get("order")
                banner.save()
        return response.Response(data={"status": "OK"})


class visitorIn(views.APIView):
    permission_classes = [permissions.AllowAny]

    def mail(self):
        date = datetime.datetime.now().strftime("%B %d, %Y %H:%M")
        send_mail(
            "NEW VISITOR",
            "A NEW VISITOR ACCESSED YOUR PAGE on %s" % date,
            from_email="developers@uxinfiniti.com",
            recipient_list=["cephaske254@gmail.com"],
        )

    def post(self, request):
        thread = threading.Thread(target=self.mail)
        thread.run()

        return response.Response(data={"status": "OK"})