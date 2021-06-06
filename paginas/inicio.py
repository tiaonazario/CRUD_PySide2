from PySide2.QtWidgets import *
import sys


class INICIO(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(INICIO, self).__init__(*args, **kwargs)
        self.setMinimumSize(600, 400)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    jan = INICIO()
    jan.show()
    sys.exit(app.exec_())
