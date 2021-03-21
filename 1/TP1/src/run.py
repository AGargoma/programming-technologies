#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from ui.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    geometry = app.primaryScreen().availableGeometry()
    main = MainWindow(geometry)
    sys.exit(app.exec_())
