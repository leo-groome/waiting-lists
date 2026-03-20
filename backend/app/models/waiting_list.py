from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class WaitingListGeneral(Base):
    __tablename__ = "waiting_list_general"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(50), nullable=False)
    plan_type = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class WaitingListExclusive(Base):
    __tablename__ = "waiting_list_exclusive"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(50), nullable=False)
    plan_type = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
