from typing import Optional

from aaio.types.response import AAIOResponse


class PayoffRates(AAIOResponse):
    USD: Optional[float] = None
    UAH: Optional[float] = None
    USDT: Optional[float] = None
    BTC: Optional[float] = None
