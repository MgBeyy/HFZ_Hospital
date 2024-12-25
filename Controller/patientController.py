from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from UI import mainPatient as mp
from Controller import loginController, patientAppointmentController


class PatientUi(QMainWindow):
    database_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.patientUi = mp.Ui_MainWindow()
        self.patientUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi Hasta Paneli")

        self.database_connection = None
        self.cursor = None

        # Signal bağlantıları
        self.patientUi.logOutButton.clicked.connect(self.logOut)
        self.patientUi.appointmentButton.clicked.connect(self.changeTableAppointment)
        self.patientUi.prescriptionButton.clicked.connect(self.changeTablePrescription)
        self.patientUi.getAppointmentButton.clicked.connect(self.getAppointment)

    def set_database_connection(self, database_connection):
        self.database_connection = database_connection
        self.cursor = self.database_connection.cursor()
        print("Database bağlantısı alındı")
        self.changeTableAppointment()

    def logOut(self):
        self.login = loginController.loginUi(self.database_connection)
        self.close()
        self.login.show()

    def getAppointment(self):
        self.appUi = patientAppointmentController.patinetAppointmenUi()
        self.database_signal.connect(self.appUi.set_database_connection)
        self.database_signal.emit(self.database_connection)
        self.appUi.show()

    def load_departments(self):
        """Veritabanından departmanları çekip döndürür."""
        if not self.database_connection:
            return []

        try:
            cursor = self.database_connection.cursor()
            cursor.execute("SELECT DepartmentName FROM Department")
            departments = [row[0] for row in cursor.fetchall()]
            return departments
        except Exception as e:
            print(f"Departmanları yüklerken hata oluştu: {e}")
            return []

    def changeTableAppointment(self):
        if not self.database_connection:
            return

        try:
            self.patientUi.tableWidget.setRowCount(0)
            self.patientUi.tableWidget.setColumnCount(6)
            self.patientUi.tableWidget.setHorizontalHeaderLabels(
                ["ID", "Doktor Adı", "Departman", "Tarih-Saat", "Durum", ""]
            )

            # Arama seçeneklerini güncelle
            self.patientUi.searchComboBox.clear()
            self.patientUi.searchComboBox.addItems(
                ["ID", "Doktor Adı", "Doktor soyadı", "Departman", "Tarih-Saat", "Durum"]
            )

            # Sütun genişliklerini ayarla
            column_widths = [20, 150, 100, 100, 150, 150]
            for i, width in enumerate(column_widths):
                self.patientUi.tableWidget.setColumnWidth(i, width)

            sql = """
            SELECT 
                Appointment.AppointmentID,
                Users.Name,
                Users.Surname,
                Department.DepartmentName,
                Appointment.DateTime,
                Appointment.Status
            FROM 
                Appointment
            INNER JOIN 
                Patient ON Appointment.PatientID = Patient.PatientID
            INNER JOIN 
                Users ON Patient.UserID = Users.UserID
            INNER JOIN 
                Department ON Appointment.DepartmentID = Department.DepartmentID;
            """

            self.cursor.execute(sql)
            rows = self.cursor.fetchall()

            for row_index, row in enumerate(rows):
                self.patientUi.tableWidget.insertRow(row_index)
                for col_index, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.patientUi.tableWidget.setItem(row_index, col_index, item)

        except Exception as e:
            print(f"Randevu tablosunu değiştirirken hata oluştu: {e}")

    def changeTablePrescription(self):
        if not self.database_connection:
            return

        try:
            self.patientUi.tableWidget.setRowCount(0)
            self.patientUi.tableWidget.setColumnCount(5)
            self.patientUi.tableWidget.setHorizontalHeaderLabels(
                ["Reçete ID", "Doktor Adı", "İlaç", "Tarih"]
            )

            # Arama seçeneklerini güncelle
            self.patientUi.searchComboBox.clear()
            self.patientUi.searchComboBox.addItems(
                ["Reçete ID", "Doktor Adı", "İlaç", "Tarih"]
            )

            # Sütun genişliklerini ayarla
            column_widths = [50, 150, 200, 100, 100]
            for i, width in enumerate(column_widths):
                self.patientUi.tableWidget.setColumnWidth(i, width)

            sql = """
            SELECT 
                p.PrescriptionID,
                p.DateTime,
                u.Name,
                u.Surname
            FROM 
                Prescription p
            JOIN 
                Doctor d ON p.DoctorID = d.DoctorID
            JOIN 
                Users u ON d.UserID = u.UserID;
            """

            self.cursor.execute(sql, (self.patient_id,))
            rows = self.cursor.fetchall()

            for row_index, row in enumerate(rows):
                self.patientUi.tableWidget.insertRow(row_index)
                for col_index, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.patientUi.tableWidget.setItem(row_index, col_index, item)

        except Exception as e:
            print(f"Reçete tablosunu değiştirirken hata oluştu: {e}")