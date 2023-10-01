from typing import Literal, Optional

from pydantic import BaseModel


class CreatePayoff(BaseModel):
    id: str
    my_id: str
    method: str
    wallet: str
    amount: float
    amount_in_currency: float
    amount_currency: str
    amount_rate: Optional[float] = None
    amount_down: float
    commission: float
    commission_type: int
    status: Literal['in_process', 'cancel', 'success']
