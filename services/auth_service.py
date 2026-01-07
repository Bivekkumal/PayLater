from model.model import Customer
from utils.security import verify_password
from utils.jwt import create_access_token



def authenticate_customer(db, email: str, password: str):
    customer = db.query(Customer).filter(Customer.email == email).first()

    if not customer:
        return None

    if not verify_password(password, customer.password):
        return None

    token = create_access_token({"sub": str(customer.id)})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
