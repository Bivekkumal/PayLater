from model.model import Merchant




def create_merchant(db, name: str, fee_percentage: float):
    merchant = Merchant(
        name=name,
        fee_percentage=fee_percentage
    )
    db.add(merchant)
    db.commit()
    db.refresh(merchant)
    return merchant


def get_merchant_by_id(db, merchant_id: int):
    return db.query(Merchant).filter(Merchant.id == merchant_id).first()
