from typing import Literal, Optional

from aaio.types.response import AAIOResponse


class PayoffInfo(AAIOResponse):
    id: Optional[str] = None
    my_id: Optional[str] = None
    method: Optional[str] = None
    wallet: Optional[str] = None
    amount: Optional[float] = None
    amount_down: Optional[float] = None
    commission: Optional[float] = None
    commission_type: Optional[Literal[0, 1]] = None
    status: Optional[Literal['in_process', 'cancel', 'success']] = None
    cancel_message: Optional[str] = None
    date: Optional[str] = None
    complete_date: Optional[str] = None
