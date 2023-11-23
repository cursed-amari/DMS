from PyQt6 import QtCore, QtGui, QtWidgets
from loguru import logger


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setStyleSheet("#background {\n"
                                      "    background-color: rgb(85, 85, 85);\n"
                                      "}")
        self.background.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.background.setObjectName("background")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.background)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.background)
        self.header.setStyleSheet("*{\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "    background: rgb(35, 35, 35);\n"
                                  "    border: none;\n"
                                  "}\n"
                                  "QPushButton{\n"
                                  "    color: rgb(85, 85, 85);\n"
                                  "    background: transparent;\n"
                                  "    border: none;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "    background: rgb(105, 105, 105);\n"
                                  "    border: none;\n"
                                  "}")
        self.header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_logo_app = QtWidgets.QFrame(self.header)
        self.frame_logo_app.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_logo_app.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_logo_app.setObjectName("frame_logo_app")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_logo_app)
        self.horizontalLayout_5.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.toolButton_logo_app = QtWidgets.QToolButton(self.frame_logo_app)
        self.toolButton_logo_app.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_logo_app.setIcon(icon)
        self.toolButton_logo_app.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_logo_app.setObjectName("toolButton_logo_app")
        self.horizontalLayout_5.addWidget(self.toolButton_logo_app)
        self.horizontalLayout_2.addWidget(self.frame_logo_app, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.frame_name_app = QtWidgets.QFrame(self.header)
        self.frame_name_app.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_name_app.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_name_app.setObjectName("frame_name_app")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_name_app)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_name_app = QtWidgets.QLabel(self.frame_name_app)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name_app.sizePolicy().hasHeightForWidth())
        self.label_name_app.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_name_app.setFont(font)
        self.label_name_app.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_name_app.setWordWrap(False)
        self.label_name_app.setObjectName("label_name_app")
        self.horizontalLayout_4.addWidget(self.label_name_app)
        self.label_username = QtWidgets.QLabel(self.frame_name_app)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_username.sizePolicy().hasHeightForWidth())
        self.label_username.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.horizontalLayout_4.addWidget(self.label_username)
        self.horizontalLayout_2.addWidget(self.frame_name_app)
        self.frame_navigations = QtWidgets.QFrame(self.header)
        self.frame_navigations.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_navigations.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_navigations.setObjectName("frame_navigations")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_navigations)
        self.horizontalLayout_3.setContentsMargins(0, 6, 5, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_minimized = QtWidgets.QPushButton(self.frame_navigations)
        self.pushButton_minimized.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/icon/minus.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushButton_minimized.setIcon(icon1)
        self.pushButton_minimized.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_minimized.setObjectName("pushButton_minimized")
        self.horizontalLayout_3.addWidget(self.pushButton_minimized)
        self.pushButton_exit = QtWidgets.QPushButton(self.frame_navigations)
        self.pushButton_exit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/icon/x.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_exit.setIcon(icon2)
        self.pushButton_exit.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout_3.addWidget(self.pushButton_exit)
        self.horizontalLayout_2.addWidget(self.frame_navigations, 0, QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout.addWidget(self.header, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.main = QtWidgets.QFrame(self.background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main.setObjectName("main")
        self.frame_menu = QtWidgets.QFrame(self.main)
        self.frame_menu.setGeometry(QtCore.QRect(0, 0, 42, 419))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_menu.sizePolicy().hasHeightForWidth())
        self.frame_menu.setSizePolicy(sizePolicy)
        self.frame_menu.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                      "color: rgb(247, 147, 30);\n"
                                      "border: none;\n")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.toolButton_menu = QtWidgets.QToolButton(self.frame_menu)
        self.toolButton_menu.setGeometry(QtCore.QRect(10, 0, 140, 23))
        self.menu_icon = QtGui.QIcon()
        self.menu_icon.addPixmap(QtGui.QPixmap("img/icon/menu.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_menu.setIcon(self.menu_icon)
        self.toolButton_menu.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_menu.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_menu.setObjectName("toolButton_menu")
        self.toolButton_tracker = QtWidgets.QToolButton(self.frame_menu)
        self.toolButton_tracker.setGeometry(QtCore.QRect(10, 42, 140, 23))
        self.tracker_icon = QtGui.QIcon()
        self.tracker_icon.addPixmap(QtGui.QPixmap("img/icon/tracker.ico"), QtGui.QIcon.Mode.Normal,
                               QtGui.QIcon.State.Off)
        self.toolButton_tracker.setIcon(self.tracker_icon)
        self.toolButton_tracker.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_tracker.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_tracker.setObjectName("toolButton_tracker")
        self.toolButton_scenario = QtWidgets.QToolButton(self.frame_menu)
        self.toolButton_scenario.setGeometry(QtCore.QRect(10, 90, 140, 23))
        self.scenario_icon = QtGui.QIcon()
        self.scenario_icon.addPixmap(QtGui.QPixmap("img/icon/scenario.ico"), QtGui.QIcon.Mode.Normal,
                                QtGui.QIcon.State.Off)
        self.toolButton_scenario.setIcon(self.scenario_icon)
        self.toolButton_scenario.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_scenario.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_scenario.setObjectName("toolButton_scenario")
        self.toolButton_notes = QtWidgets.QToolButton(self.frame_menu)
        self.toolButton_notes.setGeometry(QtCore.QRect(10, 138, 140, 23))
        self.notes_icon = QtGui.QIcon()
        self.notes_icon.addPixmap(QtGui.QPixmap("img/icon/notes.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_notes.setIcon(self.notes_icon)
        self.toolButton_notes.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_notes.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_notes.setObjectName("toolButton_notes")
        self.toolButton_rules = QtWidgets.QToolButton(self.frame_menu)
        self.toolButton_rules.setGeometry(QtCore.QRect(10, 234, 140, 23))
        self.options_icon = QtGui.QIcon()
        self.options_icon.addPixmap(QtGui.QPixmap("img/icon/options.ico"), QtGui.QIcon.Mode.Normal,
                               QtGui.QIcon.State.Off)
        self.toolButton_rules.setIcon(self.options_icon)
        self.toolButton_rules.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_rules.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_rules.setObjectName("toolButton_rules")
        self.toolButton_generate_store = QtWidgets.QToolButton(self.frame_menu)
        self.toolButton_generate_store.setGeometry(QtCore.QRect(10, 332, 140, 23))
        self.dice_icon = QtGui.QIcon()
        self.dice_icon.addPixmap(QtGui.QPixmap("img/icon/dice.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_generate_store.setIcon(self.dice_icon)
        self.toolButton_generate_store.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_generate_store.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_generate_store.setObjectName("toolButton_generate_store")
        self.toolButton_npc_generator = QtWidgets.QToolButton(self.frame_menu)
        self.toolButton_npc_generator.setGeometry(QtCore.QRect(10, 380, 140, 23))
        self.toolButton_npc_generator.setIcon(self.dice_icon)
        self.toolButton_npc_generator.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_npc_generator.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_npc_generator.setObjectName("toolButton_npc_generator")
        self.toolButton_music_changer = QtWidgets.QToolButton(self.frame_menu)
        self.toolButton_music_changer.setGeometry(QtCore.QRect(10, 186, 140, 23))
        self.music_icon = QtGui.QIcon()
        self.music_icon.addPixmap(QtGui.QPixmap("img/icon/music.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_music_changer.setIcon(self.music_icon)
        self.toolButton_music_changer.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_music_changer.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_music_changer.setObjectName("toolButton_music_changer")
        self.toolButton_img_view = QtWidgets.QToolButton(self.frame_menu)
        self.toolButton_img_view.setGeometry(QtCore.QRect(10, 280, 140, 23))
        self.img_icon = QtGui.QIcon()
        self.img_icon.addPixmap(QtGui.QPixmap("img/icon/img.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_img_view.setIcon(self.img_icon)
        self.toolButton_img_view.setIconSize(QtCore.QSize(18, 19))
        self.toolButton_img_view.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_img_view.setObjectName("toolButton_img_view")
        self.frame_main_app = QtWidgets.QFrame(self.main)
        self.frame_main_app.setGeometry(QtCore.QRect(42, 0, 795, 421))
        self.frame_main_app.setStyleSheet("")
        self.frame_main_app.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_main_app.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_main_app.setObjectName("frame_main_app")
        self.frame_scenario = QtWidgets.QFrame(self.frame_main_app)
        self.frame_scenario.setGeometry(QtCore.QRect(0, 0, 795, 421))
        self.frame_scenario.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_scenario.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_scenario.setObjectName("frame_scenario")
        self.text_chapter = QtWidgets.QTextEdit(self.frame_scenario)
        self.text_chapter.setGeometry(QtCore.QRect(10, 70, 771, 311))
        self.text_chapter.setObjectName("text_chapter")
        self.edit_add_chapter = QtWidgets.QLineEdit(self.frame_scenario)
        self.edit_add_chapter.setGeometry(QtCore.QRect(10, 40, 231, 28))
        self.edit_add_chapter.setObjectName("edit_add_chapter")
        self.list_tags = QtWidgets.QListWidget(self.frame_scenario)
        self.list_tags.setGeometry(QtCore.QRect(10, 70, 201, 301))
        self.list_tags.setObjectName("list_tags")
        self.radioButton_tags_notes = QtWidgets.QRadioButton(self.frame_scenario)
        self.radioButton_tags_notes.setGeometry(QtCore.QRect(10, 380, 95, 20))
        self.radioButton_tags_notes.setObjectName("radioButton_tags_notes")
        self.pushButton_del_chapter = QtWidgets.QPushButton(self.frame_scenario)
        self.pushButton_del_chapter.setGeometry(QtCore.QRect(285, 40, 41, 28))
        self.pushButton_del_chapter.setObjectName("pushButton_del_chapter")
        self.text_scenario = QtWidgets.QTextEdit(self.frame_scenario)
        self.text_scenario.setGeometry(QtCore.QRect(233, 36, 551, 361))
        self.text_scenario.setObjectName("text_scenario")
        self.pushButton_add_tags = QtWidgets.QPushButton(self.frame_scenario)
        self.pushButton_add_tags.setGeometry(QtCore.QRect(10, 40, 51, 28))
        self.pushButton_add_tags.setObjectName("pushButton_add_tags")
        self.pushButton_add_chapter = QtWidgets.QPushButton(self.frame_scenario)
        self.pushButton_add_chapter.setGeometry(QtCore.QRect(242, 40, 41, 28))
        self.pushButton_add_chapter.setObjectName("pushButton_add_chapter")
        self.pushButton_del_tags = QtWidgets.QPushButton(self.frame_scenario)
        self.pushButton_del_tags.setGeometry(QtCore.QRect(160, 40, 51, 28))
        self.pushButton_del_tags.setObjectName("pushButton_del_tags")
        self.comboBox_choose_chapter = QtWidgets.QComboBox(self.frame_scenario)
        self.comboBox_choose_chapter.setGeometry(QtCore.QRect(330, 40, 451, 28))
        self.comboBox_choose_chapter.setObjectName("comboBox_choose_chapter")
        self.text_chapter.raise_()
        self.list_tags.raise_()
        self.radioButton_tags_notes.raise_()
        self.pushButton_del_chapter.raise_()
        self.text_scenario.raise_()
        self.pushButton_add_tags.raise_()
        self.pushButton_add_chapter.raise_()
        self.pushButton_del_tags.raise_()
        self.comboBox_choose_chapter.raise_()
        self.edit_add_chapter.raise_()
        self.frame_notes = QtWidgets.QFrame(self.frame_main_app)
        self.frame_notes.setGeometry(QtCore.QRect(0, 0, 795, 421))
        self.frame_notes.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_notes.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_notes.setObjectName("frame_notes")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_notes)
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.note_edit_0 = QtWidgets.QTextEdit(self.frame_notes)
        self.note_edit_0.setObjectName("note_edit_0")
        self.horizontalLayout_8.addWidget(self.note_edit_0)
        self.note_edit_1 = QtWidgets.QTextEdit(self.frame_notes)
        self.note_edit_1.setObjectName("note_edit_1")
        self.horizontalLayout_8.addWidget(self.note_edit_1)
        self.note_edit_2 = QtWidgets.QTextEdit(self.frame_notes)
        self.note_edit_2.setObjectName("note_edit_2")
        self.horizontalLayout_8.addWidget(self.note_edit_2)
        self.note_edit_3 = QtWidgets.QTextEdit(self.frame_notes)
        self.note_edit_3.setObjectName("note_edit_3")
        self.horizontalLayout_8.addWidget(self.note_edit_3)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        self.frame_music_changer = QtWidgets.QFrame(self.frame_main_app)
        self.frame_music_changer.setGeometry(QtCore.QRect(0, 0, 795, 421))
        self.frame_music_changer.setStyleSheet("QFrame {\n"
                                               "    background-color: rgb(85, 85, 85);\n"
                                               "    opacity: 0.3;\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "\n"
                                               "QLineEdit {\n"
                                               "    background-color: rgb(55, 55, 55);\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "\n"
                                               "QTextEdit {\n"
                                               "    background-color: rgb(55, 55, 55);\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "\n"
                                               "QListWidget {\n"
                                               "    background-color: rgb(55, 55, 55);\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton {\n"
                                               "    background-color: rgb(55, 55, 55);\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:pressed {\n"
                                               "    background-color: rgb(105, 105, 105);\n"
                                               "}\n"
                                               "\n"
                                               "QSpinBox {\n"
                                               "    background-color: rgb(55, 55, 55);\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "\n"
                                               "QComboBox {\n"
                                               "    background-color: rgb(55, 55, 55);\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "\n"
                                               "QRadioButton {\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border-radius:  10px;\n"
                                               "}\n"
                                               "\n"
                                               "QCheckBox {\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border: none;\n"
                                               "}")
        self.frame_music_changer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_music_changer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_music_changer.setObjectName("frame_music_changer")
        self.scene_edit = QtWidgets.QLineEdit(self.frame_music_changer)
        self.scene_edit.setGeometry(QtCore.QRect(140, 40, 113, 22))
        self.scene_edit.setObjectName("scene_edit")
        self.label_category = QtWidgets.QLabel(self.frame_music_changer)
        self.label_category.setGeometry(QtCore.QRect(30, 20, 111, 16))
        self.label_category.setStyleSheet("font-weight:bold")
        self.label_category.setObjectName("label_category")
        self.pushButton_url_open = QtWidgets.QPushButton(self.frame_music_changer)
        self.pushButton_url_open.setGeometry(QtCore.QRect(370, 90, 93, 28))
        self.pushButton_url_open.setObjectName("pushButton_url_open")
        self.category_edit = QtWidgets.QLineEdit(self.frame_music_changer)
        self.category_edit.setGeometry(QtCore.QRect(40, 40, 91, 22))
        self.category_edit.setObjectName("category_edit")
        self.label_scene = QtWidgets.QLabel(self.frame_music_changer)
        self.label_scene.setGeometry(QtCore.QRect(140, 20, 111, 16))
        self.label_scene.setStyleSheet("font-weight:bold")
        self.label_scene.setObjectName("label_scene")
        self.listWidget_category = QtWidgets.QListWidget(self.frame_music_changer)
        self.listWidget_category.setGeometry(QtCore.QRect(40, 90, 151, 271))
        self.listWidget_category.setObjectName("listWidget_category")
        self.label_scene_url_2 = QtWidgets.QLabel(self.frame_music_changer)
        self.label_scene_url_2.setGeometry(QtCore.QRect(210, 70, 111, 16))
        self.label_scene_url_2.setStyleSheet("font-weight:bold")
        self.label_scene_url_2.setObjectName("label_scene_url_2")
        self.pushButton_url_delete = QtWidgets.QPushButton(self.frame_music_changer)
        self.pushButton_url_delete.setGeometry(QtCore.QRect(370, 330, 93, 28))
        self.pushButton_url_delete.setObjectName("pushButton_url_delete")
        self.listWidget_scene = QtWidgets.QListWidget(self.frame_music_changer)
        self.listWidget_scene.setGeometry(QtCore.QRect(210, 90, 151, 271))
        self.listWidget_scene.setObjectName("listWidget_scene")
        self.label_scene_url = QtWidgets.QLabel(self.frame_music_changer)
        self.label_scene_url.setGeometry(QtCore.QRect(260, 20, 111, 16))
        self.label_scene_url.setStyleSheet("font-weight:bold")
        self.label_scene_url.setObjectName("label_scene_url")
        self.label_category_open = QtWidgets.QLabel(self.frame_music_changer)
        self.label_category_open.setGeometry(QtCore.QRect(40, 70, 111, 16))
        self.label_category_open.setStyleSheet("font-weight:bold")
        self.label_category_open.setObjectName("label_category_open")
        self.pushButton_url_set = QtWidgets.QPushButton(self.frame_music_changer)
        self.pushButton_url_set.setGeometry(QtCore.QRect(640, 35, 93, 28))
        self.pushButton_url_set.setObjectName("pushButton_url_set")
        self.url_edit = QtWidgets.QLineEdit(self.frame_music_changer)
        self.url_edit.setGeometry(QtCore.QRect(260, 40, 361, 22))
        self.url_edit.setObjectName("url_edit")
        self.listWidget_music = QtWidgets.QListWidget(self.frame_music_changer)
        self.listWidget_music.setGeometry(QtCore.QRect(480, 90, 251, 221))
        self.listWidget_music.setObjectName("listWidget_music")
        self.pushButton_music_play = QtWidgets.QPushButton(self.frame_music_changer)
        self.pushButton_music_play.setGeometry(QtCore.QRect(480, 340, 93, 28))
        self.pushButton_music_play.setObjectName("pushButton_music_play")
        self.pushButton_music_pause = QtWidgets.QPushButton(self.frame_music_changer)
        self.pushButton_music_pause.setGeometry(QtCore.QRect(573, 340, 67, 28))
        self.pushButton_music_pause.setObjectName("pushButton_music_pause")
        self.pushButton_music_stop = QtWidgets.QPushButton(self.frame_music_changer)
        self.pushButton_music_stop.setGeometry(QtCore.QRect(640, 340, 93, 28))
        self.pushButton_music_stop.setObjectName("pushButton_music_stop")
        self.horizontalSlider_music = QtWidgets.QSlider(self.frame_music_changer)
        self.horizontalSlider_music.setGeometry(QtCore.QRect(480, 310, 251, 22))
        self.horizontalSlider_music.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_music.setObjectName("horizontalSlider_music")
        self.horizontalSlider_music.setStyleSheet("QSlider::handle:horizontal { background-color:  rgb(247, 147, 30); }")
        self.frame_rules = QtWidgets.QFrame(self.frame_main_app)
        self.frame_rules.setGeometry(QtCore.QRect(0, 0, 795, 421))
        self.frame_rules.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_rules.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_rules.setObjectName("frame_rules")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_rules)
        self.verticalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_box_rules = QtWidgets.QFrame(self.frame_rules)
        self.frame_box_rules.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_box_rules.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_box_rules.setObjectName("frame_box_rules")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_box_rules)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_rules = QtWidgets.QComboBox(self.frame_box_rules)
        self.comboBox_rules.setMinimumSize(QtCore.QSize(0, 20))
        self.comboBox_rules.setMaximumSize(QtCore.QSize(16777215, 20))
        self.comboBox_rules.setObjectName("comboBox_rules")
        self.gridLayout.addWidget(self.comboBox_rules, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_box_rules, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_text_rules = QtWidgets.QFrame(self.frame_rules)
        self.frame_text_rules.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_text_rules.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_text_rules.setObjectName("frame_text_rules")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_text_rules)
        self.horizontalLayout_9.setContentsMargins(9, 0, 9, 5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_rules = QtWidgets.QTextEdit(self.frame_text_rules)
        self.label_rules.setReadOnly(True)
        self.label_rules.setObjectName("label_rules")
        self.horizontalLayout_9.addWidget(self.label_rules)
        self.verticalLayout_2.addWidget(self.frame_text_rules)
        self.frame_generate_store = QtWidgets.QFrame(self.frame_main_app)
        self.frame_generate_store.setGeometry(QtCore.QRect(0, 0, 795, 421))
        self.frame_generate_store.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_generate_store.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_generate_store.setObjectName("frame_generate_store")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_generate_store)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_redaction_store = QtWidgets.QFrame(self.frame_generate_store)
        self.frame_redaction_store.setMinimumSize(QtCore.QSize(210, 0))
        self.frame_redaction_store.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_redaction_store.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_redaction_store.setObjectName("frame_redaction_store")
        self.label_race_vendor = QtWidgets.QLabel(self.frame_redaction_store)
        self.label_race_vendor.setGeometry(QtCore.QRect(10, 253, 55, 16))
        self.label_race_vendor.setObjectName("label_race_vendor")
        self.label_vendor = QtWidgets.QLabel(self.frame_redaction_store)
        self.label_vendor.setGeometry(QtCore.QRect(70, 130, 55, 16))
        self.label_vendor.setStyleSheet("font-weight:bold")
        self.label_vendor.setObjectName("label_vendor")
        self.edit_name_vendor = QtWidgets.QLineEdit(self.frame_redaction_store)
        self.edit_name_vendor.setGeometry(QtCore.QRect(10, 150, 161, 22))
        self.edit_name_vendor.setObjectName("edit_name_vendor")
        self.label_name_vendor = QtWidgets.QLabel(self.frame_redaction_store)
        self.label_name_vendor.setGeometry(QtCore.QRect(10, 130, 55, 16))
        self.label_name_vendor.setObjectName("label_name_vendor")
        self.text_notes = QtWidgets.QTextEdit(self.frame_redaction_store)
        self.text_notes.setGeometry(QtCore.QRect(10, 90, 200, 331))
        self.text_notes.setObjectName("text_notes")
        self.box_age_vendor = QtWidgets.QComboBox(self.frame_redaction_store)
        self.box_age_vendor.setGeometry(QtCore.QRect(10, 230, 161, 22))
        self.box_age_vendor.setObjectName("box_age_vendor")
        self.label_age_vendor = QtWidgets.QLabel(self.frame_redaction_store)
        self.label_age_vendor.setGeometry(QtCore.QRect(10, 213, 55, 16))
        self.label_age_vendor.setObjectName("label_age_vendor")
        self.box_sex_vendor = QtWidgets.QComboBox(self.frame_redaction_store)
        self.box_sex_vendor.setGeometry(QtCore.QRect(10, 190, 161, 22))
        self.box_sex_vendor.setObjectName("box_sex_vendor")
        self.box_race_vendor = QtWidgets.QComboBox(self.frame_redaction_store)
        self.box_race_vendor.setGeometry(QtCore.QRect(10, 270, 161, 22))
        self.box_race_vendor.setObjectName("box_race_vendor")
        self.box_choose_shop = QtWidgets.QComboBox(self.frame_redaction_store)
        self.box_choose_shop.setGeometry(QtCore.QRect(10, 40, 161, 22))
        self.box_choose_shop.setObjectName("box_choose_shop")
        self.label_store_name_2 = QtWidgets.QLabel(self.frame_redaction_store)
        self.label_store_name_2.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.label_store_name_2.setObjectName("label_store_name_2")
        self.radioButton_options_store = QtWidgets.QRadioButton(self.frame_redaction_store)
        self.radioButton_options_store.setGeometry(QtCore.QRect(10, 70, 71, 20))
        self.radioButton_options_store.setObjectName("radioButton_options_store")
        self.edit_store_name_2 = QtWidgets.QLineEdit(self.frame_redaction_store)
        self.edit_store_name_2.setGeometry(QtCore.QRect(10, 110, 161, 22))
        self.edit_store_name_2.setObjectName("edit_store_name_2")
        self.pushButton_del_store = QtWidgets.QPushButton(self.frame_redaction_store)
        self.pushButton_del_store.setGeometry(QtCore.QRect(170, 40, 41, 22))
        self.pushButton_del_store.setObjectName("pushButton_del_store")
        self.label_sex_vendor = QtWidgets.QLabel(self.frame_redaction_store)
        self.label_sex_vendor.setGeometry(QtCore.QRect(10, 173, 55, 16))
        self.label_sex_vendor.setObjectName("label_sex_vendor")
        self.box_personality_vendor = QtWidgets.QComboBox(self.frame_redaction_store)
        self.box_personality_vendor.setGeometry(QtCore.QRect(10, 310, 161, 22))
        self.box_personality_vendor.setObjectName("box_personality_vendor")
        self.label_personality_vendor = QtWidgets.QLabel(self.frame_redaction_store)
        self.label_personality_vendor.setGeometry(QtCore.QRect(10, 293, 61, 16))
        self.label_personality_vendor.setObjectName("label_personality_vendor")
        self.box_look_vendor = QtWidgets.QComboBox(self.frame_redaction_store)
        self.box_look_vendor.setGeometry(QtCore.QRect(10, 350, 161, 22))
        self.box_look_vendor.setObjectName("box_look_vendor")
        self.label_look_vendor = QtWidgets.QLabel(self.frame_redaction_store)
        self.label_look_vendor.setGeometry(QtCore.QRect(10, 333, 55, 16))
        self.label_look_vendor.setObjectName("label_look_vendor")
        self.box_voice_vendor = QtWidgets.QComboBox(self.frame_redaction_store)
        self.box_voice_vendor.setGeometry(QtCore.QRect(10, 390, 161, 22))
        self.box_voice_vendor.setObjectName("box_voice_vendor")
        self.label_voice_vendor = QtWidgets.QLabel(self.frame_redaction_store)
        self.label_voice_vendor.setGeometry(QtCore.QRect(10, 373, 55, 16))
        self.label_voice_vendor.setObjectName("label_voice_vendor")
        self.text_notes.raise_()
        self.label_race_vendor.raise_()
        self.label_vendor.raise_()
        self.edit_name_vendor.raise_()
        self.label_name_vendor.raise_()
        self.box_age_vendor.raise_()
        self.label_age_vendor.raise_()
        self.box_sex_vendor.raise_()
        self.box_race_vendor.raise_()
        self.box_choose_shop.raise_()
        self.label_store_name_2.raise_()
        self.radioButton_options_store.raise_()
        self.edit_store_name_2.raise_()
        self.pushButton_del_store.raise_()
        self.label_sex_vendor.raise_()
        self.box_personality_vendor.raise_()
        self.label_personality_vendor.raise_()
        self.box_look_vendor.raise_()
        self.label_look_vendor.raise_()
        self.box_voice_vendor.raise_()
        self.label_voice_vendor.raise_()
        self.horizontalLayout_11.addWidget(self.frame_redaction_store, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.frame_text_store = QtWidgets.QFrame(self.frame_generate_store)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_text_store.sizePolicy().hasHeightForWidth())
        self.frame_text_store.setSizePolicy(sizePolicy)
        self.frame_text_store.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_text_store.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_text_store.setObjectName("frame_text_store")
        self.box_generate_type = QtWidgets.QComboBox(self.frame_text_store)
        self.box_generate_type.setGeometry(QtCore.QRect(102, 40, 161, 28))
        self.box_generate_type.setObjectName("box_generate_type")
        self.label_shop_info = QtWidgets.QLabel(self.frame_text_store)
        self.label_shop_info.setGeometry(QtCore.QRect(59, 90, 241, 300))
        self.label_shop_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_shop_info.setObjectName("label_shop_info")
        self.box_generate_cost = QtWidgets.QComboBox(self.frame_text_store)
        self.box_generate_cost.setGeometry(QtCore.QRect(10, 40, 81, 28))
        self.box_generate_cost.setObjectName("box_generate_cost")
        self.label_cost_generate = QtWidgets.QLabel(self.frame_text_store)
        self.label_cost_generate.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.label_cost_generate.setObjectName("label_cost_generate")
        self.pushButton_generate_shop = QtWidgets.QPushButton(self.frame_text_store)
        self.pushButton_generate_shop.setGeometry(QtCore.QRect(270, 40, 93, 28))
        self.pushButton_generate_shop.setObjectName("pushButton_generate_shop")
        self.label_type_generate = QtWidgets.QLabel(self.frame_text_store)
        self.label_type_generate.setGeometry(QtCore.QRect(100, 20, 55, 16))
        self.label_type_generate.setObjectName("label_type_generate")
        self.horizontalLayout_11.addWidget(self.frame_text_store)
        self.frame_assortment_store = QtWidgets.QFrame(self.frame_generate_store)
        self.frame_assortment_store.setMinimumSize(QtCore.QSize(210, 0))
        self.frame_assortment_store.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_assortment_store.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_assortment_store.setObjectName("frame_assortment_store")
        self.label_2 = QtWidgets.QLabel(self.frame_assortment_store)
        self.label_2.setGeometry(QtCore.QRect(0, 20, 131, 16))
        self.label_2.setObjectName("label_2")
        self.search_assortment_edit = QtWidgets.QLineEdit(self.frame_assortment_store)
        self.search_assortment_edit.setGeometry(QtCore.QRect(0, 40, 201, 22))
        self.search_assortment_edit.setObjectName("search_assortment_edit")
        self.text_assortment_shop = QtWidgets.QTextEdit(self.frame_assortment_store)
        self.text_assortment_shop.setGeometry(QtCore.QRect(0, 70, 200, 351))
        self.text_assortment_shop.setObjectName("text_assortment_shop")
        self.horizontalLayout_11.addWidget(self.frame_assortment_store)
        self.frame_npc_generator = QtWidgets.QFrame(self.frame_main_app)
        self.frame_npc_generator.setGeometry(QtCore.QRect(0, 0, 795, 421))
        self.frame_npc_generator.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_npc_generator.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_npc_generator.setObjectName("frame_npc_generator")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_npc_generator)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_redaction_npc = QtWidgets.QFrame(self.frame_npc_generator)
        self.frame_redaction_npc.setMinimumSize(QtCore.QSize(190, 0))
        self.frame_redaction_npc.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_redaction_npc.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_redaction_npc.setObjectName("frame_redaction_npc")
        self.edit_npc_name = QtWidgets.QLineEdit(self.frame_redaction_npc)
        self.edit_npc_name.setGeometry(QtCore.QRect(20, 70, 161, 22))
        self.edit_npc_name.setObjectName("edit_npc_name")
        self.label_race_npc = QtWidgets.QLabel(self.frame_redaction_npc)
        self.label_race_npc.setGeometry(QtCore.QRect(20, 173, 55, 16))
        self.label_race_npc.setObjectName("label_race_npc")
        self.label_sex_npc = QtWidgets.QLabel(self.frame_redaction_npc)
        self.label_sex_npc.setGeometry(QtCore.QRect(20, 93, 55, 16))
        self.label_sex_npc.setObjectName("label_sex_npc")
        self.box_sex_npc = QtWidgets.QComboBox(self.frame_redaction_npc)
        self.box_sex_npc.setGeometry(QtCore.QRect(20, 110, 161, 22))
        self.box_sex_npc.setObjectName("box_sex_npc")
        self.pushButton_generate_npc = QtWidgets.QPushButton(self.frame_redaction_npc)
        self.pushButton_generate_npc.setGeometry(QtCore.QRect(40, 360, 93, 28))
        self.pushButton_generate_npc.setObjectName("pushButton_generate_npc")
        self.label_age_npc = QtWidgets.QLabel(self.frame_redaction_npc)
        self.label_age_npc.setGeometry(QtCore.QRect(20, 133, 55, 16))
        self.label_age_npc.setObjectName("label_age_npc")
        self.box_age_npc = QtWidgets.QComboBox(self.frame_redaction_npc)
        self.box_age_npc.setGeometry(QtCore.QRect(20, 150, 161, 22))
        self.box_age_npc.setObjectName("box_age_npc")
        self.box_race_npc = QtWidgets.QComboBox(self.frame_redaction_npc)
        self.box_race_npc.setGeometry(QtCore.QRect(20, 190, 161, 22))
        self.box_race_npc.setObjectName("box_race_npc")
        self.label_name_npc = QtWidgets.QLabel(self.frame_redaction_npc)
        self.label_name_npc.setGeometry(QtCore.QRect(20, 50, 55, 16))
        self.label_name_npc.setObjectName("label_name_npc")
        self.box_personality_npc = QtWidgets.QComboBox(self.frame_redaction_npc)
        self.box_personality_npc.setGeometry(QtCore.QRect(20, 230, 161, 22))
        self.box_personality_npc.setObjectName("box_personality_npc")
        self.label_personality_npc = QtWidgets.QLabel(self.frame_redaction_npc)
        self.label_personality_npc.setGeometry(QtCore.QRect(20, 213, 61, 16))
        self.label_personality_npc.setObjectName("label_personality_npc")
        self.box_look_npc = QtWidgets.QComboBox(self.frame_redaction_npc)
        self.box_look_npc.setGeometry(QtCore.QRect(20, 270, 161, 22))
        self.box_look_npc.setObjectName("box_look_npc")
        self.box_voice_npc = QtWidgets.QComboBox(self.frame_redaction_npc)
        self.box_voice_npc.setGeometry(QtCore.QRect(20, 313, 161, 22))
        self.box_voice_npc.setObjectName("box_voice_npc")
        self.label_look_npc = QtWidgets.QLabel(self.frame_redaction_npc)
        self.label_look_npc.setGeometry(QtCore.QRect(20, 253, 55, 16))
        self.label_look_npc.setObjectName("label_look_npc")
        self.label_voice_npc = QtWidgets.QLabel(self.frame_redaction_npc)
        self.label_voice_npc.setGeometry(QtCore.QRect(20, 296, 55, 16))
        self.label_voice_npc.setObjectName("label_voice_npc")
        self.horizontalLayout_12.addWidget(self.frame_redaction_npc, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.frame_view_npc = QtWidgets.QFrame(self.frame_npc_generator)
        self.frame_view_npc.setMinimumSize(QtCore.QSize(230, 0))
        self.frame_view_npc.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_view_npc.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_view_npc.setObjectName("frame_view_npc")
        self.label_generate_npc = QtWidgets.QLabel(self.frame_view_npc)
        self.label_generate_npc.setGeometry(QtCore.QRect(19, 104, 191, 291))
        self.label_generate_npc.setStyleSheet("font-weight:bold")
        self.label_generate_npc.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_generate_npc.setObjectName("label_generate_npc")
        self.box_generate_npc = QtWidgets.QComboBox(self.frame_view_npc)
        self.box_generate_npc.setGeometry(QtCore.QRect(60, 50, 170, 22))
        self.box_generate_npc.setObjectName("box_generate_npc")
        self.pushButton_del_npc = QtWidgets.QPushButton(self.frame_view_npc)
        self.pushButton_del_npc.setGeometry(QtCore.QRect(0, 50, 51, 22))
        self.pushButton_del_npc.setObjectName("pushButton_del_npc")
        self.horizontalLayout_12.addWidget(self.frame_view_npc, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.frame_text_npc = QtWidgets.QFrame(self.frame_npc_generator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_text_npc.sizePolicy().hasHeightForWidth())
        self.frame_text_npc.setSizePolicy(sizePolicy)
        self.frame_text_npc.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_text_npc.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_text_npc.setObjectName("frame_text_npc")
        self.text_generate_npc = QtWidgets.QTextEdit(self.frame_text_npc)
        self.text_generate_npc.setGeometry(QtCore.QRect(0, 70, 371, 340))
        self.text_generate_npc.setObjectName("text_generate_npc")
        self.horizontalLayout_12.addWidget(self.frame_text_npc)
        self.info = QtWidgets.QTextEdit(self.frame_main_app)
        self.info.setGeometry(QtCore.QRect(10, 4, 781, 411))
        self.info.setStyleSheet("QTextEdit {\n"
                                "    background-color: rgb(55, 55, 55);\n"
                                "    color: rgb(247, 147, 30);\n"
                                "    border: none;\n"
                                "}")
        self.info.setObjectName("info")
        self.frame_viewer = QtWidgets.QFrame(self.frame_main_app)
        self.frame_viewer.setGeometry(QtCore.QRect(0, 0, 791, 421))
        self.frame_viewer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_viewer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_viewer.setObjectName("frame_viewer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_viewer)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_viewer_navigations = QtWidgets.QFrame(self.frame_viewer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_viewer_navigations.sizePolicy().hasHeightForWidth())
        self.frame_viewer_navigations.setSizePolicy(sizePolicy)
        self.frame_viewer_navigations.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_viewer_navigations.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_viewer_navigations.setObjectName("frame_viewer_navigations")
        self.listWidget_img = QtWidgets.QListWidget(self.frame_viewer_navigations)
        self.listWidget_img.setGeometry(QtCore.QRect(0, 0, 521, 321))
        self.listWidget_img.setObjectName("listWidget_img")
        self.spinBox_enemy_token = QtWidgets.QSpinBox(self.frame_viewer_navigations)
        self.spinBox_enemy_token.setGeometry(QtCore.QRect(540, 10, 42, 22))
        self.spinBox_enemy_token.setObjectName("spinBox_enemy_token")
        self.spinBox_hero_token = QtWidgets.QSpinBox(self.frame_viewer_navigations)
        self.spinBox_hero_token.setGeometry(QtCore.QRect(540, 40, 42, 22))
        self.spinBox_hero_token.setObjectName("spinBox_hero_token")
        self.label_enemy_token = QtWidgets.QLabel(self.frame_viewer_navigations)
        self.label_enemy_token.setGeometry(QtCore.QRect(590, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_enemy_token.setFont(font)
        self.label_enemy_token.setObjectName("label_enemy_token")
        self.label_hero_token = QtWidgets.QLabel(self.frame_viewer_navigations)
        self.label_hero_token.setGeometry(QtCore.QRect(590, 40, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_hero_token.setFont(font)
        self.label_hero_token.setObjectName("label_hero_token")
        self.pushButton_reduce_token = QtWidgets.QPushButton(self.frame_viewer_navigations)
        self.pushButton_reduce_token.setGeometry(QtCore.QRect(540, 70, 75, 23))
        self.pushButton_reduce_token.setObjectName("pushButton_reduce_token")
        self.pushButton_increase_token = QtWidgets.QPushButton(self.frame_viewer_navigations)
        self.pushButton_increase_token.setGeometry(QtCore.QRect(540, 100, 75, 23))
        self.pushButton_increase_token.setObjectName("pushButton_increase_token")
        self.label_scale_img = QtWidgets.QLabel(self.frame_viewer_navigations)
        self.label_scale_img.setGeometry(QtCore.QRect(760, 50, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_scale_img.setFont(font)
        self.label_scale_img.setObjectName("label_scale_img")
        self.pushButton_reduce_img = QtWidgets.QPushButton(self.frame_viewer_navigations)
        self.pushButton_reduce_img.setGeometry(QtCore.QRect(760, 71, 21, 23))
        self.pushButton_reduce_img.setObjectName("pushButton_reduce_token")
        self.pushButton_increase_img = QtWidgets.QPushButton(self.frame_viewer_navigations)
        self.pushButton_increase_img.setGeometry(QtCore.QRect(760, 100, 21, 23))
        self.pushButton_increase_img.setObjectName("pushButton_increase_token")
        self.graphicsView_img = QtWidgets.QGraphicsView(self.frame_viewer_navigations)
        self.graphicsView_img.setGeometry(QtCore.QRect(525, 130, 261, 181))
        self.graphicsView_img.scale(0.25, 0.25)
        self.verticalLayout_3.addWidget(self.frame_viewer_navigations)
        self.frame_list = QtWidgets.QFrame(self.frame_viewer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_list.sizePolicy().hasHeightForWidth())
        self.frame_list.setSizePolicy(sizePolicy)
        self.frame_list.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_list.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_list.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_list.setObjectName("frame_list")
        self.pushButton_right = QtWidgets.QPushButton(self.frame_list)
        self.pushButton_right.setGeometry(QtCore.QRect(210, 10, 75, 23))
        self.pushButton_right.setObjectName("pushButton_right")
        self.pushButton_open_current = QtWidgets.QPushButton(self.frame_list)
        self.pushButton_open_current.setGeometry(QtCore.QRect(160, 40, 75, 23))
        self.pushButton_open_current.setObjectName("pushButton_open_current")
        self.pushButton_left = QtWidgets.QPushButton(self.frame_list)
        self.pushButton_left.setGeometry(QtCore.QRect(120, 10, 71, 23))
        self.pushButton_left.setObjectName("pushButton_left")
        self.pushButton_open_view = QtWidgets.QPushButton(self.frame_list)
        self.pushButton_open_view.setGeometry(QtCore.QRect(160, 70, 75, 23))
        self.pushButton_open_view.setObjectName("pushButton_open_view")
        self.pushButton_refresh_img = QtWidgets.QPushButton(self.frame_list)
        self.pushButton_refresh_img.setGeometry(QtCore.QRect(490, 0, 31, 23))
        self.pushButton_refresh_img.setText("")
        self.restore_icon = QtGui.QIcon()
        self.restore_icon.addPixmap(QtGui.QPixmap("img/icon/restore.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_refresh_img.setIcon(self.restore_icon)
        self.pushButton_refresh_img.setObjectName("pushButton_refresh_img")
        self.pushButton_add_hero_token = QtWidgets.QPushButton(self.frame_list)
        self.pushButton_add_hero_token.setGeometry(QtCore.QRect(560, 20, 101, 23))
        self.pushButton_add_hero_token.setObjectName("pushButton_add_hero_token")
        self.pushButton_add_enemy_token = QtWidgets.QPushButton(self.frame_list)
        self.pushButton_add_enemy_token.setGeometry(QtCore.QRect(560, 50, 101, 23))
        self.pushButton_add_enemy_token.setObjectName("pushButton_add_enemy_token")
        self.pushButton_add_initiative = QtWidgets.QPushButton(self.frame_list)
        self.pushButton_add_initiative.setGeometry(QtCore.QRect(680, 50, 101, 23))
        self.pushButton_add_initiative.setObjectName("pushButton_add_initiative")
        self.pushButton_add_unknown_token = QtWidgets.QPushButton(self.frame_list)
        self.pushButton_add_unknown_token.setGeometry(QtCore.QRect(680, 20, 101, 23))
        self.pushButton_add_unknown_token.setObjectName("pushButton_add_unknown_token")
        self.verticalLayout_3.addWidget(self.frame_list)
        self.tracker_hover_icon = QtGui.QIcon()
        self.tracker_hover_icon.addPixmap(QtGui.QPixmap("img/icon/hover_icon/tracker.ico"), QtGui.QIcon.Mode.Normal,
                                    QtGui.QIcon.State.Off)
        self.scenario_hover_icon = QtGui.QIcon()
        self.scenario_hover_icon.addPixmap(QtGui.QPixmap("img/icon/hover_icon/scenario.ico"), QtGui.QIcon.Mode.Normal,
                                          QtGui.QIcon.State.Off)
        self.notes_hover_icon = QtGui.QIcon()
        self.notes_hover_icon.addPixmap(QtGui.QPixmap("img/icon/hover_icon/notes.ico"), QtGui.QIcon.Mode.Normal,
                                          QtGui.QIcon.State.Off)
        self.music_hover_icon = QtGui.QIcon()
        self.music_hover_icon.addPixmap(QtGui.QPixmap("img/icon/hover_icon/music.ico"), QtGui.QIcon.Mode.Normal,
                                          QtGui.QIcon.State.Off)
        self.options_hover_icon = QtGui.QIcon()
        self.options_hover_icon.addPixmap(QtGui.QPixmap("img/icon/hover_icon/rules.ico"), QtGui.QIcon.Mode.Normal,
                                          QtGui.QIcon.State.Off)
        self.img_hover_icon = QtGui.QIcon()
        self.img_hover_icon.addPixmap(QtGui.QPixmap("img/icon/hover_icon/img.ico"), QtGui.QIcon.Mode.Normal,
                                          QtGui.QIcon.State.Off)
        self.dice_hover_icon = QtGui.QIcon()
        self.dice_hover_icon.addPixmap(QtGui.QPixmap("img/icon/hover_icon/dice.ico"), QtGui.QIcon.Mode.Normal,
                                          QtGui.QIcon.State.Off)
        self.menu_hover_icon = QtGui.QIcon()
        self.menu_hover_icon.addPixmap(QtGui.QPixmap("img/icon/hover_icon/menu.ico"), QtGui.QIcon.Mode.Normal,
                                       QtGui.QIcon.State.Off)
        self.frame_web = QtWidgets.QFrame(self.frame_main_app)
        self.frame_web.setGeometry(QtCore.QRect(0, 0, 795, 421))
        self.frame_web.setStyleSheet("QFrame {\n"
                                     "    background-color: rgb(85, 85, 85);\n"
                                     "    opacity: 0.3;\n"
                                     "    color: rgb(247, 147, 30);\n"
                                     "    border: none;\n"
                                     "}\n"
                                     "\n"
                                     "QLineEdit {\n"
                                     "    background-color: rgb(55, 55, 55);\n"
                                     "    color: rgb(247, 147, 30);\n"
                                     "    border: none;\n"
                                     "}\n"
                                     "\n"
                                     "QTextEdit {\n"
                                     "    background-color: rgb(55, 55, 55);\n"
                                     "    color: rgb(247, 147, 30);\n"
                                     "    border: none;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton {\n"
                                     "    background-color: rgb(55, 55, 55);\n"
                                     "    color: rgb(247, 147, 30);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: rgb(105, 105, 105);\n"
                                     "}\n"
                                     "\n"
                                     "QSpinBox {\n"
                                     "    background-color: rgb(55, 55, 55);\n"
                                     "    color: rgb(247, 147, 30);\n"
                                     "    border: none;\n"
                                     "}\n"
                                     "\n"
                                     "QComboBox {\n"
                                     "    background-color: rgb(55, 55, 55);\n"
                                     "    color: rgb(247, 147, 30);\n"
                                     "    border: none;\n"
                                     "}\n"
                                     "\n"
                                     "QRadioButton {\n"
                                     "    color: rgb(247, 147, 30);\n"
                                     "    border-radius:  10px;\n"
                                     "}\n"
                                     "\n"
                                     "QCheckBox {\n"
                                     "    color: rgb(247, 147, 30);\n"
                                     "    border: none;\n"
                                     "}")
        self.frame_web.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_web.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_web.setObjectName("frame_web")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_web)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_auth = QtWidgets.QFrame(self.frame_web)
        self.frame_auth.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_auth.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_auth.setObjectName("frame_auth")
        self.pushButton_auth = QtWidgets.QPushButton(self.frame_auth)
        self.pushButton_auth.setGeometry(QtCore.QRect(60, 390, 75, 23))
        self.pushButton_auth.setObjectName("pushButton_auth")
        self.lineEdit_password = QtWidgets.QLineEdit(self.frame_auth)
        self.lineEdit_password.setGeometry(QtCore.QRect(58, 350, 150, 20))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_login = QtWidgets.QLineEdit(self.frame_auth)
        self.lineEdit_login.setGeometry(QtCore.QRect(58, 300, 150, 20))
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.label_login = QtWidgets.QLabel(self.frame_auth)
        self.label_login.setGeometry(QtCore.QRect(60, 270, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        self.label_password = QtWidgets.QLabel(self.frame_auth)
        self.label_password.setGeometry(QtCore.QRect(60, 320, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.lineEdit_name = QtWidgets.QLineEdit(self.frame_auth)
        self.lineEdit_name.setGeometry(QtCore.QRect(58, 350, 150, 20))
        self.lineEdit_name.setText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.pushButton_save = QtWidgets.QPushButton(self.frame_auth)
        self.pushButton_save.setGeometry(QtCore.QRect(60, 390, 75, 23))
        self.pushButton_save.setObjectName("pushButton_save")
        self.label_name = QtWidgets.QLabel(self.frame_auth)
        self.label_name.setGeometry(QtCore.QRect(60, 320, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout_10.addWidget(self.frame_auth)
        self.frame_web_list = QtWidgets.QFrame(self.frame_web)
        self.frame_web_list.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_web_list.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_web_list.setObjectName("frame_web_list")
        self.listWidget_web_list = QtWidgets.QListWidget(self.frame_web_list)
        self.listWidget_web_list.setGeometry(QtCore.QRect(0, 0, 261, 381))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_web_list.sizePolicy().hasHeightForWidth())
        self.listWidget_web_list.setSizePolicy(sizePolicy)
        self.listWidget_web_list.setObjectName("listWidget_web_list")
        self.pushButton_load = QtWidgets.QPushButton(self.frame_web_list)
        self.pushButton_load.setGeometry(QtCore.QRect(90, 390, 75, 23))
        self.pushButton_load.setObjectName("pushButton_load")
        self.horizontalLayout_10.addWidget(self.frame_web_list)
        self.frame_3 = QtWidgets.QFrame(self.frame_web)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_10.addWidget(self.frame_3)
        self.frame_tracker = QtWidgets.QFrame(self.frame_main_app)
        self.frame_tracker.setGeometry(QtCore.QRect(0, 0, 795, 421))
        self.frame_tracker.setStyleSheet("QFrame {\n"
                                           "    background-color: rgb(85, 85, 85);\n"
                                           "    opacity: 0.3;\n"
                                           "    color: rgb(247, 147, 30);\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "\n"
                                           "QLineEdit {\n"
                                           "    background-color: rgb(55, 55, 55);\n"
                                           "    color: rgb(247, 147, 30);\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "\n"
                                           "QTextEdit {\n"
                                           "    background-color: rgb(55, 55, 55);\n"
                                           "    color: rgb(247, 147, 30);\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton {\n"
                                           "    background-color: rgb(55, 55, 55);\n"
                                           "    color: rgb(247, 147, 30);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(105, 105, 105);\n"
                                           "}\n"
                                           "\n"
                                           "QSpinBox {\n"
                                           "    background-color: rgb(55, 55, 55);\n"
                                           "    color: rgb(247, 147, 30);\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox {\n"
                                           "    background-color: rgb(55, 55, 55);\n"
                                           "    color: rgb(247, 147, 30);\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "\n"
                                           "QRadioButton {\n"
                                           "    color: rgb(247, 147, 30);\n"
                                           "    border-radius:  10px;\n"
                                           "}\n"
                                           "\n"
                                           "QCheckBox {\n"
                                           "    color: rgb(247, 147, 30);\n"
                                           "    border: none;\n"
                                           "}")
        self.frame_tracker.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tracker.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tracker.setObjectName("frame_tracker")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_tracker)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_options = QtWidgets.QFrame(self.frame_tracker)
        self.frame_options.setMinimumSize(QtCore.QSize(159, 421))
        self.frame_options.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_options.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_options.setObjectName("frame_options")
        self.radioButton_hide_create = QtWidgets.QRadioButton(self.frame_options)
        self.radioButton_hide_create.setGeometry(QtCore.QRect(30, 390, 115, 20))
        self.radioButton_hide_create.setChecked(False)
        self.radioButton_hide_create.setAutoRepeat(False)
        self.radioButton_hide_create.setObjectName("radioButton_hide_create")
        self.frame_create = QtWidgets.QFrame(self.frame_options)
        self.frame_create.setGeometry(QtCore.QRect(0, 0, 159, 391))
        self.frame_create.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_create.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_create.setObjectName("frame_create")
        self.name = QtWidgets.QLabel(self.frame_create)
        self.name.setGeometry(QtCore.QRect(10, 135, 120, 25))
        self.name.setStyleSheet("font-weight:bold")
        self.name.setObjectName("name")
        self.hp = QtWidgets.QLabel(self.frame_create)
        self.hp.setGeometry(QtCore.QRect(10, 245, 31, 25))
        self.hp.setStyleSheet("font-weight:bold")
        self.hp.setObjectName("hp")
        self.initiative_edit = QtWidgets.QLineEdit(self.frame_create)
        self.initiative_edit.setGeometry(QtCore.QRect(10, 320, 120, 25))
        self.initiative_edit.setObjectName("initiative_edit")
        self.pushButton = QtWidgets.QPushButton(self.frame_create)
        self.pushButton.setGeometry(QtCore.QRect(10, 350, 120, 25))
        self.pushButton.setObjectName("pushButton")
        self.hp_edit = QtWidgets.QLineEdit(self.frame_create)
        self.hp_edit.setGeometry(QtCore.QRect(10, 270, 41, 25))
        self.hp_edit.setObjectName("hp_edit")
        self.name_edit = QtWidgets.QLineEdit(self.frame_create)
        self.name_edit.setGeometry(QtCore.QRect(10, 160, 120, 25))
        self.name_edit.setObjectName("name_edit")
        self.initiative = QtWidgets.QLabel(self.frame_create)
        self.initiative.setGeometry(QtCore.QRect(10, 295, 120, 25))
        self.initiative.setStyleSheet("font-weight:bold")
        self.initiative.setObjectName("initiative")
        self.ac_edit = QtWidgets.QLineEdit(self.frame_create)
        self.ac_edit.setGeometry(QtCore.QRect(70, 270, 41, 25))
        self.ac_edit.setObjectName("ac_edit")
        self.ac = QtWidgets.QLabel(self.frame_create)
        self.ac.setGeometry(QtCore.QRect(70, 245, 31, 25))
        self.ac.setStyleSheet("font-weight:bold")
        self.ac.setObjectName("ac")
        self.comboBox_hero_class = QtWidgets.QComboBox(self.frame_create)
        self.comboBox_hero_class.setGeometry(QtCore.QRect(10, 220, 121, 22))
        self.comboBox_hero_class.setObjectName("comboBox")
        self.hero_class = QtWidgets.QLabel(self.frame_create)
        self.hero_class.setGeometry(QtCore.QRect(10, 190, 120, 25))
        self.hero_class.setStyleSheet("font-weight:bold")
        self.hero_class.setObjectName("hero_class")
        self.frame_tools = QtWidgets.QFrame(self.frame_options)
        self.frame_tools.setGeometry(QtCore.QRect(0, 0, 159, 391))
        self.frame_tools.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tools.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tools.setObjectName("frame")
        self.label_roll_dice = QtWidgets.QLabel(self.frame_tools)
        self.label_roll_dice.setGeometry(QtCore.QRect(20, 60, 120, 20))
        self.label_roll_dice.setStyleSheet("font-weight:bold")
        self.label_roll_dice.setText("")
        self.label_roll_dice.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_roll_dice.setObjectName("label_roll_dice")
        self.modifier_box = QtWidgets.QSpinBox(self.frame_tools)
        self.modifier_box.setGeometry(QtCore.QRect(50, 150, 41, 22))
        self.modifier_box.setMinimum(-50)
        self.modifier_box.setObjectName("modifier_box")
        self.label_modifier = QtWidgets.QLabel(self.frame_tools)
        self.label_modifier.setGeometry(QtCore.QRect(10, 150, 31, 16))
        self.label_modifier.setObjectName("label_modifier")
        self.check_advantage = QtWidgets.QCheckBox(self.frame_tools)
        self.check_advantage.setGeometry(QtCore.QRect(10, 170, 81, 20))
        self.check_advantage.setObjectName("check_advantage")
        self.dice_edit = QtWidgets.QLineEdit(self.frame_tools)
        self.dice_edit.setGeometry(QtCore.QRect(50, 130, 41, 22))
        self.dice_edit.setObjectName("dice_edit")
        self.label_amount = QtWidgets.QLabel(self.frame_tools)
        self.label_amount.setGeometry(QtCore.QRect(10, 110, 41, 16))
        self.label_amount.setObjectName("label_amount")
        self.amount_dice_box = QtWidgets.QSpinBox(self.frame_tools)
        self.amount_dice_box.setGeometry(QtCore.QRect(50, 110, 41, 22))
        self.amount_dice_box.setMinimum(1)
        self.amount_dice_box.setObjectName("amount_dice_box")
        self.pushButton_del_char = QtWidgets.QPushButton(self.frame_tools)
        self.pushButton_del_char.setGeometry(QtCore.QRect(90, 220, 51, 22))
        self.pushButton_del_char.setObjectName("pushButton_del_char")
        self.comboBox_del_char = QtWidgets.QComboBox(self.frame_tools)
        self.comboBox_del_char.setGeometry(QtCore.QRect(10, 220, 73, 22))
        self.comboBox_del_char.setObjectName("comboBox_del_char")
        self.label_dice = QtWidgets.QLabel(self.frame_tools)
        self.label_dice.setGeometry(QtCore.QRect(10, 130, 31, 16))
        self.label_dice.setObjectName("label_dice")
        self.pushButton_init_open = QtWidgets.QPushButton(self.frame_tools)
        self.pushButton_init_open.setGeometry(QtCore.QRect(10, 30, 93, 28))
        self.pushButton_init_open.setObjectName("pushButton_init_open")
        self.pushButton_roll_dice = QtWidgets.QPushButton(self.frame_tools)
        self.pushButton_roll_dice.setGeometry(QtCore.QRect(10, 80, 120, 25))
        self.pushButton_roll_dice.setObjectName("pushButton_roll_dice")
        self.label_del_char = QtWidgets.QLabel(self.frame_tools)
        self.label_del_char.setGeometry(QtCore.QRect(10, 200, 101, 16))
        self.label_del_char.setObjectName("label_del_char")
        self.horizontalLayout_6.addWidget(self.frame_options)
        self.frame_characters = QtWidgets.QFrame(self.frame_tracker)
        self.frame_characters.setMinimumSize(QtCore.QSize(636, 421))
        self.frame_characters.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_characters.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_characters.setObjectName("frame_characters")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_characters)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.gridLayout_characters = QtWidgets.QGridLayout()
        self.gridLayout_characters.setObjectName("gridLayout_characters")
        self.horizontalLayout_13.addLayout(self.gridLayout_characters)
        self.horizontalLayout_6.addWidget(self.frame_characters)
        self.info.raise_()
        self.frame_scenario.raise_()
        self.frame_notes.raise_()
        self.frame_music_changer.raise_()
        self.frame_rules.raise_()
        self.frame_npc_generator.raise_()
        self.frame_web.raise_()
        self.frame_generate_store.raise_()
        self.frame_tracker.raise_()
        self.frame_main_app.raise_()
        self.frame_menu.raise_()
        self.verticalLayout.addWidget(self.main)
        self.footer = QtWidgets.QFrame(self.background)
        self.footer.setMinimumSize(QtCore.QSize(0, 26))
        self.footer.setMaximumSize(QtCore.QSize(16777215, 26))
        self.footer.setStyleSheet("background-color: rgb(35,35,35);")
        self.footer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.footer.setObjectName("footer")
        self.verticalLayout.addWidget(self.footer)
        self.horizontalLayout.addWidget(self.background)
        MainWindow.setCentralWidget(self.centralwidget)

        self.frame_tracker.hide()


        self.toolButton_dict = {"    TRACKER": self.toolButton_tracker,
                                "    SCENARIO": self.toolButton_scenario,
                                "    NOTES": self.toolButton_notes,
                                "    RULES": self.toolButton_rules,
                                "    MUSIC CHANGER": self.toolButton_music_changer,
                                "    IMAGE VIEW": self.toolButton_img_view,
                                "    GENERATE STORE": self.toolButton_generate_store,
                                "    NPC GENERATOR": self.toolButton_npc_generator}

        self.toolButton_icon = {"    TRACKER": self.tracker_icon,
                                "    SCENARIO": self.scenario_icon,
                                "    NOTES": self.notes_icon,
                                "    RULES": self.options_icon,
                                "    GENERATE STORE": self.dice_icon,
                                "    NPC GENERATOR": self.dice_icon,
                                "    MUSIC CHANGER": self.music_icon,
                                "    IMAGE VIEW": self.img_icon}

        self.toolButton_hover_icon = {"    TRACKER": self.tracker_hover_icon,
                                      "    SCENARIO": self.scenario_hover_icon,
                                      "    NOTES": self.notes_hover_icon,
                                      "    RULES": self.options_hover_icon,
                                      "    GENERATE STORE": self.dice_hover_icon,
                                      "    NPC GENERATOR": self.dice_hover_icon,
                                      "    MUSIC CHANGER": self.music_hover_icon,
                                      "    IMAGE VIEW": self.img_hover_icon}

        self.menu_frame = {"    TRACKER": self.frame_tracker,
                           "    SCENARIO": self.frame_scenario,
                           "    NOTES": self.frame_notes,
                           "    MUSIC CHANGER": self.frame_music_changer,
                           "    RULES": self.frame_rules,
                           "    GENERATE STORE": self.frame_generate_store,
                           "    NPC GENERATOR": self.frame_npc_generator,
                           "    IMAGE VIEW": self.frame_viewer}

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_name_app.setText(_translate("MainWindow", "DnD Master support"))
        self.label_username.setText(_translate("MainWindow", "Not authorized"))
        self.toolButton_menu.setText(_translate("MainWindow", "    MENU"))
        self.toolButton_tracker.setText(_translate("MainWindow", "    TRACKER"))
        self.toolButton_scenario.setText(_translate("MainWindow", "    SCENARIO"))
        self.toolButton_notes.setText(_translate("MainWindow", "    NOTES"))
        self.toolButton_rules.setText(_translate("MainWindow", "    RULES"))
        self.toolButton_generate_store.setText(_translate("MainWindow", "    GENERATE STORE"))
        self.toolButton_npc_generator.setText(_translate("MainWindow", "    NPC GENERATOR"))
        self.toolButton_music_changer.setText(_translate("MainWindow", "    MUSIC CHANGER"))
        self.toolButton_img_view.setText(_translate("MainWindow", "    IMAGE VIEW"))
        self.label_dice.setText(_translate("MainWindow", "Dice"))
        self.pushButton_roll_dice.setText(_translate("MainWindow", "Roll dice"))
        self.ac.setText(_translate("MainWindow", "Ac"))
        self.hero_class.setText(_translate("MainWindow", "Class"))
        self.label_del_char.setText(_translate("MainWindow", "Delete character"))
        self.name.setText(_translate("MainWindow", "Name"))
        self.initiative.setText(_translate("MainWindow", "Initiative"))
        self.label_amount.setText(_translate("MainWindow", "Amout"))
        self.hp.setText(_translate("MainWindow", "Hp"))
        self.check_advantage.setText(_translate("MainWindow", "advantage"))
        self.pushButton_del_char.setText(_translate("MainWindow", "Delete"))
        self.pushButton.setText(_translate("MainWindow", "Create"))
        self.pushButton_init_open.setText(_translate("MainWindow", "Initiative"))
        self.label_modifier.setText(_translate("MainWindow", "Mod"))
        self.radioButton_hide_create.setText(_translate("MainWindow", "Creation off"))
        self.dice_edit.setText(_translate("MainWindow", "20"))
        self.radioButton_tags_notes.setText(_translate("MainWindow", "tags notes"))
        self.pushButton_del_chapter.setText(_translate("MainWindow", "del"))
        self.pushButton_add_tags.setText(_translate("MainWindow", "Add"))
        self.pushButton_add_chapter.setText(_translate("MainWindow", "add"))
        self.pushButton_del_tags.setText(_translate("MainWindow", "delete"))
        self.label_category.setText(_translate("MainWindow", "Category name"))
        self.pushButton_url_open.setText(_translate("MainWindow", "open"))
        self.label_scene.setText(_translate("MainWindow", "Scene name"))
        self.label_scene_url_2.setText(_translate("MainWindow", "Choose scene"))
        self.pushButton_url_delete.setText(_translate("MainWindow", "delete"))
        self.label_scene_url.setText(_translate("MainWindow", "URL music"))
        self.label_category_open.setText(_translate("MainWindow", "Category name"))
        self.pushButton_url_set.setText(_translate("MainWindow", "set"))
        self.pushButton_music_play.setText(_translate("MainWindow", "play"))
        self.pushButton_music_pause.setText(_translate("MainWindow", "pause"))
        self.pushButton_music_stop.setText(_translate("MainWindow", "stop"))
        self.label_rules.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_race_vendor.setText(_translate("MainWindow", "Race"))
        self.label_vendor.setText(_translate("MainWindow", "Vendor"))
        self.label_name_vendor.setText(_translate("MainWindow", "Name"))
        self.label_age_vendor.setText(_translate("MainWindow", "Age"))
        self.label_store_name_2.setText(_translate("MainWindow", "Name store"))
        self.radioButton_options_store.setText(_translate("MainWindow", "options"))
        self.pushButton_del_store.setText(_translate("MainWindow", "del"))
        self.label_sex_vendor.setText(_translate("MainWindow", "Sex"))
        self.label_personality_vendor.setText(_translate("MainWindow", "Personality"))
        self.label_look_vendor.setText(_translate("MainWindow", "Look"))
        self.label_voice_vendor.setText(_translate("MainWindow", "Voice"))
        self.label_sex_vendor.setText(_translate("MainWindow", "Sex"))
        self.label_shop_info.setText(_translate("MainWindow", "Shop_info"))
        self.label_cost_generate.setText(_translate("MainWindow", "Cost"))
        self.pushButton_generate_shop.setText(_translate("MainWindow", "Generate"))
        self.label_type_generate.setText(_translate("MainWindow", "Type"))
        self.label_2.setText(_translate("MainWindow", "Search by assortment"))
        self.label_race_npc.setText(_translate("MainWindow", "Race"))
        self.pushButton_del_npc.setText(_translate("MainWindow", "Delete"))
        self.label_sex_npc.setText(_translate("MainWindow", "Sex"))
        self.pushButton_generate_npc.setText(_translate("MainWindow", "Generate"))
        self.label_age_npc.setText(_translate("MainWindow", "Age"))
        self.label_name_npc.setText(_translate("MainWindow", "Name"))
        self.label_personality_npc.setText(_translate("MainWindow", "Personality"))
        self.label_look_npc.setText(_translate("MainWindow", "Look"))
        self.label_voice_npc.setText(_translate("MainWindow", "Voice"))
        self.label_generate_npc.setText(_translate("MainWindow", "Text NPC"))

        self.info.setHtml(_translate("MainWindow",
                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">More info --&gt; https://github.com/cursed-amari/DMS</span></p>\n"
                                     "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Запрещено любое коммерческое использование!</span></p>\n"
                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Распространяется исключительно на бесплатной основе!</span></p>\n"
                                     "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Any commercial use is prohibited!</span></p>\n"
                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Distributed exclusively on a free basis!</span></p></body></html>"))
        self.label_enemy_token.setText(_translate("MainWindow", "Enemy token"))
        self.label_hero_token.setText(_translate("MainWindow", "Hero token"))
        self.pushButton_reduce_token.setText(_translate("MainWindow", "Reduce token"))
        self.pushButton_increase_token.setText(_translate("MainWindow", "Increase token"))
        self.pushButton_reduce_img.setText(_translate("MainWindow", "-"))
        self.pushButton_increase_img.setText(_translate("MainWindow", "+"))
        self.label_scale_img.setText(_translate("MainWindow", "0"))
        self.pushButton_open_view.setText(_translate("MainWindow", "Open view"))
        self.pushButton_open_current.setText(_translate("MainWindow", "Open"))
        self.pushButton_right.setText(_translate("MainWindow", "right"))
        self.pushButton_left.setText(_translate("MainWindow", "left"))
        self.pushButton_auth.setText(_translate("MainWindow", "Login"))
        self.label_login.setText(_translate("MainWindow", "Login"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.pushButton_load.setText(_translate("MainWindow", "load"))
        self.pushButton_add_hero_token.setText(_translate("MainWindow", "Add hero token"))
        self.pushButton_add_enemy_token.setText(_translate("MainWindow", "Add enemy token"))
        self.pushButton_add_initiative.setText(_translate("MainWindow", "Add initiative"))
        self.pushButton_add_unknown_token.setText(_translate("MainWindow", "Add unknown token"))

        self.frame_name_app.mousePressEvent = self.press_window
        self.label_name_app.mousePressEvent = self.press_window
        self.frame_name_app.mouseMoveEvent = self.move_window
        self.label_name_app.mouseMoveEvent = self.move_window

        self.add_style()
        self.hide_aplications()
        self.app_func()

    @logger.catch
    def add_style(self):
        self.frame_main_app.setStyleSheet(
            "QFrame#frame_main_app {background-image: url(img/fon_mini.png) no-repeat;}")


        self.frame_tracker.setStyleSheet("QFrame {\n"
                                         "    background-image: url(img/fon_tracker_open.png);\n"
                                         "    color: rgb(247, 147, 30);\n"
                                         "    border: none;\n"
                                         "}\n"
                                         "QLabel {\n"
                                         "    background: none;\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit {\n"
                                         "    background-color: rgb(55, 55, 55);\n"
                                         "    color: rgb(247, 147, 30);\n"
                                         "    border: none;\n"
                                         "}\n"
                                         "\n"
                                         "QTextEdit {\n"
                                         "    background-color: rgb(55, 55, 55);\n"
                                         "    color: rgb(247, 147, 30);\n"
                                         "    border: none;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton {\n"
                                         "    background-color: rgb(55, 55, 55);\n"
                                         "    color: rgb(247, 147, 30);\n"
                                         "    border-radius: 5px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(75, 75, 75);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: rgb(105, 105, 105);\n"
                                         "}\n"
                                         "\n"
                                         "QSpinBox {\n"
                                         "    background-color: rgb(55, 55, 55);\n"
                                         "    color: rgb(247, 147, 30);\n"
                                         "    border: none;\n"
                                         "}\n"
                                         "\n"
                                         "QComboBox {\n"
                                         "    background-color: rgb(55, 55, 55);\n"
                                         "    color: rgb(247, 147, 30);\n"
                                         "    border: none;\n"
                                         "}\n"
                                         "\n"
                                         "QRadioButton {\n"
                                         "    color: rgb(247, 147, 30);\n"
                                         "    border-radius:  10px;\n"
                                         "}\n"
                                         "\n"
                                         "QCheckBox {\n"
                                         "    color: rgb(247, 147, 30);\n"
                                         "    border: none;\n"
                                         "}")
        self.frame_scenario.setStyleSheet("QFrame {\n"
                                          "    background-image: url(img/fon_tracker_open.png);\n"
                                          "    opacity: 0.3;\n"
                                          "    color: rgb(247, 147, 30);\n"
                                          "    border: none;\n"
                                          "}\n"
                                          "\n"
                                          "QLineEdit {\n"
                                          "    background-color: rgb(55, 55, 55);\n"
                                          "    color: rgb(247, 147, 30);\n"
                                          "    border: none;\n"
                                          "}\n"
                                          "\n"
                                          "QTextEdit {\n"
                                          "    background-color: rgb(55, 55, 55);\n"
                                          "    color: rgb(247, 147, 30);\n"
                                          "    border: none;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton {\n"
                                          "    background-color: rgb(55, 55, 55);\n"
                                          "    color: rgb(247, 147, 30);\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb(75, 75, 75);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color: rgb(105, 105, 105);\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox {\n"
                                          "    background-color: rgb(55, 55, 55);\n"
                                          "    color: rgb(247, 147, 30);\n"
                                          "    border: none;\n"
                                          "}\n"
                                          "\n"
                                          "QRadioButton {\n"
                                          "    color: rgb(247, 147, 30);\n"
                                          "    border-radius:  10px;\n"
                                          "}\n"
                                          "\n"
                                          "QListWidget {\n"
                                          "    background-color: rgb(55, 55, 55);\n"
                                          "    color: rgb(247, 147, 30);\n"
                                          "    border: none;\n"
                                          "}")
        self.frame_notes.setStyleSheet("QFrame {\n"
                                       "    background-image: url(img/fon_tracker_open.png);\n"
                                       "    opacity: 0.3;\n"
                                       "    color: rgb(247, 147, 30);\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "\n"
                                       "QTextEdit {\n"
                                       "    background-color: rgb(55, 55, 55);\n"
                                       "    color: rgb(247, 147, 30);\n"
                                       "    border: none;\n"
                                       "}\n")
        self.frame_music_changer.setStyleSheet("QFrame {\n"
                                               "    background-image: url(img/fon_tracker_open.png);\n"
                                               "    opacity: 0.3;\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "\n"
                                               "QLabel {\n"
                                               "    background: none;\n"
                                               "}\n"
                                               "\n"
                                               "QLineEdit {\n"
                                               "    background-color: rgb(55, 55, 55);\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "\n"
                                               "QListWidget {\n"
                                               "    background-color: rgb(55, 55, 55);\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton {\n"
                                               "    background-color: rgb(55, 55, 55);\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border-radius: 5px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "    background-color: rgb(75, 75, 75);\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:pressed {\n"
                                               "    background-color: rgb(105, 105, 105);\n"
                                               "}\n"
                                               "\n"
                                               "QComboBox {\n"
                                               "    background-color: rgb(55, 55, 55);\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border: none;\n"
                                               "}")
        self.frame_rules.setStyleSheet("QFrame {\n"
                                       "    background-image: url(img/fon_tracker_open.png);\n"
                                       "    opacity: 0.3;\n"
                                       "    color: rgb(247, 147, 30);\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "\n"
                                       "QTextEdit {\n"
                                       "    background-color: rgb(55, 55, 55);\n"
                                       "    color: rgb(247, 147, 30);\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "\n"
                                       "QComboBox {\n"
                                       "    background-color: rgb(55, 55, 55);\n"
                                       "    color: rgb(247, 147, 30);\n"
                                       "    border: none;\n"
                                       "}")
        self.frame_viewer.setStyleSheet("QFrame {\n"
                                        "    background-image: url(img/fon_tracker_open.png);\n"
                                        "    opacity: 0.3;\n"
                                        "    color: rgb(247, 147, 30);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "\n"
                                        "QLineEdit {\n"
                                        "    background-color: rgb(55, 55, 55);\n"
                                        "    color: rgb(247, 147, 30);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "\n"
                                        "QTextEdit {\n"
                                        "    background-color: rgb(55, 55, 55);\n"
                                        "    color: rgb(247, 147, 30);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "\n"
                                        "QListWidget {\n"
                                        "    background-color: rgb(55, 55, 55);\n"
                                        "    color: rgb(247, 147, 30);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton {\n"
                                        "    background-color: rgb(55, 55, 55);\n"
                                        "    color: rgb(247, 147, 30);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(75, 75, 75);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: rgb(105, 105, 105);\n"
                                        "}\n"
                                        "\n"
                                        "QSpinBox {\n"
                                        "    background-color: rgb(55, 55, 55);\n"
                                        "    color: rgb(247, 147, 30);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "\n"
                                        "QComboBox {\n"
                                        "    background-color: rgb(55, 55, 55);\n"
                                        "    color: rgb(247, 147, 30);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "\n"
                                        "QRadioButton {\n"
                                        "    color: rgb(247, 147, 30);\n"
                                        "    border-radius:  10px;\n"
                                        "}\n"
                                        "\n"
                                        "QCheckBox {\n"
                                        "    color: rgb(247, 147, 30);\n"
                                        "    border: none;\n"
                                        "}")
        self.frame_generate_store.setStyleSheet("QFrame {\n"
                                                "    background-image: url(img/fon_tracker_open.png);\n"
                                                "    opacity: 0.3;\n"
                                                "    color: rgb(247, 147, 30);\n"
                                                "    border: none;\n"
                                                "}\n"
                                                "\n"
                                                "QLabel#label_shop_info {\n"
                                                "    background-color: rgb(55, 55, 55);\n"
                                                "}\n"
                                                "\n"
                                                "QLineEdit {\n"
                                                "    background-color: rgb(55, 55, 55);\n"
                                                "    color: rgb(247, 147, 30);\n"
                                                "    border: none;\n"
                                                "}\n"
                                                "\n"
                                                "QTextEdit {\n"
                                                "    background-color: rgb(55, 55, 55);\n"
                                                "    color: rgb(247, 147, 30);\n"
                                                "    border: none;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton {\n"
                                                "    background-color: rgb(55, 55, 55);\n"
                                                "    color: rgb(247, 147, 30);\n"
                                                "    border-radius: 5px;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: rgb(75, 75, 75);\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "    background-color: rgb(105, 105, 105);\n"
                                                "}\n"
                                                "\n"
                                                "QComboBox {\n"
                                                "    background-color: rgb(55, 55, 55);\n"
                                                "    color: rgb(247, 147, 30);\n"
                                                "    border: none;\n"
                                                "}\n"
                                                "\n"
                                                "QRadioButton {\n"
                                                "    color: rgb(247, 147, 30);\n"
                                                "    border-radius:  10px;\n"
                                                "}")
        self.frame_npc_generator.setStyleSheet("QFrame {\n"
                                               "    background-image: url(img/fon_tracker_open.png);\n"
                                               "    opacity: 0.3;\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "\n"
                                               "QLabel#label_generate_npc {\n"
                                               "    background-color: rgb(55, 55, 55);\n"
                                               "}\n"
                                               "\n"
                                               "QLineEdit {\n"
                                               "    background-color: rgb(55, 55, 55);\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "\n"
                                               "QTextEdit {\n"
                                               "    background-color: rgb(55, 55, 55);\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton {\n"
                                               "    background-color: rgb(55, 55, 55);\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border-radius: 5px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                                "    background-color: rgb(75, 75, 75);\n"
                                                "}\n"
                                                "\n"
                                               "QPushButton:pressed {\n"
                                               "    background-color: rgb(105, 105, 105);\n"
                                               "}\n"
                                               "\n"
                                               "QComboBox {\n"
                                               "    background-color: rgb(55, 55, 55);\n"
                                               "    color: rgb(247, 147, 30);\n"
                                               "    border: none;\n"
                                               "}")
        self.setStyleSheet("QInputDialog {\n"
                           "    background-color: rgb(85, 85, 85);\n"
                           "    opacity: 0.3;\n"
                           "    color: rgb(247, 147, 30);\n"
                           "    border: none;\n"
                           "}\n"
                           "\n"
                           "QLineEdit {\n"
                           "    background-color: rgb(55, 55, 55);\n"
                           "    color: rgb(247, 147, 30);\n"
                           "    border: none;\n"
                           "}\n"
                           "\n"
                           "QPushButton {\n"
                           "    background: rgb(55, 55, 55);\n"
                           "    border-radius: 5px;\n"
                           "    color: rgb(247, 147, 30);\n"
                           "}\n"
                           "\n"
                           "QPushButton:hover {\n"
                                                "    background-color: rgb(75, 75, 75);\n"
                                                "}\n"
                                                "\n"
                           "QPushButton:pressed {\n"
                           "    background-color: rgb(105, 105, 105);\n"
                           "}\n"
                           "\n"
                           "QSpinBox {\n"
                           "    background-color: rgb(55, 55, 55);\n"
                           "    color: rgb(247, 147, 30);\n"
                           "    border: none;\n"
                           "}\n"
                           "QLabel{\n"
                           "    background-color: rgb(55, 55, 55);\n"
                           "    color: rgb(247, 147, 30);\n"
                           "}\n")

    @logger.catch
    def app_func(self):
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

    @logger.catch
    def hide_aplications(self):
        self.frame_tracker.hide()
        self.frame_scenario.hide()
        self.frame_notes.hide()
        self.frame_music_changer.hide()
        self.frame_rules.hide()
        self.frame_generate_store.hide()
        self.frame_npc_generator.hide()
        self.frame_viewer.hide()
        self.frame_web.hide()
        self.label_name.hide()
        self.lineEdit_name.hide()
        self.pushButton_save.hide()

        self.frame_tools.hide()
        self.label_store_name_2.hide()
        self.edit_store_name_2.hide()
        self.label_vendor.hide()
        self.label_name_vendor.hide()
        self.edit_name_vendor.hide()
        self.label_sex_vendor.hide()
        self.box_sex_vendor.hide()
        self.label_age_vendor.hide()
        self.box_age_vendor.hide()
        self.label_race_vendor.hide()
        self.box_race_vendor.hide()
        self.label_personality_vendor.hide()
        self.box_personality_vendor.hide()
        self.label_look_vendor.hide()
        self.box_look_vendor.hide()
        self.label_voice_vendor.hide()
        self.box_voice_vendor.hide()
        self.pushButton_add_tags.hide()
        self.pushButton_del_tags.hide()
        self.list_tags.hide()
        self.text_scenario.hide()

        self.info.hide()

        self.name.show()
        self.name_edit.show()
        self.hp.show()
        self.hp_edit.show()
        self.initiative.show()
        self.initiative_edit.show()
        self.pushButton.show()
    @logger.catch
    def press_window(self, event):
        self.dragPos = event.globalPosition().toPoint()

    @logger.catch
    def move_window(self, event):
        try:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
        except AttributeError:
            pass
