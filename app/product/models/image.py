from django.db import models


class Image(models.Model):
    product = models.ForeignKey('product.product', on_delete=models.SET_NULL, related_name='r_prdct_img', verbose_name='商品情報', blank=True, null=True)
    image = models.ImageField(upload_to='images/', verbose_name='商品画像', blank=True, null=True)
