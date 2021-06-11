from PySide2.QtWidgets import *
from biblioteca import *
import sys


class EDITAR(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(EDITAR, self).__init__(*args, **kwargs)

        # === === === CORPO === === ===
        self.CentroEditar = QWidget(self)
        self.setCentralWidget(self.CentroEditar)
        self.LayoutCentroEditar = QGridLayout(self)
        self.CentroEditar.setLayout(self.LayoutCentroEditar)

        # => Rotulos das labels
        self.RotuloEditar = QLabel('EDITAR', self)
        self.RotuloProduto = QLabel('Produto', self)
        self.RotuloQuantidade = QLabel('Quantidade', self)
        self.RotuloTipo = QLabel('Tipo', self)
        self.RotuloValor = QLabel('Valor', self)
        self.RotuloData = QLabel('Data', self)
        self.BotaoSalvar = QPushButton('Salvar', self)
        # Colocar os componentes no LayoutCentroAdicionar
        self.LayoutCentroEditar.addWidget(self.RotuloEditar, 0, 0, 1, 2)
        self.LayoutCentroEditar.addWidget(self.RotuloProduto, 1, 0, 1, 1)
        self.LayoutCentroEditar.addWidget(self.RotuloQuantidade, 2, 0, 1, 1)
        self.LayoutCentroEditar.addWidget(self.RotuloTipo, 3, 0, 1, 1)
        self.LayoutCentroEditar.addWidget(self.RotuloValor, 4, 0, 1, 1)
        self.LayoutCentroEditar.addWidget(self.RotuloData, 5, 0, 1, 1)
        self.LayoutCentroEditar.addWidget(self.BotaoSalvar, 6, 0, 1, 1)

        # => Caixas de texto e listas
        self.CTProduto = QTextEdit(self)
        self.CTQuantidade = QTextEdit(self)
        self.CBTipo = QComboBox(self)
        self.CTValor = QTextEdit(self)
        self.CTData = QTextEdit(self)
        self.BotaoLimpar = QPushButton('Limpar', self)
        # Colocar os componentes no LayoutCentroAdicionar
        self.LayoutCentroEditar.addWidget(self.CTProduto, 1, 1, 1, 1)
        self.LayoutCentroEditar.addWidget(self.CTQuantidade, 2, 1, 1, 1)
        self.LayoutCentroEditar.addWidget(self.CBTipo, 3, 1, 1, 1)
        self.LayoutCentroEditar.addWidget(self.CTValor, 4, 1, 1, 1)
        self.LayoutCentroEditar.addWidget(self.CTData, 5, 1, 1, 1)
        self.LayoutCentroEditar.addWidget(self.BotaoLimpar, 6, 1, 1, 1)

        self.formatar()

    def formatar(self):
        label(self.RotuloEditar, tamfixoalt=60,
              alinhar=Qt.AlignCenter, estilo=fonte(tamanho='20pt', estilo='bold'))
        label(self.RotuloProduto, estilo=fonte(estilo='bold'))
        label(self.RotuloQuantidade, estilo=fonte(estilo='bold'))
        label(self.RotuloTipo, estilo=fonte(estilo='bold'))
        label(self.RotuloValor, estilo=fonte(estilo='bold'))
        label(self.RotuloData, estilo=fonte(estilo='bold'))
        textedit(self.CTProduto, (250, 30))
        textedit(self.CTQuantidade, (250, 30))
        combobox(self.CBTipo, (250, 30))
        textedit(self.CTValor, (250, 30))
        textedit(self.CTData, (250, 30))
        pushbutton(self.BotaoSalvar, tamfixo=(100, 40))
        pushbutton(self.BotaoLimpar, tamfixo=(100, 40))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    jan = EDITAR()
    jan.show()
    sys.exit(app.exec_())
