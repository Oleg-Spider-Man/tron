from pydantic import BaseModel


class AddressInfo(BaseModel):
    address: str
    balance: float
    energy: int
    bandwidth: int


class AddressRequest(BaseModel):
    address: str


class AddressInfoDB(AddressInfo):
    id: int

    class Config:
        orm_mode = True
