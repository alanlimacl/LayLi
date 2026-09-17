from fastapi import FastAPI
from controller.rota_requisicao import roteador_requisicao

app = FastAPI(title="LayLi - Rastrear Preços",
              description="Api da LayLi para comunicação do sistema.")

app.include_router(roteador_requisicao)
