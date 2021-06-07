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

        self.LVJanela = QVBoxLayout(self)
        self.CentroJanela.setLayout(self.LVJanela)

        self.FrameBotoes = QFrame(self)
        self.LHBotoes = QHBoxLayout(self)
        self.FrameBotoes.setLayout(self.LHBotoes)
        self.LVJanela.addWidget(self.FrameBotoes)
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
        self.LVJanela.addWidget(self.Paginas)

        # funções do programa
        self.formatar()

    def formatar(self):
        layout(self.LVJanela)
        frame(self.FrameBotoes, (500, 60))
        pushbutton(self.BotaoInicio, 'imagens/svg/inicio.svg')
        pushbutton(self.BotaoAdicionar, 'imagens/svg/adicionar.svg')
        pushbutton(self.BotaoEditar, 'imagens/svg/editar.svg')
        pushbutton(self.BotaoExcluir, 'imagens/svg/excluir.svg')
        pushbutton(self.BotaoPesquisar, 'imagens/svg/pesquisar.svg')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    jan = JANELA()
    jan.show()

    sys.exit(app.exec_())
