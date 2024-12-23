from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from UI import doctorPrescription as dp


class prescriptionUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pUi = dp.Ui_MainWindow()
        self.pUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi Reçete Paneli")

        self.pUi.exitButton.clicked.connect(self.exit)

    def set_database_connection(self, database_connection):
        self.database_connection = database_connection
        self.load_medicene()
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
                SELECT * FROM Medicines
            """)
            medicines = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]

            # column_headers = ["Randevu ID", "Doktor", "Hasta Adı", "Hasta Soyadı", "Tarih", "Durum"]
            self.pUi.tableWidget.setColumnCount(len(column_names))
            self.pUi.tableWidget.setHorizontalHeaderLabels(column_names)

            self.pUi.tableWidget.setRowCount(0)

            for row_idx, appointment in enumerate(medicines):
                self.pUi.tableWidget.insertRow(row_idx)
                for col_idx, value in enumerate(appointment):
                    self.pUi.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        except Exception as e:
            print(f"Error loading medicines: {str(e)}")
