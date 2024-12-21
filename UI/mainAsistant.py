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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")



        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMaximumSize(QtCore.QSize(1500, 1000))
        self.tableWidget.setStyleSheet("""QTableWidget {
        background-color: rgb(255, 255, 255);
        font: 12pt "Segoe UI";
        border: none;
        gridline-color: rgb(224, 224, 224);
}
    
QTableWidget::item {
        padding: 10px;
        background-color: transparent;
        border: none;
}

QTableWidget::item:selected {
        background-color: rgb(183, 230, 255);
        color: black;
}
    
QHeaderView::section {
        background-color: rgb(255, 255, 255, 0);
        padding: 5px;
        font: 12pt "Segoe UI";
        border: none;
		 border-bottom: 2px solid rgb(44, 89, 209);
    }""")
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

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.searchComboBox.setMaximumSize(QtCore.QSize(170, 16777215))
        self.searchComboBox.setStyleSheet("QComboBox {\n"
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
        self.searchComboBox.setObjectName("searchComboBox")
        self.searchComboBox.addItem("")
        self.searchComboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.searchComboBox)
        self.searchLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLineEdit.setMinimumSize(QtCore.QSize(500, 40))
        self.searchLineEdit.setMaximumSize(QtCore.QSize(500, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.searchLineEdit.setFont(font)
        self.searchLineEdit.setStyleSheet("QLineEdit{\n"
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
        self.searchLineEdit.setText("")
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout_2.addWidget(self.searchLineEdit)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setMinimumSize(QtCore.QSize(120, 40))
        self.searchButton.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("QPushButton{\n"
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
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.searchWarning = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.searchWarning.setFont(font)
        self.searchWarning.setStyleSheet("font: 12pt \"Segoe UI\";\n"
"color: red;")
        self.searchWarning.setText("")
        self.searchWarning.setObjectName("searchWarning")
        self.horizontalLayout_2.addWidget(self.searchWarning)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.tableComboBox.setMaximumSize(QtCore.QSize(170, 16777215))
        self.tableComboBox.setStyleSheet("QComboBox {\n"
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
        self.tableComboBox.setObjectName("tableComboBox")
        self.tableComboBox.addItem("")
        self.tableComboBox.addItem("")
        self.verticalLayout.addWidget(self.tableComboBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.prescriptionButton = QtWidgets.QPushButton(self.centralwidget)
        self.prescriptionButton.setMinimumSize(QtCore.QSize(0, 40))
        self.prescriptionButton.setStyleSheet("QPushButton{\n"
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
        self.prescriptionButton.setObjectName("prescriptionButton")
        self.verticalLayout.addWidget(self.prescriptionButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.addPatient = QtWidgets.QPushButton(self.centralwidget)
        self.addPatient.setMinimumSize(QtCore.QSize(0, 40))
        self.addPatient.setStyleSheet("QPushButton{\n"
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
"}\n"
"")
        self.addPatient.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.addPatient)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.logOutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logOutButton.setMinimumSize(QtCore.QSize(0, 50))
        self.logOutButton.setStyleSheet("QPushButton{\n"
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
        self.logOutButton.setObjectName("logOutButton")
        self.verticalLayout.addWidget(self.logOutButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        self.searchComboBox.setItemText(0, _translate("MainWindow", "New Item"))
        self.searchComboBox.setItemText(1, _translate("MainWindow", "New Item"))
        self.searchLineEdit.setPlaceholderText(_translate("MainWindow", "Ara"))
        self.searchButton.setText(_translate("MainWindow", "ARA"))
        self.label.setText(_translate("MainWindow", "Tablo Seç:"))
        self.tableComboBox.setItemText(0, _translate("MainWindow", "New Item"))
        self.tableComboBox.setItemText(1, _translate("MainWindow", "New Item"))
        self.prescriptionButton.setText(_translate("MainWindow", "Randevu Oluştur"))
        self.addPatient.setText(_translate("MainWindow", "Hasta Ekle"))
        self.logOutButton.setText(_translate("MainWindow", "Çıkış"))
