from langchain_core.tools import tool

from app.database.connection import SessionLocal
from app.database.crud import get_order_by_id


def fetch_order_status(order_id: str, customer_id: str):
    db = SessionLocal()

    try:
        order = get_order_by_id(db, order_id)

        if not order:
            return {
                "success": False,
                "message": "Order not found."
            }

        if order.customer_id != customer_id:
            return {
                "success": False,
                "message": "Unauthorized order access."
            }

        return {
            "success": True,
            "order_id": order.order_id,
            "product": order.product,
            "status": order.status,
            "expected_delivery": (
                order.expected_delivery.isoformat()
                if order.expected_delivery else None
            )
        }

    finally:
        db.close()


@tool
def get_order_status(order_id: str, customer_id: str):
    """
    Retrieve the status and expected delivery date of a customer's order.
    Requires the order ID and authenticated customer ID.
    """
    return fetch_order_status(order_id, customer_id)