from typing import Dict

from pydantic import BaseModel


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


class PaymentMethods(BaseModel):
    list: Dict[str, PaymentMethod]
