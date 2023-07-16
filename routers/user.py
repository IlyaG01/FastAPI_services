from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import user
from schema import schema

router = APIRouter()

@router.post('/', tags=['user'])
async def create(data: schema.User = None, db: Session = Depends(get_db)):
    return user.create_user(data, db)

@router.get('/{id}', tags=['user'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return user.get_user(id, db)
