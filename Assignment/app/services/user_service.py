from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from app import models
import app.repositories.user_repository as user_repo
import app.schemas as schemas
from sqlalchemy.future import select


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_user(request: schemas.CreateContact, db: AsyncSession):
    existing_user = await user_repo.UserRepository.get_user_by_email(db, request.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_password = pwd_context.hash(request.password)
    return await user_repo.UserRepository.create_user(db, request, hashed_password)

async def get_all_users(skip: int, limit: int, db: AsyncSession):
    result = await db.execute(select(models.User).offset(skip).limit(limit))
    return result.scalars().all()

async def update_user(user_id: int, request: schemas.UserProfileBase, db: AsyncSession):
    user = await user_repo.UserRepository.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return await user_repo.UserRepository.update_user(db, user, request.dict(exclude_unset=True))

async def delete_user(user_id: int, db: AsyncSession):
    user = await user_repo.UserRepository.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return await user_repo.UserRepository.delete_user(db, user)
