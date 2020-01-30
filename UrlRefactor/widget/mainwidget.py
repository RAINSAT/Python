from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtWidgets import QPushButton


class UrlWidget(QMainWindow):
    def __init__(self, parent=None):
        super(UrlWidget, self).__init__(parent=parent)
        self.__gui_init()

    def __gui_init(self):
        # self.setFixedSize(QSize(1280, 720))
        self.setWindowIcon(QIcon("./res/icon.png"))
        self.setWindowTitle("UrlRefactor")

        # 竖直布局
        vlayout = QVBoxLayout()

        # 水平布局 上
        hlayout_up = QHBoxLayout()
        # 水平布局 下
        hlayout_down = QHBoxLayout()

        # 水平布局 上 控件
        openBtn: QPushButton = QPushButton("test", self)
        closeBtn: QPushButton = QPushButton("close", self)
        hlayout_up.addWidget(openBtn,0, alignment=Qt.AlignCenter)
        hlayout_up.addStretch(1)
        hlayout_up.addWidget(closeBtn, 1, alignment=Qt.AlignCenter)
        # 水平布局 下 控件
        central_widget = QWidget(self, flags=Qt.Widget)
        palette = central_widget.palette()
        palette.setColor(QPalette.Window,QColor(15,120,166))
        hlayout_down.addWidget(central_widget, alignment=Qt.AlignCenter)
        # 添加布局
        vlayout.addLayout(hlayout_up)
        vlayout.addLayout(hlayout_down)
        self.setLayout(vlayout)


