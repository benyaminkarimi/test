from rest_framework import serializers
from products.models import ProductModel, CategoryModel
import logging
import datetime

logger = logging.getLogger(__name__)

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CategoryModel
        fields="__all__"

class productSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    def create(self, validated_data):
        user =  self.context['request'].user


        categories = validated_data.pop('category')
        product = ProductModel.objects.create(user=user ,**validated_data)

        for category in categories:
            obj, created = CategoryModel.objects.get_or_create(**category)
            product.category.add(obj)
        logger.info(
            f"product created. id: {product.id}" + str(datetime.datetime.now()),
            )
        return product

    class Meta:
        model = ProductModel
        fields = ('id','name', 'description', 'price', 'stock', 'createAt', 'category')
