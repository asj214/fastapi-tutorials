from fastapi import APIRouter
from api import (auth)


router = APIRouter()
router.include_router(auth.router, tags=['auth'], prefix='/auth')