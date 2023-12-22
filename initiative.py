import json

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMessageBox, QFileDialog
from loguru import logger

from enemy_class import Enemy
from initializing_windows.initiative_class import Ui_MainWindow_init
from initializing_windows.initiative_add_enemy_dialog import Ui_Dialog_add_enemy
from initializing_windows.initiative_redaction_enemy_dialog import Ui_Dialog_redaction_enemy_in_enemy
from initializing_windows.initiative_redaction_enemy_dialog_2 import Ui_Dialog_redaction_enemy_in_initiative
from initializing_windows.initiative_save_preset_enemy_dialog import Ui_Dialog_save_preset_enemy
import random
import constants


class InitiativeWindow(QtWidgets.QMainWindow, Ui_MainWindow_init):
    del_enemy_signal = pyqtSignal(list)
    def __init__(self, hero, dict_preset):
        super().__init__()
        self.setupUi(self)
        self.hero = hero
        self.status_initiative = "enemy"
        self.enemy_list = []
        self.hero_list = []
        self.in_initiative_hero = {}
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
        self.add_player_dice()
        self.view_player_initiative()
        self.load_enemy_data()
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
    def add_player_dice(self):
        for i in self.hero:
            if i not in self.in_initiative_hero:
                label_set_player_dice = QtWidgets.QLabel(self.options_frame)
                label_set_player_dice.setGeometry(QtCore.QRect(10, 250, 71, 25))
                label_set_player_dice.setStyleSheet("font-weight:bold")
                label_set_player_dice.setText(str(i))

                set_player_dice_edit = QtWidgets.QLineEdit(self.options_frame)
                set_player_dice_edit.setGeometry(QtCore.QRect(90, 250, 51, 25))

                self.in_initiative_hero.update({str(i): set_player_dice_edit})

                self.verticalLayout.addWidget(label_set_player_dice)
                self.verticalLayout.addWidget(set_player_dice_edit)

    @logger.catch
    def add_enemy(self, bool_val):
        self.token_path = None

        self.Dialog_add_enemy = QtWidgets.QDialog()
        self.Dialog_add_enemy.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.Dialog_add_enemy.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui_add_enemy = Ui_Dialog_add_enemy()
        self.ui_add_enemy.setupUi(self.Dialog_add_enemy)

        self.app_func_for_add_enemy()

        self.Dialog_add_enemy.exec()

    @logger.catch
    def app_func_for_add_enemy(self):
        self.add_enemy_set_comboBox()

        # self.ui_add_enemy.pushButton_ok.clicked.connect(self.check_type_enemy)
        self.ui_add_enemy.comboBox_danger.currentIndexChanged.connect(self.add_enemy_danger_sort)
        self.ui_add_enemy.lineEdit_search_enemy.textChanged.connect(self.add_enemy_search)
        self.ui_add_enemy.radioButton_fast_gen.toggled.connect(self.add_enemy_radiobutton)
        self.ui_add_enemy.listWidget_enemy.clicked.connect(self.add_enemy_show_enemy)
        self.ui_add_enemy.pushButton_token.clicked.connect(self.add_enemy_open_token)
        self.ui_add_enemy.pushButton_ok.clicked.connect(self.add_enemy_to_initiative)
        self.ui_add_enemy.spinBox_amount_enemy.valueChanged.connect(self.check_amoun_enemy)
        #method
        self.add_enemy_set_listWidget(self.data)

    @logger.catch
    def check_amoun_enemy(self, bool_val=False):
        if int(self.ui_add_enemy.spinBox_amount_enemy.text()) >= 8:
            self.user_error('Максимум 8 противников', "Больше просто не влезает на карту XD", "")
        else:
            pass

    @logger.catch
    def load_enemy_data(self):
        with open("./dnd_monsters.json", mode="r", encoding="UTF8") as file:
            self.data = json.load(file)

    @logger.catch
    def add_enemy_radiobutton(self, bool_val):
        if bool_val:
            self.ui_add_enemy.frame_gen.hide()
            self.ui_add_enemy.frame_fast_gen.show()
        else:
            self.ui_add_enemy.frame_gen.show()
            self.ui_add_enemy.frame_fast_gen.hide()

    @logger.catch
    def add_enemy_set_comboBox(self):
        for i in constants.ENEMY_DANGER:
            self.ui_add_enemy.comboBox_danger.addItem(i)

    @logger.catch
    def add_enemy_set_listWidget(self, data):
        self.ui_add_enemy.listWidget_enemy.clear()
        for i in data:
            self.ui_add_enemy.listWidget_enemy.addItem(i)

    @logger.catch
    def add_enemy_danger_sort(self, bool_val):
        if self.ui_add_enemy.comboBox_danger.currentText() != "all":
            sort_list = []
            for i in self.data.values():
                if i.get('danger') == self.ui_add_enemy.comboBox_danger.currentText():
                    sort_list.append(i)
            self.add_enemy_set_listWidget(sort_list)
        else:
            self.add_enemy_set_listWidget(self.data)

    @logger.catch
    def add_enemy_search(self, bool_val):
        if self.ui_add_enemy.lineEdit_search_enemy.text() == "":
            self.add_enemy_set_listWidget(self.data)
        else:
            sort_list = []
            for i in self.data:
                if self.ui_add_enemy.lineEdit_search_enemy.text() in i:
                    sort_list.append(i)
            self.add_enemy_set_listWidget(sort_list)

    @logger.catch
    def add_enemy_open_token(self, bool_val):
        self.token_path = QFileDialog.getOpenFileName(self, filter="Save (*.png)")[0]

    @logger.catch
    def add_enemy_show_enemy(self, bool_val):
        text = ""
        for key, value in self.data.get(self.ui_add_enemy.listWidget_enemy.currentItem().text()).items():
            text += key + ":" + str(value) + "\n"
        self.ui_add_enemy.label_enemy.setText(text)

    @logger.catch
    def add_enemy_to_initiative(self, bool_val):
        if self.ui_add_enemy.radioButton_fast_gen.isChecked():
            for i in range(int(self.ui_add_enemy.spinBox_amount_enemy.text())):
                if len(self.enemy_list) >= 8:
                    self.user_error('Максимум 8 противников', "Больше просто не влезает на карту XD", "")
                    break
                else:
                    enemy = Enemy(self.ui_add_enemy.enemy_name_edit.text(), self.ui_add_enemy.enemy_hp_edit.text(),
                                  self.ui_add_enemy.enemy_initiative_edit.text(), i+1, self.token_path, self.data)
                    self.enemy_list.append(enemy)
        else:
            for i in range(int(self.ui_add_enemy.spinBox_amount_enemy.text())):
                if len(self.enemy_list) >= 8:
                    self.user_error('Максимум 8 противников', "Больше просто не влезает на карту XD", "")
                    break
                else:
                    enemy = Enemy(self.ui_add_enemy.listWidget_enemy.currentItem().text(), "", "", i+1, self.token_path, self.data)
                    self.enemy_list.append(enemy)
        self.show_enemy()

    @logger.catch
    def show_enemy(self):
        self.listWidget_initiative.clear()
        for i in self.enemy_list:
            text = f"{i.get_modifier_initiative()} {i} {i.hp}"
            self.listWidget_initiative.addItem(text)

    @logger.catch
    def initiative_sort(self, bool_val):
        self.initiative_list = []
        self.hero_list = []

        for i in self.hero:
            initiative = "NotFound"
            for x in self.in_initiative_hero:
                if i == x:
                    if self.in_initiative_hero.get(x).text() == "":
                        initiative = "NOT"
                    else:
                        initiative = int(self.in_initiative_hero.get(i).text())

            if initiative != "NOT" and initiative != "NotFound":
                name = i
                hp = int(self.hero.get(i).current_hp)
                self.initiative_list += [initiative, name, hp],
                self.hero_list.append(name, )
            else:
                pass

        for i in self.enemy_list:
            initiative = i.get_initiative()
            name = i.name
            hp = i.hp
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
            self.listWidget_initiative.addItem(f"{i.get_modifier_initiative()} {i.name} {i.hp}")

    @logger.catch
    def del_enemy(self, bool_val=True):
        try:
            value = " ".join(self.listWidget_initiative.currentItem().text().split(" ")[1:-1])
            if value not in self.hero_list:
                for i in enumerate(self.initiative_list):
                    if value == self.initiative_list[i[0]][1]:
                        self.initiative_list.pop(i[0])
                for key, enemy in enumerate(self.enemy_list):
                    if value == enemy.name:
                        self.enemy_list.pop(key)
                if self.status_initiative == "initiative":
                    self.initiative_sort_view()
                else:
                    self.initiative_enemy_view()
            else:
                self.user_error('Нельзя удалить героя из битвы', "", "")
                logger.info("input_chek. except")
            self.del_enemy_signal.emit(self.initiative_list)
        except AttributeError:
            self.user_error('Выберите объект для удаления!', "", "")
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
            self.user_error('Выберите объект для редактирования!', "", "")
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
            self.user_error('Не корректный ввод!', "", 'HP и инициатива должны состоять только из цифр')
            logger.info("input_chek. except")

    @logger.catch
    def set_redaction_enemy_in_enemy(self):
        for i in self.enemy_list:
            if str(i) == " ".join(self.listWidget_initiative.currentItem().text().split(" ")[1:-1]):
                i.new_initiative(self.ui_redaction_enemy_in_enemy.enemy_initiative_edit.text())
                i.new_name(self.ui_redaction_enemy_in_enemy.enemy_name_edit.text())
                i.new_hp(self.ui_redaction_enemy_in_enemy.enemy_hp_edit.text())
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
            self.user_error('Выберите объект для редактирования!', "", "")
            logger.info("input_chek. except")

    @logger.catch
    def app_func_for_redaction_enemy_in_initiative(self):
        try:
            self.ui_redaction_enemy_in_initiative.pushButton_ok.clicked.connect(self.add_hp_enemy_in_initiative)
            self.ui_redaction_enemy_in_initiative.pushButton_minus_hp.clicked.connect(self.minus_hp_enemy_in_initiative)
            self.ui_redaction_enemy_in_initiative.pushButton_set_hp.clicked.connect(self.set_hp_enemy_in_initiative)
        except ValueError:
            self.user_error('Не корректный ввод!', "", 'HP и инициатива должны состоять только из цифр')
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
        for i in self.in_initiative_hero:
            self.in_initiative_hero.get(i).setText(str(int(self.hero.get(i).initiative) + random.randint(1, 20)))

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
        list_enemy = []
        for i in self.enemy_list:
            list_enemy.append(i.get_save_stats())
        self.enemy_dict_preset[self.ui_save_preset_enemy.preset_name_edit.text()] = list_enemy
        print(self.enemy_dict_preset)
        self.view_enemy_preset()

    @logger.catch
    def view_enemy_preset(self):
        self.listWidget_preset.clear()
        for i in self.enemy_dict_preset.keys():
            self.listWidget_preset.addItem(i)

    @logger.catch
    def load_preset(self, bool_val=False):
        try:
            self.enemy_list = []
            preset = self.enemy_dict_preset.get(self.listWidget_preset.currentItem().text())
            for i in preset:
                enemy = Enemy(i[0], i[1], i[2], i[3], i[4], self.data)
                self.enemy_list.append(enemy)
            self.initiative_enemy_view()
        except AttributeError as er:
            self.user_error('Выберите объект для загрузки!', "", "")
            logger.info(f"input_chek. except ({er})")

    @logger.catch
    def del_preset(self, bool_val=False):
        try:
            self.enemy_dict_preset.pop(self.listWidget_preset.currentItem().text())
            self.view_enemy_preset()
        except AttributeError:
            self.user_error('Выберите объект для удаления!', "", "")
            logger.info("input_chek. except")

    @logger.catch()
    def user_error(self, text: str, informative_text: str, detailed_text: str):
        error = QMessageBox()
        error.setWindowTitle('Ошибка')
        error.setText(text)
        error.setIcon(QMessageBox.Icon.Warning)
        error.setStandardButtons(QMessageBox.StandardButton.Ok)
        error.setDefaultButton(QMessageBox.StandardButton.Ok)
        error.setInformativeText(informative_text)
        error.setDetailedText(detailed_text)

        error.buttonClicked.connect(self.popup_action)

        error.exec()

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