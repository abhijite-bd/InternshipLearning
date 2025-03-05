from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
import app.models as models
import app.schemas as schemas

class UserRepository:
    @staticmethod
    async def get_user_by_email(db: AsyncSession, email: str):
        result = await db.execute(select(models.User).filter(models.User.email == email))
        return result.scalar_one_or_none()

    @staticmethod
    async def create_user(db: AsyncSession, user_data: schemas.CreateContact, hashed_password: str):
        new_user = models.User(
            name=user_data.name,
            username=user_data.username,
            email=user_data.email,
            phone=user_data.phone,
            password=hashed_password
        )
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user

    @staticmethod
    async def get_user_by_id(db: AsyncSession, user_id: int):
        result = await db.execute(select(models.User).filter(models.User.id == user_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def update_user(db: AsyncSession, user: models.User, update_data: dict):
        for key, value in update_data.items():
            setattr(user, key, value)
        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    async def delete_user(db: AsyncSession, user: models.User):
        await db.delete(user)
        await db.commit()
        return user
