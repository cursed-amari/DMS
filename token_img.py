import os

from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QGraphicsTextItem, \
    QGraphicsObject, QMenu, QFileDialog, QGraphicsRectItem, QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt, QPointF, QRect, pyqtSignal, QPoint
from PyQt6.QtGui import QGuiApplication, QPixmap, QPainter, QFont, QColor, QIcon, QTransform
from loguru import logger


class InitiativeImg(QGraphicsPixmapItem):
    """
    Объект листа инициативы для QGraphicsScene
    initiative_list: initiative_list из initiative.py
    """
    def __init__(self, initiative_list: list):
        super().__init__()
        self.initiative_list = initiative_list
        self.setPos(0, 0)
        self.setPixmap(QPixmap('img/initiative_fon.png').scaled(QGuiApplication.primaryScreen().availableGeometry().width(), 50))
        text_items = []
        text_initiative_line_one = ""
        text_initiative_line_two = ""
        text_letter_counter = 0
        for i in initiative_list:
            text = f" {i[0]} {i[1]} |"
            text_letter_counter += len(text)
            if text_letter_counter >= 309:
                text_initiative_line_two += text
            else:
                text_initiative_line_one += text

        if text_initiative_line_one:
            text_one = QGraphicsTextItem(text_initiative_line_one, self)
            text_one.setDefaultTextColor(Qt.GlobalColor.white)
            text_one.setPos(10, 5)
            text_items.append(text_one)

        if text_initiative_line_two:
            text_two = QGraphicsTextItem(text_initiative_line_two, self)
            text_two.setDefaultTextColor(Qt.GlobalColor.white)
            text_two.setPos(10, 25)
            text_items.append(text_two)


class TokenImg(QGraphicsPixmapItem):
    """
    Объект токена для QGraphicsScene
    x, y: Кординаты
    r: Размер
    image: False(синий) True(красный)
    num: Номер токена
    """

    del_signal = pyqtSignal(QGraphicsPixmapItem)

    def __init__(self, x, y, r, num, image, player_class="", text="Unknown", type_token=""):
        super().__init__()
        self.r = r
        self.image_path = image
        self.num = num
        if "Spell_zone" in type_token:
            self.text = ""
        else:
            self.text = text
        self.player_class = player_class
        self.type_token = type_token
        self.rotate = 0
        self.setPos(x, y)


        self.init_text()
        self.set_image_path()

    def __str__(self):
        return self.text

    def init_text(self):
        self.text_item = QGraphicsTextItem(self.text, self)
        self.text_item.setDefaultTextColor(Qt.GlobalColor.black)
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.text_item.setFont(font)
        self.text_item.setPos(5, -20)

        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(QColor("white"))
        shadow_effect.setOffset(0, 0)
        self.text_item.setGraphicsEffect(shadow_effect)

        self.setAcceptHoverEvents(True)

    def set_image_path(self):
        if self.image_path:
            pass
        else:
            if self.type_token == "Hero":
                if os.path.exists(f"img/token/{self.player_class}.png"):
                    self.image_path = f"img/token/{self.player_class}.png"
                else:
                    self.image_path = f"img/token/token.png"
                self.set_pixmap()

            elif self.type_token == "Enemy":
                self.image_path = "img/token/token-" + self.num + ".png"
                self.type_token = "Enemy"

            elif self.type_token == "Ally":
                self.image_path = "img/token/token.hero-" + self.num + ".png"
                self.type_token = "Hero"

            else:
                if len(self.image_path) > 5:
                    self.set_pixmap()
        self.set_pixmap()

    @logger.catch
    def reduce_token(self, bool_val=False):
        if "Spell_zone" in self.type_token:
            if self.r >= 10:
                self.r -= 5
                self.set_pixmap()
        else:
            if self.r > 25:
                self.r -= 25
                self.set_pixmap()

    @logger.catch
    def increase_token(self, bool_val=False):
        if "Spell_zone" in self.type_token:
            self.r += 5
            self.set_pixmap()
        else:
            if self.r <= 200:
                self.r += 25
                self.set_pixmap()

    @logger.catch
    def open_image(self, bool_val=False):
        data = QFileDialog.getOpenFileName(self.parentWidget(), filter="Save (*.png)")[0]
        self.image_path = data
        self.set_pixmap()

    @logger.catch
    def set_pixmap(self):
        if self.image_path:
            self.pix = QPixmap(self.image_path).scaled(self.r, self.r, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
                                            transformMode=Qt.TransformationMode.SmoothTransformation).transformed(
            QTransform().rotate(self.rotate), Qt.TransformationMode.SmoothTransformation)
            self.set_image()

    @logger.catch
    def set_image(self):
        self.setPixmap(self.pix)

    @logger.catch
    def rotate_left(self):
        self.rotate -= 90
        self.set_pixmap()

    @logger.catch
    def rotate_right(self):
        self.rotate += 90
        self.set_pixmap()

    @logger.catch
    def contextMenuEvent(self, event) -> None:
        menu = QMenu()
        menu.setStyleSheet("QMenu    {background-color: rgb(55, 55, 55);\n"
                           "    color: rgb(247, 147, 30);}\n"
                           "QMenu::item {background-color: transparent;}\n"
                           "QMenu::item:selected {background-color: rgb(85, 85, 85);}")
        action_save = menu.addAction("Reduce", self.reduce_token)
        icon_save = QIcon()
        icon_save.addPixmap(QPixmap("img/icon/save.ico"), QIcon.Mode.Normal,
                            QIcon.State.Off)
        action_save.setIcon(icon_save)

        action_load = menu.addAction("Increase", self.increase_token)
        icon_load = QIcon()
        icon_load.addPixmap(QPixmap("img/icon/load.ico"), QIcon.Mode.Normal,
                            QIcon.State.Off)
        action_load.setIcon(icon_load)

        action_image = menu.addAction("Image", self.open_image)
        icon_save = QIcon()
        icon_save.addPixmap(QPixmap("img/icon/save.ico"), QIcon.Mode.Normal,
                            QIcon.State.Off)
        action_image.setIcon(icon_save)

        action_rotate_left = menu.addAction("rotate_left", self.rotate_left)

        action_rotate_right = menu.addAction("rotate_right", self.rotate_right)

        menu.exec(QPoint(self.cursor().pos()))

    @logger.catch
    def wheelEvent(self, event):
        if event.delta() <= 0:
            self.reduce_token()
        else:
            self.increase_token()

    @logger.catch
    def mousePressEvent(self, event):
        pass

    @logger.catch
    def mouseMoveEvent(self, event):
        orig_cursor_position = event.lastScenePos()
        updated_cursor_position = event.scenePos()

        orig_position = self.scenePos()

        updated_cursor_x = updated_cursor_position.x() - orig_cursor_position.x() + orig_position.x()
        updated_cursor_y = updated_cursor_position.y() - orig_cursor_position.y() + orig_position.y()
        self.setPos(QPointF(updated_cursor_x, updated_cursor_y))
        self.text_item.setY = self.text_item.y() + self.r
