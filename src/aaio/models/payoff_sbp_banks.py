from pydantic import BaseModel


class SbpBank(BaseModel):
    bankId: str
    bankName: str
    bankIcon: str


class PayoffSbpBanks(BaseModel):
    list: list[SbpBank]
