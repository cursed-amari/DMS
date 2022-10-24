# Form implementation generated from reading ui file 'calc_init.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from calc_init_class import Ui_MainWindow_init
import random


enemy_list = []
class InitiativeWindow(QtWidgets.QMainWindow, Ui_MainWindow_init):
    def __init__(self, hero):
        super().__init__()
        self.setupUi(self)
        self.app_func()
        self.hero = hero

    def app_func(self):
        self.pushButton_initiative.clicked.connect(self.calk_initiative)
        self.pushButton_add.clicked.connect(self.check_input)
        self.pushButton_clean_enemy.clicked.connect(self.clean_enemy)

    def check_input(self):
        try:
            initiative = int(self.enemy_initiative_edit.text())
            self.add_enemy()
        except:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Не корректный ввод инициативы')
            error.setIcon(QMessageBox.Icon.Warning)
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.setDefaultButton(QMessageBox.StandardButton.Ok)

            error.buttonClicked.connect(self.popup_action)

            error.exec()

    def add_enemy(self):
        global enemy_list
        value = ''
        in_enemy_list = False
        name = self.enemy_name_edit.text()
        initiative = int(self.enemy_initiative_edit.text())
        if name == '':
            if not enemy_list:
                name = 'Enemy_0'
            else:
                for i in range(len(enemy_list)):
                    name = 'Enemy_' + str(i+1)
        for item in range(len(enemy_list)):
            if name in enemy_list[item]:
                in_enemy_list = True
        if in_enemy_list == True:
            name += '_' + str(item)
        enemy_list += (initiative + random.randint(1, 20), name),
        for i in range(len(enemy_list)):
            value += f'{enemy_list[i][1]}' + ' ' + f'{enemy_list[i][0]}' + '\n'
        self.label_enemy.setText(value)

    def clean_enemy(self):
        global enemy_list
        enemy_list = []
        self.label_enemy.setText('')

    def calk_initiative(self):
        '''
        DOCKSTRING: подсчёт инициативы
        :param but:
        :return:
        '''
        global enemy_list
        chr_list = []
        chr_list += enemy_list
        value = ''
        for i in range(len(self.hero)):
            t = int(self.hero['charapter' + str(i)]['initiative']) + random.randint(1, 20)
            n = self.hero['charapter' + str(i)]['name']
            chr_list += (t, n),

        chr_list.sort(key=lambda x: (x[0], x[1]), reverse=True)
        for i in range(len(chr_list)):
            value += f'{chr_list[i][1]}' + ' ' + f'{chr_list[i][0]}' + '\n'
        self.label_calk_enemy.setText(value)

    def popup_action(self, but):
        if but.text() == 'Ok':
            print('Ошибка ввода')
        pass


