from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("The price must be 1 or more")
        return value

    def validate_stock_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("The stock quantity must be 1 or more")
        return value
