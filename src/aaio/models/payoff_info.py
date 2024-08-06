from typing import Optional

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

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

    def is_success(self) -> bool:
        return self.status == 'success'

    def is_in_process(self) -> bool:
        return self.status == 'in_process'

    def is_canceled(self) -> bool:
        return self.status == 'cancel'
