from PyQt5.QtWidgets import QMainWindow

from UI import forgotPass as fp
from Controller import loginController


class ForgotPassUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.forgotUi = fp.Ui_MainWindow()
        self.forgotUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi")

        self.forgotUi.logInButton.clicked.connect(self.logIn)

    def logIn(self):
        self.close()
        self.logInUi = loginController.loginUi()
        self.logInUi.show()