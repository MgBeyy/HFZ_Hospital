from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from UI import createAccount as ca
from Controller import loginController
from Functions import Auth


class CreateAccUi(QMainWindow):
    database_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.Ui = ca.Ui_MainWindow()
        self.Ui.setupUi(self)

        self.database_connection = None

        self.Ui.logInButton.clicked.connect(self.logIn)
        self.Ui.createAccountButton.clicked.connect(self.createAcc)

    def set_database_connection(self, database_connection):
        self.database_connection = database_connection
        print("Database bağlantısı alındı")

    def logIn(self):
        self.close()
        self.logInUi = loginController.loginUi(self.database_connection)
        self.logInUi.show()

    def createAcc(self):
        self.name = self.Ui.nameLineEdit.text()
        self.surname = self.Ui.lastNameLineEdit.text()
        self.tc_number = self.Ui.tcNoLineEdit.text()
        self.phone_number = self.Ui.numberLineEdit.text()
        self.email = self.Ui.emailLineEdit.text()
        self.adress = self.Ui.adressLineEdit.text()
        self.password = self.Ui.passwordLineEdit.text()
        self.gender = self.Ui.genderComboBox.currentText()
        self.birthdate = self.Ui.birthDateEdit.date().toString("yyyy-MM-dd")

        self.deficient = False


        if self.name.strip() == "":
            self.deficient = True
            self.errorMessage("İsim Eksik")
        elif self.surname.strip() == "":
            self.deficient = True
            self.errorMessage("Soyad Eksik")

        elif self.tc_number.strip() == "":
            self.deficient = True
            self.errorMessage("TC No Eksik")
        elif not self.tc_number.isdigit() or len(self.tc_number) != 11:
            self.deficient = True
            self.errorMessage("Geçersiz TC No")

        elif self.phone_number.strip() == "":
            self.deficient = True
            self.errorMessage("Numara Eksik")
        elif not self.phone_number.isdigit() or len(self.phone_number) != 11:
            self.deficient = True
            self.errorMessage("Geçersiz Numara")

        elif self.email.strip() == "":
            self.deficient = True
            self.errorMessage("E-Mail Eksik")

        elif self.adress.strip() == "":
            self.deficient = True
            self.errorMessage("Adres Eksik")

        elif self.password.strip() == "":
            self.deficient = True
            self.errorMessage("Şifre Eksik")

        elif self.gender == "Seçiniz":
            self.deficient = True
            self.errorMessage("Cinsiyet Seçiniz")

        if not self.deficient:
            self.authentication = Auth.User(self.database_connection)

            self.gender = ("E" if self.Ui.genderComboBox.currentText() == "Erkek" else "K")

            print("Tc No:", self.tc_number)
            print("Ad:", self.name)
            print("Soyad:", self.surname)
            print("Numara:", self.phone_number)
            print("E-mail:", self.email)
            print("Adres:", self.adress)
            print("Şifre:", self.password)
            print("Cinsiyet:", self.gender)
            print("Doğum Tarihi:", self.birthdate)

            self.is_created, self.message = self.authentication.register_user(self.tc_number, self.name, self.surname,
                                                                              self.birthdate, self.gender, self.email,
                                                                              self.adress, self.phone_number, self.password)
            if self.is_created:
                self.possitiveMessage("Hesap Başarıyla Oluşturuldu.")
            else:
                self.errorMessage(self.message)

    def errorMessage(self, message):
        self.Ui.infoLabel.setStyleSheet("""QLabel{
                                         background-color: rgba(255, 255, 255, 0);
                                         color: rgb(255, 0, 0);
                                         font: 12pt \Segoe UI\;
                                     }""")
        self.Ui.infoLabel.setText(message)

    def possitiveMessage(self, message):
        self.Ui.infoLabel.setStyleSheet("""QLabel{
                                         background-color: rgba(255, 255, 255, 0);
                                         color: rgb(0, 255, 0);
                                         font: 12pt \Segoe UI\;
                                     }""")
        self.Ui.infoLabel.setText(message)
