import django_filters as filters
from app.product.models.product import Product

class ProductSearchFilter(filters.FilterSet):
    
    class Meta:
        model = Product
        exclude = ['create_at', 'update_at', 'create_user', 'update_user',]
