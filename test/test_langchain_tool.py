from app.tools.order_tool import get_order_status


def test_tool_metadata():
    assert get_order_status.name == "get_order_status"
    assert "order" in get_order_status.description.lower()


def test_tool_invocation():
    result = get_order_status.invoke({
        "order_id": "ORD-1024",
        "customer_id": "CUST-101"
    })

    assert result["success"] is True
    assert result["status"] == "shipped"