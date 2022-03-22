from django.urls import path
from app.product.views.product_update_view import ProductUpdateView
from app.product.views.product_search_view import ProductSearchListView
from django.views.generic import TemplateView
from app.product.views.product_detail_view import ProductDetailView

app_name = 'product'

urlpatterns = [
    path('', TemplateView.as_view(template_name='product/product_top.html'), name='top'),
    path('search/', ProductSearchListView.as_view(), name='product_search'),
    path('create/', TemplateView.as_view(template_name='product/product_create.html'), name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('detail/<str:pk>', ProductDetailView.as_view(), name='product_detail'),
]
