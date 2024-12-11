import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

from UI import mainDoctor


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainDoctor.Ui_MainWindow()
        self.ui.setupUi(self)

App = QApplication([])
window = Main()
window.show()
App.exec()