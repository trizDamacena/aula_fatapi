from fastapi import FastAPI, HTTPException, status
from models import PersonagensOnePiece
from typing import Any
from routes import curso_router, usuario_router
import requests


app = FastAPI(title="API dos personagens de One Piece - DS17", version="0.01",
              description="Uma API para o estudar de FASTAPI")

app.include_router(curso_router.router, tags=["Cursos"])
app.include_router(usuario_router.router, tags=["Usuário"])

@app.get("/personagem/{personagem_id}")
def get_ponei(id: int):
    response = requests.get(f"https://ponyapi.net/v1/character/{id}")

    if response.status_code == 200:
        return response.json()
    else:
        return {"Message": "Ponei não encontrado"}


def fake_db():
    try:
        print("Abrindo conexão com banco de dados")
    finally:
        print("Conexão oncluída")

personagens = {
    1:{
        "nome": "Monkey: D. Luffy",
        "fruta": "Gomu no Go",
        "recompensa": 30000000,
        "funcao": "Capitão",
        "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4NC9L7JTEnCCw0e-KdL8UHflzZleTuC1cNw&s"

    },

    2:{
        "nome": "Trafalgar D. Water Law",
        "fruta": "Ope Ope no Mi",
        "recompensa": 30000000,
        "funcao": "Capitão",
        "foto": "https://cdn.selectgame.net/wp-content/uploads/2023/01/Trafalgar-D.-Water-Law-de-One-Piece-01.jpg"
    }
}

@app.get("/")
def teste():
    return {"Mensagem": "Fun"}

@app.get("/personagens")
async def get_personagens():
    return personagens


#Personagem especifico
@app.get("/personagens/{personagem_id}", description="Retora 1 personagem com ID especifico ou retorna o erro 404",
         summary="Retorna um personagem especifico")

async def get_personagem(personagem_id: int):
    try:
        personagem = personagens[personagem_id]
        return personagem
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")
    

#Criar personagem
@app.post("/personagens", status_code=status.HTTP_201_CREATED)
async def post_personagem(personagem: PersonagensOnePiece):
    next_id = len(personagens) + 1
    personagens[next_id] = personagem

    
    return personagem 


#Editar informações do usuário
@app.put("/personagens/{personagem_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_personagem(personagem_id: int, personsagem: PersonagensOnePiece):
    if personagem_id in personagens:
        personagens[personagem_id] = personsagem
        personsagem.id = personagem_id
        del personsagem.id
        return personsagem

#Deletar personagem:
@app.delete("/personagens/{personagem_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_usuario(personagem_id: int):
    if personagem_id in personagens: 
        del personagens[personagem_id]
        
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")
    

@app.get("/calculadora")
async def calcular(a: int, b: int):
    soma = a + b
    return print(f"Soma: {soma}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port= 8002, log_level="info", reload=True)


# Exercicio, API Taylor Swift

