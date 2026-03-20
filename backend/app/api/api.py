from fastapi import APIRouter
from app.api.endpoints import waiting_list

api_router = APIRouter()
api_router.include_router(waiting_list.router, prefix="/waiting-list", tags=["Waiting Lists"])
