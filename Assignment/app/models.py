import sqlalchemy as _sql
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, nullable=False)
    username = _sql.Column(_sql.String, unique=True, nullable=False)
    email = _sql.Column(_sql.String, unique=True, nullable=False)    
    phone = _sql.Column(_sql.String, nullable=True)    
    password = _sql.Column(_sql.String, nullable=False)  # Hashed password
