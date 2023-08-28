from typing import Optional

from aaio.types.response import AAIOResponse


class Balance(AAIOResponse):
    balance: Optional[float] = None
    referral: Optional[float] = None
    hold: Optional[float] = None
