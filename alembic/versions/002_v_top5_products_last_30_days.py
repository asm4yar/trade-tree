"""002_v_top5_products_last_30_days

Revision ID: f8f09e93827b
Revises: 001_baseline
Create Date: 2026-02-07 12:06:44.711328

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f8f09e93827b"
down_revision: Union[str, Sequence[str], None] = "001_baseline"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

VIEW_NAME = "v_top5_products_last_30_days"

VIEW_SQL = f"""
CREATE OR REPLACE VIEW {VIEW_NAME} as 
with recursive sales as (
select
	oi.product_id,
	SUM(oi.qty) as sold_qty
from
	order_items oi
join orders o on
	o.id = oi.order_id
where
	o.created_at >= now() - interval '30 days'
group by
	oi.product_id
),
start_cats as (
select
	distinct p.category_id
from
	products p
join sales s on
	s.product_id = p.id
),
cat_up as (
select
	sc.category_id as start_cat_id,
	c.id as cur_cat_id,
	c.parent_id,
	c.name
from
	start_cats sc
join categories c on
	c.id = sc.category_id
union all
select
	cu.start_cat_id,
	p.id as cur_cat_id,
	p.parent_id,
	p.name
from
	cat_up cu
join categories p on
	p.id = cu.parent_id
),
root_cat as (
select
	start_cat_id,
	cur_cat_id as root_category_id,
	name as root_category_name
from
	cat_up
where
	parent_id is null
)
select
	p.name as product_name,
	rc.root_category_name as category_level1,
	s.sold_qty as total_sold_qty
from
	sales s
join products p on
	p.id = s.product_id
join root_cat rc on
	rc.start_cat_id = p.category_id
order by
	s.sold_qty desc,
	p.name
limit 5;
"""


def upgrade() -> None:
    """Upgrade schema."""
    op.execute(VIEW_SQL)


def downgrade() -> None:
    """Downgrade schema."""
    op.execute(f"DROP VIEW IF EXISTS {VIEW_NAME}")
