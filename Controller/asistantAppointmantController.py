import datetime

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from UI import asistantAppointment


class asistantAppointmantUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.aaUi = asistantAppointment.Ui_MainWindow()
        self.aaUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi")

        self.database_connection = None
        self.doctorIDs = []
        self.patientIDs = []

        self.aaUi.exitButton.clicked.connect(self.close)
        self.aaUi.departmantComboBox.currentIndexChanged.connect(self.changeDepartment)
        self.aaUi.getAppointmentButton.clicked.connect(self.getAppointment)

    def set_database_connection(self, database_connection):
        self.database_connection = database_connection
        print("Database bağlantısı alındı")
        self.setTable()
        self.setComboBox()

    def setComboBox(self):
        self.aaUi.departmantComboBox.clear()
        self.aaUi.departmantComboBox.addItem("Hepsi")

        self.cursor = self.database_connection.cursor()
        self.sql = """
        SELECT DepartmentName FROM Department
        """

        self.cursor.execute(self.sql)
        self.rows = self.cursor.fetchall()

        for value in self.rows:
            departmantName = value[0]
            self.aaUi.departmantComboBox.addItem(departmantName)

        self.aaUi.patientComboBox.clear()
        self.aaUi.patientComboBox.addItem("Hasta Seçiniz")

        self.sql = """
        SELECT Name, PatientID FROM Patient 
        JOIN Users ON Patient.UserID = Users.UserID
        """

        self.cursor.execute(self.sql)
        self.rows = self.cursor.fetchall()

        for value in self.rows:
            patientName = value[0]
            self.aaUi.patientComboBox.addItem(patientName)
            self.patientIDs.append(value[1])

    def setTable(self):
        self.cursor = self.database_connection.cursor()
        self.sql = """
        SELECT DoctorID, CONCAT(Users.Name, ' ', Users.Surname) as Name, DepartmentName FROM Doctor
        JOIN Department ON Doctor.DepartmentID = Department.DepartmentID
        JOIN Users ON Doctor.UserID = Users.UserID
        """

        self.cursor.execute(self.sql)
        self.rows = self.cursor.fetchall()

        self.aaUi.tableWidget.setColumnCount(3)
        self.aaUi.tableWidget.setHorizontalHeaderLabels(["Tarih", "Doktor", "Bölüm"])
        self.aaUi.tableWidget.setColumnWidth(0, 200)
        self.aaUi.tableWidget.setColumnWidth(1, 300)
        self.aaUi.tableWidget.setColumnWidth(2, 300)
        self.aaUi.tableWidget.setRowCount(0)

        self.row_index = 0
        for row in self.rows:
            base_date = datetime.datetime.today()

            for i in range(3):
                self.aaUi.tableWidget.insertRow(self.row_index)

                for col_index, value in enumerate(row):
                    if col_index == 0:
                        self.doctorIDs.append(value)
                        continue
                    self.aaUi.tableWidget.setItem(self.row_index, col_index, QTableWidgetItem(str(value)))

                new_date = base_date + datetime.timedelta(days=i)
                self.aaUi.tableWidget.setItem(self.row_index, 0, QTableWidgetItem(new_date.strftime('%d-%m-%Y')))

                self.row_index += 1

    def changeDepartment(self):
        self.departmentName = self.aaUi.departmantComboBox.currentText()
        self.doctorIDs = []

        if self.departmentName == "Hepsi":
            self.setTable()
            return

        self.cursor = self.database_connection.cursor()
        self.sql = f"""
        SELECT DoctorID, CONCAT(Users.Name, ' ', Users.Surname) as Name, DepartmentName FROM Doctor
        JOIN Department ON Doctor.DepartmentID = Department.DepartmentID
        JOIN Users ON Doctor.UserID = Users.UserID WHERE Department.DepartmentName = '{self.departmentName}'
        """

        self.cursor.execute(self.sql)
        self.rows = self.cursor.fetchall()

        self.aaUi.tableWidget.setColumnCount(3)
        self.aaUi.tableWidget.setHorizontalHeaderLabels(["Tarih", "Doktor", "Bölüm"])
        self.aaUi.tableWidget.setColumnWidth(0, 200)
        self.aaUi.tableWidget.setColumnWidth(1, 300)
        self.aaUi.tableWidget.setColumnWidth(2, 300)
        self.aaUi.tableWidget.setRowCount(0)

        self.row_index = 0
        for row in self.rows:
            base_date = datetime.datetime.today()

            for i in range(3):
                self.aaUi.tableWidget.insertRow(self.row_index)

                for col_index, value in enumerate(row):
                    if col_index == 0:
                        self.doctorIDs.append(value)
                        continue
                    self.aaUi.tableWidget.setItem(self.row_index, col_index, QTableWidgetItem(str(value)))

                new_date = base_date + datetime.timedelta(days=i)
                self.aaUi.tableWidget.setItem(self.row_index, 0, QTableWidgetItem(new_date.strftime('%d-%m-%Y')))

                self.row_index += 1

    def getAppointment(self):
        self.cursor = self.database_connection.cursor()
        self.row = self.aaUi.tableWidget.currentRow()

        self.rowData = []
        self.columnCount = self.aaUi.tableWidget.columnCount()

        for i in range(self.columnCount):
            item = self.aaUi.tableWidget.item(self.row, i)
            value = item.text()
            if i == 0:
                value = datetime.datetime.strptime(value, "%d-%m-%Y")
                value = value.strftime("%Y-%m-%d")
            self.rowData.append(value)

        self.selectedPatient = self.aaUi.patientComboBox.currentIndex() - 1

        if self.selectedPatient == -1:
            self.aaUi.patientLabel.setStyleSheet("color: rgb(255, 0, 0);")
            return

        self.aaUi.patientLabel.setStyleSheet("color: rgb(0, 0, 0);")

        self.date = self.rowData[0]
        self.patientID = self.patientIDs[self.selectedPatient]
        self.doctorID = self.doctorIDs[self.row]
        self.departmentName = self.rowData[2]

        self.sql = f"""
        SELECT DepartmentID FROM Department WHERE DepartmentName = ?
        """
        self.cursor.execute(self.sql, (self.departmentName,))
        self.departmentID = self.cursor.fetchone()
        self.departmentID = self.departmentID[0]

        self.sql = """
        SELECT Status FROM Appointment
        JOIN Patient ON Appointment.PatientID = Patient.PatientID
        WHERE DepartmentID = ? AND Patient.PatientID = ? AND Status = ?
        """
        self.cursor.execute(self.sql, (self.departmentID, self.patientID, 'P'))

        self.alreadyHas = self.cursor.fetchone()
        if self.alreadyHas != None:
            print("Zaten randevusu var.")
            return

        self.sql = f"""
        INSERT INTO Appointment 
        (DoctorID, PatientID, DepartmentID, DateTime, Status) 
        VALUES (?, ?, ?, ?, ?)
        """
        self.cursor.execute(self.sql, (self.doctorID, self.patientID, self.departmentID, self.date, 'P'))

        self.database_connection.commit()
