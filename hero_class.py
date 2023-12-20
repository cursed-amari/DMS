import random

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QPoint

from initializing_windows.redaction_hp_tracker import Ui_Dialog_redaction_hp_tracker
from loguru import logger

from hero_stats_window import HeroStats


class Hero:
    def __init__(self, centralwidget, name: str, max_hp: int, ac: int, initiative: int, notes: str, player_class: str, current_hp: int=False, lss_json: dict=False):
        self.lss_json = lss_json
        if lss_json:
            self.json_flag = True
            self.name = lss_json.get('name').get('value')
            self.race = lss_json.get('info').get('race').get('value')
            self.player_class = lss_json.get('info').get('charClass').get('value')
            self.level = lss_json.get('info').get('level').get('value')
            try:
                self.gold = lss_json.get('coins').get('gp').get('value')
            except AttributeError:
                self.gold = 0
            if 'initiative' in lss_json.get('vitality'):
                self.initiative = lss_json.get('vitality').get('initiative').get('value')
            else:
                self.initiative = lss_json.get('stats').get('dex').get('modifier')
            self.ac = lss_json.get('vitality').get('ac').get('value')
            self.speed = lss_json.get('vitality').get('speed').get('value')
            self.max_hp = lss_json.get('vitality').get('hp-max').get('value')
            self.current_hp = lss_json.get('vitality').get('hp-current').get('value')
            self.str = lss_json.get('stats').get('str').get('score')
            self.dex = lss_json.get('stats').get('dex').get('score')
            self.con = lss_json.get('stats').get('con').get('score')
            self.int = lss_json.get('stats').get('int').get('score')
            self.wis = lss_json.get('stats').get('wis').get('score')
            self.cha = lss_json.get('stats').get('cha').get('score')
            self.str_mod = lss_json.get('stats').get('str').get('modifier')
            self.dex_mod = lss_json.get('stats').get('dex').get('modifier')
            self.con_mod = lss_json.get('stats').get('con').get('modifier')
            self.int_mod = lss_json.get('stats').get('int').get('modifier')
            self.wis_mod = lss_json.get('stats').get('wis').get('modifier')
            self.cha_mod = lss_json.get('stats').get('cha').get('modifier')
            self.str_save = lss_json.get('stats').get('str').get('modifier') + lss_json.get('proficiency') \
                if lss_json.get('saves').get('str').get('isProf') else lss_json.get('stats').get('str').get('modifier')
            self.dex_save = lss_json.get('stats').get('dex').get('modifier') + lss_json.get('proficiency') \
                if lss_json.get('saves').get('dex').get('isProf') else lss_json.get('stats').get('dex').get('modifier')
            self.con_save = lss_json.get('stats').get('con').get('modifier') + lss_json.get('proficiency') \
                if lss_json.get('saves').get('con').get('isProf') else lss_json.get('stats').get('con').get('modifier')
            self.int_save = lss_json.get('stats').get('int').get('modifier') + lss_json.get('proficiency') \
                if lss_json.get('saves').get('int').get('isProf') else lss_json.get('stats').get('int').get('modifier')
            self.wis_save = lss_json.get('stats').get('wis').get('modifier') + lss_json.get('proficiency') \
                if lss_json.get('saves').get('wis').get('isProf') else lss_json.get('stats').get('wis').get('modifier')
            self.cha_save = lss_json.get('stats').get('cha').get('modifier') + lss_json.get('proficiency') \
                if lss_json.get('saves').get('cha').get('isProf') else lss_json.get('stats').get('cha').get('modifier')
            self.notes = lss_json.get("text").get("equipment").get("value").get("data").get("content")
        else:
            self.json_flag = False
            self.name = name
            if current_hp:
                self.current_hp = int(current_hp)
            else:
                self.current_hp = int(max_hp)
            self.max_hp = max_hp
            self.ac = ac
            self.initiative = initiative
            self.notes = notes
            self.player_class = player_class

        self.hero_stat_window = HeroStats()

        self.__initialization(centralwidget)
        self.__app_func(centralwidget)
        self.__sets_app()
        self.__refresh_stat_hero_window()

        self.label_name.enterEvent = self.show_hero_stat_window
        self.label_name.leaveEvent = self.hide_hero_stat_window

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @logger.catch
    def get_save_stats(self):
        return self.name, self.max_hp, self.ac, self.initiative, self.notes,\
               self.player_class, self.current_hp, self.lss_json

    @logger.catch
    def get_initiative(self):
        return random.randint(1, 20) + self.initiative

    @logger.catch
    def get_player_class(self):
        return self.player_class

    @logger.catch
    def __initialization(self, centralwidget):
        self.frame_hero = QtWidgets.QFrame(centralwidget)
        self.frame_hero.setGeometry(QtCore.QRect(230, 130, 160, 200))
        self.frame_hero.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_hero.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        self.frame_hero.setSizePolicy(sizePolicy)
        self.label_name = QtWidgets.QLabel(self.frame_hero)
        self.label_name.setGeometry(QtCore.QRect(0, 0, 160, 25))
        self.label_name.setStyleSheet("font-weight:bold")
        self.label_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_hp_character = QtWidgets.QLabel(self.frame_hero)
        self.label_hp_character.setGeometry(QtCore.QRect(15, 27, 25, 25))
        self.label_hp_character.setStyleSheet("font-weight:bold")
        self.pushButton_hp = QtWidgets.QPushButton(self.frame_hero)
        self.pushButton_hp.setGeometry(QtCore.QRect(40, 27, 50, 25))
        self.pushButton_hp.setText("HP")
        self.label_initiative = QtWidgets.QLabel(self.frame_hero)
        self.label_initiative.setGeometry(QtCore.QRect(30, 60, 60, 25))
        self.label_initiative.setStyleSheet("font-weight:bold")
        self.label_initiative.setText("Initiative")
        self.label_initiative.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_initiative = QtWidgets.QLineEdit(self.frame_hero)
        self.lineEdit_initiative.setGeometry(QtCore.QRect(90, 60, 50, 25))
        self.label_ac = QtWidgets.QLabel(self.frame_hero)
        self.label_ac.setGeometry(QtCore.QRect(95, 27, 25, 25))
        self.label_ac.setStyleSheet("font-weight:bold")
        self.lineEdit_ac = QtWidgets.QLineEdit(self.frame_hero)
        self.lineEdit_ac.setGeometry(QtCore.QRect(120, 27, 25, 25))
        self.lineEdit_ac.setText("AC")
        self.textEdit_notes = QtWidgets.QTextEdit(self.frame_hero)
        self.textEdit_notes.setGeometry(QtCore.QRect(20, 90, 120, 100))

        _translate = QtCore.QCoreApplication.translate
        self.label_hp_character.setText(_translate("MainWindow", "Hp"))
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.label_ac.setText(_translate("MainWindow", "Ac"))
        self.label_initiative.setText(_translate("MainWindow", "Initiative"))


    @logger.catch
    def get_all_widgets(self):
        return (self.frame_hero, self.label_name, self.label_hp_character, self.pushButton_hp, self.label_initiative,
                self.lineEdit_initiative, self.label_ac, self.lineEdit_ac, self.textEdit_notes)
    @logger.catch
    def __app_func(self, centralwidget):
        #textEdit
        self.textEdit_notes.textChanged.connect(self._save_text)
        #pushButton
        self.pushButton_hp.clicked.connect(self._hp_edit)
        #lineEdit
        self.lineEdit_ac.textChanged.connect(self._save_ac)
        self.lineEdit_initiative.textChanged.connect(self._save_initiative)

    @logger.catch
    def show_hero_stat_window(self, event):
        self.hero_stat_window.move(self.frame_hero.mapToGlobal(QPoint(0+160, 0)))

        self.__refresh_stat_hero_window()

        self.hero_stat_window.show()

    @logger.catch
    def hide_hero_stat_window(self, event):
        self.hero_stat_window.hide()

    @logger.catch
    def _save_ac(self, bool_val=False):
        self.ac = self.lineEdit_ac.text()

    @logger.catch
    def _save_initiative(self, bool_val=False):
        self.initiative = self.lineEdit_initiative.text()

    @logger.catch
    def _save_text(self, bool_val=False):
        self.notes = self.textEdit_notes.toPlainText()

    @logger.catch
    def __sets_app(self):
        self._set_name()
        self._set_hp()
        self._set_ac()
        self._set_initiative()
        self._set_notes()

    @logger.catch
    def _set_name(self):
        self.label_name.setText(self.name)

    @logger.catch
    def _set_hp(self):
        self.pushButton_hp.setText(f"{self.current_hp}/{self.max_hp}")

    @logger.catch
    def _set_ac(self):
        self.lineEdit_ac.setText(str(self.ac))

    @logger.catch
    def _set_initiative(self):
        self.lineEdit_initiative.setText(str(self.initiative))

    @logger.catch
    def _set_notes(self):
        if self.json_flag:
            text = ""

            for i in self.notes:
                if i.get("content"):
                    for k in i.get("content"):
                        text += k.get("text")

            self.textEdit_notes.setText(f"Gold: {self.gold}\n{text}")
        else:
            self.textEdit_notes.setText(self.notes)

    @logger.catch
    def get_frame(self):
        return self.frame_hero

    @logger.catch
    def _hp_edit(self, bool_val):
        Dialog_redaction_hp = QtWidgets.QDialog()
        self.ui_redaction_hp = Ui_Dialog_redaction_hp_tracker()
        self.ui_redaction_hp.setupUi(Dialog_redaction_hp)
        Dialog_redaction_hp.show()
        self.ui_redaction_hp.label_current_hp.setText(self.name)
        self.ui_redaction_hp.label_view_current_hp.setText(f'Hp: {self.current_hp}/{self.max_hp}')

        self.ui_redaction_hp.pushButton_add_hp.clicked.connect(self._add_hp_hero)
        self.ui_redaction_hp.pushButton_minus_hp.clicked.connect(self._minus_hp_hero)
        self.ui_redaction_hp.pushButton_set_hp.clicked.connect(self._set_hp_hero)
        self.ui_redaction_hp.pushButton_restore_hp.clicked.connect(self._restore_hp_hero)
        Dialog_redaction_hp.exec()

    @logger.catch
    def _add_hp_hero(self, bool_val):
        self.current_hp = self.current_hp + int(self.ui_redaction_hp.edit_new_hp.text())
        self._set_hp()

    @logger.catch
    def _minus_hp_hero(self, bool_val):
        self.current_hp = self.current_hp - int(self.ui_redaction_hp.edit_new_hp.text())
        self._set_hp()

    @logger.catch
    def _set_hp_hero(self, bool_val):
        self.max_hp = int(self.ui_redaction_hp.edit_new_hp.text())
        self._set_hp()

    @logger.catch
    def _restore_hp_hero(self, bool_val):
        self.current_hp = self.max_hp
        self._set_hp()

    @logger.catch
    def __refresh_stat_hero_window(self):
        if self.json_flag:
            self.hero_stat_window.label_name.setText(f"{self.name}\n{self.race} {self.player_class}\n{self.level}")
            self.hero_stat_window.lineEdit_ac.setText(f"Ac: {self.ac}")
            self.hero_stat_window.lineEdit_speed.setText(f"Speed: {self.speed}")
            self.hero_stat_window.lineEdit_hp.setText(f"Hp: {self.current_hp}/{self.max_hp}")
            self.hero_stat_window.lineEdit_initiative.setText(f"Initiative {self.initiative}")
            self.hero_stat_window.label_str.setText(f"Str: {self.str}; Modifier: {self.str_mod}; Save: {self.str_save}")
            self.hero_stat_window.label_dex.setText(f"Dex: {self.dex}; Modifier: {self.dex_mod}; Save: {self.dex_save}")
            self.hero_stat_window.label_con.setText(f"Con: {self.con}; Modifier: {self.con_mod}; Save: {self.con_save}")
            self.hero_stat_window.label_int.setText(f"Int: {self.int}; Modifier: {self.int_mod}; Save: {self.int_save}")
            self.hero_stat_window.label_wis.setText(f"Wis: {self.wis}; Modifier: {self.wis_mod}; Save: {self.wis_save}")
            self.hero_stat_window.label_cha.setText(f"Cha: {self.cha}; Modifier: {self.cha_mod}; Save: {self.cha_save}")
        else:
            self.hero_stat_window.label_name.setText(f"{self.name}\n{self.player_class}")
            self.hero_stat_window.lineEdit_ac.setText(f"Ac: {self.ac}")
            self.hero_stat_window.lineEdit_hp.setText(f"Hp: {self.current_hp}/{self.max_hp}")
            self.hero_stat_window.lineEdit_initiative.setText(f"Initiative {self.initiative}")
