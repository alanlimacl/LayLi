from fastapi import APIRouter, Depends, HTTPException, status
from schemas.esquema_requisicao import EsquemaRequisicao

roteador_requisicao = APIRouter(prefix="/requisicao", tags=["Requiscao"])

@roteador_requisicao.get("/")
async def root():
    return {"messages": "Rota Root da Requisição"}


@roteador_requisicao.post("/criar_requisicao", status_code=status.HTTP_201_CREATED)
async def rota_requisicao(esquema_requisicao: EsquemaRequisicao):
    requisicao_teste = esquema_requisicao

    return {"messages": requisicao_teste.model_dump_json()}

