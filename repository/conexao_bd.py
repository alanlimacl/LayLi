from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


PASTA_DATABASE = Path("database")
ARQUIVO = "banco_teste.db"

PASTA_DATABASE.mkdir(parents=True, exist_ok=True)

CAMINHO_ARQUIVO = (PASTA_DATABASE / ARQUIVO).resolve()

URL_CONEXAO = f"sqlite:///{CAMINHO_ARQUIVO.as_posix()}"

engine = create_engine(url=URL_CONEXAO)
Session = sessionmaker(engine) 

