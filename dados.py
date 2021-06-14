import sqlite3
from PySide2.QtWidgets import QTableWidgetItem


class DADOS:
    def __init__(self):
        # === === === Criando conexão === === ===
        self.Conexao = sqlite3.connect("dados.db")
        self.Indicador = self.Conexao.cursor()
        self.Indicador.execute("""CREATE TABLE IF NOT EXISTS ListarProdutos
                              (codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                              produto TEXT, quantidade INTEGER, tipo TEXT,
                              valor TEXT, datacadastro DATE)""")
        self.Indicador.close()

        self.variaveis = ["produto", "quantidade",
                          "tipo", "valor", "datacadastro"]

    def novo(self, dados):
        try:
            self.Conexao = sqlite3.connect("dados.db")
            self.Indicador = self.Conexao.cursor()
            self.Indicador.execute(
                """INSERT INTO ListarProdutos
                (produto, quantidade, tipo, valor, datacadastro) VALUES
                (?, ?, ?, ?, ?)""", dados)
            self.Conexao.commit()
            self.Indicador.close()
            self.Conexao.close()
            print('Produto cadastrado')

        except Exception:
            print('ERRO! Não foi possivel salvar esse produto')

    def carregar(self, tabela):
        self.Conexao = sqlite3.connect("dados.db")
        inquerir = "SELECT * FROM ListarProdutos"
        resultado = self.Conexao.execute(inquerir)
        tabela.setRowCount(0)
        for linha, valorlinha in enumerate(resultado):
            tabela.insertRow(linha)
            for coluna, valorcoluna in enumerate(valorlinha):
                tabela.setItem(
                    linha, coluna, QTableWidgetItem(str(valorcoluna)))

    def editar(self, codigo, dados):
        try:
            self.Conexao = sqlite3.connect("dados/bdgeral.db")
            self.Indicador = self.Conexao.cursor()
            for indice, valor in enumerate(self.variaveis):
                dado = dados[valor]
                self.Indicador.execute("UPDATE ListarProdutos SET " + str(valor) +
                                       " = ? WHERE codigo = ?", (dado, codigo))
            self.Conexao.commit()
            self.Indicador.close()
            self.Conexao.close()
            print("Dados editados com sucesso")
        except Exception:
            print("ERRO!")

    def visualizar(self, codigo):
        try:
            self.Conexao = sqlite3.connect("dados/bdgeral.db")
            self.Indicador = self.Conexao.cursor()
            resultado = self.Indicador.execute(
                "SELECT * from ListarProdutos WHERE codigo =" + str(codigo))
            encontrado = resultado.fetchone()
            self.Conexao.commit()
            self.Indicador.close()
            self.Conexao.close()
            return encontrado
        except Exception:
            print("ERRO!")

    def excluir(self, codigo):
        try:
            self.Conexao = sqlite3.connect("dados.db")
            self.Indicador = self.Conexao.cursor()
            self.Indicador.execute(
                "DELETE from ListarProdutos WHERE codigo =" + str(codigo))
            self.Conexao.commit()
            self.Indicador.close()
            self.Conexao.close()
            print('Produto deletado')
        except Exception:
            print('ERRO')

    def pesquisar(self, nome, tabela):
        try:
            self.Conexao = sqlite3.connect("dados.db")
            self.Indicador = self.Conexao.cursor()
            resultado = self.Indicador.execute(
                "SELECT * FROM ListarProdutos WHERE produto LIKE '%" + nome + "%' ")

            tabela.setRowCount(0)
            for linha, linhavalor in enumerate(resultado):
                tabela.insertRow(linha)
                for coluna, colunavalor in enumerate(linhavalor):
                    tabela.setItem(linha, coluna,
                                   QTableWidgetItem(str(colunavalor)))

            self.Conexao.commit()
            self.Indicador.close()
            self.Conexao.close()

        except Exception:
            print("ERRO!\nNão foi possivel realisar a pesquisa.")
