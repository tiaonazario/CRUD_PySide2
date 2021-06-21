from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


def fonte(nome='MS Sans Serif', tamanho='12pt', estilo=''):
    return f'font:{estilo} {nome}; font-size:{tamanho};'


def combobox(nome, tamfixo=''):
    if tamfixo != '':
        nome.setFixedSize(tamfixo[0], tamfixo[1])
    nome.setStyleSheet(fonte())


def frame(nome, tamfixo='', tamfixolarg='', tamfixoalt=''):
    if tamfixo != '':
        nome.setFixedSize(tamfixo[0], tamfixo[1])
    if tamfixolarg != '':
        nome.setFixedWidth(tamfixolarg)
    if tamfixoalt != '':
        nome.setFixedHeight(tamfixoalt)


def label(nome, tamfixoalt='', alinhar='', estilo=fonte()):
    if alinhar != '':
        nome.setAlignment(alinhar)
    if tamfixoalt != '':
        nome.setFixedHeight(tamfixoalt)
    nome.setStyleSheet(estilo)


def layout(nome, margem=0, espaco=0):
    """
    Função para personalizar os objetos QVBoxLayout, QHLayout e QGridLayout
    """
    nome.setMargin(margem)
    nome.setSpacing(espaco)


def pushbutton(nome, icone='', tamfixo='', estilo=fonte(), borda='', fundo=''):
    if tamfixo != '':
        nome.setFixedSize(tamfixo[0], tamfixo[1])
        nome.setIconSize(QSize(tamfixo[0], tamfixo[1]))
    if icone != '':
        nome.setIcon(QIcon(icone))
    nome.setStyleSheet(f'{estilo} border:{borda}; background-color:{fundo};')
    nome.setCursor(Qt.OpenHandCursor)


def table(nome, estilo=fonte()):
    tamcoluna = [30, 150, 70, 100, 100, 100]
    cabecalho = ['ID', 'PRODUTO', 'QTD.', 'TIPO', 'VALOR', 'DATA']

    nome.setColumnCount(6)
    nome.horizontalHeader().setStretchLastSection(True)
    nome.setEditTriggers(QAbstractItemView.NoEditTriggers)
    nome.setSelectionBehavior(QAbstractItemView.SelectRows)
    nome.horizontalHeader().setVisible(True)
    nome.verticalHeader().setVisible(False)
    for numero, valor in enumerate(tamcoluna):
        nome.setColumnWidth(numero, valor)
    nome.setHorizontalHeaderLabels(cabecalho)
    nome.setStyleSheet(estilo)
    """ nome.setStyleSheet('''QTableWidget {padding: #262626; border-radius: 10px;
                      gridline-color: 5px; border-bottom: 1px #262626}
                      QTableWidget::item {border-color: #000000; padding-left: 5px; padding-right: 5px; gridline-color: #000000}
                      QTableWidget::item:selected {background-color: #424242}
                      QScrollBar:horizontal {border:None; background: #BB2020; height:14px; margin: 0px 21px 0px 21px; border-radius: 0px}
                      QScrollBar:vertical {border:None; background: #BB2020; height:14px; margin: 0px 21px 0px 21px; border-radius: 0px}
                      QHeaderView::section{Background-color: #FFEB4D;max-width: 30px; border: 1px #FFEB4D; border-style: None; border-bottom: 1px #FFEB4D; border-right: 1px #FFEB4D}
                      QTableWidget::horizontalHeader {background-color: #A68F1F}
                      QHeaderView::section:horizontal {border: 1px #FFEB4D; background-color: #506AD4; padding: 3px; border-top-left-radius: 7px; border-top-right-radius: 7px}
                      QHeaderView::section:vertical {border: 1px #FFEB4D}''') """


def lineedit(nome, tamfixo='', estilo=fonte()):
    if tamfixo != '':
        nome.setFixedSize(tamfixo[0], tamfixo[1])
    nome.setStyleSheet(estilo)
