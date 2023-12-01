import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status
from uuid import uuid4

from patrimonio.tests.utils import generate_fake_patrimony


@pytest.mark.anyio
async def test_get_patrimonys(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("get_patrimonys")
    response = await client.get(url)
    assert response.status_code == 200
    patrimony_data = response.json()
    assert isinstance(patrimony_data, list)


@pytest.mark.anyio
async def test_get_patrimony_correct(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("create_patrimony")
    patrimony = generate_fake_patrimony()
    response = await client.post(url, json=patrimony)
    assert response.status_code == 200
    patrimony_data = response.json()
    patrimony_id = patrimony_data["id"]

    url = fastapi_app.url_path_for("get_patrimony", patrimony_id=patrimony_id)
    response = await client.get(url)
    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_patrimony_incorrect(
    client: AsyncClient, fastapi_app: FastAPI
) -> None:
    url = fastapi_app.url_path_for("get_patrimony", patrimony_id=str(uuid4()))
    response = await client.get(url)
    assert response.status_code == 404


@pytest.mark.anyio
async def test_create_patrimony_correct(
    client: AsyncClient, fastapi_app: FastAPI
) -> None:
    url = fastapi_app.url_path_for("create_patrimony")
    patrimony = generate_fake_patrimony()
    response = await client.post(url, json=patrimony)
    assert response.status_code == 200


@pytest.mark.anyio
async def test_create_patrimony_incorrect(
    client: AsyncClient, fastapi_app: FastAPI
) -> None:
    url = fastapi_app.url_path_for("create_patrimony")
    patrimony = generate_fake_patrimony()
    patrimony.pop("name")
    response = await client.post(url, json=patrimony)
    assert response.status_code == 422


@pytest.mark.anyio
async def test_update_patrimony_correct(
    client: AsyncClient, fastapi_app: FastAPI
) -> None:
    url = fastapi_app.url_path_for("create_patrimony")
    patrimony = generate_fake_patrimony()
    response = await client.post(url, json=patrimony)
    assert response.status_code == 200
    patrimony_data = response.json()
    patrimony_id = patrimony_data["id"]

    url = fastapi_app.url_path_for("update_patrimony", patrimony_id=patrimony_id)
    response = await client.put(url, json={"name": "table"})
    assert response.status_code == 200


@pytest.mark.anyio
async def test_update_patrimony_incorrect(
    client: AsyncClient, fastapi_app: FastAPI
) -> None:
    url = fastapi_app.url_path_for("update_patrimony", patrimony_id=str(uuid4()))
    response = await client.put(url, json={})
    assert response.status_code == 404


@pytest.mark.anyio
async def test_delete_patrimony_correct(
    client: AsyncClient, fastapi_app: FastAPI
) -> None:
    url = fastapi_app.url_path_for("create_patrimony")
    patrimony = generate_fake_patrimony()
    response = await client.post(url, json=patrimony)
    assert response.status_code == 200
    patrimony_data = response.json()
    patrimony_id = patrimony_data["id"]

    url = fastapi_app.url_path_for("delete_patrimony", patrimony_id=patrimony_id)
    response = await client.delete(url)
    assert response.status_code == 200


@pytest.mark.anyio
async def test_delete_patrimony_incorrect(
    client: AsyncClient, fastapi_app: FastAPI
) -> None:
    url = fastapi_app.url_path_for("delete_patrimony", patrimony_id=str(uuid4()))
    response = await client.delete(url)
    assert response.status_code == 200
