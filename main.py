"""
uvicorn main:app --reload
"""
import fastapi

app = fastapi.FastAPI()
iden = 5
todos = [
    {"id": 1, "description": "correr", "active": True},
    {"id": 2, "description": "malhar", "active": True},
    {"id": 3, "description": "viajar", "active": False},
    {"id": 4, "description": "comprar", "active": True},
]

@app.get("/pegar")
def pegar(identifica: int=None, ativo: bool=True):
    for dic in todos:
        if dic["id"] == identifica and dic["active"] == ativo:
            return dic
        
@app.post("/inserir")
def inserir(desc: str=None, ativo: bool=True):
    global iden
    try:
        todos.append({"id": iden, "description": desc, "active": ativo})
        iden += 1
        return "Enviado com sucesso"
    except:
        return "Erro no envio"