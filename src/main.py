from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from src.users.router import router as users_router
from src.interestZones.router import router as interest_zones_router
from src.records.router import router as records_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/api")
app.include_router(interest_zones_router, prefix="/api")
app.include_router(records_router, prefix="/api")
