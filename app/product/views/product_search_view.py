from app.product.filter.product_search_filter import ProductSearchFilter
from app.product.models.product import Product
from django_filters.views import FilterView


class ProductSearchListView(FilterView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'product/product_search.html'
    filter_class = ProductSearchFilter
    paginate_by = 10

    def get_queryset(self):
        if not self.is_search():
            self.queryset = Product.objects.none()
        return self.queryset

    def is_search(self):
        return 'product_search' in self.request.GET
