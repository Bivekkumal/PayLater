from fastapi import FastAPI,Depends
from pydantic import BaseModel
from db.db import SessionMaker
from services.transaction_service import create_transaction, get_transaction_by_id
from utils.deps import get_current_customer

session_maker = SessionMaker()

class TransactionCreate(BaseModel):
    cust_id: int
    merchant_id: int
    amount: float

def init_transaction(app: FastAPI):

    @app.post("/transaction",tags=["Transaction"])
    def add_transaction(txn: TransactionCreate):
        db = session_maker.get_session()()
        result = create_transaction(
            db,
            txn.cust_id,
            txn.merchant_id,
            txn.amount
        )
        db.close()
        return result

    @app.get("/transaction/{txn_id}",tags=["Transaction"])
    def get_txn(txn_id: int):
        db = session_maker.get_session()()
        txn = get_transaction_by_id(db, txn_id)
        db.close()
        return txn or {"error": "Transaction not found"}
    

    @app.post("/transaction", tags=["Transaction"])
    def add_transaction(txn: TransactionCreate, customer_id=Depends(get_current_customer)):
       ...  