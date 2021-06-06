from PySide2.QtWidgets import *
import sys


class JanelaPrincipal(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(JanelaPrincipal, self).__init__(*args, **kwargs)
        self.setWindowTitle("Controle de Estoque")
        self.setMinimumSize(600, 400)

    def abrir(self):
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    j = JanelaPrincipal()
    j.abrir()

    sys.exit(app.exec_())
