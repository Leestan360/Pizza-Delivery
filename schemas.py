from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]


    class Config:
        orm_mode = True
        schema_extra = {
            'example':{
                'username': 'stanleymay',
                'email': 'stanleym@gmail.com',
                'password': 'password',
                'is_staff': False,
                'is_active': True
            }
        }


class Settings(BaseModel):
    authjwt_secret_key: str='4e3fb94e23c863dedeb15c202693aa3b9ee5c134d9c242f1025e4cd43eed0139'


class LoginModel(BaseModel):
    username: str
    password: str


class OrderModel(BaseModel):
    id: Optional[int]
    quantity: int
    order_status: Optional[str]="PENDING"
    pizza_size: Optional[str]="SMALL"
    user_id: Optional[int]

    class Config:
        orm_mode = True
        schema_extra = {
            "example":{
                "quantity": 2,
                "pizza_size": "LARGE"
            }
        }


class OrderStatusModel(BaseModel):
    order_status: Optional[str]="PENDING"

    class Config:
        orm_mode = True
        schema_extra = {
            "example":{
                "order_status":"PENDING"
            }
        }