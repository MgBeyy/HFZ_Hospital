from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 178, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 8, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.tcNoLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.tcNoLineEdit.setMinimumSize(QtCore.QSize(300, 40))
        self.tcNoLineEdit.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.tcNoLineEdit.setFont(font)
        self.tcNoLineEdit.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"    border: 3px solid;\n"
"    border-color: rgb(121, 177, 236);\n"
"    font: 14pt \"Segoe UI\";\n"
"}\n"
"QLineEdit::focus{\n"
"    border: 2px solid;\n"
"    border-color: rgb(44, 89, 209);\n"
"}\n"
"")
        self.tcNoLineEdit.setObjectName("tcNoLineEdit")
        self.horizontalLayout_2.addWidget(self.tcNoLineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setMinimumSize(QtCore.QSize(120, 50))
        self.loginButton.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(44, 89, 209);\n"
"    font: 75 18pt \"Segoe UI\";\n"
"    font-weight: bold;\n"
"    color: rgb(198, 205, 213);\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(198, 205, 213);\n"
"    color: rgb(44, 89, 209);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(198, 205, 213);\n"
"    color: rgb(44, 89, 209);\n"
"    padding-top: 3px;\n"
"    border: 2px solid;\n"
"    border-color: rgb(13, 17, 23);\n"
"}")
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout_4.addWidget(self.loginButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.forgotPassButton = QtWidgets.QPushButton(self.centralwidget)
        self.forgotPassButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgb(106, 146, 255);\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgb(44, 89, 209);\n"
"    font: 10pt \"Segoe UI\";\n"
"}")
        self.forgotPassButton.setObjectName("forgotPassButton")
        self.horizontalLayout_3.addWidget(self.forgotPassButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.gridLayout.addLayout(self.verticalLayout, 6, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 4, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem8 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setEnabled(True)
        self.passwordLineEdit.setMinimumSize(QtCore.QSize(300, 40))
        self.passwordLineEdit.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"    border: 3px solid;\n"
"    border-color: rgb(121, 177, 236);\n"
"    font: 14pt \"Segoe UI\";\n"
"}\n"
"QLineEdit::focus{\n"
"    border: 2px solid;\n"
"    border-color: rgb(44, 89, 209);\n"
"}")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.horizontalLayout.addWidget(self.passwordLineEdit)
        spacerItem9 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 2, 1, 1)
        self.labelInfo = QtWidgets.QLabel(self.centralwidget)
        self.labelInfo.setStyleSheet("QLabel{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgb(255, 0, 0);\n"
"    font: 12pt \"Segoe UI\";\n"
"}")
        self.labelInfo.setText("")
        self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfo.setObjectName("labelInfo")
        self.gridLayout.addWidget(self.labelInfo, 5, 2, 1, 1)
        self.createAccountButton = QtWidgets.QPushButton(self.centralwidget)
        self.createAccountButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgb(106, 146, 255);\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgb(44, 89, 209);\n"
"    font: 10pt \"Segoe UI\";\n"
"}")
        self.createAccountButton.setObjectName("createAccountButton")
        self.gridLayout.addWidget(self.createAccountButton, 9, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "HFZ HASTANESİ\n"
"Bilgi Yönetim Sistemi\n"
"Hoş Geldiniz"))
        self.label.setText(_translate("MainWindow", "TC Kimlik No:"))
        self.loginButton.setText(_translate("MainWindow", "Giriş Yap"))
        self.forgotPassButton.setText(_translate("MainWindow", "Şifremi Unuttum"))
        self.label_2.setText(_translate("MainWindow", "Şifre:"))
        self.createAccountButton.setText(_translate("MainWindow", "Hesap Oluştur"))
