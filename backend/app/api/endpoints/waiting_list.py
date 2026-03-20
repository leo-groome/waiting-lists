from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app.db.session import get_db
from app.models.waiting_list import WaitingListGeneral, WaitingListExclusive
from app.schemas.waiting_list import WaitingListCreate, WaitingListResponse

router = APIRouter()

@router.post("/general", response_model=WaitingListResponse)
async def create_general(entry: WaitingListCreate, db: AsyncSession = Depends(get_db)):
    db_entry = WaitingListGeneral(**entry.model_dump())
    db.add(db_entry)
    await db.commit()
    await db.refresh(db_entry)
    return db_entry

@router.get("/general", response_model=List[WaitingListResponse])
async def list_general(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WaitingListGeneral).order_by(WaitingListGeneral.created_at.desc()))
    return result.scalars().all()

@router.post("/exclusive", response_model=WaitingListResponse)
async def create_exclusive(entry: WaitingListCreate, db: AsyncSession = Depends(get_db)):
    db_entry = WaitingListExclusive(**entry.model_dump())
    db.add(db_entry)
    await db.commit()
    await db.refresh(db_entry)
    return db_entry

@router.get("/exclusive", response_model=List[WaitingListResponse])
async def list_exclusive(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WaitingListExclusive).order_by(WaitingListExclusive.created_at.desc()))
    return result.scalars().all()
