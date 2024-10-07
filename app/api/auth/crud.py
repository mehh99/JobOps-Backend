from sqlalchemy.orm import Session
from app.api.auth import models
import app.api.auth.schemas as schemas
from app.core.security import pwd_context
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

def create_operator_user(db: Session, user: schemas.CreateOperator):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password, operator_id=user.operator_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user