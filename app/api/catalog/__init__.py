from .orders import router as order_router
from .categories import router as categories_router
from .top_products import router as top_products_router

routers = (order_router, categories_router, top_products_router)

__ALL__ = ["routers"]
