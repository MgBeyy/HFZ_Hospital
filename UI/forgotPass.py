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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
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
        self.forgotPassTC = QtWidgets.QLineEdit(self.centralwidget)
        self.forgotPassTC.setMinimumSize(QtCore.QSize(300, 40))
        self.forgotPassTC.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.forgotPassTC.setFont(font)
        self.forgotPassTC.setStyleSheet("QLineEdit{\n"
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
        self.forgotPassTC.setObjectName("forgotPassTC")
        self.horizontalLayout.addWidget(self.forgotPassTC)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
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
        self.forgotPassEPosta = QtWidgets.QLineEdit(self.centralwidget)
        self.forgotPassEPosta.setMinimumSize(QtCore.QSize(300, 40))
        self.forgotPassEPosta.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.forgotPassEPosta.setFont(font)
        self.forgotPassEPosta.setStyleSheet("QLineEdit{\n"
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
        self.forgotPassEPosta.setObjectName("forgotPassEPosta")
        self.horizontalLayout_2.addWidget(self.forgotPassEPosta)
        spacerItem4 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.getPass = QtWidgets.QPushButton(self.centralwidget)
        self.getPass.setMinimumSize(QtCore.QSize(120, 50))
        self.getPass.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.getPass.setFont(font)
        self.getPass.setStyleSheet("QPushButton{\n"
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
        self.getPass.setObjectName("getPass")
        self.horizontalLayout_3.addWidget(self.getPass)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
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
        self.horizontalLayout_4.addWidget(self.logInButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 8, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 3, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem8, 10, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 126, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 9, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem10, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 2)
        self.labelInfo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.labelInfo.setFont(font)
        self.labelInfo.setStyleSheet("QLabel{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: rgb(112, 231, 60);\n"
"    font: 12pt \"Segoe UI\";\n"
"}")
        self.labelInfo.setText("")
        self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfo.setObjectName("labelInfo")
        self.gridLayout.addWidget(self.labelInfo, 7, 1, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem11 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.forgotPassPhone = QtWidgets.QLineEdit(self.centralwidget)
        self.forgotPassPhone.setMinimumSize(QtCore.QSize(300, 40))
        self.forgotPassPhone.setMaximumSize(QtCore.QSize(300, 40))
        self.forgotPassPhone.setStyleSheet("QLineEdit{\n"
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
        self.forgotPassPhone.setObjectName("forgotPassPhone")
        self.horizontalLayout_5.addWidget(self.forgotPassPhone)
        spacerItem12 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        spacerItem13 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.gridLayout.addLayout(self.horizontalLayout_5, 6, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "TC Kimlik No:"))
        self.label.setText(_translate("MainWindow", "E-Posta:"))
        self.getPass.setText(_translate("MainWindow", "Şifre Al"))
        self.logInButton.setText(_translate("MainWindow", "Giriş Yap"))
        self.label_4.setText(_translate("MainWindow", "HFZ Hastanesi\n"
"Bilgi Yönetim Sistemi"))
        self.label_3.setText(_translate("MainWindow", "Telefon:"))
