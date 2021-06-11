from PySide2.QtWidgets import QMainWindow, QWidget, QGridLayout, QFrame, QPushButton, QTextEdit, QStackedWidget, QApplication
import sys
from biblioteca import *
from inicio import INICIO
from adicionar import ADICIONAR
from editar import EDITAR


class PRINCIPAL(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(PRINCIPAL, self).__init__(*args, **kwargs)
        self.setWindowTitle('Controle de Estoque')  # titulo
        self.setMinimumSize(700, 450)  # menores dimensões

        # === === === CORPO DO SOFTWARE === === ===
        self.CentroPrincipal = QWidget(self)  # ferramenta central
        self.setCentralWidget(self.CentroPrincipal)  # definir
        self.LayoutCentroPrincipal = QGridLayout(self)  # plano responsivo
        self.CentroPrincipal.setLayout(self.LayoutCentroPrincipal)  # definir

        # => Quadro que recebe tudo
        self.Quadro = QFrame(self)
        self.LayoutQuadro = QGridLayout(self)  # plano responsivo
        self.Quadro.setLayout(self.LayoutQuadro)
        # adicionar o 'Quadro' no  a ferramenta 'LayoutCentroPrincipal'
        self.LayoutCentroPrincipal.addWidget(self.Quadro)

        # => Botões e caixa de pesquisa
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

        # => Paginas
        self.Paginas = QStackedWidget(self)
        self.LayoutQuadro.addWidget(self.Paginas, 1, 0, 1, 6)
        # Carregar as paginas: INICIO, ADICIONAR, EDITAR
        self.PaginaInicio = INICIO()
        self.PaginaAdicionar = ADICIONAR()
        self.PaginaEditar = EDITAR()
        self.Paginas.addWidget(self.PaginaInicio.CentroInicio)
        self.Paginas.addWidget(self.PaginaAdicionar.CentroAdicionar)
        self.Paginas.addWidget(self.PaginaEditar.CentroEditar)

        # => Chamando as funções
        self.formatar()
        self.clique()

    def formatar(self):
        # widget(self.CentroPrincipal)
        frame(self.Quadro, tamfixolarg=680)
        pushbutton(self.BotaoInicio, 'imagens/svg/inicio.svg',
                   (40, 40), borda='None')
        pushbutton(self.BotaoAdicionar, 'imagens/svg/adicionar.svg',
                   (40, 40), borda='None')
        pushbutton(self.BotaoEditar, 'imagens/svg/editar.svg',
                   (40, 40), borda='None')
        pushbutton(self.BotaoExcluir, 'imagens/svg/excluir.svg',
                   (40, 40), borda='None')
        pushbutton(self.BotaoPesquisar, 'imagens/svg/pesquisar.svg',
                   (40, 40), borda='None')
        textedit(self.CTPesquisa, (250, 30))

    def selpagina(self, indice=0):
        self.Paginas.setCurrentIndex(indice)

    def clique(self):
        self.BotaoInicio.clicked.connect(lambda: self.selpagina(0))
        self.BotaoAdicionar.clicked.connect(lambda: self.selpagina(1))
        self.BotaoEditar.clicked.connect(lambda: self.selpagina(2))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    jan = PRINCIPAL()
    jan.show()

    sys.exit(app.exec_())
