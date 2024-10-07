from sqlalchemy.orm import Session
from app.api.auth import models
import app.api.auth.schemas as schemas
# from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_admin(db: Session, user: schemas.CreateAdmin):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.Admin(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user