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

        self.variaveis = ['', 'vprodutor', 'vquantidade',
                          'vtipo', 'vvalor', 'vdatacadastro']

    def novo(self, dados):
        try:
            self.Conexao = sqlite3.connect("dados.db")
            self.Indicador = self.Conexao.cursor()
            for indice, variavel in enumerate(self.variaveis):
                item = dados[indice]
                self.Indicador.execute(
                    "INSERT INTO ListarProdutos" + str(variavel) + "VALUES ?", item)
            self.Conexao.commit()
            self.Indicador.close()
            self.Conexao.close()
            print('Novo produto cadastrado com sucesso')

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


asd = DADOS()

novodados = ['banana', '3', 'Vender', '7', '12/02/2021']

asd.novo(novodados)
