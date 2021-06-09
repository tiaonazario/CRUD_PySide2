from PySide2.QtWidgets import QMainWindow, QWidget, QGridLayout, QTableWidget, QApplication
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    jan = INICIO()
    jan.show()
    sys.exit(app.exec_())
