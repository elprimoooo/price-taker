from decimal import Decimal

from pydantic import BaseModel, Field

class ScrapedProduct(BaseModel):
    """Data o produktu získaná z jedné stránky e-shopu."""

    name: str = Field(min_length=1)
    price: Decimal = Field(gt=0)
    currency: str = Field(pattern=r"^[A-Z]{3}$")
    in_stock: bool
    external_id: str | None = None