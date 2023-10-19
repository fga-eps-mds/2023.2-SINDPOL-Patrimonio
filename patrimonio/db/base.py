from ormar import ModelMeta

from patrimonio.db.config import database
from patrimonio.db.meta import meta


class BaseMeta(ModelMeta):
    """Base metadata for models."""

    database = database
    metadata = meta
