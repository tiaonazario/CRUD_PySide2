from PySide2.QtWidgets import *
import sys


class JANELA(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(JANELA, self).__init__(*args, **kwargs)
        self.setWindowTitle("Controle de Estoque")  # titulo da janela
        self.setMinimumSize(600, 400)  # as menores dimensoes aceitavel pelo programa

    def abrir(self):
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    j = JANELA()
    j.abrir()

    sys.exit(app.exec_())
