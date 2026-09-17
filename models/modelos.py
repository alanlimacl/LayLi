from sqlalchemy import Column, Integer, Float, String, ForeignKey, event, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime, UTC, timezone

from repository.conexao_bd import engine

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    senha = Column(String(100), nullable=False)
    
    # RELACIONAMENTO: Se o usuário sumir, os produtos somem.
    # Se remover um produto da lista do usuário, o produto é deletado
    produtos = relationship("Produto", back_populates="usuario", cascade="all, delete-orphan")
    
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        

class Produto(Base):
    __tablename__ = "produtos"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    preco_inicial = Column(Float)
    preco_desejado = Column(Float, nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"))

    usuario = relationship("Usuario", back_populates="produtos")
    historico_precos = relationship("HistoricoPreco", back_populates="produtos", cascade="all, delete-orphan")
    

    def __init__(self, nome, preco_inicial, preco_desejado, id_usuario):
        self.nome = nome
        self.preco_inicial = preco_inicial
        self.preco_desejado = preco_desejado
        self.id_usuario = id_usuario


class HistoricoPreco(Base):
    __tablename__ = "historico_precos"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_produto = Column(Integer, ForeignKey("produtos.id"))
    preco_inicial = Column(Float) 
    data_registro = Column(DateTime, default= lambda: datetime.now(timezone.utc))
    
    produtos = relationship("Produto", back_populates="historico_precos")
    
    # def __init__(self, preco_inicial):
    #     self.preco_inicial = preco_inicial


Base.metadata.create_all(engine)


@event.listens_for(Produto, 'init')
def receber_novo_produto(target, args, kwargs):
    preco_inicial = kwargs.get('preco_inicial')
    
    if preco_inicial is not None:
        # Adiciona o histórico diretamente na relação do produto
        target.historico_precos.append(HistoricoPreco(preco_inicial=preco_inicial))
        
    

