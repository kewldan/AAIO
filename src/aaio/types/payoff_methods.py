from typing import Optional

from pydantic import BaseModel

from aaio.types.response import AAIOResponse


class PayoffMethod(BaseModel):
    name: str
    min: float
    max: float
    commission_percent: float
    commission_sum: float


class PayoffMethods(AAIOResponse):
    list: Optional[dict[str, PayoffMethod]] = None
