from typing import Literal, Optional

from pydantic import BaseModel


class PayoffInfo(BaseModel):
    id: str
    my_id: str
    method: str
    wallet: str
    amount: float
    amount_down: float
    commission: float
    commission_type: Literal[0, 1]
    status: Literal['in_process', 'cancel', 'success']
    cancel_message: Optional[str] = None
    date: str
    complete_date: Optional[str] = None
