from pydantic import BaseModel, EmailStr
from app.api.auth.models import Role
from typing import Optional

#Operator
class OperatorBase(BaseModel):
    name : str

class CreateOperator(OperatorBase):
    pass

class GetOperator(OperatorBase):
    id : str
    class Config:
        from_attributes = True

#User
class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: Role

class CreateOperatorUser(UserBase):
    operator_id: str
    password: str

class CreateAdmin(UserBase):
    password: str

class GetUser(UserBase):
    id: str

    class Config:
        from_attributes = True
        
class GetOperatorUser(UserBase):
    id: str
    operator_id: Optional[str] = None
    
    class Config:
        from_attributes = True

class VerifyUser(GetUser):
    verfied_status: bool