from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
import sys
from random import randint, choice, random

import data.functions


class Manager(QWidget):
    generated = False

    def __init__(self):
        super().__init__()
        self.Manager()
        self.crutch()
    def Manager(self):
        self.setGeometry(100, 100, 852, 645)
        self.setWindowTitle('менеджер паролей')

        self.generated_pass = QLabel(self)
        self.generated_pass.resize(235, 28)
        self.generated_pass.move(280, 87)

        self.Generatebutton = QPushButton(self)
        self.Generatebutton.resize(235,28)
        self.Generatebutton.move(22,87)
        self.Generatebutton.clicked.connect(lambda: self.crutch())
        self.Generatebutton.setText('Сгенерировать пароль')

    def crutch(self):
        if Manager.generated:

            self.a = data.functions.generate_pass(self)
            self.generated_pass.setText(self.a)
        else:
            self.generated_pass.setText('здесь будет ваш пароль')
            Manager.generated = True


