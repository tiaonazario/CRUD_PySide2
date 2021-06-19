from dados import DADOS
from biblioteca.funcoes import *
from PySide2.QtWidgets import *
from biblioteca import *
import sys


class ADICIONAR(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ADICIONAR, self).__init__(*args, **kwargs)

        # === === === CORPO === === ===
        self.CentroAdicionar = QWidget(self)
        self.setCentralWidget(self.CentroAdicionar)
        self.LayoutCentroAdicionar = QGridLayout(self)
        self.CentroAdicionar.setLayout(self.LayoutCentroAdicionar)

        # => Rotulos das labels
        self.RotuloAdicionar = QLabel('ADICIONAR', self)
        self.RotuloProduto = QLabel('Produto', self)
        self.RotuloQuantidade = QLabel('Quantidade', self)
        self.RotuloTipo = QLabel('Tipo', self)
        self.RotuloValor = QLabel('Valor', self)
        self.RotuloData = QLabel('Data', self)
        self.BotaoSalvar = QPushButton('Salvar', self)
        # Colocar os componentes no LayoutCentroAdicionar
        self.LayoutCentroAdicionar.addWidget(self.RotuloAdicionar, 0, 0, 1, 2)
        self.LayoutCentroAdicionar.addWidget(self.RotuloProduto, 1, 0, 1, 1)
        self.LayoutCentroAdicionar.addWidget(self.RotuloQuantidade, 2, 0, 1, 1)
        self.LayoutCentroAdicionar.addWidget(self.RotuloTipo, 3, 0, 1, 1)
        self.LayoutCentroAdicionar.addWidget(self.RotuloValor, 4, 0, 1, 1)
        self.LayoutCentroAdicionar.addWidget(self.RotuloData, 5, 0, 1, 1)
        self.LayoutCentroAdicionar.addWidget(self.BotaoSalvar, 6, 0, 1, 1)

        # => Caixas de texto e listas
        self.CTProduto = QLineEdit(self)
        self.CTQuantidade = QLineEdit(self)
        self.CBTipo = QComboBox(self)
        self.CTValor = QLineEdit(self)
        self.CTData = QLineEdit(self)
        self.BotaoLimpar = QPushButton('Limpar', self)
        # Colocar os componentes no LayoutCentroAdicionar
        self.LayoutCentroAdicionar.addWidget(self.CTProduto, 1, 1, 1, 1)
        self.LayoutCentroAdicionar.addWidget(self.CTQuantidade, 2, 1, 1, 1)
        self.LayoutCentroAdicionar.addWidget(self.CBTipo, 3, 1, 1, 1)
        self.LayoutCentroAdicionar.addWidget(self.CTValor, 4, 1, 1, 1)
        self.LayoutCentroAdicionar.addWidget(self.CTData, 5, 1, 1, 1)
        self.LayoutCentroAdicionar.addWidget(self.BotaoLimpar, 6, 1, 1, 1)

        self.formatar()
        self.clique()

    def formatar(self):
        label(self.RotuloAdicionar, tamfixoalt=60,
              alinhar=Qt.AlignCenter, estilo=fonte(tamanho='20pt', estilo='bold'))
        label(self.RotuloProduto, estilo=fonte(estilo='bold'))
        label(self.RotuloQuantidade, estilo=fonte(estilo='bold'))
        label(self.RotuloTipo, estilo=fonte(estilo='bold'))
        label(self.RotuloValor, estilo=fonte(estilo='bold'))
        label(self.RotuloData, estilo=fonte(estilo='bold'))
        lineedit(self.CTProduto, (250, 30))
        lineedit(self.CTQuantidade, (250, 30))
        combobox(self.CBTipo, (250, 30))
        lista(['Comprar', 'Vender'], self.CBTipo)
        lineedit(self.CTValor, (250, 30))
        lineedit(self.CTData, (250, 30))
        pushbutton(self.BotaoSalvar, tamfixo=(100, 40))
        pushbutton(self.BotaoLimpar, tamfixo=(100, 40))

    def salvarproduto(self):
        matriz = [self.CTProduto, self.CTQuantidade,
                  self.CBTipo, self.CTValor, self.CTData]
        variaveis = obter(matriz)
        salvar(variaveis)

    def limparcampos(self):
        matriz = [self.CTProduto, self.CTQuantidade,
                  self.CBTipo, self.CTValor, self.CTData]
        definir(matriz, ['', '', '', '', '', ''])

    def clique(self):
        self.BotaoSalvar.clicked.connect(self.salvarproduto)
        self.BotaoLimpar.clicked.connect(self.limparcampos)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    jan = ADICIONAR()
    jan.show()
    sys.exit(app.exec_())
