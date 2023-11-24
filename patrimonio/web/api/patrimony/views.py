import logging
from typing import List
from uuid import uuid4

from asyncpg.exceptions import UniqueViolationError
from fastapi import APIRouter, HTTPException

from patrimonio.db.models.patrimony import Patrimony
from patrimonio.web.api.patrimony.schemas import CreatePatrimonyDTO, UpdatePatrimonyDTO

router = APIRouter()

@router.get("/")
async def get_patrimonys(
    limit: int = 10,
    offset: int = 0,
) -> List[Patrimony]:
    return await Patrimony.objects.limit(limit).offset(offset,).all()

@router.get("/{patrimony_id}")
async def get_patrimony(patrimony_id: str) -> Patrimony:
    try:
        return await Patrimony.objects.get(id=patrimony_id)
    except Exception:
        logging.error("Error occurred while get patrimony", exc_info=True)
        raise HTTPException(status_code=404, detail="Patrimony not found")

@router.post("/")
async def create_patrimony(patrimony: CreatePatrimonyDTO) -> Patrimony:
    try:
        create_patrimony_dict = patrimony.dict()
        patrimony_id = str(uuid4())
        await Patrimony.objects.create(
            id=patrimony_id, **create_patrimony_dict
        )
        return await Patrimony.objects.get(id=patrimony_id)
    except UniqueViolationError:
        logging.error("Patrimony already exists", exc_info=True)
        raise HTTPException(status_code=400, detail="Patrimony already exists",)
    except Exception:
        logging.error("Error occurred while creating patrimony", exc_info=True)
        raise HTTPException(status_code=400, detail="Error occurred while creating patrimony",)

@router.put("/{patrimony_id}")
async def update_patrimony(patrimony_id: str, update_patrimony: UpdatePatrimonyDTO) -> Patrimony:
    try:
        patrimony = await Patrimony.objects.get(id=patrimony_id)
        await patrimony.update(**update_patrimony.dict(exclude_none=True))
        return await Patrimony.objects.get(id=patrimony_id)
    except Exception:
        logging.error("Patrimony not found", exc_info=True)
        raise HTTPException(status_code=404, detail="Patrimony not found",)

@router.delete("/{patrimony_id}")
async def delete_patrimony(patrimony_id: str) -> None:
    try:
        await Patrimony.objects.delete(id=patrimony_id)
    except Exception:
        logging.error("Error occurred while deleting patrimony", exc_info=True)
        raise HTTPException(status_code=404, detail="Error occurred while deleting patrimony",)
