from model.model import Transactions, Customer

def create_transaction(db, cust_id: int, merchant_id: int, amount: float):
    customer = db.query(Customer).filter(Customer.id == cust_id).first()

    if not customer:
        return {"error": "Customer not found"}

    # ✅ check available balance
    if amount > customer.current_balance:
        return {"error": "Insufficient credit balance"}

    txn = Transactions(
        cust_id=cust_id,
        merchant_id=merchant_id,
        amount=amount
    )

    # ✅ deduct from available balance
    customer.current_balance -= amount

    db.add(txn)
    db.commit()
    db.refresh(txn)

    return txn



def get_transaction_by_id(db, txn_id: int):
    return db.query(Transactions).filter(Transactions.id == txn_id).first()