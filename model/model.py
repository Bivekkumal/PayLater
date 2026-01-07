from sqlalchemy import Column, Integer, VARCHAR, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100), nullable=False)
    email = Column(VARCHAR(100), nullable=False, unique=True)
    password = Column(VARCHAR(100), nullable=False)  
    credit_limit = Column(Float)
    current_balance = Column(Float)


class Merchant(Base):
    __tablename__ = "merchants"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100), nullable=False)
    fee_percentage = Column(Float, default=0.0)


class Transactions(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    cust_id = Column(Integer, ForeignKey("customers.id"))
    merchant_id = Column(Integer, ForeignKey("merchants.id"))
    amount = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)  


class Payback(Base):
    __tablename__ = "paybacks"

    id = Column(Integer, primary_key=True)
    cust_id = Column(Integer, ForeignKey("customers.id"))
    amount = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)  
