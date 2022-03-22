# batchファイル修正 -回答-

こちらは先程の問題の回答になります。<br>
以下のように修正するとバッチが起動して正常にデータを取り込めるようになります。

修正できたら、以下のコマンドを実行します。
```sh
docker-compose exec web python manage.py product_data
```

修正箇所がすべて解消できていれば、現在以下の内容がターミナルに出力されていると思います。

※日付、登録データの内容は割愛しています。
```text
商品データ登録 - INFO - == batch処理開始 ==
商品データ登録 - INFO - base_dir = /meetup/app/batch/bathes
商品データ登録 - INFO - db_path = /meetup/app/batch/bathes/db.sqlite3
商品データ登録 - INFO - === > Start DB登録 ==
商品データ登録 - DEBUG - add_data = {......}
商品データ登録 - DEBUG - add_data = {......}
商品データ登録 - INFO - === > End DB登録 ==
商品データ登録 - INFO - == batch処理終了 ==
```

## 回答
### Question１
正.③
>django側で設定している、BASE_DIRはプロジェクトルートを指しています。
そのため、os.path.joinメソッドでは、「プロジェクトルート」から対象ファイルまでのパスとして設定します。
```python
FILE_NAME = os.path.join(BASE_DIR, 'csv', 'data.csv')
```

### Question2
正.①
>今回操作するモデルオブジェクトは「Product」のため、必要な記述は①です。
カスタムコマンドにより、Djangoの機能を利用すること出来るため、
従来のDjangoと遜色なくModelオブジェクトを操作することが出来ます。
```python
from app.product.models.product import Product
```
