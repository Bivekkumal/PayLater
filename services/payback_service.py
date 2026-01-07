from model.model import Customer, Payback

def repay_amount(db, cust_id: int, amount: float):
    customer = db.query(Customer).filter(Customer.id == cust_id).first()

    if not customer:
        return {"error": "Customer not found"}

    # Calculate used amount
    used_amount = customer.credit_limit - customer.current_balance

   
    if used_amount <= 0:
        return {"error": "No outstanding dues"}

    if amount > used_amount:
        return {
            "error": "Repay amount exceeds outstanding dues",
            "outstanding_dues": used_amount
        }

    # ✅ Apply payback
    customer.current_balance += amount

    payback = Payback(
        cust_id=cust_id,
        amount=amount
    )

    db.add(payback)
    db.commit()
    db.refresh(payback)

    return {
        "message": "Payback successful",
        "paid_amount": amount,
        "outstanding_dues": customer.credit_limit - customer.current_balance,
        "available_balance": customer.current_balance
    }
