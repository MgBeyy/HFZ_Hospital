from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from UI import forgotPass as fp
from Controller import loginController


class ForgotPassUi(QMainWindow):
    database_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.forgotUi = fp.Ui_MainWindow()
        self.forgotUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi")

        self.forgotUi.logInButton.clicked.connect(self.logIn)

    def set_database_connection(self, database_connection):
        self.database_connection = database_connection
        print("Database bağlantısı alındı")

    def logIn(self):
        self.close()
        self.logInUi = loginController.loginUi(self.database_connection)
        self.logInUi.show()