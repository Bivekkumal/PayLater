
from model.model import Customer
from utils.security import hash_password

def create_customer(
    db,
    name: str,
    email: str,
    password: str,
    credit_limit: float
):
    customer = Customer(
        name=name,
        email=email,
        password=hash_password(password),
        credit_limit=credit_limit,
        current_balance=credit_limit  # available balance
    )

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer



def get_customer_by_id(db, cust_id):
    return db.query(Customer).filter(Customer.id == cust_id).first()

def get_current_dues(db, cust_id):
    c = get_customer_by_id(db, cust_id)
    if not c:
        return None
    return {
        "Customer_Id": c.id,
        "Credit_Limit": c.credit_limit,
        "Current_Balance": c.current_balance,
        "Dues": c.credit_limit - c.current_balance
    }




