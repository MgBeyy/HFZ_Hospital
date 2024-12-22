from PyQt5.QtWidgets import QMainWindow

from Functions import Auth
from UI import addPatient


class addPatientUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.apUi = addPatient.Ui_MainWindow()
        self.apUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi")

        self.database_connection = None

        self.apUi.createAccountButton.clicked.connect(self.createAcc)

    def set_database_connection(self, database_connection):
        self.database_connection = database_connection
        print("Database bağlantısı alındı")

    def createAcc(self):
        self.name = self.apUi.nameLineEdit.text()
        self.surname = self.apUi.lastNameLineEdit.text()
        self.tc_number = self.apUi.tcNoLineEdit.text()
        self.phone_number = self.apUi.numberLineEdit.text()
        self.email = self.apUi.emailLineEdit.text()
        self.adress = self.apUi.adressLineEdit.text()
        self.password = self.apUi.passwordLineEdit.text()
        self.gender = self.apUi.genderComboBox.currentText()
        self.birthdate = self.apUi.birthDateEdit.date().toString("yyyy-MM-dd")

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
                                                                              self.phone_number, self.adress, self.password)
            if self.is_created:
                self.possitiveMessage("Hesap Başarıyla Oluşturuldu.")
            else:
                self.errorMessage(self.message)

    def errorMessage(self, message):
        self.apUi.infoLabel.setStyleSheet("""QLabel{
                                         background-color: rgba(255, 255, 255, 0);
                                         color: rgb(255, 0, 0);
                                         font: 12pt \Segoe UI\;
                                     }""")
        self.apUi.infoLabel.setText(message)

    def possitiveMessage(self, message):
        self.apUi.infoLabel.setStyleSheet("""QLabel{
                                         background-color: rgba(255, 255, 255, 0);
                                         color: rgb(0, 255, 0);
                                         font: 12pt \Segoe UI\;
                                     }""")
        self.Ui.infoLabel.setText(message)
