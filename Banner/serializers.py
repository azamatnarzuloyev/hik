from rest_framework import serializers
from .models import RasmAdd,RasmImages

class RasmImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = RasmImages
        fields = "__all__"

class RasmAdserializers(serializers.ModelSerializer):
    images = RasmImagesSerializers(required=False, read_only=True, many=True)
    class Meta:
        model= RasmAdd
        fields = (
            'name',
            'images',

        )

