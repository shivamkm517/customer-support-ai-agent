from app.database.models import (
    Customer,
    Order,
    SupportTicket
)


def get_customer_by_id(db, customer_id):
    return db.query(Customer).filter(
        Customer.customer_id == customer_id
    ).first()


def get_order_by_id(db, order_id):
    return db.query(Order).filter(
        Order.order_id == order_id
    ).first()


def get_customer_orders(db, customer_id):
    return db.query(Order).filter(
        Order.customer_id == customer_id
    ).all()


def create_support_ticket(
    db,
    ticket_id,
    customer_id,
    issue_type,
    description,
    priority="medium"
):
    ticket = SupportTicket(
        ticket_id=ticket_id,
        customer_id=customer_id,
        issue_type=issue_type,
        description=description,
        priority=priority
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return ticket


def get_ticket_by_id(db, ticket_id):
    return db.query(SupportTicket).filter(
        SupportTicket.ticket_id == ticket_id
    ).first()