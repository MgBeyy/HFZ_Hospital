from PyQt5.QtWidgets import QApplication, QMainWindow

from UI import login as l
from UI import forgotPass as fp
from UI import mainPatient as mp
from UI import mainDoctor as md


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.loginUi = l.Ui_MainWindow()
        self.setWindowTitle("HFZ Hastanesi")
        self.loginUi.setupUi(self)

        self.loginUi.loginButton.clicked.connect(self.login)

    def login(self):
        if self.loginUi.tcNoLineEdit.text() == 'd':
            self.hide()
            self.doctorUi = DoctorUi()
            self.doctorUi.show()

        elif self.loginUi.tcNoLineEdit.text() == 'p':
            self.hide()
            self.patientUi = PatientUi()
            self.patientUi.show()
            
        else:
            print("Hatalı Giriş.")


class DoctorUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.doctorUi = md.Ui_MainWindow()
        self.setWindowTitle("HFZ Hastanesi")
        self.doctorUi.setupUi(self)


class PatientUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.patientUi = mp.Ui_MainWindow()
        self.setWindowTitle("HFZ Hastanesi")
        self.patientUi.setupUi(self)


App = QApplication([])
window = Main()
window.show()
App.exec()