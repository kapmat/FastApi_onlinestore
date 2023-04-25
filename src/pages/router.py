from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from products.router import search_product

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")


@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@router.get("/search/{tags}")
def get_search_page(request: Request, products=Depends(search_product)):
    return templates.TemplateResponse("search.html", {"request": request, "products": products["data"]})
