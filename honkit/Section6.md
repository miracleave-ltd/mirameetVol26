# batchファイル修正 -問題-

先程のセクションでご説明させていただいた、未実装となっている２つのファイルを修正していただきたいと思います。

- /meetup/app/batch/management/commands/product_data.py
- /meetup/app/batch/batches/product_import.py


また、こちらのバッチでの内容について簡単ですが触れておきたいと思います。

今回修正いただくバッチは、data.csvというcsvファイルに記載してあるデータで商品登録を行うバッチです。

data.csvを覗いてみましょう。

書いてある内容は、１行目には登録するデータのカラム、２・３行目には商品登録時に必要な各カラムのデータになります。

以降の修正が終わった後、バッチ実行後にこちらの内容が登録していることを確認してみましょう。

```
code,name,explanation,price,create_user,update_user
2,orange,mamde in japan,500,999,999
3,computer,mac,5000,999,999
```

## product_data.py（コード修正）

では、まずコードの修正から着手したいと思います。

現在、product_data.pyにはコードが記載されていないため、バッチが起動できません。

以下のコードを反映させて、起動できる状態に修正して下さい。

```python
from django.core.management.base import BaseCommand
from app.batch.bathes.product_import import main


class Command(BaseCommand):

    def handle(self, *args, **options):
        main()
```

これでバッチファイルが起動できるようになりますが、呼び出している処理先の**product_import.py**も修正する必要があります。

そちらに関しては、以下の問題の回答を反映させて修正をして下さい。

## 問題
対象ファイル：product_import.py
### Question１
１．バッチが読み込む対象のファイルを設定してあげましょう。(対象行：L23)

FILE_NAMEの変数に設定するパスをいずれかから１つの組み合わせを選んで下さい。

ヒント：os.path.joinメソッドは引数に渡した文字列を結合することで１つのパスにすることが出来ます。


```python
# example
path = os.path.join('config', 'settings.py')
# path => config/settings.py
```

- ①
> a: 'data', b:'csv'
- ②
> a: '/meetup/csv/', b:'data.csv'
- ③
> a: 'csv', b:'data.csv'

### Question2
２．対象データを処理するためにimportの記述が必要です。(対象行：L8)

必要な記述はどちらでしょうか？

ヒント：登録画面で作成したモデルを使用します。

- ①
> from app.product.models.product import Product
- ②
> from app.product.models.product import Image