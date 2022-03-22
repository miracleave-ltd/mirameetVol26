from django.contrib import admin
from app.product.models.product import Product
from app.product.models.image import Image

admin.site.register(Product)
admin.site.register(Image)
