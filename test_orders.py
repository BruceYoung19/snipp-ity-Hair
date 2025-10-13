import pytest

def test_order_initialization():
 # GIVEN valid order details
  # WHEN an Order is created
    order = Order(order_id=1, customer_id=101, Hair_id=202, total_cost=150.0, date="2025-09-23")
 # THEN the Order should have the correct attributes
    assert order.order_id == 1
    assert order.customer_id == 101
    assert order.Hair_id == 202
    assert order.total_cost == 150.0
    assert order.date == "2025-09-23"


def test_order_missing_parameters():
    # GIVEN missing date parameter
    # WHEN creating an Order without all required arguments
    # THEN a TypeError should be raised
    with pytest.raises(TypeError):
        Order(order_id=1, customer_id=101, Hair_id=202, total_cost=150.0)  # Missing date
