import sqlite3


class DADOS:
    def __init__(self):
        # === Criando conexão com o banco de dados ===
        self.Conexao = sqlite3.connect("dados.db")
        self.Indicador = self.Conexao.cursor()
        self.Indicador.execute("""CREATE TABLE IF NOT EXISTS ListarProdutos
                              (codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                              produto TEXT, quantidade INTEGER, tipo TEXT,
                              valor TEXT, datacadastro DATE)""")
        self.Indicador.close()


a = DADOS()
