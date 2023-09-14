from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QGraphicsTextItem, \
    QGraphicsObject, QMenu, QFileDialog
from PyQt6.QtCore import Qt, QPointF, QRect, pyqtSignal, QPoint
from PyQt6.QtGui import QGuiApplication, QPixmap, QPainter, QFont, QColor, QIcon
from loguru import logger


class InitiativeImg(QGraphicsPixmapItem):
    def __init__(self, initiative_list: list):
        super().__init__()
        self.initiative_list = initiative_list
        self.setPos(0, 0)
        self.setPixmap(QPixmap('img/initiative_fon.png').scaled(QGuiApplication.primaryScreen().availableGeometry().width(), 50))
        text_pos = 10
        text_items = []
        for i in initiative_list:
            text = QGraphicsTextItem(f"{i[0]} {i[1]}", self)
            text.setDefaultTextColor(Qt.GlobalColor.white)
            text.setPos(text_pos, 20)
            text_pos += 75
            text_items.append(text)


class TokenImg(QGraphicsPixmapItem):
    """
    Объект токена для QGraphicsScene
    x, y: Кординаты
    r: Размер
    image: False(синий) True(красный)
    num: Номер токена
    """

    def __init__(self, x, y, r, num, image, player_class="", text="Unknown"):
        super().__init__()
        self.r = r
        self.image_path = image
        self.num = num
        self.text = text
        self.player_class = player_class
        self.setPos(x, y)

        self.init_text()
        self.app_func()

    def __str__(self):
        return self.text

    def init_text(self):
        self.text_item = QGraphicsTextItem(self.text, self)
        self.text_item.setDefaultTextColor(Qt.GlobalColor.blue)
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.text_item.setFont(font)
        self.text_item.setPos(5, -20)


        self.setAcceptHoverEvents(True)

    def app_func(self):
        if self.player_class:
            self.image_path = f"img/token/{self.player_class}.png"
            self.set_image()
        else:
            if len(self.image_path) > 1:
                self.set_image()
            else:
                self.show_token()

    @logger.catch
    def reduce_token(self, bool_val=False):
        if self.r >= 20:
            self.r -= 25
            self.set_image()

    @logger.catch
    def increase_token(self, bool_val=False):
        if self.r <= 200:
            self.r += 25
            self.set_image()

    @logger.catch
    def show_token(self, bool_val=False):
        if self.image_path == "Enemy":
            self.image_path = "img/token/token-" + self.num + ".png"

        elif self.image_path == "Hero":
            self.image_path = "img/token/token.hero-" + self.num + ".png"

        self.set_image()

    @logger.catch
    def open_image(self, bool_val=False):
        data = QFileDialog.getOpenFileName(self.parentWidget(), filter="Save (*.png)")[0]
        self.image_path = data
        self.set_image()

    @logger.catch
    def set_image(self):
        if self.image_path:
            self.pix = QPixmap(self.image_path).scaled(self.r, self.r, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
                                            transformMode=Qt.TransformationMode.SmoothTransformation)
            self.setPixmap(self.pix)

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

        menu.exec(QPoint(self.cursor().pos()))

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
