from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base
from enum import Enum as pyEnum
import uuid


class Role(pyEnum):
    Admin = "Admin"
    Operator = "Operator"

class Operator(Base):
    __tablename__ = "operator"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    name = Column(String(255), unique=True, index=True)  # Assuming name can be lengthy, up to 255 characters
    users = relationship("OperatorUser", back_populates="operator", cascade="all, delete-orphan")
    jobs = relationship("Job", back_populates="operator", cascade="all, delete-orphan")
    area = relationship("Area", back_populates='operator', cascade="all, delete-orphan")
    well_instances = relationship("WellInstance", back_populates='operator', cascade="all, delete-orphan")

class User(Base):
    __tablename__ = "users"

    id = Column(String(25), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    username = Column(String(50), unique=True, index=True)  # Typical username length is around 50 characters
    email = Column(String(100), unique=True, index=True)  # Email addresses typically max out at 100 characters
    hashed_password = Column(String(128))  # Common length for hashed passwords
    role = Column(Enum(Role), nullable=False)
    
    verified_status = Column(Boolean)
    
    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": role
    }

class Admin(User):
    __tablename__ = "user_admin"

    id = Column(String(25), ForeignKey('users.id'), primary_key=True)
    
    __mapper_args__ = {
        "polymorphic_identity": Role.Admin,
    }

class OperatorUser(User):
    __tablename__ = "user_operator"

    id = Column(String(25), ForeignKey('users.id'), primary_key=True)
    operator_id = Column(String(25), ForeignKey('operator.id'))
    operator = relationship("operator", back_populates="users")
    
    __mapper_args__ = {
        "polymorphic_identity": Role.Operator
    }