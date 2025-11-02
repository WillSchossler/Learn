from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    texto: str
    estado: bool = False


tarefas = [
    Todo(texto="Dançar"),
    Todo(texto="Estudar"),
    Todo(texto="Trabalhar"),
    Todo(texto="Dançar"),
    Todo(texto="Estudar"),
    Todo(texto="Trabalhar"),
]


@app.get("/")
def home():
    return "Bem vindo à página inicial!"


@app.get("/tarefa")
def tarefa(index: int):
    return tarefas[index]

@app.post("/tarefa")
def colocar(dado: Todo):
    tarefas.append(dado)
    return "Sucesso"