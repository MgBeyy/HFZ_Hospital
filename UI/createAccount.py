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
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setMinimumSize(QtCore.QSize(100, 0))
        self.label_17.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_17.addWidget(self.label_17)
        self.numberLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.numberLineEdit.setMinimumSize(QtCore.QSize(300, 40))
        self.numberLineEdit.setMaximumSize(QtCore.QSize(300, 40))
        self.numberLineEdit.setStyleSheet("QLineEdit{\n"
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
        self.numberLineEdit.setObjectName("numberLineEdit")
        self.horizontalLayout_17.addWidget(self.numberLineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_17, 6, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.createAccountButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.createAccountButton_2.setMinimumSize(QtCore.QSize(120, 50))
        self.createAccountButton_2.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.createAccountButton_2.setFont(font)
        self.createAccountButton_2.setStyleSheet("QPushButton{\n"
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
        self.createAccountButton_2.setObjectName("createAccountButton_2")
        self.horizontalLayout_4.addWidget(self.createAccountButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout, 11, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
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
        spacerItem5 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout, 9, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
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
        spacerItem8 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 2, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem10)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setMinimumSize(QtCore.QSize(100, 0))
        self.label_15.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_15.addWidget(self.label_15)
        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setMinimumSize(QtCore.QSize(300, 40))
        self.nameLineEdit.setMaximumSize(QtCore.QSize(300, 40))
        self.nameLineEdit.setStyleSheet("QLineEdit{\n"
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
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.horizontalLayout_15.addWidget(self.nameLineEdit)
        spacerItem11 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem12)
        self.gridLayout.addLayout(self.horizontalLayout_15, 3, 2, 1, 1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem13)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setMinimumSize(QtCore.QSize(100, 0))
        self.label_19.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_19.addWidget(self.label_19)
        self.adressLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.adressLineEdit.setMinimumSize(QtCore.QSize(300, 40))
        self.adressLineEdit.setMaximumSize(QtCore.QSize(300, 40))
        self.adressLineEdit.setStyleSheet("QLineEdit{\n"
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
        self.adressLineEdit.setObjectName("adressLineEdit")
        self.horizontalLayout_19.addWidget(self.adressLineEdit)
        spacerItem14 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem15)
        self.gridLayout.addLayout(self.horizontalLayout_19, 8, 2, 1, 1)
        self.logInButton = QtWidgets.QPushButton(self.centralwidget)
        self.logInButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgb(106, 146, 255);\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgb(44, 89, 209);\n"
"    font: 10pt \"Segoe UI\";\n"
"}")
        self.logInButton.setObjectName("logInButton")
        self.gridLayout.addWidget(self.logInButton, 15, 2, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem16, 1, 2, 1, 1)
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
        spacerItem17 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 5, 0, 1, 2)
        self.labelInfo = QtWidgets.QLabel(self.centralwidget)
        self.labelInfo.setStyleSheet("QLabel{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgb(255, 0, 0);\n"
"    font: 12pt \"Segoe UI\";\n"
"}")
        self.labelInfo.setText("")
        self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfo.setObjectName("labelInfo")
        self.gridLayout.addWidget(self.labelInfo, 12, 2, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 49, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem18, 13, 2, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem19, 5, 3, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem20)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setMinimumSize(QtCore.QSize(100, 0))
        self.label_18.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_18.addWidget(self.label_18)
        self.emailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emailLineEdit.setMinimumSize(QtCore.QSize(300, 40))
        self.emailLineEdit.setMaximumSize(QtCore.QSize(300, 40))
        self.emailLineEdit.setStyleSheet("QLineEdit{\n"
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
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.horizontalLayout_18.addWidget(self.emailLineEdit)
        spacerItem21 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem21)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem22)
        self.gridLayout.addLayout(self.horizontalLayout_18, 7, 2, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem23)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setMinimumSize(QtCore.QSize(100, 0))
        self.label_16.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_16.addWidget(self.label_16)
        self.lastNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lastNameLineEdit.setMinimumSize(QtCore.QSize(300, 40))
        self.lastNameLineEdit.setMaximumSize(QtCore.QSize(300, 40))
        self.lastNameLineEdit.setStyleSheet("QLineEdit{\n"
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
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.horizontalLayout_16.addWidget(self.lastNameLineEdit)
        spacerItem24 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem24)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem25)
        self.gridLayout.addLayout(self.horizontalLayout_16, 4, 2, 1, 1)
        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        self.infoLabel.setStyleSheet("QLabel{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgb(255, 0, 0);\n"
"    font: 12pt \"Segoe UI\";\n"
"}")
        self.infoLabel.setText("")
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName("infoLabel")
        self.gridLayout.addWidget(self.infoLabel, 10, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_17.setText(_translate("MainWindow", "Telefon:"))
        self.createAccountButton_2.setText(_translate("MainWindow", "Hesap Oluştur"))
        self.label_2.setText(_translate("MainWindow", "Şifre:"))
        self.label.setText(_translate("MainWindow", "TC Kimlik No:"))
        self.label_15.setText(_translate("MainWindow", "İsim:"))
        self.label_19.setText(_translate("MainWindow", "Adres:"))
        self.logInButton.setText(_translate("MainWindow", "Giriş Yap"))
        self.label_3.setText(_translate("MainWindow", "HFZ HASTANESİ\n"
"Bilgi Yönetim Sistemi\n"
"Kayıt Ol"))
        self.label_18.setText(_translate("MainWindow", "E-Mail:"))
        self.label_16.setText(_translate("MainWindow", "Soyad:"))
