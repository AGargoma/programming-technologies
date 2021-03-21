#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtGui import QScreen
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from ui.Paint import Paint
from ui.ToolBar import ToolBar


class MainWindow(QWidget):
    def __init__(self, geometry):
        super().__init__()
        self.paint = Paint(self)
        self.toolbar = ToolBar(self)
        self.paint.resize(geometry.size())
        self.toolbar.resize(self.paint.width(), self.toolbar.height())
        self.show()
