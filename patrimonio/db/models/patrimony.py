from datetime import date, datetime
from typing import Optional

import ormar

from patrimonio.db.base import BaseMeta


class Patrimony(ormar.Model):
    class Meta(BaseMeta):
        tablename = "patrimony"

    id: str = ormar.String(max_length=200, primary_key=True)
    name: str = ormar.String(max_length=200)
    description: str = ormar.String(max_length=200)
    items_description: str = ormar.String(max_length=200)
    acquisition_date: date = ormar.Date()
    local: str = ormar.String(max_length=100)
    serial_number: int = ormar.Integer()
    patrimony_type: str = ormar.String(max_length=100)
    patrimony_value: float = ormar.Float()
    items_value: float = ormar.Float()
    sector: str = ormar.String(max_length=200)
    conservation_state: int = ormar.Integer()
    invoice_number: int = ormar.Integer()
    brand: str = ormar.String(max_length=200)
    manufacturer: str = ormar.String(max_length=200)
    model: str = ormar.String(max_length=200)
    depreciation_value: float = ormar.Float()

    created_at: datetime = ormar.DateTime(timezone=True, default=datetime.now)
    updated_at: datetime = ormar.DateTime(
        timezone=True,
        default=datetime.now,
        onupdate=datetime.now,
    )
