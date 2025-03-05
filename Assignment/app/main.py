from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from app.database import get_db
import app.schemas as schemas
import app.services.user_service as user_service

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.post("/profile/", response_model=schemas.Contact)
async def create_profile(request: schemas.CreateContact, db: AsyncSession = Depends(get_db)):
    return await user_service.create_user(request, db)

@app.get("/profiles/", response_model=list[schemas.Contact])
async def get_all_profiles(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await user_service.get_all_users(skip, limit, db)

@app.put("/profile/{user_id}", response_model=schemas.Contact)
async def update_profile(user_id: int, request: schemas.UserProfileBase, db: AsyncSession = Depends(get_db)):
    return await user_service.update_user(user_id, request, db)

@app.delete("/profile/{user_id}", response_model=schemas.Contact)
async def delete_profile(user_id: int, db: AsyncSession = Depends(get_db)):
    return await user_service.delete_user(user_id, db)

@app.get("/")
async def hello():
    return {"message": "Hello, FastAPI is running!"}
