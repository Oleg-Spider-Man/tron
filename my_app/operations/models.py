from sqlalchemy import Column, Integer, String, Float, BigInteger
from my_app.database import Base


class QueryInfo(Base):
    __tablename__ = "query_info"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    balance = Column(Float)
    energy = Column(BigInteger)
    bandwidth = Column(Integer)
