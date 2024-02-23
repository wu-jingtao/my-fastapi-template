from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from ..models.user import User

router = APIRouter()
views = Jinja2Templates("src/views")


@router.get("/")
async def index(request: Request):
    return views.TemplateResponse(request, "index.html", {"content": "Index Page"})


@router.post("/get_user")
async def get_user(user: User):
    return user
