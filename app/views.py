from sqlalchemy import Table, Column, String, Integer, MetaData

metadata = MetaData()

v_top5_products_last_30_days = Table(
    "v_top5_products_last_30_days",
    metadata,
    Column("product_name", String),
    Column("category_level1", String),
    Column("total_sold_qty", Integer),
)
