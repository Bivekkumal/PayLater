from fastapi import FastAPI,Depends
from pydantic import BaseModel
from db.db import SessionMaker
from services.merchant_service import create_merchant, get_merchant_by_id
from utils.deps import get_current_customer

session_maker = SessionMaker()

class MerchantCreate(BaseModel):
    name: str
    fee_percentage: float


def init_merchant(app: FastAPI):

    # 🔐 PROTECTED
    @app.post("/merchant", tags=["merchant"])
    def add_merchant(
        merchant: MerchantCreate,
        customer_id: int = Depends(get_current_customer)  # 🔒 lock
    ):
        db = session_maker.get_session()()
        result = create_merchant(
            db,
            merchant.name,
            merchant.fee_percentage
        )
        db.close()
        return result

    # 🔓 OPTIONAL (public)
    @app.get("/merchant/{merchant_id}", tags=["merchant"])
    def get_merchant(merchant_id: int):
        db = session_maker.get_session()()
        merchant = get_merchant_by_id(db, merchant_id)
        db.close()
        return merchant or {"error": "Merchant not found"}
