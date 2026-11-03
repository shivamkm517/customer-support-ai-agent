
from uuid import uuid4

from langchain_core.tools import tool

from app.database.connection import SessionLocal
from app.database.crud import (
    get_customer_by_id,
    create_support_ticket as save_support_ticket
)


def fetch_create_ticket(
    customer_id: str,
    issue_type: str,
    description: str,
    priority: str = "medium"
):
    db = SessionLocal()

    try:
        customer = get_customer_by_id(db, customer_id)

        if not customer:
            return {
                "success": False,
                "message": "Customer not found."
            }

        ticket_id = f"TKT-{uuid4().hex[:8].upper()}"

        ticket = save_support_ticket(
            db=db,
            ticket_id=ticket_id,
            customer_id=customer_id,
            issue_type=issue_type,
            description=description,
            priority=priority
        )

        return {
            "success": True,
            "ticket_id": ticket.ticket_id,
            "status": ticket.status,
            "priority": ticket.priority,
            "message": "Support ticket created successfully."
        }

    finally:
        db.close()


@tool
def create_support_ticket(
    customer_id: str,
    issue_type: str,
    description: str,
    priority: str = "medium"
):
    """
    Create a support ticket for a customer.
    Use this when a customer reports an issue that requires support.
    """
    return fetch_create_ticket(
        customer_id,
        issue_type,
        description,
        priority
    )
