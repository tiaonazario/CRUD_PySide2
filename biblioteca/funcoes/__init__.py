from dados import DADOS
from biblioteca import *


def lista(itens, caixacombinacao):
    for indice, item in enumerate(itens):
        caixacombinacao.addItem(item)


def atualizar(tabela):
    basedados = DADOS()
    basedados.carregar(tabela)


def obter(valores):
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


def definir(ferramentas, valores):
    try:
        for indice, valor in enumerate(ferramentas):
            tipo = str(type(valor))
            tipo = tipo.split(".")
            tipo = tipo[2].replace("'>", "")
            if tipo == 'QComboBox':
                valor.setCurrentText(str(valores[indice+1]))
            if tipo == 'QLineEdit':
                valor.setText(str(valores[indice+1]))
    except Exception:
        print("ERRO! VERIFIQUE A FUNÇÃO 'produto'")


def salvar(variaveis):
    bancodados = DADOS()
    bancodados.novo(variaveis)


def codigo(ferramenta):
    try:
        codigo = ferramenta.currentRow()
        if codigo >= 0:
            novocodigo = ferramenta.item(codigo, 0).text()
        else:
            novocodigo = 0
        return int(novocodigo)
    except Exception:
        print('ERRO! Não foi possível determinar o código')


def visualizar(codigoproduto):
    bancodados = DADOS()
    valores = bancodados.visualizar(codigoproduto)
    print(valores)
    return valores


def editar(codigoproduto, variaveis):
    try:
        bancodados = DADOS()
        bancodados.editar(codigoproduto, variaveis)
    except Exception:
        print('ERRO!')


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


def pesquisar(nomeproduto, ferramenta):
    try:
        bancodados = DADOS()
        bancodados.pesquisar(nomeproduto, ferramenta)
    except Exception:
        print("ERRO!")
