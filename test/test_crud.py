from app.database.connection import SessionLocal
from app.database.crud import (
    get_customer_by_id,
    get_order_by_id,
    get_customer_orders
)


def test_crud_operations():
    db = SessionLocal()

    try:
        customer = get_customer_by_id(db, "CUST-101")
        assert customer is not None
        assert customer.name == "Rahul Sharma"

        order = get_order_by_id(db, "ORD-1024")
        assert order is not None
        assert order.product == "Wireless Headphones"

        orders = get_customer_orders(db, "CUST-101")
        assert len(orders) == 2

    finally:
        db.close()