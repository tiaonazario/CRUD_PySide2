from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


def layout(nome, margem=0, espaco=0):
    try:
        nome.setMargin(margem)
        nome.setSpacing(espaco)
    except:
        print("ERRO!\nVerifique se os parametros foram ofertados corretamente.")


def pushbutton(nome, icone=''):
    nome.setFixedSize(50, 50)
    nome.setIcon(QIcon(icone))
    nome.setIconSize(QSize(50, 50))
