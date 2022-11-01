from django.contrib import admin
from products.models import ProductModel, CategoryModel



# admin site register
admin.site.register(ProductModel)
admin.site.register(CategoryModel)
