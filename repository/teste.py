from models.modelos import Usuario, Produto, HistoricoPreco
from repository.conexao_bd import Session


if __name__ == "__main__":
    with Session() as sessao:
        novo_usuario = Usuario(nome="Alan", email="alan@email.com", senha="123")
        
        sessao.add(novo_usuario)
        sessao.commit()
        
        print(f"Usuário: {novo_usuario.nome}, registrado com sucesso!")