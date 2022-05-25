
from rest_framework import serializers
from product.serializers import CategorySerializer, StatuSerializer, CategorySerializerMini
from .models import Children, FIlterProduct

class ChildrenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = 'name'



class FiltermodelSerializers(serializers.ModelSerializer):
    childrens = serializers.SerializerMethodField()
    # categories = CategorySerializerMini(read_only=True)
    categories = serializers.SerializerMethodField()
    categorystatuses = serializers.SerializerMethodField()
    class Meta:
        model = FIlterProduct
        fields = ('name','childrens','categories','categorystatuses')
   
    def get_childrens(self, obj):
        objects = obj.childrens.all()
        data = [(children.name) for children in objects]
        return data 

    def get_categorystatuses(self, obj):
        objects = obj.categorystatuses.all()
        data = [(categoryStatus.name) for categoryStatus in objects]
        return data

    def get_categories(self, obj):
        objects = obj.categories.all()
        data = [(categories.slug) for categories in objects]
        return data
      