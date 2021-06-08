from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# tam = (0, 3000)  # tamanho (minimo, maximo)


def estilo(corfundo='#262626', cor='#ffffff', fonte='bold MS Sans Serif', tamanho='12pt'):
    formato = f'''background-color: {corfundo}; color: {cor}; font: {fonte};
    font-size: {tamanho}'''
    return formato


def widget(nome, fonte=estilo()):
    nome.setStyleSheet(fonte)


def layout(nome, margem=0, espaco=0):
    """
    Função para personalizar os objetos QVBoxLayout, QHLayout e QGridLayout
    """
    nome.setMargin(margem)
    nome.setSpacing(espaco)


def frame(nome, tamfixo='', tamfixolarg='', tamfixoalt=''):
    if tamfixo != '':
        nome.setFixedSize(tamfixo[0], tamfixo[1])
    if tamfixolarg != '':
        nome.setFixedWidth(tamfixolarg)
    if tamfixoalt != '':
        nome.setFixedHeight(tamfixoalt)


def pushbutton(nome, icone='', tamfixo=''):
    if tamfixo != '':
        nome.setFixedSize(tamfixo[0], tamfixo[1])
        nome.setIconSize(QSize(tamfixo[0], tamfixo[1]))
    if icone != '':
        nome.setIcon(QIcon(icone))


def label(nome, tamfixo='', tamfixolarg='', tamfixoalt='', alinhar=''):
    # nome.setStyleSheet(fonte)
    if alinhar != '':
        nome.setAlignment(alinhar)
    if tamfixo != '':
        nome.setFixedSize(tamfixo[0], tamfixo[1])
    if tamfixolarg != '':
        nome.setFixedWidth(tamfixolarg)
    if tamfixoalt != '':
        nome.setFixedHeight(tamfixoalt)


def textedit(nome, tamfixo=''):
    if tamfixo != '':
        nome.setFixedSize(tamfixo[0], tamfixo[1])


def combobox(nome, tamfixo=''):
    if tamfixo != '':
        nome.setFixedSize(tamfixo[0], tamfixo[1])
