from PySide2.QtWidgets import *
import sys


class INICIO(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(INICIO, self).__init__(*args, **kwargs)
        self.CentroInicio = QWidget(self)
        self.setCentralWidget(self.CentroInicio)
        self.LGInicio = QGridLayout(self)
        self.CentroInicio.setLayout(self.LGInicio)

        self.TabelaInicio = QTableWidget(self)
        self.LGInicio.addWidget(self.TabelaInicio, 0, 1, 1, 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    jan = INICIO()
    jan.show()
    sys.exit(app.exec_())
