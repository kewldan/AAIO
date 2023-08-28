from typing import Literal, Optional

from aaio.types.response import AAIOResponse


class CreatePayoff(AAIOResponse):
    id: Optional[str] = None
    my_id: Optional[str] = None
    method: Optional[str] = None
    wallet: Optional[str] = None
    amount: Optional[float] = None
    amount_in_currency: Optional[float] = None
    amount_currency: Optional[str] = None
    amount_rate: Optional[float] = None
    amount_down: Optional[float] = None
    commission: Optional[float] = None
    commission_type: Optional[int] = None
    status: Optional[Literal['in_process', 'cancel', 'success']] = None
