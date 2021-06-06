from PySide2.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Controle de Estoque")
        self.setMinimumSize(600, 400)

    def abrir(self):
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    j = MainWindow()
    j.abrir()

    sys.exit(app.exec_())
