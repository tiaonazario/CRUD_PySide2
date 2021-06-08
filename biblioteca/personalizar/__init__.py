from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# tam = (0, 3000)  # tamanho (minimo, maximo)
estilo = '''background-color: #262626; color: #ffffff; font: MS Sans Serif; font-size: 12pt'''


def widget(nome, fonte=estilo):
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


def label(nome, tamfixo=''):
    if tamfixo != '':
        nome.setFixedSize(tamfixo[0], tamfixo[1])


def textedit(nome, tamfixo=''):
    if tamfixo != '':
        nome.setFixedSize(tamfixo[0], tamfixo[1])
