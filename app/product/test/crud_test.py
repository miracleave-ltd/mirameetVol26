from app.product.test.conftest import cursor


# insertのテスト
def test_create(cursor):
    insert_query = "insert into product_product values('99','テストプラン','これはテストプランです', '99999', '2021-08-18','2021-08-19','createuser','updateuser');"
    cursor.execute(insert_query)

    # 件数確認
    counts_query = "select count(1) from product_product where code = 99;"
    cursor.execute(counts_query)
    result = cursor.fetchone()[0]
    # 1件のデータを入れたため1件の結果を想定
    expected = 2

    print("result:{}".format(result))
    print("expected:{}".format(expected))
    assert result == expected

# selectのテスト
def test_read(cursor):
    # 1件のデータを挿入
    insert_query = "insert into product_product values('99','テストプラン','これはテストプランです', '99999', '2021-08-18','2021-08-19','createuser','updateuser');"
    cursor.execute(insert_query)

    # データ取得
    select_query = "select * from product_product where code = 99;"
    cursor.execute(select_query)
    result = cursor.fetchall()

    expected = [('99','テストプラン','これはテストプランです', 99999, '2021-08-18','2021-08-19','createuser','updateuser')]  # insertの入力と同じデータが入っている確認

    print("result:{}".format(result))
    print("expected:{}".format(expected))
    assert result == expected

# updateのテスト
def test_update(cursor):
    # 1件のデータを挿入
    insert_query = "insert into product_product values('99','テストプラン','これはテストプランです', '99999', '2021-08-18','2021-08-19','createuser','updateuser');"
    cursor.execute(insert_query)
    # code=99のnameをtest99に変更する
    update_query = "update product_product set name = 'test99' where code = 99;"
    cursor.execute(update_query)

    # データ取得
    select_query = "select name from product_product where code = 99;"
    cursor.execute(select_query)
    result = cursor.fetchone()[0]

    expected = 'test99' # code=99のnameがtest99になっていることを確認

    print("result:{}".format(result))
    print("expected:{}".format(expected))
    assert result != expected