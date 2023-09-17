from typing import Literal, Optional

from aaio.types.response import AAIOResponse


class PaymentInfo(AAIOResponse):
    id: Optional[str] = None
    order_id: Optional[str] = None
    desc: Optional[str] = None
    merchant_id: Optional[str] = None
    merchant_domain: Optional[str] = None
    method: Optional[str] = None
    amount: Optional[float] = None
    currency: Optional[Literal['RUB', 'UAH', 'EUR', 'USD']] = None
    profit: Optional[float] = None
    commission: Optional[float] = None
    commission_client: Optional[float] = None
    commission_type: Optional[str] = None
    email: Optional[str] = None
    status: Optional[Literal['in_process', 'success', 'expired', 'hold']] = None
    date: Optional[str] = None
    expired_date: Optional[str] = None
    complete_date: Optional[str] = None
    us_vars: Optional[list[str]] = None
