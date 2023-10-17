import random

from PyQt6 import QtCore, QtGui, QtWidgets
from initializing_windows.redaction_hp_tracker import Ui_Dialog_redaction_hp_tracker
from loguru import logger


class Hero:
    def __init__(self, centralwidget, name: str, max_hp: int, ac: int, initiative: int, notes: str, player_class: str, current_hp: int = False,):
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

        self.__initialization(centralwidget)
        self.__app_func(centralwidget)
        self.__sets_app()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @logger.catch
    def get_save_stats(self):
        return self.name, self.max_hp, self.ac, self.initiative, self.notes, self.player_class, self.current_hp

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
    def __app_func(self, centralwidget):
        #textEdit
        self.textEdit_notes.textChanged.connect(self._save_text)
        #pushButton
        self.pushButton_hp.clicked.connect(self._hp_edit)
        #lineEdit
        self.lineEdit_ac.textChanged.connect(self._save_ac)
        self.lineEdit_initiative.textChanged.connect(self._save_initiative)

    @logger.catch
    def _save_ac(self, bool_val):
        self.ac = self.lineEdit_ac.text()

    @logger.catch
    def _save_initiative(self, bool_val):
        self.initiative = self.lineEdit_initiative.text()

    @logger.catch
    def _save_text(self, bool_val):
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
