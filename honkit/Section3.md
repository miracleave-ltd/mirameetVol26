# アプリケーションコード修正を行う前に

デモアプリの中身について説明します。

## 前提 その1
本日実装いただく以下の登録画面についてですが、現在は登録ボタンを押してもエラーとなり、

動作しない状態となっていますので、正常に動作するように修正いただきつつ、途中ポイントの説明をさせていただきます。

- 商品情報登録画面

## 前提 その2
今回使用するモデルの内容は、それぞれ以下の通りです。

商品名称などを保持、また商品に紐づく画像を保持する2テーブルを準備しております。

>app\product\models\product.py

```python
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

```

>app\product\models\image.py

```python
from django.db import models


class Image(models.Model):
    product = models.ForeignKey('product.product', on_delete=models.SET_NULL, related_name='r_prdct_img', verbose_name='商品情報', blank=True, null=True)
    image = models.ImageField(upload_to='images/', verbose_name='商品画像', blank=True, null=True)
```

- ポイント

  ForeignKeyとは、異なるテーブルに対して設定し「1対多」の親子関係を持たせることの出来るDjangoの機能です。

  今回事前に用意した2テーブルについてもProductを親、Imageを子としてForeignKeyを設定しています。
  
  
  > Productテーブル

  | 商品コード | 商品名     | ・・・ | 
  | ---------- | ---------- | ------ | 
  | 10         | PC         | ・・・ | 
  | 11         | マウス     | ・・・ | 
  | 12         | キーボード | ・・・ | 

  > Imageテーブル

  | ID | **商品情報(ForeignKey)** | 商品画像 |
  | - | - | - |
  | 1 | **10** | 画像1-1 |
  | 2 | **10** | 画像1-2 |
  | 3 | **11** | 画像2 |
  | 4 | **12** | 画像3 |


  ForeignKeyを設定することで、親子テーブル間で以下のようなデータ取得が可能となります。
  
  〇 Image(子)に紐づくProduct(親)の取得
  
  ```python
  image = Image.objects.get(id=1)
  product = image.product
  ```

  〇Product(親)に紐づくImage(子)の取得

  ```python
  product = Product.objects.get(code=10)
  images = product.r_prdct_img.all()
  for image in images:
      # 任意の処理
  ```

  〇Product情報を元にImageの絞り込み

  ```python
  hoge = Product.objects.get(code=10)
  images = Image.objects.filter(product=hoge)
  ```


## 前提 その3
イチからプロジェクトを作成する場合は、以下手順を実施する必要があります。

デモアプリでは実施済みの状態ですので、当手順自体はスキップしてください。

> コマンド

```
django-admin.py startproject config .
```

> コマンド

```
python manage.py startapp app
```

> コマンド

```
cd app
```

> コマンド

```
python ../manage.py startapp product
```

> config\settings.py

```python
import os

# 一部省略

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 一部省略

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

# 一部省略

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'statics')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'
```

> app\product\apps.py

```python
name = 'app.product'
```
