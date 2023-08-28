from typing import Optional

from pydantic import BaseModel

from aaio.types.response import AAIOResponse


class PaymentMethodAmounts(BaseModel):
    RUB: float
    UAH: float
    USD: float
    EUR: float


class PaymentMethod(BaseModel):
    name: str
    min: PaymentMethodAmounts
    max: PaymentMethodAmounts
    commission_type: float


class PaymentMethods(AAIOResponse):
    list: Optional[dict[str, PaymentMethod]] = None
