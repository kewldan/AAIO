from typing import Literal

from pydantic import BaseModel


class PaymentWebhookData(BaseModel):
    merchant_id: str
    invoice_id: str
    order_id: str
    amount: float
    currency: Literal['RUB', 'UAH', 'EUR', 'USD']
    profit: float
    commission: float
    commission_client: float
    commission_type: str
    sign: str
    method: str
    desc: str
    email: str
    us_key: str
