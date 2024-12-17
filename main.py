from PyQt5.QtWidgets import QApplication

from Controller import loginController

import os

os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = r"D:\Ders Notları\Veritabanı Yönetim Sistemleri\Project\HFZ_Hospital\.venv\Lib\site-packages\PyQt5\Qt5\plugins"




App = QApplication([])
window = loginController.loginUi()
window.show()
App.exec()