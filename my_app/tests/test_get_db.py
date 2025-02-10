import pytest


@pytest.mark.asyncio
async def test_read_db(aclient):
    response = await aclient.get("/tron/tron/get/db")
    assert response.status_code == 200
    assert response.json() == []
