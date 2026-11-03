from datetime import date

from app.database.connection import SessionLocal
from app.database.models import Customer, Order


def seed_customers(db):
    customers = [
        Customer(
            customer_id="CUST-101",
            name="Rahul Sharma",
            email="rahul@example.com",
            account_status="active"
        ),
        Customer(
            customer_id="CUST-102",
            name="Amit Verma",
            email="amit@example.com",
            account_status="active"
        ),
        Customer(
            customer_id="CUST-103",
            name="Priya Singh",
            email="priya@example.com",
            account_status="active"
        )
    ]

    db.add_all(customers)


def seed_orders(db):
    orders = [
        Order(
            order_id="ORD-1024",
            customer_id="CUST-101",
            product="Wireless Headphones",
            status="shipped",
            expected_delivery=date(2026, 11, 5)
        ),
        Order(
            order_id="ORD-1025",
            customer_id="CUST-102",
            product="Smart Watch",
            status="processing",
            expected_delivery=date(2026, 11, 7)
        ),
        Order(
            order_id="ORD-1026",
            customer_id="CUST-101",
            product="Laptop",
            status="delivered",
            expected_delivery=date(2026, 10, 30)
        ),
        Order(
            order_id="ORD-1027",
            customer_id="CUST-103",
            product="Keyboard",
            status="shipped",
            expected_delivery=date(2026, 11, 6)
        ),
        Order(
            order_id="ORD-1028",
            customer_id="CUST-102",
            product="Mouse",
            status="processing",
            expected_delivery=date(2026, 11, 8)
        )
    ]

    db.add_all(orders)


def seed_database():
    db = SessionLocal()

    try:
        seed_customers(db)
        seed_orders(db)

        db.commit()

        print("Sample data inserted successfully!")

    except Exception as e:
        db.rollback()
        print(f"Error inserting data: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()