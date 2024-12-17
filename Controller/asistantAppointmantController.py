from PyQt5.QtWidgets import QMainWindow

from UI import asistantAppointment


class asistantAppointmantUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.aaUi = asistantAppointment.Ui_MainWindow()
        self.setWindowTitle("HFZ Hastanesi")
        self.aaUi.setupUi(self)
