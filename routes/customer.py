from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from db.db import SessionMaker
from services.customer_service import (
    create_customer,
    get_customer_by_id,
    get_current_dues
)

session_maker = SessionMaker()

class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    credit_limit: float   # ✅ REQUIRED

def init_customer(app: FastAPI):

    @app.post("/Customer Registration Form", tags=["Register Customer"])
    def add_customer(customer: CustomerCreate):
        db = session_maker.get_session()()

        result = create_customer(
            db,
            customer.name,
            customer.email,
            customer.password,
            customer.credit_limit  # ✅ PASSED CORRECTLY
        )

        db.close()
        return result


    @app.get("/customer/{cust_id}",tags=["Customer"])
    def get_customer(cust_id: int):
        db = session_maker.get_session()()
        c = get_customer_by_id(db, cust_id)
        db.close()
        return c or {"error": "Customer not found"}

   
    @app.get("/customer/{cust_id}/dues",tags=["Customer"])
    def get_dues(cust_id: int):
        db = session_maker.get_session()()
        dues = get_current_dues(db, cust_id)
        db.close()
        return dues or {"error": "Customer not found"}
