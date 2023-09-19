from pydantic import BaseModel


class PayoffRates(BaseModel):
    USD: float
    UAH: float
    USDT: float
    BTC: float
