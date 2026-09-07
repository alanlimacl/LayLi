from fastapi import APIRouter, Depends, HTTPException, status

roteador_requisicao = APIRouter(prefix="/requisitar", tags=["Requisitar"])

@roteador_requisicao.post("/")
async def root():
    return {"messages": "Rota Root da Requisição"}


@roteador_requisicao.post("/")
async def rota_requisicao():
    