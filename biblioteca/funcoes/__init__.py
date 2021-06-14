from dados import DADOS
from biblioteca import *


def lista(itens, caixacombinacao):
    for indice, item in enumerate(itens):
        caixacombinacao.addItem(item)


def atualizar(tabela):
    basedados = DADOS()
    basedados.carregar(tabela)


def entradas(valores):
    try:
        lista = []
        for valor in valores:
            tipo = str(type(valor))
            tipo = tipo.split(".")
            tipo = tipo[2].replace("'>", "")
            if tipo == 'QComboBox':
                variavel = valor.itemText(valor.currentIndex())
            if tipo == 'QLineEdit':
                variavel = valor.text()
            lista.append(variavel)
        return lista
    except Exception:
        print('ERRO! VERIFIQUE A FUNÇÃO produto')


def codigo(ferramenta):
    try:
        codigo = ferramenta.currentRow()
        if codigo >= 0:
            novocodigo = ferramenta.item(codigo, 0).text()
        else:
            novocodigo = 0
        return int(novocodigo)
    except Exception:
        pass


def excluir(ferramenta):
    try:
        novocodigo = codigo(ferramenta)
        if novocodigo == 0:
            print("Selecione um cliente na tabela")
        else:
            basedados = DADOS()
            basedados.excluir(novocodigo)
            atualizar(ferramenta)
    except Exception:
        print("ERRO!")
