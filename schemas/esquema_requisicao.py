from pydantic import BaseModel

class EsquemaRequisicao(BaseModel):
    link_produto: str
    email_usuario: str
    preco_desejado: str
    
    class Config:
        from_attributes = True
        