from typing import Literal

from pydantic import BaseModel


class PayoffWebhookData(BaseModel):
    id: str
    my_id: str
    method: str
    bank: str
    wallet: str
    amount: float
    amount_in_currency: float
    amount_currency: str
    amount_rate: float
    amount_down: float
    commission: float
    commission_type: Literal[0, 1]
    status: Literal['cancel', 'success']
    cancel_message: str | None = None
    date: str
    complete_date: str
    sign: str
