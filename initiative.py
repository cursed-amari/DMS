from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from loguru import logger
from initiative_class import Ui_MainWindow_init
from initiative_add_enemy_dialog import Ui_Dialog_add_enemy
from initiative_redaction_enemy_dialog import Ui_Dialog_redaction_enemy_in_enemy
from initiative_redaction_enemy_dialog_2 import Ui_Dialog_redaction_enemy_in_initiative
from initiative_save_preset_enemy_dialog import Ui_Dialog_save_preset_enemy
import random
import copy

class InitiativeWindow(QtWidgets.QMainWindow, Ui_MainWindow_init):
    def __init__(self, hero, dict_preset):
        super().__init__()
        self.setupUi(self)
        self.hero = hero
        self.status_initiative = "enemy"
        self.enemy_list = []
        self.hero_list = []
        self.initiative_list = []
        self.enemy_dict_preset = dict_preset
        self.app_func()

    def app_func(self):
        #radioButton
        self.checkBox_left_menu.toggled.connect(self.show_left_menu)
        self.checkBox_right_menu.toggled.connect(self.show_right_menu)
        #pushButton
        self.pushButton_add_enemy.clicked.connect(self.add_enemy)
        self.pushButton_redaction_enemy.clicked.connect(self.choose_redaction)
        self.pushButton_add_preset.clicked.connect(self.add_preset)
        self.pushButton_roll_initiative.clicked.connect(self.initiative_sort)
        self.pushButton_del_enemy.clicked.connect(self.del_enemy)
        self.pushButton_clear_list.clicked.connect(self.clear_list)
        self.pushButton_load_preset.clicked.connect(self.load_preset)
        self.pushButton_del_preset.clicked.connect(self.del_preset)
        self.pushButton_apply_player_dice.clicked.connect(self.view_player_initiative)
        #lineEdit

        #method
        self.view_player_initiative()
        self.view_enemy_preset()


    """
    Main
    """

    def show_left_menu(self, bool_val):
        if bool_val:
            self.options_frame.show()
        else:
            self.options_frame.hide()

    def show_right_menu(self, bool_val):
        if bool_val:
            self.preset_frame.show()
        else:
            self.preset_frame.hide()

    @logger.catch
    def add_enemy(self, bool_val):
        self.Dialog_add_enemy = QtWidgets.QDialog()
        self.ui_add_enemy = Ui_Dialog_add_enemy()
        self.ui_add_enemy.setupUi(self.Dialog_add_enemy)

        self.app_func_for_add_enemy()

        self.Dialog_add_enemy.exec()

    @logger.catch
    def app_func_for_add_enemy(self):
        self.ui_add_enemy.pushButton_ok.clicked.connect(self.check_input_for_add_enemy)

    @logger.catch
    def check_input_for_add_enemy(self, bool_val):
        try:
            chek_initiative = int(self.ui_add_enemy.enemy_initiative_edit.text())
            chek_initiative = str(self.ui_add_enemy.enemy_name_edit.text())
            chek_initiative = int(int(self.ui_add_enemy.enemy_hp_edit.text()))

            self.collect_add_enemy()
        except ValueError:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Не корректный ввод!')
            error.setIcon(QMessageBox.Icon.Warning)
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.setDefaultButton(QMessageBox.StandardButton.Ok)
            error.setDetailedText('HP и инициатива должны состоять только из цифр')

            error.buttonClicked.connect(self.popup_action)

            error.exec()
            logger.info("input_chek. except")

    @logger.catch
    def collect_add_enemy(self):
        if self.ui_add_enemy.enemy_name_edit.text() != "":
            if self.ui_add_enemy.spinBox_amount_enemy.text() == "0":
                self.enemy_list.append([self.ui_add_enemy.enemy_initiative_edit.text(), self.ui_add_enemy.enemy_name_edit.text(),
                                   int(self.ui_add_enemy.enemy_hp_edit.text())], )
            else:
                for i in range(int(self.ui_add_enemy.spinBox_amount_enemy.text())):
                    self.enemy_list.append(
                        [self.ui_add_enemy.enemy_initiative_edit.text(),
                         self.ui_add_enemy.enemy_name_edit.text() + "_" + str(i+1), int(self.ui_add_enemy.enemy_hp_edit.text())], )
        else:
            if self.ui_add_enemy.spinBox_amount_enemy.text() == "0":
                self.enemy_list.append([self.ui_add_enemy.enemy_initiative_edit.text(), "Enemy",
                                   int(self.ui_add_enemy.enemy_hp_edit.text())], )
            else:
                for i in range(int(self.ui_add_enemy.spinBox_amount_enemy.text())):
                    self.enemy_list.append(
                        [self.ui_add_enemy.enemy_initiative_edit.text(),
                         "Enemy" + "_" + str(i+1), int(self.ui_add_enemy.enemy_hp_edit.text())], )
        self.initiative_enemy_view()

    @logger.catch
    def initiative_sort(self, bool_val):
        self.initiative_list = []
        self.hero_list = []

        for i in self.hero.keys():
            initiative = "NotFound"
            if i == "character0":
                key_hero = "character0"
                if self.set_player_dice_edit_char_0.text() == "":
                    initiative = "NOT"
                else:
                    initiative = int(self.set_player_dice_edit_char_0.text())
            if i == "character1":
                key_hero = "character1"
                if self.set_player_dice_edit_char_1.text() == "":
                    initiative = "NOT"
                else:
                    initiative = int(self.set_player_dice_edit_char_1.text())
            if i == "character2":
                key_hero = "character2"
                if self.set_player_dice_edit_char_2.text() == "":
                    initiative = "NOT"
                else:
                    initiative = int(self.set_player_dice_edit_char_2.text())
            if i == "character3":
                key_hero = "character3"
                if self.set_player_dice_edit_char_3.text() == "":
                    initiative = "NOT"
                else:
                    initiative = int(self.set_player_dice_edit_char_3.text())

            if initiative != "NOT" and initiative != "NotFound":
                name = self.hero[i]['name']
                hp = int(self.hero[i]['hp'])
                self.initiative_list += [initiative, name, hp],
                self.hero_list.append(name, )
            else:
                pass

        for i in enumerate(self.enemy_list):
            initiative = int(self.enemy_list[i[0]][0]) + random.randint(1, 20)
            name = self.enemy_list[i[0]][1]
            hp = int(self.enemy_list[i[0]][2])
            self.initiative_list += [initiative, name, hp],

        self.initiative_list.sort(key=lambda x: (x[0], x[1]), reverse=True)
        self.initiative_sort_view()

    @logger.catch
    def initiative_sort_view(self):
        self.status_initiative = "initiative"
        self.listWidget_initiative.clear()
        for i in self.initiative_list:
            self.listWidget_initiative.addItem(f"{i[0]} {i[1]} {i[2]}")

    @logger.catch
    def initiative_enemy_view(self):
        self.status_initiative = "enemy"
        self.listWidget_initiative.clear()
        for i in self.enemy_list:
            self.listWidget_initiative.addItem(f"{i[0]} {i[1]} {i[2]}")

    @logger.catch
    def del_enemy(self, bool_val=True):
        try:
            value = " ".join(self.listWidget_initiative.currentItem().text().split(" ")[1:-1])
            if value not in self.hero_list:
                for i in enumerate(self.initiative_list):
                    if value == self.initiative_list[i[0]][1]:
                        self.initiative_list.pop(i[0])
                for i in enumerate(self.enemy_list):
                    if value == self.enemy_list[i[0]][1]:
                        self.enemy_list.pop(i[0])
                if self.status_initiative == "initiative":
                    self.initiative_sort_view()
                else:
                    self.initiative_enemy_view()
            else:
                error = QMessageBox()
                error.setWindowTitle('Ошибка')
                error.setText('Нельзя удалить героя из битвы')
                error.setIcon(QMessageBox.Icon.Warning)
                error.setStandardButtons(QMessageBox.StandardButton.Ok)
                error.setDefaultButton(QMessageBox.StandardButton.Ok)

                error.buttonClicked.connect(self.popup_action)

                error.exec()
                logger.info("input_chek. except")
        except AttributeError:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Выберите объект для удаления!')
            error.setIcon(QMessageBox.Icon.Warning)
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.setDefaultButton(QMessageBox.StandardButton.Ok)

            error.buttonClicked.connect(self.popup_action)

            error.exec()
        logger.info("input_chek. except")

    @logger.catch
    def choose_redaction(self, bool_val):
        if self.status_initiative == "initiative":
            self.redaction_enemy_in_initiative()
        else:
            self.redaction_enemy_in_enemy()


    @logger.catch
    def redaction_enemy_in_enemy(self):
        try:
            self.Dialog_redaction_enemy_in_enemy = QtWidgets.QDialog()
            self.ui_redaction_enemy_in_enemy = Ui_Dialog_redaction_enemy_in_enemy()
            self.ui_redaction_enemy_in_enemy.setupUi(self.Dialog_redaction_enemy_in_enemy)
            self.ui_redaction_enemy_in_enemy.enemy_name_edit.setText(" ".join(self.listWidget_initiative.currentItem().text().split(" ")[1:-1]))
            self.ui_redaction_enemy_in_enemy.enemy_initiative_edit.setText(self.listWidget_initiative.currentItem().text().split(" ")[0])
            self.ui_redaction_enemy_in_enemy.enemy_hp_edit.setText(self.listWidget_initiative.currentItem().text().split(" ")[-1])

            self.app_func_for_redaction_enemy_in_enemy()

            self.Dialog_redaction_enemy_in_enemy.exec()
        except AttributeError:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Выберите объект для редактирования!')
            error.setIcon(QMessageBox.Icon.Warning)
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.setDefaultButton(QMessageBox.StandardButton.Ok)

            error.buttonClicked.connect(self.popup_action)

            error.exec()
            logger.info("input_chek. except")

    @logger.catch
    def app_func_for_redaction_enemy_in_enemy(self):
        self.ui_redaction_enemy_in_enemy.pushButton_ok.clicked.connect(self.check_input_redaction_enemy_in_enemy)

    @logger.catch
    def check_input_redaction_enemy_in_enemy(self, bool_val):
        try:
            name = str(self.ui_redaction_enemy_in_enemy.enemy_name_edit.text())
            initiative = int(self.ui_redaction_enemy_in_enemy.enemy_initiative_edit.text())
            hp = int(self.ui_redaction_enemy_in_enemy.enemy_hp_edit.text())

            self.set_redaction_enemy_in_enemy()
        except ValueError:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Не корректный ввод!')
            error.setIcon(QMessageBox.Icon.Warning)
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.setDefaultButton(QMessageBox.StandardButton.Ok)
            error.setDetailedText('HP и инициатива должны состоять только из цифр')

            error.buttonClicked.connect(self.popup_action)

            error.exec()
            logger.info("input_chek. except")

    @logger.catch
    def set_redaction_enemy_in_enemy(self):
        for i in self.enemy_list:
            if i[1] == " ".join(self.listWidget_initiative.currentItem().text().split(" ")[1:-1]):
                i[0] = self.ui_redaction_enemy_in_enemy.enemy_initiative_edit.text()
                i[1] = self.ui_redaction_enemy_in_enemy.enemy_name_edit.text()
                i[2] = self.ui_redaction_enemy_in_enemy.enemy_hp_edit.text()
        self.initiative_enemy_view()

    @logger.catch
    def redaction_enemy_in_initiative(self):
        try:
            self.Dialog_redaction_enemy_in_initiative = QtWidgets.QDialog()
            self.ui_redaction_enemy_in_initiative = Ui_Dialog_redaction_enemy_in_initiative()
            self.ui_redaction_enemy_in_initiative.setupUi(self.Dialog_redaction_enemy_in_initiative)
            self.ui_redaction_enemy_in_initiative.enemy_current_hp.setText(self.listWidget_initiative.currentItem().text().split(" ")[-1])

            self.app_func_for_redaction_enemy_in_initiative()

            self.Dialog_redaction_enemy_in_initiative.exec()
        except AttributeError:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Выберите объект для редактирования!')
            error.setIcon(QMessageBox.Icon.Warning)
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.setDefaultButton(QMessageBox.StandardButton.Ok)

            error.buttonClicked.connect(self.popup_action)

            error.exec()
            logger.info("input_chek. except")

    @logger.catch
    def app_func_for_redaction_enemy_in_initiative(self):
        try:
            self.ui_redaction_enemy_in_initiative.pushButton_ok.clicked.connect(self.add_hp_enemy_in_initiative)
            self.ui_redaction_enemy_in_initiative.pushButton_minus_hp.clicked.connect(self.minus_hp_enemy_in_initiative)
            self.ui_redaction_enemy_in_initiative.pushButton_set_hp.clicked.connect(self.set_hp_enemy_in_initiative)
        except ValueError:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Не корректный ввод!')
            error.setIcon(QMessageBox.Icon.Warning)
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.setDefaultButton(QMessageBox.StandardButton.Ok)
            error.setDetailedText('HP и инициатива должны состоять только из цифр')

            error.buttonClicked.connect(self.popup_action)

            error.exec()
            logger.info("input_chek. except")

    @logger.catch
    def add_hp_enemy_in_initiative(self, bool_val):
        for i in self.initiative_list:
            if i[1] == " ".join(self.listWidget_initiative.currentItem().text().split(" ")[1:-1]):
                i[2] = int(i[2]) + int(self.ui_redaction_enemy_in_initiative.enemy_hp_edit.text())
        self.initiative_sort_view()

    @logger.catch
    def minus_hp_enemy_in_initiative(self, bool_val):
        try:
            for i in self.initiative_list:
                if i[1] == " ".join(self.listWidget_initiative.currentItem().text().split(" ")[1:-1]):
                    i[2] = int(i[2]) - int(self.ui_redaction_enemy_in_initiative.enemy_hp_edit.text())
                    if i[2] <= 0 and " ".join(
                            self.listWidget_initiative.currentItem().text().split(" ")[1:-1]) not in self.hero_list:
                        self.del_enemy()
            self.initiative_sort_view()
        except AttributeError:
            pass

    @logger.catch
    def set_hp_enemy_in_initiative(self, bool_val):
        for i in self.initiative_list:
            if i[1] == " ".join(self.listWidget_initiative.currentItem().text().split(" ")[1:-1]):
                i[2] = int(self.ui_redaction_enemy_in_initiative.enemy_hp_edit.text())
                if i[2] <= 0 and " ".join(
                        self.listWidget_initiative.currentItem().text().split(" ")[1:-1]) not in self.hero_list:
                    self.del_enemy()
        self.initiative_sort_view()

    @logger.catch
    def clear_list(self, bool_):
        self.listWidget_initiative.clear()
        self.enemy_list = []

    """
    Options
    """

    @logger.catch
    def view_player_initiative(self, bool_val=False):
        if "character0" in self.hero.keys():
            self.set_player_dice_edit_char_0.setText(
                str(int(self.hero["character0"]["initiative"]) + random.randint(1, 20)))
            self.initiative_char_0 = self.hero["character0"]["initiative"]
        if "character1" in self.hero.keys():
            self.set_player_dice_edit_char_1.setText(
                str(int(self.hero["character1"]["initiative"]) + random.randint(1, 20)))
            self.initiative_char_1 = self.hero["character1"]["initiative"]
        if "character2" in self.hero.keys():
            self.set_player_dice_edit_char_2.setText(
                str(int(self.hero["character2"]["initiative"]) + random.randint(1, 20)))
            self.initiative_char_2 = self.hero["character2"]["initiative"]
        if "character3" in self.hero.keys():
            self.set_player_dice_edit_char_3.setText(
                str(int(self.hero["character3"]["initiative"]) + random.randint(1, 20)))
            self.initiative_char_3 = self.hero["character3"]["initiative"]

    """
    Preset
    """

    @logger.catch
    def add_preset(self, bool_val):
        self.Dialog_add_preset = QtWidgets.QDialog()
        self.ui_save_preset_enemy = Ui_Dialog_save_preset_enemy()
        self.ui_save_preset_enemy.setupUi(self.Dialog_add_preset)


        self.app_func_for_add_preset()

        self.Dialog_add_preset.exec()

    @logger.catch
    def app_func_for_add_preset(self):
        self.ui_save_preset_enemy.pushButton_ok.clicked.connect(self.collect_add_preset)

    @logger.catch
    def collect_add_preset(self, bool_val):
        copy_list = copy.copy(self.enemy_list)
        self.enemy_dict_preset[self.ui_save_preset_enemy.preset_name_edit.text()] = copy_list
        self.view_enemy_preset()

    def view_enemy_preset(self):
        if self.enemy_dict_preset:
            self.listWidget_preset.clear()
            for i in self.enemy_dict_preset.keys():
                self.listWidget_preset.addItem(i)

    def load_preset(self):
        try:
            self.enemy_list = []
            copy_list = copy.copy(self.enemy_dict_preset[self.listWidget_preset.currentItem().text()])
            self.enemy_list = copy_list
            self.initiative_enemy_view()
        except AttributeError:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Выберите объект для загрузки!')
            error.setIcon(QMessageBox.Icon.Warning)
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.setDefaultButton(QMessageBox.StandardButton.Ok)

            error.buttonClicked.connect(self.popup_action)

            error.exec()
            logger.info("input_chek. except")

    def del_preset(self):
        try:
            self.enemy_dict_preset.pop(self.listWidget_preset.currentItem().text())
            self.view_enemy_preset()
        except AttributeError:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Выберите объект для удаления!')
            error.setIcon(QMessageBox.Icon.Warning)
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.setDefaultButton(QMessageBox.StandardButton.Ok)

            error.buttonClicked.connect(self.popup_action)

            error.exec()
            logger.info("input_chek. except")

    @logger.catch
    def popup_action(self, but):
        '''
        DOCKSTRING: Заглушка для ошибок
        '''
        if but.text() == 'Ok':
            logger.info("popup_action")





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = InitiativeWindow()
    MainWindow.show()
    sys.exit(app.exec())