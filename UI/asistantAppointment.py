from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMaximumSize(QtCore.QSize(1500, 1000))
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"        background-color: rgb(255, 255, 255);\n"
"        font: 12pt \"Segoe UI\";\n"
"        border: none;\n"
"        gridline-color: rgb(224, 224, 224);\n"
"}\n"
"    \n"
"QTableWidget::item {\n"
"        padding: 10px;\n"
"        background-color: transparent;\n"
"        border: none;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"        background-color: rgb(183, 230, 255);\n"
"        color: black;\n"
"}\n"
"    \n"
"QHeaderView::section {\n"
"        background-color: rgb(255, 255, 255, 0);\n"
"        padding: 5px;\n"
"        font: 12pt \"Segoe UI\";\n"
"        border: none;\n"
"         border-bottom: 2px solid rgb(44, 89, 209);\n"
"    }")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.patientLabel = QtWidgets.QLabel(self.centralwidget)
        self.patientLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.patientLabel.setFont(font)
        self.patientLabel.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.patientLabel)
        self.patientComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.patientComboBox.setMaximumSize(QtCore.QSize(170, 16777215))
        self.patientComboBox.setStyleSheet("QComboBox {\n"
"    font: 12pt \"Segoe UI\";\n"
"    border: 2px solid;\n"
"    border-color: rgb(96, 205, 255);\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox QListView {\n"
"    background: white;\n"
"    border: 2px solid rgb(44, 89, 209);\n"
"\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"\n"
"    background-bottom-right-radius: 5px;\n"
"    background-bottom-left-radius: 5px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QComboBox QListView::item:hover {\n"
"                padding: 5px;\n"
"                margin: 2px;\n"
"                font-size: 14px;\n"
"                background-color: #f0f0f0;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background:  rgb(183, 230, 255);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: rgb(119, 249, 255);\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 3px solid;\n"
"    border-color: rgb(44, 89, 209);\n"
"}")
        self.patientComboBox.setObjectName("patinetComboBox")
        self.patientComboBox.addItem("")
        self.patientComboBox.addItem("")
        self.patientComboBox.addItem("")
        self.verticalLayout_3.addWidget(self.patientComboBox)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.departmantComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.departmantComboBox.setMaximumSize(QtCore.QSize(170, 16777215))
        self.departmantComboBox.setStyleSheet("QComboBox {\n"
"    font: 12pt \"Segoe UI\";\n"
"    border: 2px solid;\n"
"    border-color: rgb(96, 205, 255);\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox QListView {\n"
"    background: white;\n"
"    border: 2px solid rgb(44, 89, 209);\n"
"\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"\n"
"    background-bottom-right-radius: 5px;\n"
"    background-bottom-left-radius: 5px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QComboBox QListView::item:hover {\n"
"                padding: 5px;\n"
"                margin: 2px;\n"
"                font-size: 14px;\n"
"                background-color: #f0f0f0;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background:  rgb(183, 230, 255);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: rgb(119, 249, 255);\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 3px solid;\n"
"    border-color: rgb(44, 89, 209);\n"
"}")
        self.departmantComboBox.setObjectName("departmantComboBox")
        self.departmantComboBox.addItem("")
        self.departmantComboBox.addItem("")
        self.verticalLayout.addWidget(self.departmantComboBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.getAppointmentButton = QtWidgets.QPushButton(self.centralwidget)
        self.getAppointmentButton.setMinimumSize(QtCore.QSize(0, 40))
        self.getAppointmentButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(44, 89, 209);\n"
"    font: 75 16pt \"Segoe UI\";\n"
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
        self.getAppointmentButton.setObjectName("getAppointmentButton")
        self.verticalLayout_2.addWidget(self.getAppointmentButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setMinimumSize(QtCore.QSize(0, 50))
        self.exitButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(44, 89, 209);\n"
"    font: 75 16pt \"Segoe UI\";\n"
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
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout_2.addWidget(self.exitButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HFZ Hastanesi"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Tarih"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Doktor"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Bölüm"))
        self.patientLabel.setText(_translate("MainWindow", "Hasta Seç:"))
        self.patientComboBox.setItemText(0, _translate("MainWindow", "New Item"))
        self.patientComboBox.setItemText(1, _translate("MainWindow", "New Item"))
        self.patientComboBox.setItemText(2, _translate("MainWindow", "New Item"))
        self.label.setText(_translate("MainWindow", "Bölüm Seç:"))
        self.departmantComboBox.setItemText(0, _translate("MainWindow", "New Item"))
        self.departmantComboBox.setItemText(1, _translate("MainWindow", "New Item"))
        self.getAppointmentButton.setText(_translate("MainWindow", "Randevu Al"))
        self.exitButton.setText(_translate("MainWindow", "Çıkış"))
