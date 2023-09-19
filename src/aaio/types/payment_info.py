from typing import Literal

from pydantic import BaseModel


class PaymentInfo(BaseModel):
    id: str
    order_id: str
    desc: str
    merchant_id: str
    merchant_domain: str
    method: str
    amount: float
    currency: Literal['RUB', 'UAH', 'EUR', 'USD']
    profit: float
    commission: float
    commission_client: float
    commission_type: str
    email: str
    status: Literal['in_process', 'success', 'expired', 'hold']
    date: str
    expired_date: str
    complete_date: str
    us_vars: list[str]
