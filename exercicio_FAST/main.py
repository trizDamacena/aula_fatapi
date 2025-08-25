from fastapi import FastAPI, HTTPException, status
from models import albunsTaylorSwift

app = FastAPI()

albuns = {
    1:{
        "nomeAlbum": "Taylor Swift",
        "single": "Tim McGraw",
        "anoLancamento": 2006,
        "produtora": "Big Machine Records"
    }
}

#Personagem especifico
@app.get("/albuns/{album_id}")
async def get_album(album_id: int):
    album = albuns[album_id]
    return album
#------------------------------------------


@app.get("/albuns")
def get_musicas():
    return albuns

@app.post("/album", status_code=status.HTTP_201_CREATED)
async def post_albuns(album: albunsTaylorSwift):
    id_proximo = len(albuns) + 1
    albuns[id_proximo] = album

@app.put("/albuns/{album_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_album(album_id:int, album: albunsTaylorSwift):
    if album_id in albuns:
        albuns[album_id] = album 
        album.id = album_id
        del album.id
        return album
    
@app.delete("/albuns/{album_id}")
async def del_album(album_id: int, pesonagem: albunsTaylorSwift):
    if album_id in albuns:
        del albuns[album_id]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Albúm não encontrado")