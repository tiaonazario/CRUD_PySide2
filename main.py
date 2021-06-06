from PySide2.QtWidgets import *
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
        self.BotaoAdicionar = QPushButton("Adicionar", self)
        self.BotaoEditar = QPushButton("Editar", self)
        self.BotaoExcluir = QPushButton("Excluir", self)
        self.BotaoPesquisar = QPushButton("Pesquisar", self)
        # Colocar os botões no layout horizontal (LHBotoes)
        self.LHBotoes.addWidget(self.BotaoAdicionar)
        self.LHBotoes.addWidget(self.BotaoEditar)
        self.LHBotoes.addWidget(self.BotaoExcluir)
        self.LHBotoes.addWidget(self.BotaoPesquisar)
        # Paginas
        self.Paginas = QStackedWidget(self)
        self.LVJanela.addWidget(self.Paginas)

    def abrir(self):
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    j = JANELA()
    j.abrir()

    sys.exit(app.exec_())
