from PySide2.QtWidgets import *
import sys


class ADICIONAR(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ADICIONAR, self).__init__(*args, **kwargs)
        self.CentroAdicionar = QWidget(self)
        self.setCentralWidget(self.CentroAdicionar)
        self.LHAdicionar = QHBoxLayout(self)
        self.CentroAdicionar.setLayout(self.LHAdicionar)

        self.FrameCampos = QFrame(self)
        self.LGCampos = QGridLayout(self)
        self.FrameCampos.setLayout(self.LGCampos)
        self.LHAdicionar.addWidget(self.FrameCampos)

        self.RotuloAdicionar = QLabel('ADICIONAR', self)
        self.RotuloProduto = QLabel('Produto', self)
        self.RotuloQuantidade = QLabel('Quantidade', self)
        self.RotuloTipo = QLabel('Tipo', self)
        self.RotuloValor = QLabel('Valor', self)
        self.RotuloData = QLabel('Data', self)
        self.BotaoSalvar = QPushButton('Salvar', self)

        """ self.CTProduto = QTextEdit(self)
        self.CTQuantidade = QTextEdit(self)
        self.CTTipo = QTextEdit(self)
        self.CTValor = QTextEdit(self)
        self.CTData = QTextEdit(self)
        self.BotaoLimpar = QPushButton(self) """

        self.LGCampos.addWidget(self.RotuloAdicionar, 0, 0, 1, 3)
        self.LGCampos.addWidget(self.RotuloProduto, 1, 1, 1, 1)
        self.LGCampos.addWidget(self.RotuloQuantidade, 2, 1, 1, 1)
        self.LGCampos.addWidget(self.RotuloTipo, 3, 1, 1, 1)
        self.LGCampos.addWidget(self.RotuloValor, 4, 1, 1, 1)
        self.LGCampos.addWidget(self.RotuloData, 5, 1, 1, 1)
        self.LGCampos.addWidget(self.BotaoSalvar, 6, 1, 1, 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    jan = ADICIONAR()
    jan.show()
    sys.exit(app.exec_())
