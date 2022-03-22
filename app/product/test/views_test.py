import pytest
from django import urls
from app.product.models import Product


# テスト実施用に登録するProductモデルをfixtureとして用意
@pytest.fixture
def get_model():
    return Product.objects.create(
        code='1',
        name='テスト用商品',
        explanation='テスト用商品の説明です。',
        price=90000,
        create_at='2021-08-18',
        update_at='2021-08-19',
        create_user='テスト用作成者',
        update_user='テスト用更新者'
    )


@pytest.mark.django_db
@pytest.mark.parametrize('param', [
    {'temp_name': 'product:product_create', 'url': '/product/search/'},
    {'temp_name': 'product:product_detail', 'url': '/product/detail/1'},
    {'temp_name': 'product:product_create', 'url': '/product/create/'},
    {'temp_name': 'product:product_update', 'url': '/product/update/1/'}
])
def test_render_views(client, param, get_model):

    if param['temp_name'] == 'product:product_detail' or \
            param['temp_name'] == 'product:product_update':
        temp_url = urls.reverse(param['temp_name'], args=(1,))
    else:
        temp_url = urls.reverse(param['temp_name'])

    print("\n" + "result:{}".format(temp_url))
    print("expected:{}".format(param['url']) + "\n")
    # 正しいテンプレートを使用しているかテスト
    assert temp_url == param['url']

    response = client.get(temp_url)

    print("result:{}".format(response.status_code))
    print("expected:{}".format(200))
    # 正しいステータスコードかをテスト
    assert response.status_code == 200