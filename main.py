import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from backend_ui import Ui_MainWindow
from backend_connection import Connect

class MainWindow(QMainWindow):
    def __init__(self, APP):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("8BALLPOOL_IMG_LABELER")
        Connect(self.ui)  # connect front end to backend

if __name__ == '__main__':
    APP = QApplication(sys.argv)
    window = MainWindow(APP)
    window.setWindowIcon(QIcon("./BLANK.jpg"))
    window.show()
    sys.exit(APP.exec_())
