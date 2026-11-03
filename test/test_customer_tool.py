
from app.tools.customer_tool import get_customer_details


def test_valid_customer():
    result = get_customer_details.invoke({
        "customer_id": "CUST-101"
    })

    assert result["success"] is True
    assert result["name"] == "Rahul Sharma"
    assert result["account_status"] == "active"


def test_invalid_customer():
    result = get_customer_details.invoke({
        "customer_id": "CUST-999"
    })

    assert result["success"] is False


def test_tool_metadata():
    assert get_customer_details.name == "get_customer_details"
