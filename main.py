from paginas.inicio import *
from biblioteca import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys


class JANELA(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(JANELA, self).__init__(*args, **kwargs)
        self.setWindowTitle("Controle de Estoque")  # Titulo da janela
        self.setMinimumSize(600, 400)  # dimensões da janela
        self.CentroJanela = QWidget(self)  # criar uma ferramenta central
        self.setCentralWidget(self.CentroJanela)  # atribuir a Janela
        self.LayoutJanela = QGridLayout(self)
        self.CentroJanela.setLayout(self.LayoutJanela)

        self.Quadro = QFrame(self)
        self.LayoutQuadro = QGridLayout(self)
        self.Quadro.setLayout(self.LayoutQuadro)
        self.LayoutJanela.addWidget(self.Quadro)
        # Botões
        self.BotaoInicio = QPushButton(self)
        self.BotaoAdicionar = QPushButton(self)
        self.BotaoEditar = QPushButton(self)
        self.BotaoExcluir = QPushButton(self)
        self.BotaoPesquisar = QPushButton(self)
        self.CTPesquisa = QTextEdit(self)
        # Colocar os componentes no LayoutQuadro
        self.LayoutQuadro.addWidget(self.BotaoInicio, 0, 0, 1, 1)
        self.LayoutQuadro.addWidget(self.BotaoAdicionar, 0, 1, 1, 1)
        self.LayoutQuadro.addWidget(self.BotaoEditar, 0, 2, 1, 1)
        self.LayoutQuadro.addWidget(self.BotaoExcluir, 0, 3, 1, 1)
        self.LayoutQuadro.addWidget(self.BotaoPesquisar, 0, 4, 1, 1)
        self.LayoutQuadro.addWidget(self.CTPesquisa, 0, 5, 1, 1)
        # Paginas
        self.Paginas = QStackedWidget(self)
        self.LayoutQuadro.addWidget(self.Paginas, 1, 0, 1, 6)
        # carregar as paginas: INICIO, ADICIONAR, EDITAR
        self.PaginaInicio = INICIO()
        self.Paginas.addWidget(self.PaginaInicio.CentroInicio)
        # funções do programa
        self.formatar()

    def formatar(self):
        widget(self.CentroJanela)
        # layout(self.LayoutJanela)
        # layout(self.LayoutQuadro)
        frame(self.Quadro, tamfixolarg=500)
        pushbutton(self.BotaoInicio, 'imagens/svg/inicio.svg', (40, 40))
        pushbutton(self.BotaoAdicionar, 'imagens/svg/adicionar.svg', (40, 40))
        pushbutton(self.BotaoEditar, 'imagens/svg/editar.svg', (40, 40))
        pushbutton(self.BotaoExcluir, 'imagens/svg/excluir.svg', (40, 40))
        pushbutton(self.BotaoPesquisar, 'imagens/svg/pesquisar.svg', (40, 40))
        textedit(self.CTPesquisa, (250, 30))

    def selpagina(self, indice=0):
        self.Paginas.setCurrentIndex(indice)

    def clique(self):
        self.BotaoInicio.clicked(lambda: self.selpagina(0))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    jan = JANELA()
    jan.show()

    sys.exit(app.exec_())
