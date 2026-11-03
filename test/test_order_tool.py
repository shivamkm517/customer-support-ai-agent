
from app.tools.order_tool import get_order_status


def test_valid_order():
    result = get_order_status.invoke({
        "order_id": "ORD-1024",
        "customer_id": "CUST-101"
    })

    assert result["success"] is True
    assert result["status"] == "shipped"


def test_invalid_order():
    result = get_order_status.invoke({
        "order_id": "ORD-9999",
        "customer_id": "CUST-101"
    })

    assert result["success"] is False


def test_unauthorized_order():
    result = get_order_status.invoke({
        "order_id": "ORD-1024",
        "customer_id": "CUST-102"
    })

    assert result["success"] is False
