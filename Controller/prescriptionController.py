from PyQt5.QtWidgets import QMainWindow

from UI import doctorPrescription as dp


class prescriptionUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pUi = dp.Ui_MainWindow()
        self.pUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi")

        self.pUi.exitButton.clicked.connect(self.exit)

    def exit(self):
        self.close()
