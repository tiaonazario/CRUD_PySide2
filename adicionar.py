from PySide2.QtWidgets import *
from biblioteca.personalizar import *
import sys


class ADICIONAR(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ADICIONAR, self).__init__(*args, **kwargs)
        self.CentroAdicionar = QWidget(self)
        self.setCentralWidget(self.CentroAdicionar)
        self.LayoutAdicionar = QGridLayout(self)
        self.CentroAdicionar.setLayout(self.LayoutAdicionar)

        self.Quadro = QFrame(self)
        self.LayoutQuadro = QGridLayout(self)
        self.Quadro.setLayout(self.LayoutQuadro)
        self.LayoutAdicionar.addWidget(self.Quadro)

        self.RotuloAdicionar = QLabel('ADICIONAR', self)
        self.RotuloProduto = QLabel('Produto', self)
        self.RotuloQuantidade = QLabel('Quantidade', self)
        self.RotuloTipo = QLabel('Tipo', self)
        self.RotuloValor = QLabel('Valor', self)
        self.RotuloData = QLabel('Data', self)
        self.BotaoSalvar = QPushButton('Salvar', self)

        self.LayoutQuadro.addWidget(self.RotuloAdicionar, 0, 0, 1, 1)
        self.LayoutQuadro.addWidget(self.RotuloProduto, 1, 0, 1, 1)
        self.LayoutQuadro.addWidget(self.RotuloQuantidade, 2, 0, 1, 1)
        self.LayoutQuadro.addWidget(self.RotuloTipo, 3, 0, 1, 1)
        self.LayoutQuadro.addWidget(self.RotuloValor, 4, 0, 1, 1)
        self.LayoutQuadro.addWidget(self.RotuloData, 5, 0, 1, 1)
        self.LayoutQuadro.addWidget(self.BotaoSalvar, 6, 0, 1, 1)

        self.CTProduto = QTextEdit(self)
        self.CTQuantidade = QTextEdit(self)
        self.CBTipo = QComboBox(self)
        self.CTValor = QTextEdit(self)
        self.CTData = QTextEdit(self)
        self.BotaoLimpar = QPushButton('Limpar', self)

        self.LayoutQuadro.addWidget(self.CTProduto, 1, 1, 1, 1)
        self.LayoutQuadro.addWidget(self.CTQuantidade, 2, 1, 1, 1)
        self.LayoutQuadro.addWidget(self.CBTipo, 3, 1, 1, 1)
        self.LayoutQuadro.addWidget(self.CTValor, 4, 1, 1, 1)
        self.LayoutQuadro.addWidget(self.CTData, 5, 1, 1, 1)
        self.LayoutQuadro.addWidget(self.BotaoLimpar, 6, 1, 1, 1)

        self.formatar()

    def formatar(self):
        frame(self.Quadro, tamfixo=(500, 400))
        label(self.RotuloAdicionar, tamfixoalt=60)
        textedit(self.CTProduto, (250, 30))
        textedit(self.CTQuantidade, (250, 30))
        textedit(self.CTValor, (250, 30))
        textedit(self.CTData, (250, 30))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    jan = ADICIONAR()
    jan.show()
    sys.exit(app.exec_())
