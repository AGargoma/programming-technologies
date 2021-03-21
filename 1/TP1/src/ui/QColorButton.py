#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtWidgets import QPushButton


class QColorButton(QPushButton):

    def __init__(self, color):
        super(QColorButton, self).__init__()
        self.color = color
        self.pressed.connect(self.choose_color)

    def get_color(self):
        return QColor(self.color)

    def choose_color(self):
        dlg = QColorDialog(self)
        dlg.setCurrentColor(QColor(self.color))
        if dlg.exec_():
            self.color = dlg.currentColor().name()
            # self.setStyleSheet("background-color: %s;" % self.color)
