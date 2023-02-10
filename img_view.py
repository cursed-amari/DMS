# Form implementation generated from reading ui file 'img_view.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Window_viewer(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtGui.QGuiApplication.primaryScreen().availableGeometry().width(),
                          QtGui.QGuiApplication.primaryScreen().availableGeometry().height())
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMinimumSize(QtCore.QSize(0, 25))
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
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.app_name = QtWidgets.QFrame(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_name.sizePolicy().hasHeightForWidth())
        self.app_name.setSizePolicy(sizePolicy)
        self.app_name.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.app_name.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.app_name.setObjectName("app_name")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.app_name)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_name_app_2 = QtWidgets.QLabel(self.app_name)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name_app_2.sizePolicy().hasHeightForWidth())
        self.label_name_app_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_name_app_2.setFont(font)
        self.label_name_app_2.setText("")
        self.label_name_app_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_name_app_2.setWordWrap(False)
        self.label_name_app_2.setObjectName("label_name_app_2")
        self.horizontalLayout_8.addWidget(self.label_name_app_2)
        self.navigation = QtWidgets.QFrame(self.app_name)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navigation.sizePolicy().hasHeightForWidth())
        self.navigation.setSizePolicy(sizePolicy)
        self.navigation.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.navigation.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.navigation.setObjectName("navigation")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.navigation)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_minimize = QtWidgets.QPushButton(self.navigation)
        self.pushButton_minimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon/minus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_minimize.setIcon(icon)
        self.pushButton_minimize.setObjectName("pushButton_minimize")
        self.horizontalLayout_7.addWidget(self.pushButton_minimize)
        self.pushButton_full_creen = QtWidgets.QPushButton(self.navigation)
        self.pushButton_full_creen.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/icon/minimized.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_full_creen.setIcon(icon1)
        self.pushButton_full_creen.setObjectName("pushButton_full_creen")
        self.horizontalLayout_7.addWidget(self.pushButton_full_creen)
        self.pushButton_exit_2 = QtWidgets.QPushButton(self.navigation)
        self.pushButton_exit_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/icon/x.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_exit_2.setIcon(icon2)
        self.pushButton_exit_2.setObjectName("pushButton_exit_2")
        self.horizontalLayout_7.addWidget(self.pushButton_exit_2)
        self.horizontalLayout_8.addWidget(self.navigation)
        self.horizontalLayout_6.addWidget(self.app_name)
        self.verticalLayout.addWidget(self.header)
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img = QtWidgets.QFrame(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img.sizePolicy().hasHeightForWidth())
        self.img.setSizePolicy(sizePolicy)
        self.img.setStyleSheet("QGraphicsView {\n"
                               "    background-color: rgb(55, 55, 55);\n"
                               "    color: rgb(247, 147, 30);\n"
                               "    border: none;\n"
                               "}")
        self.img.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.img.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.img.setObjectName("img")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.img)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphicsView_img = QtWidgets.QGraphicsView(self.img)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_img.sizePolicy().hasHeightForWidth())
        self.graphicsView_img.setSizePolicy(sizePolicy)
        self.graphicsView_img.setMinimumSize(QtCore.QSize(950, 510))
        self.graphicsView_img.setMaximumSize(
            QtCore.QSize(QtGui.QGuiApplication.primaryScreen().availableGeometry().width(),
                          QtGui.QGuiApplication.primaryScreen().availableGeometry().height()))
        self.graphicsView_img.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.graphicsView_img.setObjectName("graphicsView_img")
        self.horizontalLayout_2.addWidget(self.graphicsView_img)
        self.verticalLayout_2.addWidget(self.img)
        self.verticalLayout.addWidget(self.main)
        self.horizontalLayout.addWidget(self.background)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.app_name.mousePressEvent = self.press_window
        self.label_name_app_2.mousePressEvent = self.press_window
        self.app_name.mouseMoveEvent = self.move_window
        self.label_name_app_2.mouseMoveEvent = self.move_window

    def press_window(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def move_window(self, event):
        try:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
        except AttributeError:
            pass

class Window_viewer_show(QtWidgets.QMainWindow, Window_viewer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_minimize.clicked.connect(self.showMinimized)
        self.pushButton_full_creen.clicked.connect(self.showFullScreen)
        self.pushButton_exit_2.clicked.connect(self.close)
