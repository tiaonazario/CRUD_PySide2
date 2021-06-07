from paginas.inicio import INICIO
from biblioteca.personalizar import *
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
        self.LGJanela = QGridLayout(self)
        self.CentroJanela.setLayout(self.LGJanela)

        self.FrameBotoes = QFrame(self)
        self.LHBotoes = QHBoxLayout(self)
        self.FrameBotoes.setLayout(self.LHBotoes)
        self.LGJanela.addWidget(self.FrameBotoes, 0, 1, 1, 1)
        # Botões
        self.BotaoInicio = QPushButton(self)
        self.BotaoAdicionar = QPushButton(self)
        self.BotaoEditar = QPushButton(self)
        self.BotaoExcluir = QPushButton(self)
        self.BotaoPesquisar = QPushButton(self)
        self.CTPesquisa = QTextEdit(self)
        # Colocar os componentes no layout horizontal (LHBotoes)
        self.LHBotoes.addWidget(self.BotaoInicio)
        self.LHBotoes.addWidget(self.BotaoAdicionar)
        self.LHBotoes.addWidget(self.BotaoEditar)
        self.LHBotoes.addWidget(self.BotaoExcluir)
        self.LHBotoes.addWidget(self.BotaoPesquisar)
        self.LHBotoes.addWidget(self.CTPesquisa)
        # Paginas
        self.Paginas = QStackedWidget(self)
        self.LGJanela.addWidget(self.Paginas, 1, 0, 1, 3)
        # carregar as paginas: INICIO, ADICIONAR, EDITAR
        self.PaginaInicio = INICIO()
        self.Paginas.addWidget(self.PaginaInicio.CentroInicio)
        # funções do programa
        self.formatar()

    def formatar(self):
        widget(self.CentroJanela)
        layout(self.LGJanela)
        frame(self.FrameBotoes, (500, 60))
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
