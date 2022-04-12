
from rest_framework import serializers
from product.serializers import CategorySerializer, StatuSerializer, CategorySerializerMini
from .models import Children, FIlterProduct

class ChildrenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = 'name'



class FiltermodelSerializers(serializers.ModelSerializer):
    childrens = serializers.SerializerMethodField()
    categories = CategorySerializerMini(read_only=True)
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
        data = [(categoryStatus.slug) for categoryStatus in objects]
        return data
    