from sqlalchemy import Column, Integer, String, Text, DateTime, Date, ForeignKey
from datetime import datetime
from sqlalchemy.sql import func
from app.database.connection import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    account_status = Column(String, default="active")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String, unique=True, nullable=False)
    customer_id = Column(String, ForeignKey("customers.customer_id"))
    product = Column(String, nullable=False)
    status = Column(String, default="processing")
    expected_delivery = Column(Date)


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(String, unique=True, nullable=False)
    customer_id = Column(String, ForeignKey("customers.customer_id"))
    created_at = Column(DateTime, server_default=func.now())


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(String, ForeignKey("conversations.conversation_id"))
    role = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class SupportTicket(Base):
    __tablename__ = "support_tickets"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(String, unique=True, nullable=False)
    customer_id = Column(String, ForeignKey("customers.customer_id"))
    issue_type = Column(String, nullable=False)
    description = Column(Text)
    priority = Column(String, default="medium")
    status = Column(String, default="open")
    created_at = Column(DateTime, default=datetime.utcnow)