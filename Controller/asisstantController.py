from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from UI import mainAsistant as ma
from Controller import loginController, addPatientController, asistantAppointmantController

class AsistantUi(QMainWindow):
    database_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.asistantUi = ma.Ui_MainWindow()
        self.asistantUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi")

        self.database_connection = None
        self.table = None

        self.asistantUi.tableComboBox.clear()
        self.asistantUi.tableComboBox.addItems(["Hastalar", "Doktorlar", "Bölümler"])

        self.asistantUi.logOutButton.clicked.connect(self.logOut)
        self.asistantUi.prescriptionButton.clicked.connect(self.prescription)
        self.asistantUi.addPatient.clicked.connect(self.addPatient)
        self.asistantUi.tableComboBox.currentIndexChanged.connect(self.changeTable)
        self.asistantUi.searchButton.clicked.connect(self.search)

    def set_database_connection(self, database_connection):
        self.database_connection = database_connection
        print("Database bağlantısı alındı")
        self.changeTable()

    def logOut(self):
        self.login = loginController.loginUi(self.database_connection)
        self.close()
        self.login.show()

    def prescription(self):
        self.asAp = asistantAppointmantController.asistantAppointmantUi()
        self.database_signal.connect(self.asAp.set_database_connection)
        self.database_signal.emit(self.database_connection)
        self.asAp.show()

    def addPatient(self):
        self.addPatient = addPatientController.addPatientUi()
        self.database_signal.connect(self.addPatient.set_database_connection)
        self.database_signal.emit(self.database_connection)
        self.addPatient.show()

    def changeTable(self):
        self.selectedTable = self.asistantUi.tableComboBox.currentIndex()
        self.cursor = self.database_connection.cursor()

        self.asistantUi.tableWidget.setRowCount(0)
        self.asistantUi.tableWidget.setColumnCount(9)
        self.asistantUi.tableWidget.setHorizontalHeaderLabels(["ID", "TC", "İsim", "Soyad", "Email", "Numara",
                                                               "Doğum Tarihi", "Cinsiyet", "Adres"])
        self.asistantUi.searchComboBox.clear()
        self.asistantUi.searchComboBox.addItems(["ID", "TC", "İsim", "Email", "Numara",
                                                "Doğum Tarihi", "Cinsiyet", "Adres"])
        self.asistantUi.tableWidget.setColumnWidth(0, 20)
        self.asistantUi.tableWidget.setColumnWidth(1, 150)
        self.asistantUi.tableWidget.setColumnWidth(2, 100)
        self.asistantUi.tableWidget.setColumnWidth(3, 100)
        self.asistantUi.tableWidget.setColumnWidth(4, 150)
        self.asistantUi.tableWidget.setColumnWidth(5, 150)
        self.asistantUi.tableWidget.setColumnWidth(6, 150)
        self.asistantUi.tableWidget.setColumnWidth(7, 70)
        self.asistantUi.tableWidget.setColumnWidth(8, 150)

        if self.selectedTable == 0:
            self.table = "Patient"
            self.sql = """
            SELECT PatientID, TC, Name, Surname, Email, PhoneNumber, 
            Birthdate, Gender, Address FROM Patient
            JOIN Users ON Patient.UserID = Users.UserID
            """

        elif self.selectedTable == 1:
            self.table = "Doctor"
            self.sql = """
            SELECT DoctorID, TC, Name, Surname, Email, PhoneNumber, 
            Birthdate, Gender, Address FROM Doctor
            JOIN Users ON Doctor.UserID = Users.UserID
            """

        else:
            self.table = "Department"
            self.sql = """
            SELECT * FROM Department
            """
            self.asistantUi.tableWidget.setColumnCount(2)
            self.asistantUi.tableWidget.setHorizontalHeaderLabels(["Branş ID", "Branş Adı"])
            self.asistantUi.searchComboBox.clear()
            self.asistantUi.searchComboBox.addItems(["Branş ID", "Branş Adı"])
            self.asistantUi.tableWidget.setColumnWidth(0, 100)
            self.asistantUi.tableWidget.setColumnWidth(1, 400)

        self.cursor.execute(self.sql)
        self.rows = self.cursor.fetchall()

        for row_index, row in enumerate(self.rows):
            self.asistantUi.tableWidget.insertRow(row_index)
            for col_index, value in enumerate(row):
                self.asistantUi.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(value)))

    def search(self):
        self.searchString = self.asistantUi.searchLineEdit.text()
        self.selectedColumn = self.asistantUi.searchComboBox.currentText()

        if self.searchString is None:
            print("Arama yapmalısınız")
            return

        self.cursor = self.database_connection.cursor()

        if self.table == "Department":
            if self.selectedColumn == "Branş ID":
                self.sql = """
                SELECT * FROM Department WHERE DepartmentID = ?
                """
                self.cursor.execute(self.sql, (self.searchString))

            else:
                self.sql = """
                SELECT * FROM Department WHERE DepartmentName LIKE ?
                """
                self.cursor.execute(self.sql, (f"%{self.searchString}%"))

        else:
            if self.selectedColumn == "ID":
                self.sql = f"""
                SELECT {self.table}ID, TC, Name, Surname, Email, PhoneNumber, Birthdate, Gender, Address 
                FROM {self.table}
                JOIN Users ON {self.table}.UserID = Users.UserID
                WHERE {self.table}ID = ?
                """
                self.cursor.execute(self.sql, (self.searchString,))

            elif self.selectedColumn == "TC":
                self.sql = f"""
                SELECT {self.table}ID, TC, Name, Surname, Email, PhoneNumber, Birthdate, Gender, Address 
                FROM {self.table}
                JOIN Users ON {self.table}.UserID = Users.UserID
                WHERE TC = ?
                """
                self.cursor.execute(self.sql, (self.searchString,))

            elif self.selectedColumn == "İsim":
                self.sql = f"""
                SELECT {self.table}ID, TC, Name, Surname, Email, PhoneNumber, Birthdate, Gender, Address 
                FROM {self.table}
                JOIN Users ON {self.table}.UserID = Users.UserID
                WHERE Name LIKE ? OR Surname LIKE ?
                """
                self.cursor.execute(self.sql, (f"%{self.searchString}%", f"%{self.searchString}%"))

            elif self.selectedColumn == "Email":
                self.sql = f"""
                SELECT {self.table}ID, TC, Name, Surname, Email, PhoneNumber, Birthdate, Gender, Address 
                FROM {self.table}
                JOIN Users ON {self.table}.UserID = Users.UserID
                WHERE Email LIKE ?
                """
                self.cursor.execute(self.sql, (f"%{self.searchString}%",))

            elif self.selectedColumn == "Numara":
                self.sql = f"""
                SELECT {self.table}ID, TC, Name, Surname, Email, PhoneNumber, Birthdate, Gender, Address 
                FROM {self.table}
                JOIN Users ON {self.table}.UserID = Users.UserID
                WHERE PhoneNumber = ?
                """
                self.cursor.execute(self.sql, (self.searchString,))

            elif self.selectedColumn == "Doğum Tarihi":
                self.sql = f"""
                SELECT {self.table}ID, TC, Name, Surname, Email, PhoneNumber, Birthdate, Gender, Address 
                FROM {self.table}
                JOIN Users ON {self.table}.UserID = Users.UserID
                WHERE Birthdate = ?
                """
                self.cursor.execute(self.sql, (self.searchString,))

            elif self.selectedColumn == "Cinsiyet":
                self.sql = f"""
                SELECT {self.table}ID, TC, Name, Surname, Email, PhoneNumber, Birthdate, Gender, Address 
                FROM {self.table}
                JOIN Users ON {self.table}.UserID = Users.UserID
                WHERE Gender = ?
                """
                self.cursor.execute(self.sql, (self.searchString,))

            elif self.selectedColumn == "Adres":
                self.sql = f"""
                SELECT {self.table}ID, TC, Name, Surname, Email, PhoneNumber, Birthdate, Gender, Address 
                FROM {self.table}
                JOIN Users ON {self.table}.UserID = Users.UserID
                WHERE Address LIKE ?
                """
                self.cursor.execute(self.sql, (f"%{self.searchString}%",))

        self.rows = self.cursor.fetchall()

        self.asistantUi.tableWidget.setRowCount(0)

        for row_index, row in enumerate(self.rows):
            self.asistantUi.tableWidget.insertRow(row_index)
            for col_index, value in enumerate(row):
                self.asistantUi.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(value)))
