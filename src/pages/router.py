from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from products.router import search_product, get_all_products, get_product
from orders.router import get_order


router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")


@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@router.get("/main")
def get_main_page(request: Request, products=Depends(get_all_products)):
    return templates.TemplateResponse("main.html", {"request": request, "products": products["data"]})


@router.get("/product/{product_id}")
def get_main_page(request: Request, product=Depends(get_product)):
    return templates.TemplateResponse("product.html", {"request": request, "product": product["data"]})


@router.get("/search/{tags}")
def get_search_page(request: Request, products=Depends(search_product)):
    return templates.TemplateResponse("search.html", {"request": request, "products": products["data"]})


@router.get("/order/{order_id}")
def get_order_page(request: Request, order=Depends(get_order), all_products=Depends(get_all_products)):
    return templates.TemplateResponse(
        "order.html",
        {
            "request": request,
            "order": order["data"],
            "all_products": all_products["data"]
        }
    )