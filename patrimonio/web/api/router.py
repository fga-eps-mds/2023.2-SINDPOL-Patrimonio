from fastapi.routing import APIRouter

from patrimonio.web.api import echo, monitoring, patrimony

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(patrimony.router, prefix="/patrimony", tags=["patrimony"])
