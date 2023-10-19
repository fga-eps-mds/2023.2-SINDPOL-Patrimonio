from databases import Database

from patrimonio.settings import settings

database = Database(str(settings.db_url))
