from django import forms
from app.product.models.product import Product 


class ProductCreateForm(forms.ModelForm):

    image = forms.ImageField(label='商品画像', required=False)

    class Meta:
        model = Product
        exclude = ['create_at', 'update_at', 'create_user', 'update_user',]