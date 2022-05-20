
from .models import FIlterProduct
from .serializers import FiltermodelSerializers
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as fil



class filtersproduct(fil.FilterSet):


    class Meta:
        model = FIlterProduct
        fields = ['categories__slug','categorystatuses__name',]
        




class FilterViews(ListAPIView):
    serializer_class =FiltermodelSerializers
    queryset = FIlterProduct.objects.all()
    filter_backends = (fil.DjangoFilterBackend,)
    filterset_class = filtersproduct