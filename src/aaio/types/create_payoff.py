from typing import Optional

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

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
