
from fastapi import FastAPI,Depends
from pydantic import BaseModel
from db.db import SessionMaker
from services.payback_service import repay_amount
from utils.deps import get_current_customer
from fastapi import Depends

session_maker = SessionMaker()


class PaybackRequest(BaseModel):
    cust_id: int
    amount: float

def init_payback(app: FastAPI):
    @app.post("/payback",tags=["Payback"])
    def pay(req: PaybackRequest):
        db = session_maker.get_session()()
        r = repay_amount(db, req.cust_id, req.amount)
        db.close()
        return r
    

    @app.post("/payback", tags=["Payback"])
    def pay(req: PaybackRequest, customer_id=Depends(get_current_customer)):
        ...

