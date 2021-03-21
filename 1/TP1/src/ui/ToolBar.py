#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import partial

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QInputDialog, QSpinBox, QFrame, QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget

from shapes import *
from ui.QColorButton import QColorButton


class ToolBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.active = None
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('lightgrey'))
        self.setPalette(p)
        self.setAutoFillBackground(True)
        self.btns = list(map(lambda cls: QPushButton(cls.name()), shapes))
        self.brd_color_btn = QColorButton('purple')
        self.bg_color_btn = QColorButton('white')

        self.paint_rbtn = QRadioButton('Paint')
        self.paint_rbtn.setChecked(True)
        self.parent.mode = 'Paint'
        self.move_rbtn = QRadioButton('Move')
        self.num = 3
        self.num_box = QSpinBox(self)
        self.num_box.setRange(3, 9999)
        self.reset_btn = QPushButton('Reset', self)

        self.create_buttons()
        self.show()

    def create_buttons(self):
        layout = QHBoxLayout()
        self.parent.active = self.btns[0].text()
        layout.addWidget(QLabel('Border color:', self))
        layout.addWidget(self.brd_color_btn)
        layout.addWidget(QLabel('Background color:', self))
        layout.addWidget(self.bg_color_btn)
        radiolayout = QVBoxLayout()
        radiolayout.addWidget(self.paint_rbtn)
        radiolayout.addWidget(self.move_rbtn)
        layout.addLayout(radiolayout)
        layout.addWidget(QLabel('Figures:', self))
        for item in self.btns:
            layout.addWidget(item)
        layout.addWidget(QLabel('Angles'))
        layout.addWidget(self.num_box)
        layout.addWidget(self.reset_btn)

        self.paint_rbtn.toggled.connect(self.radio_paint_click)
        self.move_rbtn.toggled.connect(self.radio_move_click)
        for i in range(len(self.btns)):
            self.btns[i].clicked.connect(partial(self.figure_click, self.btns[i]))
        self.num_box.valueChanged.connect(self.set_num)
        self.reset_btn.clicked.connect(self.parent.paint.reset)

        self.setLayout(layout)

    def set_num(self, i):
        self.num = i

    def radio_paint_click(self, t):
        if t:
            self.parent.mode = 'Paint'
            self.parent.paint.update()

    def radio_move_click(self, t):
        if t:
            self.parent.mode = 'Move'
            self.parent.paint.update()

    def figure_click(self, btn):
        self.parent.active = btn.text()
