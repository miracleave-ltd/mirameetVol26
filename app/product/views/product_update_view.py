from app.product.forms.product_update_forms import ProductUpdateForm
from app.product.models.image import Image
from app.product.models.product import Product
from django.urls import reverse
from django.views.generic import UpdateView


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'product/product_update.html'

    def get_success_url(self):
        return reverse('product:product_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        obj = form.save()
        uploaded_image = Image.objects.filter(product=obj).first()
        if uploaded_image and form.cleaned_data['image']:
            uploaded_image.image = form.cleaned_data['image']
            uploaded_image.save()
        return super().form_valid(form)
