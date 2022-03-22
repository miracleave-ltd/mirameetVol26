from app.product.models.product import Product
from django.views.generic import DetailView


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
