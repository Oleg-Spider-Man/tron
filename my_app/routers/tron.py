from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from tronpy import AsyncTron
from tronpy.providers import AsyncHTTPProvider
from my_app.config import API_KEY_TRON
from my_app.dependencies import get_async_session
from my_app.operations import crud
from my_app.operations.models import QueryInfo
from my_app.operations.schemas import AddressInfo, AddressRequest, AddressInfoDB

router = APIRouter(
    prefix="/tron",
    tags=["rout_tron"],
)


@router.post("/tron/get/info", response_model=AddressInfo)
async def get_address_info(
        address: AddressRequest,
        db: AsyncSession = Depends(get_async_session)
):
    provider = AsyncHTTPProvider(api_key=f"{API_KEY_TRON}")
    tron = AsyncTron(provider=provider)
    try:
        data_tr = await tron.get_account(address.address)
        data_res = await tron.get_account_resource(address.address)
        print(data_tr)
        print(data_res)
        query_info = QueryInfo(
            address=address.address,
            balance=float(data_tr['balance']) / 1000000,
            energy=data_res['TotalEnergyWeight'],
            bandwidth=data_res['TotalNetLimit']
        )
        return await crud.add_info(db=db, query_info=query_info, address=address.address)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/tron/get/db", response_model=list[AddressInfoDB])
async def get_address_info(limit: int = Query(10, ge=0), db: AsyncSession = Depends(get_async_session)):
    data = await crud.get_info_tron_db(db=db, limit=limit)
    return data
