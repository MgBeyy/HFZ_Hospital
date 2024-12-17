from PyQt5.QtWidgets import QMainWindow

from UI import forgotPass as fp
from Controller import loginController


class ForgotPassUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.forgotUi = fp.Ui_MainWindow()
        self.forgotUi.setupUi(self)

        self.forgotUi.logInButton.clicked.connect(self.logIn)

    def clear(self):
        self.forgotUi.forgotPassTC.clear()
        self.forgotUi.forgotPassPhone.clear()
        self.forgotUi.forgotPassEPosta.clear()

    def logIn(self):
        self.clear()
        self.hide()
        self.logInUi = loginController.loginUi()
        self.logInUi.show()