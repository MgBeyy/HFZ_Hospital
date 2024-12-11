import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi


app = QApplication(sys.argv)
widget = loadUi('UI\\mainDoctor.ui')
widget.show()
sys.exit(app.exec_())
