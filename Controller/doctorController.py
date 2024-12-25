from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QComboBox

import Globals
from Controller import loginController, prescriptionController
from UI import mainDoctor as md

class DoctorUi(QMainWindow):
    database_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.doctorUi = md.Ui_MainWindow()
        self.doctorUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi Doktor Paneli")

        self.database_connection = None
        self.table = None
        self.selectedTable = 0


        self.doctorUi.tableComboBox.addItems(["Hastalar", "Randevular", "Reçeteler"])
        self.doctorUi.searchComboBox.clear()
        self.doctorUi.searchComboBox.addItems(["ID", "TC", "İsim", "Email", "Numara",
                                                 "Doğum Tarihi", "Cinsiyet", "Adres"])
        self.doctorUi.logOutButton.clicked.connect(self.logOut)
        self.doctorUi.prescriptionButton.clicked.connect(self.prescription)
        self.doctorUi.searchButton.clicked.connect(self.search)
        self.doctorUi.tableComboBox.currentIndexChanged.connect(self.changeTable)





    def set_database_connection(self, database_connection):
        self.database_connection = database_connection
        self.changeTable()
        print("Database bağlantısı alındı")

    def logOut(self):
        self.login = loginController.loginUi(self.database_connection)
        self.close()
        self.login.show()

    def prescription(self):
        self.pUi = prescriptionController.prescriptionUi()
        self.database_signal.connect(self.pUi.set_database_connection)
        self.database_signal.emit(self.database_connection)
        self.pUi.show()

    def changeTable(self):
        try:
            print(f"Selected Table Index: {self.selectedTable}")

            self.selectedTable = self.doctorUi.tableComboBox.currentIndex()
            self.cursor = self.database_connection.cursor()

            self.doctorUi.tableWidget.setRowCount(0)

            if self.selectedTable == 0:
                self.table = "Patient"
                self.sql = """
                SELECT PatientID, TC, Name, Surname, Email, PhoneNumber, 
                Birthdate, Gender, Address FROM Patient
                JOIN Users ON Patient.UserID = Users.UserID
                """
                self.doctorUi.tableWidget.setColumnCount(9)
                self.doctorUi.tableWidget.setHorizontalHeaderLabels(["ID", "TC", "İsim", "Soyad", "Email", "Numara",
                                                                     "Doğum Tarihi", "Cinsiyet", "Adres"])
                self.doctorUi.searchComboBox.clear()
                self.doctorUi.searchComboBox.addItems(["ID", "TC", "İsim", "Email", "Numara",
                                                       "Doğum Tarihi", "Cinsiyet", "Adres"])

            elif self.selectedTable == 1:
                self.table = "Appointment"
                self.sql = """
                            SELECT 
                              A.AppointmentID AS "Randevu ID", 
                              U1.TC AS "TC", 
                              U1.Name + ' ' + U1.Surname AS "Doktor İsim",
                              U2.Name AS "Hasta İsim",
                              U2.Surname AS "Hasta Soyad",
                              D.DepartmentName AS "Departman",
                              A.DateTime AS "Tarih"
                            FROM Appointment A
                            INNER JOIN Doctor Doc ON A.DoctorID = Doc.DoctorID
                            INNER JOIN Users U1 ON Doc.UserID = U1.UserID
                            INNER JOIN Patient P ON A.PatientID = P.PatientID
                            INNER JOIN Users U2 ON P.UserID = U2.UserID
                            INNER JOIN Department D ON A.DepartmentID = D.DepartmentID
                            WHERE Doc.DoctorID = ?
                            """
                self.doctorUi.tableWidget.setColumnCount(7)
                self.doctorUi.tableWidget.setHorizontalHeaderLabels(["Randevu ID", "TC", "Doktor İsim", "Hasta İsim",
                                                                     "Hasta Soyad", "Departman", "Tarih"])
                self.doctorUi.searchComboBox.clear()
                self.doctorUi.searchComboBox.addItems(["Randevu ID", "TC", "Doktor İsim", "Hasta İsim",
                                                       "Hasta Soyad", "Departman", "Tarih"])

            elif self.selectedTable == 2:
                self.table = "PrescriptionMedicine"
                self.sql = """
                SELECT * FROM PrescriptionMedicine
                """
                self.doctorUi.tableWidget.setColumnCount(2)
                self.doctorUi.tableWidget.setHorizontalHeaderLabels(["Reçete ID", "İlaç ID"])
                self.doctorUi.searchComboBox.clear()
                self.doctorUi.searchComboBox.addItems(["Reçete ID", "İlaç ID"])

            else:
                print("Hatalı tablo seçimi!")
                return

            if self.selectedTable == 1:
                print(f"Executing SQL: {self.sql}")
                self.cursor.execute(self.sql, (Globals.doktor_id,))
                self.rows = self.cursor.fetchall()
                print(f"Rows fetched: {len(self.rows)}")
            else:
                print(f"Executing SQL: {self.sql}")
                self.cursor.execute(self.sql)
                self.rows = self.cursor.fetchall()
                print(f"Rows fetched: {len(self.rows)}")

            for row_index, row in enumerate(self.rows):
                self.doctorUi.tableWidget.insertRow(row_index)
                for col_index, value in enumerate(row):
                    self.doctorUi.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(value)))

        except Exception as e:
            print(f"Error in changeTable: {str(e)}")

    def search(self):
        self.searchString = self.doctorUi.searchLineEdit.text()
        self.selectedColumn = self.doctorUi.searchComboBox.currentText()

        if self.searchString is None:
            print("Arama yapmalısınız")
            return

        self.cursor = self.database_connection.cursor()

        if self.table == "PrescriptionMedicine":
            if self.selectedColumn == "Reçete ID":
                self.sql = """
                SELECT * FROM PrescriptionMedicine WHERE PrescriptionID = ?
                """
                self.cursor.execute(self.sql, (self.searchString))

            else:
                self.sql = """
                SELECT * FROM PrescriptionMedicine WHERE MedicineID LIKE ?
                """
                self.cursor.execute(self.sql, (f"%{self.searchString}%"))
        elif self.table == "Appointment":
            if self.selectedColumn == "Randevu ID":
                self.sql = """
                           SELECT 
                               A.AppointmentID AS "Randevu ID", 
                               U1.TC AS "TC", 
                               U1.Name + ' ' + U1.Surname AS "Doktor İsim",
                               U2.Name AS "Hasta İsim",
                               U2.Surname AS "Hasta Soyad",
                               D.DepartmentName AS "Departman",
                               A.DateTime AS "Tarih"
                           FROM Appointment A
                           INNER JOIN Doctor Doc ON A.DoctorID = Doc.DoctorID
                           INNER JOIN Users U1 ON Doc.UserID = U1.UserID
                           INNER JOIN Patient P ON A.PatientID = P.PatientID
                           INNER JOIN Users U2 ON P.UserID = U2.UserID
                           INNER JOIN Department D ON A.DepartmentID = D.DepartmentID
                           WHERE A.AppointmentID = ?
                           """
                self.cursor.execute(self.sql, (self.searchString,))

            elif self.selectedColumn == "TC":
                self.sql = """
                           SELECT 
                               A.AppointmentID AS "Randevu ID", 
                               U1.TC AS "TC", 
                               U1.Name + ' ' + U1.Surname AS "Doktor İsim",
                               U2.Name AS "Hasta İsim",
                               U2.Surname AS "Hasta Soyad",
                               D.DepartmentName AS "Departman",
                               A.DateTime AS "Tarih"
                           FROM Appointment A
                           INNER JOIN Doctor Doc ON A.DoctorID = Doc.DoctorID
                           INNER JOIN Users U1 ON Doc.UserID = U1.UserID
                           INNER JOIN Patient P ON A.PatientID = P.PatientID
                           INNER JOIN Users U2 ON P.UserID = U2.UserID
                           INNER JOIN Department D ON A.DepartmentID = D.DepartmentID
                           WHERE U1.TC = ? OR U2.TC = ?
                           """
                self.cursor.execute(self.sql, (self.searchString, self.searchString))

            elif self.selectedColumn == "Doktor İsim":
                self.sql = """
                           SELECT 
                               A.AppointmentID AS "Randevu ID", 
                               U1.TC AS "TC", 
                               U1.Name + ' ' + U1.Surname AS "Doktor İsim",
                               U2.Name AS "Hasta İsim",
                               U2.Surname AS "Hasta Soyad",
                               D.DepartmentName AS "Departman",
                               A.DateTime AS "Tarih"
                           FROM Appointment A
                           INNER JOIN Doctor Doc ON A.DoctorID = Doc.DoctorID
                           INNER JOIN Users U1 ON Doc.UserID = U1.UserID
                           INNER JOIN Patient P ON A.PatientID = P.PatientID
                           INNER JOIN Users U2 ON P.UserID = U2.UserID
                           INNER JOIN Department D ON A.DepartmentID = D.DepartmentID
                           WHERE U1.Name LIKE ? OR U1.Surname LIKE ?
                           """
                self.cursor.execute(self.sql, (f"%{self.searchString}%", f"%{self.searchString}%"))

            elif self.selectedColumn == "Hasta İsim":
                self.sql = """
                           SELECT 
                               A.AppointmentID AS "Randevu ID", 
                               U1.TC AS "TC", 
                               U1.Name + ' ' + U1.Surname AS "Doktor İsim",
                               U2.Name AS "Hasta İsim",
                               U2.Surname AS "Hasta Soyad",
                               D.DepartmentName AS "Departman",
                               A.DateTime AS "Tarih"
                           FROM Appointment A
                           INNER JOIN Doctor Doc ON A.DoctorID = Doc.DoctorID
                           INNER JOIN Users U1 ON Doc.UserID = U1.UserID
                           INNER JOIN Patient P ON A.PatientID = P.PatientID
                           INNER JOIN Users U2 ON P.UserID = U2.UserID
                           INNER JOIN Department D ON A.DepartmentID = D.DepartmentID
                           WHERE U2.Name LIKE ? OR U2.Surname LIKE ?
                           """
                self.cursor.execute(self.sql, (f"%{self.searchString}%", f"%{self.searchString}%"))

            elif self.selectedColumn == "Departman":
                self.sql = """
                           SELECT 
                               A.AppointmentID AS "Randevu ID", 
                               U1.TC AS "TC", 
                               U1.Name + ' ' + U1.Surname AS "Doktor İsim",
                               U2.Name AS "Hasta İsim",
                               U2.Surname AS "Hasta Soyad",
                               D.DepartmentName AS "Departman",
                               A.DateTime AS "Tarih"
                           FROM Appointment A
                           INNER JOIN Doctor Doc ON A.DoctorID = Doc.DoctorID
                           INNER JOIN Users U1 ON Doc.UserID = U1.UserID
                           INNER JOIN Patient P ON A.PatientID = P.PatientID
                           INNER JOIN Users U2 ON P.UserID = U2.UserID
                           INNER JOIN Department D ON A.DepartmentID = D.DepartmentID
                           WHERE D.DepartmentName LIKE ?
                           """
                self.cursor.execute(self.sql, (f"%{self.searchString}%",))

            elif self.selectedColumn == "Tarih":
                self.sql = """
                           SELECT 
                               A.AppointmentID AS "Randevu ID", 
                               U1.TC AS "TC", 
                               U1.Name + ' ' + U1.Surname AS "Doktor İsim",
                               U2.Name AS "Hasta İsim",
                               U2.Surname AS "Hasta Soyad",
                               D.DepartmentName AS "Departman",
                               A.DateTime AS "Tarih"
                           FROM Appointment A
                           INNER JOIN Doctor Doc ON A.DoctorID = Doc.DoctorID
                           INNER JOIN Users U1 ON Doc.UserID = U1.UserID
                           INNER JOIN Patient P ON A.PatientID = P.PatientID
                           INNER JOIN Users U2 ON P.UserID = U2.UserID
                           INNER JOIN Department D ON A.DepartmentID = D.DepartmentID
                           WHERE CONVERT(DATE, A.DateTime) = ?
                           """
                self.cursor.execute(self.sql, (self.searchString,))

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

        self.doctorUi.tableWidget.setRowCount(0)

        for row_index, row in enumerate(self.rows):
            self.doctorUi.tableWidget.insertRow(row_index)
            for col_index, value in enumerate(row):
                self.doctorUi.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(value)))
