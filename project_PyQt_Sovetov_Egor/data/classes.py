from forms import mainForm
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QMainWindow
from data.functions import generate_pass, check_password


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(852, 645)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 481, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.generateButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.generateButton.setObjectName("pushButton")
        self.generateButton.clicked(generate_pass())

        self.horizontalLayout.addWidget(self.generateButton)

        self.generatedPass = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.generatedPass.setText("")
        self.generatedPass.setObjectName("label")

        self.horizontalLayout.addWidget(self.generatedPass)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.pass_for_check = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.pass_for_check.setObjectName("lineEdit")
        self.pass_for_check.setText('введите пароль для проверки(от 8 до 20 символов)')

        self.horizontalLayout_2.addWidget(self.pass_for_check)

        self.checkButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.checkButton.setObjectName("pushButton_1")
        self.checkButton.clicked(check_password())

        self.horizontalLayout_2.addWidget(self.checkButton)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 390, 181, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.tableView = QtWidgets.QTableView(parent=self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(560, 10, 256, 571))
        self.tableView.setObjectName("tableView")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 26))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.generateButton.setText(_translate("MainWindow", "сгенерировать пароль:"))
        self.checkButton.setText(_translate("MainWindow", "проверить пароль"))
        self.pushButton_2.setText(_translate("MainWindow", "сохранить пароль"))



class Manager(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
