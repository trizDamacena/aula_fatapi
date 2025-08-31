from typing import Optional
from pydantic import BaseModel
from datetime import date

class albunsTaylorSwift(BaseModel):
    id: Optional[int] | None = None 
    nameAlbum: str
    single: str 
    dataLancamento: int
    produtora: str

