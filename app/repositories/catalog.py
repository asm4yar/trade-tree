from sqlalchemy import select
from sqlalchemy.orm import Session
from app.views import v_top5_products_last_30_days


def get_top5_products_last_30_days(session: Session):
    stmt = (
        select(
            v_top5_products_last_30_days.c.product_name,
            v_top5_products_last_30_days.c.category_level1,
            v_top5_products_last_30_days.c.total_sold_qty,
        ).order_by(v_top5_products_last_30_days.c.total_sold_qty.desc())
    )
    result = session.execute(stmt)
    return result.mappings().all()
