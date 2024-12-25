from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from Controller.prescriptionController import prescriptionUi
from UI import login as l
from Controller import doctorController, asisstantController, patientController, forgotPassController, \
    createAccController
from Functions import Auth
from Globals import doktor_id


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
        self.is_info_true, self.message= self.authentication.login(self.tc_number, self.password)

        if self.is_info_true:
            import Globals
            self.user_id = self.message.get('user_id')
            self.user_type = self.message.get('user_type')
            Globals.doktor_id =self.user_id
            if self.user_type == 'D':
                cursor = self.database_connection.cursor()
                cursor.execute("""
                                    SELECT DoctorID FROM Doctor WHERE UserID = ?
                                """, (self.user_id,))
                doctor_is_result = cursor.fetchone()

                if doctor_is_result:
                    doctor_id_temp = doctor_is_result[0]
                    Globals.doktor_id = doctor_id_temp

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
            self.loginUi.labelInfo.setText("Hatalı TC veya Şifre")

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
