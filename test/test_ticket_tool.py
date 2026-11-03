
from app.tools.ticket_tool import create_support_ticket
from app.tools.escalation_tool import escalate_to_human


def test_create_ticket():
    result = create_support_ticket.invoke({
        "customer_id": "CUST-101",
        "issue_type": "delivery_issue",
        "description": "My order has not arrived.",
        "priority": "medium"
    })

    assert result["success"] is True
    assert result["ticket_id"].startswith("TKT-")


def test_ticket_invalid_customer():
    result = create_support_ticket.invoke({
        "customer_id": "CUST-999",
        "issue_type": "delivery_issue",
        "description": "My order has not arrived.",
        "priority": "medium"
    })

    assert result["success"] is False


def test_escalation():
    result = escalate_to_human.invoke({
        "customer_id": "CUST-101",
        "issue_description": "Customer has an unresolved refund issue."
    })

    assert result["success"] is True
    assert result["escalated"] is True
    assert result["priority"] == "high"
