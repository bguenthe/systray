#! /usr/bin/env python
import ctypes
import glob
import sys
import os

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMenu, QSystemTrayIcon, QAction, QWidget, QGridLayout, QToolButton, \
    QHBoxLayout


class RightClickMenu(QMenu):
    def __init__(self, parent=None):
        QMenu.__init__(self, "File", None)

        icon = QtGui.QIcon("system-shutdown")
        offAction = QAction(icon, "&Close", self)
        offAction.triggered.connect(lambda: parent.off_action())
        self.addAction(offAction)


class SelectBackgroundWindow(QWidget):
    def __init__(self):
        super(SelectBackgroundWindow, self).__init__()
        self.installEventFilter(self)
        self.mapper = QtCore.QSignalMapper(self)
        self.icon_width = 40
        self.icon_height = 30

        gridLayout = QHBoxLayout()
        self.picnames = self.get_pictures()

        for pic in self.picnames:
            pixmap = QPixmap(os.getcwd() + pic)

            button = QToolButton()
            self.mapper.setMapping(button, os.getcwd() + pic)
            button.clicked.connect(self.mapper.map)

            qicon = QIcon(pixmap)
            button.setIcon(qicon)
            button.setIconSize(QSize(self.icon_width, self.icon_height))

            gridLayout.addWidget(button)

        self.mapper.mapped['QString'].connect(self.clicked)
        self.setLayout(gridLayout)

        rec = QApplication.desktop().screenGeometry()
        self.height = rec.height()
        self.width = rec.width()

        self.move(self.width - (len(self.picnames) * self.icon_width + 100), self.height - self.icon_height - 100)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def clicked(self, pic):
        self.set_background(pic)

    def get_pictures(self):
        return glob.glob("./backgrounds/*")

    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.WindowActivate:
            print("widget window has gained focus")
            self.show()
        elif event.type() == QtCore.QEvent.WindowDeactivate:
            self.hide()
            print("widget window has lost focus")
        elif event.type() == QtCore.QEvent.FocusIn:
            print("widget has gained keyboard focus")
        elif event.type() == QtCore.QEvent.FocusOut:
            self.hide()
            print("widget has lost keyboard focus")

        return False


    def set_background(self, file):
        SPI_SETDESKWALLPAPER = 20
        path = os.path.abspath(file)
        ok = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 2)


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        QSystemTrayIcon.__init__(self, parent)
        self.setIcon(QtGui.QIcon("gnomeradio.xpm"))

        self.right_menu = RightClickMenu(self)
        self.setContextMenu(self.right_menu)

        self.activated.connect(self.onTrayIconActivated)

        self.selectwallpaperwindow = SelectBackgroundWindow()

    def onTrayIconActivated(self, reason):
        self.selectwallpaperwindow.show()

    def show(self):
        QSystemTrayIcon.show(self)

    def off_action(self):
        sys.exit(1)


if __name__ == "__main__":
    app = QApplication([])

    tray = SystemTrayIcon()
    tray.show()

    app.exec_()