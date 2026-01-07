from fastapi import FastAPI
from db.db import SessionMaker
from model.model import Base
from routes.customer import init_customer
from routes.merchant import init_merchant
from routes.transaction import init_transaction
from routes.payback import init_payback
from routes.auth import init_auth

tags_metadata = [
    {
        "name": "Register Customer",
        
    },
    {
        "name": "Login",
       
    },   
]

app = FastAPI(
    title="PayLater App",
    openapi_tags=tags_metadata
)

session_maker = SessionMaker()
engine = session_maker.get_engine()
Base.metadata.create_all(bind=engine)

init_auth(app)
init_customer(app)
init_merchant(app)
init_transaction(app)
init_payback(app)

