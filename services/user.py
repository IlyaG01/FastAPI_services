from models.models import User
from sqlalchemy.orm import Session
from schema import schema

def create_user(data: schema.User, db: Session):
    user = User(name = data.name)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user

def get_user(id: int, db: Session):
    return db.query(User).filter(User.id==id).first()