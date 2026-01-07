from fastapi import FastAPI
from pydantic import BaseModel
from db.db import SessionMaker
from services.auth_service import authenticate_customer

session_maker = SessionMaker()

class LoginRequest(BaseModel):
    email: str
    password: str

def init_auth(app: FastAPI):

    @app.post("/login", tags=["Login"])
    def login(data: LoginRequest):
        db = session_maker.get_session()()
        result = authenticate_customer(db, data.email, data.password)
        db.close()

        if not result:
            return {"error": "Invalid credentials"}

        return result
