from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
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

        self.doctorUi.logOutButton.clicked.connect(self.logOut)
        self.doctorUi.prescriptionButton.clicked.connect(self.prescription)

    def set_database_connection(self, database_connection):
        self.database_connection = database_connection
        self.load_appointments()
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

    def load_appointments(self):
        if not self.database_connection:
            print("Veritabanı bağlantısı kurulmadı!")
            return

        try:
            cursor = self.database_connection.cursor()
            cursor.execute("""
                SELECT A.AppointmentID, D.Title, U.Name, U.Surname, A.DateTime, A.Status
                FROM Appointment A
                INNER JOIN Doctor D ON A.DoctorID = D.DoctorID
                INNER JOIN Users U ON A.PatientID = U.UserID
            """)
            appointments = cursor.fetchall()
            #column_names = [desc[0] for desc in cursor.description]  # Sütun adlarını al

            column_headers = ["Randevu ID", "Doktor", "Hasta Adı", "Hasta Soyadı", "Tarih", "Durum"]
            self.doctorUi.tableWidget.setColumnCount(len(column_headers))
            self.doctorUi.tableWidget.setHorizontalHeaderLabels(column_headers)

            self.doctorUi.tableWidget.setRowCount(0)

            for row_idx, appointment in enumerate(appointments):
                self.doctorUi.tableWidget.insertRow(row_idx)
                for col_idx, value in enumerate(appointment):
                    self.doctorUi.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        except Exception as e:
            print(f"Error loading appointments: {str(e)}")
