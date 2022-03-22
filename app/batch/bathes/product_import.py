import csv
import os.path
from datetime import datetime as dt
from logging import getLogger, StreamHandler, Formatter, DEBUG, FileHandler
import sqlite3
from contextlib import closing
from config.settings import BASE_DIR
# Question2


# ログ出力設定
logger = getLogger("商品データ登録")
logger.setLevel(DEBUG)

# コンソール出力設定
stream_handler = StreamHandler()
formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# 登録対象csv名

FILE_NAME = os.path.join(BASE_DIR, a, b) # Question1

# DB名
DB_NAME = 'db.sqlite3'


def regist_data():
    # ファイル読み込み（CSV形式）
    try:
        file = FILE_NAME
    except IOError:
        logger.warning('対象ファイルが存在しません：' + FILE_NAME)
        logger.warning('DB登録は行いません：' + FILE_NAME)
        return
    logger.info('=== > Start DB登録 ==')
    with open(file) as f:
        reader = csv.reader(f)
        header = next(reader)  # ヘッダーをスキップ
        for row in reader:
            str_time = [dt.now().strftime('%Y-%m-%d %H:%M:%S')]
            product = Product.objects.filter(code=row[0]).first()
            # 更新フラグ
            flg = False
            if product:
                # 更新項目と差分があれば更新、更新フラグをTrueに設定
                if product.name != row[1]: product.name = row[1]; flg = True
                if product.explanation != row[2]: product.explanation = row[2]; flg = True
                if product.price != int(row[3]): product.price = row[3]; flg = True
                if flg: product.update_at = dt.now(); product.update_user = row[5]
                if not flg: continue
            else:
                product = Product(
                    code=row[0], # 商品コード
                    name=row[1], # 商品名
                    explanation=row[2], # 商品説明
                    price=row[3], # 商品価格
                    create_at=dt.now(), # 作成日時
                    update_at=dt.now(), # 更新日時
                    create_user=row[4], # 登録ユーザー
                    update_user=row[5], # 更新ユーザー
                )
            product.save()
            logger.debug('add_data = ' + str(vars(product)))

    logger.info("=== > End DB登録 ==")


### 実処理（main） ###
def main():
    logger.info('== batch処理開始 ==')

    # DB処理
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, DB_NAME)
    logger.info('base_dir = ' + base_dir)
    logger.info('db_path = ' + db_path)

    # 処理開始
    regist_data()

    logger.info('== batch処理終了 ==')

# main関数を実行
if __name__ == '__main__':
    main()
