from typing import Optional
from pydantic import BaseModel

class PersonagensOnePiece(BaseModel):
    id: Optional[int] = None
    name: str
    fruta: str
    recompensa: float
    funcao: str
    foto: str
    
