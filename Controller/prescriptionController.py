from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

import Globals
from UI import doctorPrescription as dp
from datetime import datetime
from Globals import doktor_id


class prescriptionUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pUi = dp.Ui_MainWindow()
        self.pUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi Reçete Paneli")

        self.selected_medicines = []
        import Globals
        print(f"Doktor ID'si: {Globals.doktor_id}")
        self.user_id = None


        # UI bağlantıları
        self.pUi.exitButton.clicked.connect(self.exit)
        self.pUi.addMedicineButton.clicked.connect(self.add_medicine_to_list)
        self.pUi.prescriptionButton.clicked.connect(self.create_prescription)

    def set_user_info(self, user_id):
        self.user_id = user_id
        print(f"Doktor ID'si ayarlandı: {self.user_id}")  # Debug amaçlı kontrol edebilirsiniz

    def set_database_connection(self, database_connection):
        self.database_connection = database_connection
        self.load_medicene()
        self.setComboBox()
        print("Database bağlantısı alındı")

    def exit(self):
        self.close()

    def load_medicene(self):
        if not self.database_connection:
            print("Veritabanı bağlantısı kurulmadı!")
            return

        try:
            cursor = self.database_connection.cursor()
            cursor.execute("""
                SELECT MedicineID, MedicineName, Manufacturer, Type, Dose FROM Medicines
            """)
            medicines = cursor.fetchall()
            column_names = ["İlaç ID", "İlaç Adı", "Üretiçi", "Tipi", "Doz"]

            self.pUi.tableWidget.setColumnCount(len(column_names))
            self.pUi.tableWidget.setHorizontalHeaderLabels(column_names)
            self.pUi.tableWidget.setRowCount(0)

            for row_idx, medicine in enumerate(medicines):
                self.pUi.tableWidget.insertRow(row_idx)
                for col_idx, value in enumerate(medicine):
                    self.pUi.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        except Exception as e:
            print(f"Error loading medicines: {str(e)}")

    def setComboBox(self):
        if not self.database_connection:
            print("Veritabanı bağlantısı kurulmadı!")
            return

        try:
            cursor = self.database_connection.cursor()
            cursor.execute(
                "SELECT DISTINCT U.TC FROM Users U INNER JOIN Patient P ON U.UserID = P.UserID INNER JOIN Appointment A ON P.PatientID = A.PatientID; ")
            patients = cursor.fetchall()

            self.pUi.patinetComboBox.clear()

            for patient in patients:
                self.pUi.patinetComboBox.addItem(str(patient[0]))

            print("PatientID'ler ComboBox'a eklendi.")

        except Exception as e:
            print(f"Error setting ComboBox: {str(e)}")

    def add_medicine_to_list(self):
        selected_row = self.pUi.tableWidget.currentRow()
        if selected_row == -1:
            print("Herhangi bir ilaç seçilmedi.")
            return

        medicine_id = self.pUi.tableWidget.item(selected_row, 0).text()
        if medicine_id in self.selected_medicines:
            print("Bu ilaç zaten listeye eklenmiş.")
            return

        self.selected_medicines.append(medicine_id)
        print(f"İlaç eklendi: {medicine_id}")

    def create_prescription(self):
        if not self.database_connection:
            print("Veritabanı bağlantısı kurulmadı!")
            return

        if not self.selected_medicines:
            print("Herhangi bir ilaç seçilmedi.")
            return

        try:
            cursor = self.database_connection.cursor()

            # Hasta bilgilerini al
            selected_tc = self.pUi.patinetComboBox.currentText()
            cursor.execute("SELECT P.PatientID FROM Patient P INNER JOIN Users U ON P.UserID = U.UserID WHERE U.TC = ?",
                           (selected_tc,))
            patient_id_result = cursor.fetchone()

            if not patient_id_result:
                print(f"TC {selected_tc} ile hasta bulunamadı.")
                return

            patient_id = patient_id_result[0]

            # Doktor ID'si
            doctor_id = Globals.doktor_id #(burada sabit değer kullanılıyor)
            if not doctor_id:
                print("Doktor ID'si bulunamadı.")
                return

            appointment_id = 5
            print("doctor", doctor_id)
            print("patient", patient_id)
            print("appointment", appointment_id)
            print("date", datetime.now())

            cursor.execute("""
                INSERT INTO Prescription (DoctorID, PatientID, DateTime, AppointmentID)
                VALUES (?, ?, ?, ?);
            """, (doctor_id, patient_id, datetime.now(), appointment_id))

            cursor.execute("SELECT SCOPE_IDENTITY() AS PrescriptionID;")
            result = cursor.fetchone()

            if not result or not result[0]:
                print("PrescriptionID alınamadı.")
                return

            prescription_id = int(result[0])
            print(f"PrescriptionID alındı: {prescription_id}")

            for medicine_id in self.selected_medicines:
                cursor.execute("""
                    INSERT INTO PrescriptionMedicine (PrescriptionID, MedicineID)
                    VALUES (?, ?)
                """, (prescription_id, int(medicine_id)))

            self.database_connection.commit()
            print("Reçete başarıyla oluşturuldu.")
            self.selected_medicines.clear()

        except Exception as e:
            import traceback
            print(f"Error creating prescription: {str(e)}")
            traceback.print_exc()

