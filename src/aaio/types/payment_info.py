from typing import Optional, List

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

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
    profit: Optional[float] = None
    commission: Optional[float] = None
    commission_client: Optional[float] = None
    commission_type: Optional[str] = None
    email: Optional[str] = None
    status: Literal['in_process', 'success', 'expired', 'hold']
    date: str
    expired_date: str
    complete_date: Optional[str] = None
    us_vars: List[str]

    def is_success(self) -> bool:
        return self.status == 'success'

    def is_in_process(self) -> bool:
        return self.status == 'in_process'

    def is_on_hold(self) -> bool:
        return self.status == 'hold'

    def is_expired(self) -> bool:
        return self.status == 'expired'
