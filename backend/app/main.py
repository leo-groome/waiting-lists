from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Waiting Lists API",
    description="Backend SaaS Multi-tenant (B2B/B2C) - Vertical Slice Architecture.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173", 
        "http://127.0.0.1:5173", 
        "http://localhost:8000",
        "https://www.vantasolutions.tech",
        "https://vantasolutions.tech",
        "https://vanta-waiting-lists.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health Check
@app.get("/", tags=["Root"])
async def root():
    return JSONResponse(content={"message": "Waiting Lists API is online."})

# --- Routers ---
API_PREFIX = "/api/v1"

from app.api.api import api_router
app.include_router(api_router, prefix=API_PREFIX)
