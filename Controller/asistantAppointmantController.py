from PyQt5.QtWidgets import QMainWindow

from UI import asistantAppointment


class asistantAppointmantUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.aaUi = asistantAppointment.Ui_MainWindow()
        self.aaUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi")

        self.aaUi.exitButton.clicked.connect(self.exit)

    def exit(self):
        self.close()
