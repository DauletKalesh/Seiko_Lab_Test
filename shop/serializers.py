from pyexpat import model
from rest_framework import serializers
from shop.models import Categories, Items, Shops

class ItemSerializers(serializers.ModelSerializer):

    class Meta:
        model = Items
        fields = '__all__'

