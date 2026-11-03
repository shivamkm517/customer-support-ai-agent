
from langchain_core.tools import tool

from app.tools.ticket_tool import fetch_create_ticket


@tool
def escalate_to_human(
    customer_id: str,
    issue_description: str
):
    """
    Escalate an unresolved or sensitive customer issue to a human support agent.
    Creates a high-priority support ticket for follow-up.
    """
    result = fetch_create_ticket(
        customer_id=customer_id,
        issue_type="human_escalation",
        description=issue_description,
        priority="high"
    )

    if not result["success"]:
        return result

    return {
        "success": True,
        "escalated": True,
        "ticket_id": result["ticket_id"],
        "priority": "high",
        "message": "Issue escalated for human support."
    }
