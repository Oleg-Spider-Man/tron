from pydantic import BaseModel


class AddressInfo(BaseModel):
    address: str
    balance: float
    energy: int
    bandwidth: int


class AddressRequest(BaseModel):
    address: str


class AddressInfoDB(BaseModel):
    id: int
    address: str
    balance: float
    energy: int
    bandwidth: int

    class Config:
        orm_mode = True
