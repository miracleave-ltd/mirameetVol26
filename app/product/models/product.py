from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=3, verbose_name='商品コード', primary_key=True, db_index=True)
    name = models.CharField(max_length=100, verbose_name='商品名')
    explanation = models.CharField(max_length=300, verbose_name='商品説明')
    price = models.IntegerField(default=0, verbose_name='商品価格')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')
    create_user = models.CharField(max_length=10, verbose_name='作成者', blank=True, null=True)
    update_user = models.CharField(max_length=10, verbose_name='更新者', blank=True, null=True)