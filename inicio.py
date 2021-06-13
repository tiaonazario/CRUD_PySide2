from biblioteca.funcoes import atualizar
from dados import DADOS
from biblioteca.personalizar import table
from PySide2.QtWidgets import QMainWindow, QWidget, QGridLayout, QTableWidget, QApplication, QAbstractItemView
import sys


class INICIO(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(INICIO, self).__init__(*args, **kwargs)

        # === === === CORPO === === ===
        self.CentroInicio = QWidget(self)
        self.setCentralWidget(self.CentroInicio)
        self.LayoutCentroInicio = QGridLayout(self)
        self.CentroInicio.setLayout(self.LayoutCentroInicio)

        self.TabelaInicio = QTableWidget(self)
        self.LayoutCentroInicio.addWidget(self.TabelaInicio, 0, 1, 1, 1)

        self.formatar()
        self.carregar()

    def formatar(self):
        table(self.TabelaInicio)

    def carregar(self):
        atualizar(self.TabelaInicio)
        # self.basedados.carregar(self.TabelaInicio)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    jan = INICIO()
    jan.show()
    sys.exit(app.exec_())
