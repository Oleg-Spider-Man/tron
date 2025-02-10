from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from my_app.operations import models
from my_app.operations.schemas import AddressInfo


async def add_info(db: AsyncSession, query_info: models.QueryInfo, address: str):
    db.add(query_info)
    await db.commit()
    return AddressInfo(
        address=address,
        balance=query_info.balance,
        energy=query_info.energy,
        bandwidth=query_info.bandwidth
    )


async def get_info_tron_db(db: AsyncSession, limit: int = 10):
    query = select(models.QueryInfo).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()
