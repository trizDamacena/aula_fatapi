from typing import Optional
from pydantic import BaseModel
from datetime import date

class PersonagensOnePiece(BaseModel):
    id: Optional[int] = None
    name: str
    fruta: str
    recompensa: float
    funcao: str
    foto: str
    
class MusicasTaylorSwift(BaseModel):
    id: Optional[int] = None
    name: str
    album: str 
    dataLancamento: date
    