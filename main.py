from biblioteca.funcoes import atualizar, codigo, definir, excluir, obter, pesquisar, visualizar
from PySide2.QtWidgets import QMainWindow, QWidget, QGridLayout, QFrame, QPushButton, QLineEdit, QStackedWidget, QApplication
from PySide2.QtGui import QIcon
from PySide2.QtCore import *
import sys
from biblioteca.personalizar import frame, pushbutton, lineedit
from inicio import INICIO
from adicionar import ADICIONAR
from editar import EDITAR


class PRINCIPAL(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(PRINCIPAL, self).__init__(*args, **kwargs)
        self.setWindowTitle("Sistema de Cadastro - CRUD")  # titulo
        self.setMinimumSize(700, 450)  # menores dimensões
        self.setWindowIcon(QIcon('imagens/svg/logo.svg'))

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
        self.CTPesquisa = QLineEdit(self)
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
        lineedit(self.CTPesquisa, (250, 30))

    def selpagina(self, indice=0):
        self.Paginas.setCurrentIndex(indice)

    def ocultarbotao(self, ocultar):
        try:
            botao = [self.BotaoInicio, self.BotaoAdicionar, self.BotaoEditar,
                     self.BotaoExcluir, self.BotaoPesquisar, self.CTPesquisa]
            for indice, valor in enumerate(ocultar):
                if valor.lower() == "s":
                    botao[indice].setEnabled(False)
                else:
                    botao[indice].setEnabled(True)
        except Exception:
            print("ERRO! Não foi possível ocultar o botao")

    def abririnicio(self):
        self.ocultarbotao(['N', 'N', 'N', 'N', 'N', 'N'])
        self.selpagina(0)
        atualizar(self.PaginaInicio.TabelaInicio)

    def abriradicionar(self):
        self.selpagina(1)
        self.ocultarbotao(['N', 'N', 'S', 'S', 'S', 'S'])

    def abrireditar(self):
        self.PaginaEditar.Codigo = ''
        codigoproduto = codigo(self.PaginaInicio.TabelaInicio)
        print(codigoproduto)
        if codigoproduto != '' and codigoproduto != None and codigoproduto != 0:
            self.ocultarbotao(['N', 'S', 'N', 'S', 'S', 'S'])
            self.PaginaEditar.Codigo = codigoproduto
            ferramentas = [self.PaginaEditar.CTProduto,
                           self.PaginaEditar.CTQuantidade, self.PaginaEditar.CBTipo,
                           self.PaginaEditar.CTValor, self.PaginaEditar.CTData]
            valores = visualizar(codigoproduto)
            definir(ferramentas, valores)
            self.selpagina(2)
        else:
            print("ERRO! Selecione um produto na tabela.")

    def pesquisarproduto(self):
        nomeproduto = str(obter([self.CTPesquisa])[0])
        pesquisar(nomeproduto, self.PaginaInicio.TabelaInicio)

    def clique(self):
        self.BotaoInicio.clicked.connect(self.abririnicio)
        self.BotaoAdicionar.clicked.connect(self.abriradicionar)
        self.BotaoEditar.clicked.connect(self.abrireditar)
        self.BotaoExcluir.clicked.connect(
            lambda: excluir(self.PaginaInicio.TabelaInicio))
        self.BotaoPesquisar.clicked.connect(self.pesquisarproduto)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    jan = PRINCIPAL()
    jan.show()

    sys.exit(app.exec_())
