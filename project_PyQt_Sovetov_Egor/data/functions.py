from random import randint, choice, random
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QApplication
import sys
import data
from forms import form

def generate_pass(self):
    eng_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                   'h', 'i', 'j', 'k', 'l', 'm', 'n',
                   'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z']
    rus_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
                   'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                   'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
                   'э', 'ю', 'я']
    spec_symbols = ['`', '~', '@', '#', '№', '$', '%', '^', '&', '?',
                    '*', '-', '_', '+', '=', '/', '|', ',', '.', '>',
                    '<', ':', ';']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ]
    password = ''
    low_register = False
    up_register = False
    spec_symb = False
    onenum = False
    twonum = False
    TwoInRow = False
    symb_num = randint(8, 20)
    all_lists = [eng_letters, rus_letters, spec_symbols, nums]
    for symbols in range(symb_num - 4):
        ch = choice(all_lists)
        if ch == rus_letters or ch == eng_letters:
            r = choice([0, 1])
            if r == 1:
                symb = choice(ch).upper()
                up_register = True
            else:
                symb = choice(ch)
                low_register = True
        if ch == spec_symbols:
            symb = choice(ch)
            spec_symb = True
        if ch == nums:
            symb = choice(ch)
            if onenum:
                symb = choice(ch)
                twonum = True
            else:
                symb = choice(ch)
                onenum = True
        for symbol in range(len(password)):
            if password.count(symb) == 4:
                ch.remove(symb)
        if TwoInRow:
            ch = choice(all_lists)
            if ch == rus_letters or ch == eng_letters:
                if choice([0, 1]) == 1:
                    symb = choice(ch).upper()
                    up_register = True
                else:
                    symb = choice(ch)
                    low_register = True
            if ch == spec_symbols:
                symb = choice(ch)
                spec_symb = True
            if ch == nums:
                symb = choice(ch)
                if onenum:
                    symb = choice(ch)
                    twonum = True
                else:
                    symb = choice(ch)
                    onenum = True
            for symbol in range(len(password)):
                if password.count(symb) == 4:
                    ch.remove(symb)
        password = f'{password}{symb}'
        if len(password) > 2:
            if password[-1] == password[-2]:
                TwoInRow = True
            else:
                TwoInRow = False
    for i in range(4):
        if not up_register:
            letters_list = [eng_letters, rus_letters]
            ch = choice(letters_list)
            symb = choice(ch).upper()
        elif not low_register:
            langlist = [eng_letters, rus_letters]
            ch = choice(langlist)
            symb = choice(ch)
        elif not spec_symb:
            symb = choice(spec_symbols)
        elif not onenum:
            symb = choice(nums)
        elif onenum and not twonum:
            symb = choice(nums)
        else:
            ch = choice(all_lists)
            if ch == rus_letters or ch == eng_letters:
                if random == 1:
                    symb = choice(ch).upper()
                    print(symb)
                    up_register = True
                else:
                    symb = choice(ch)
                    low_register = True
            if ch == spec_symbols:
                symb = choice(ch)
                spec_symb = True
            if ch == nums:
                symb = choice(ch)
                if onenum:
                    symb = choice(ch)
                    twonum = True
                else:
                    symb = choice(ch)
                    onenum = True
            for symbol in range(len(password)):
                if password.count(symb) == 4:
                    ch.remove(symb)
            if TwoInRow:
                ch = choice(all_lists)
                if ch == rus_letters or ch == eng_letters:
                    if choice([0, 1]) == 1:
                        symb = choice(ch).upper()
                        up_register = True
                    else:
                        symb = choice(ch)
                        low_register = True
                if ch == spec_symbols:
                    symb = choice(ch)
                    spec_symb = True
                if ch == nums:
                    symb = choice(ch)
                    if onenum:
                        symb = choice(ch)
                        twonum = True
                    else:
                        symb = choice(ch)
                        onenum = True
                for symbol in range(len(password)):
                    if password.count(symb) == 4:
                        ch.remove(symb)
        password = f'{password}{symb}'
        if len(password) > 2:
            if password[-1] == password[-2]:
                TwoInRow = True
            else:
                TwoInRow = False
        password = f'{password}{symb}'
    return password

def check_password():
    password = pass_for_check
    low_register = False
    up_register = False
    spec_symb = False
    onenum = False
    twonum = False
    if 7 < len(pass_for_check) < 21:
        for i in range(len(pass_for_check)):
            letter = pass_for_check[i]
            if letter in eng_letters or letter in rus_letters:
                if letter.islower():
                    low_register = True
                if letter.isupper():
                    up_register = True
            if letter in spec_symbols:
                spec_symb = True
            if letter in nums:
                if not onenum:
                    onenum = True
                else:
                    twonum = True
            if pass_for_check.count(letter) > 4:
                self.pass_for_check.setText('пароль ненадежный')
                break
            if i >= 2:
                if pass_for_check[i] == pass_for_check[i - 1] and pass_for_check[i] == pass_for_check[i - 2]:
                    self.pass_for_check.setText('пароль ненадежный')
        if low_register and up_register and spec_symb and twonum:
            self.pass_for_check.setText('пароль безопасен')
    else:
        self.pass_for_check.setText('пароль безопасен')


def main():
    app = QApplication(sys.argv)
    ex = form.Manager()
    ex.show()
    sys.exit(app.exec())


