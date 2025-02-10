from unittest.mock import patch, AsyncMock

import pytest


@pytest.mark.asyncio
async def test_pars_add_db(aclient):
    mock_account_data = {
        "address": "TJi9f9QCPpVtzJw9AzYVsboY6QCRjPNWjk",
        "balance": 1602491,
        "net_usage": 4619268
    }

    mock_resource_data = {
        "TotalEnergyWeight": 16273456553
    }
    mock_tron = AsyncMock()
    mock_tron.get_account.return_value = mock_account_data
    mock_tron.get_account_resource.return_value = mock_resource_data
    with patch('my_app.routers.tron.AsyncTron', return_value=mock_tron):
        response = await aclient.post("/tron/tron/get/info", json={
         "address": "TJi9f9QCPpVtzJw9AzYVsboY6QCRjPNWjk"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["address"] == mock_account_data["address"]
        assert data["balance"] == float(mock_account_data["balance"]) / 1000000
        assert data["energy"] == mock_resource_data["TotalEnergyWeight"]
        assert data["bandwidth"] == mock_account_data["net_usage"]


@pytest.mark.asyncio
async def test_read_db(aclient):
    response = await aclient.get("/tron/tron/get/db")
    assert response.status_code == 200
    assert response.json() == [
        {
         "id": 1,
         "address": "TJi9f9QCPpVtzJw9AzYVsboY6QCRjPNWjk",
         "balance": 1.602491,
         "energy": 16273456553,
         "bandwidth": 4619268
        }
    ]

