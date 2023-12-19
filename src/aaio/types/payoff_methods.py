from typing import Dict

from pydantic import BaseModel


class PayoffMethod(BaseModel):
    name: str
    min: float
    max: float
    commission_percent: float
    commission_sum: float


class PayoffMethods(BaseModel):
    list: Dict[str, PayoffMethod]
