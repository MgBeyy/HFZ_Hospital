from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from UI import login as l
from Controller import doctorController, asisstantController, patientController, forgotPassController, \
    createAccController
from Functions import Auth


class loginUi(QMainWindow):
    database_signal = pyqtSignal(object)

    def __init__(self, database_connection):
        super().__init__()

        self.loginUi = l.Ui_MainWindow()
        self.loginUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi")

        self.database_connection = database_connection

        self.loginUi.loginButton.clicked.connect(self.login)
        self.loginUi.forgotPassButton.clicked.connect(self.forgotPass)
        self.loginUi.createAccountButton.clicked.connect(self.createAccount)

    def set_database_connection(self, database_connection):
        self.database_connection = database_connection

    def login(self):
        self.tc_number = self.loginUi.tcNoLineEdit.text()
        self.password = self.loginUi.passwordLineEdit.text()

        if not self.tc_number.isdigit() or len(self.tc_number) != 11:
            self.loginUi.labelInfo.setText("Geçersiz TC No")
            return
        elif len(self.password) == 0:
            self.loginUi.labelInfo.setText("Lütfen Şifrenizi Giriniz.")
            return

        self.authentication = Auth.User(self.database_connection)
        self.is_info_true, self.message = self.authentication.login(self.tc_number, self.password)

        if self.is_info_true:
            self.user_type = self.message.get('user_type')
            if self.user_type == 'D':
                self.close()
                self.doctorUi = doctorController.DoctorUi()
                self.database_signal.connect(self.doctorUi.set_database_connection)
                self.database_signal.emit(self.database_connection)
                self.doctorUi.show()
            elif self.user_type == 'P':
                self.close()
                self.patientUi = patientController.PatientUi()
                self.database_signal.connect(self.patientUi.set_database_connection)
                self.database_signal.emit(self.database_connection)
                self.patientUi.show()
            else:
                self.close()
                self.asistantUi = asisstantController.AsistantUi()
                self.database_signal.connect(self.asistantUi.set_database_connection)
                self.database_signal.emit(self.database_connection)
                self.asistantUi.show()
        else:
            self.loginUi.labelInfo.setText("Hesap Oluşturulamadı")

        # if self.tc_number == 'd':
        #     self.close()
        #     self.doctorUi = doctorController.DoctorUi()
        #     self.doctorUi.show()
        #
        # elif self.tc_number == 'p':
        #     self.close()
        #     self.patientUi = patientController.PatientUi()
        #     self.patientUi.show()
        #
        # elif self.tc_number == 'a':
        #     self.close()
        #     self.asistantUi = asisstantController.AsistantUi()
        #     self.asistantUi.show()
        #
        # else:
        #     self.loginUi.labelInfo.setText("Hatalı Giriş!")
        #     print("Hatalı Giriş.")
        #     return

    def forgotPass(self):
        self.close()
        self.forgotUi = forgotPassController.ForgotPassUi()
        self.database_signal.connect(self.forgotUi.set_database_connection)
        self.database_signal.emit(self.database_connection)
        self.forgotUi.show()

    def createAccount(self):
        self.close()
        self.createAcc = createAccController.CreateAccUi()
        self.database_signal.connect(self.createAcc.set_database_connection)
        self.database_signal.emit(self.database_connection)
        self.createAcc.show()
