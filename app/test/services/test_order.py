import pytest

from app.test.utils.functions import get_random_string, get_random_price


def test_create_orders_service(create_orders):
    for order in create_orders:
        pytest.assume(order.status.startswith('200'))
        pytest.assume(order.json['_id'])
        pytest.assume(order.json['client_name'])
        pytest.assume(order.json['client_address'])
        pytest.assume(order.json['client_dni'])
        pytest.assume(order.json['client_phone'])

def test_get_orders_service(client, create_orders, order_uri):
    response = client.get(order_uri)
    result_order = {order['_id']: order for order in response.json}
    pytest.assume(response.status.startswith('200'))
    pytest.assume(len(create_orders) == len(result_order))
