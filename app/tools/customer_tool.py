
from langchain_core.tools import tool

from app.database.connection import SessionLocal
from app.database.crud import get_customer_by_id


def fetch_customer_details(customer_id: str):
    db = SessionLocal()

    try:
        customer = get_customer_by_id(db, customer_id)

        if not customer:
            return {
                "success": False,
                "message": "Customer not found."
            }

        return {
            "success": True,
            "customer_id": customer.customer_id,
            "name": customer.name,
            "email": customer.email,
            "account_status": customer.account_status
        }

    finally:
        db.close()


@tool
def get_customer_details(customer_id: str):
    """
    Retrieve customer profile details using the customer ID.
    """
    return fetch_customer_details(customer_id)
