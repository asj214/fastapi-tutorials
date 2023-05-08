from fastapi import APIRouter


router = APIRouter()

@router.post("/register", name="auth:register")
async def login():
    return "auth register api"


@router.post("/login", name="auth:login")
async def login():
    return "auth login api"


@router.get("/me", name="auth:me")
async def login():
    return "auth me api"
