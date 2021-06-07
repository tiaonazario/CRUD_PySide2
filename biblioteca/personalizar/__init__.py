from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

tam = (0, 3000)  # tamanho (minimo, maximo)


def layout(nome, margem=0, espaco=0):
    nome.setMargin(margem)
    nome.setSpacing(espaco)


def frame(nome, tamfixo=''):
    if tamfixo != '':
        nome.setFixedSize(tamfixo[0], tamfixo[1])


def pushbutton(nome, icone=''):
    nome.setFixedSize(50, 50)
    nome.setIcon(QIcon(icone))
    nome.setIconSize(QSize(50, 50))
