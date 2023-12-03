from datetime import date
from typing import Optional

from pydantic import BaseModel


class CreatePatrimonyDTO(BaseModel):
    name: str
    description: str
    items_description: str
    acquisition_date: date
    local: str
    serial_number: int
    patrimony_type: str
    patrimony_value: float
    items_value: float
    sector: str
    conservation_state: int
    invoice_number: int
    brand: str
    manufacturer: str
    model: str
    depreciation_value: float


class UpdatePatrimonyDTO(BaseModel):
    name: Optional[str]
    description: Optional[str]
    items_description: Optional[str]
    acquisition_date: Optional[date]
    local: Optional[str]
    serial_number: Optional[int]
    patrimony_type: Optional[str]
    patrimony_value: Optional[float]
    items_value: Optional[float]
    sector: Optional[str]
    conservation_state: Optional[int]
    invoice_number: Optional[int]
    brand: Optional[str]
    manufacturer: Optional[str]
    model: Optional[str]
    depreciation_value: Optional[float]
