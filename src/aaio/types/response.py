from typing import Optional, Literal

from pydantic import BaseModel


class AAIOResponse(BaseModel):
    type: Literal['error', 'success']
    code: Optional[int] = None
    message: Optional[str] = None
