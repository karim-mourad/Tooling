# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from lxml import etree as ET

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(952, 309)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1211, 601))
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.PORTA0 = QGroupBox(self.tab)
        self.PORTA0.setObjectName(u"PORTA0")
        self.PORTA0.setEnabled(True)
        self.PORTA0.setGeometry(QRect(210, 10, 131, 71))
        self.PORTA0_high = QRadioButton(self.PORTA0)
        self.PORTA0_high.setObjectName(u"PORTA0_high")
        self.PORTA0_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTA0_high.setChecked(True)
        self.PORTA0_low = QRadioButton(self.PORTA0)
        self.PORTA0_low.setObjectName(u"PORTA0_low")
        self.PORTA0_low.setGeometry(QRect(10, 50, 82, 17))
        self.PINA0 = QGroupBox(self.tab)
        self.PINA0.setObjectName(u"PINA0")
        self.PINA0.setEnabled(False)
        self.PINA0.setGeometry(QRect(340, 10, 131, 71))
        self.PINA0_pullup = QRadioButton(self.PINA0)
        self.PINA0_pullup.setObjectName(u"PINA0_pullup")
        self.PINA0_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINA0_highimp = QRadioButton(self.PINA0)
        self.PINA0_highimp.setObjectName(u"PINA0_highimp")
        self.PINA0_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINA0_highimp.setChecked(True)
        self.DDRA0 = QGroupBox(self.tab)
        self.DDRA0.setObjectName(u"DDRA0")
        self.DDRA0.setGeometry(QRect(80, 10, 131, 71))
        self.DDRA0.setFlat(False)
        self.DDRA0.setCheckable(False)
        self.DDRA0_output = QRadioButton(self.DDRA0)
        self.DDRA0_output.setObjectName(u"DDRA0_output")
        self.DDRA0_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRA0_output.setChecked(True)
        self.DDRA0_input = QRadioButton(self.DDRA0)
        self.DDRA0_input.setObjectName(u"DDRA0_input")
        self.DDRA0_input.setGeometry(QRect(10, 50, 82, 17))
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 47, 13))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setTextFormat(Qt.AutoText)
        self.PORTA1 = QGroupBox(self.tab)
        self.PORTA1.setObjectName(u"PORTA1")
        self.PORTA1.setEnabled(True)
        self.PORTA1.setGeometry(QRect(210, 80, 131, 71))
        self.PORTA1_high = QRadioButton(self.PORTA1)
        self.PORTA1_high.setObjectName(u"PORTA1_high")
        self.PORTA1_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTA1_high.setChecked(True)
        self.PORTA1_low = QRadioButton(self.PORTA1)
        self.PORTA1_low.setObjectName(u"PORTA1_low")
        self.PORTA1_low.setGeometry(QRect(10, 50, 82, 17))
        self.PINA1 = QGroupBox(self.tab)
        self.PINA1.setObjectName(u"PINA1")
        self.PINA1.setEnabled(False)
        self.PINA1.setGeometry(QRect(340, 80, 131, 71))
        self.PINA1_pullup = QRadioButton(self.PINA1)
        self.PINA1_pullup.setObjectName(u"PINA1_pullup")
        self.PINA1_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINA1_highimp = QRadioButton(self.PINA1)
        self.PINA1_highimp.setObjectName(u"PINA1_highimp")
        self.PINA1_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINA1_highimp.setChecked(True)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 110, 47, 13))
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setTextFormat(Qt.AutoText)
        self.DDRA1 = QGroupBox(self.tab)
        self.DDRA1.setObjectName(u"DDRA1")
        self.DDRA1.setGeometry(QRect(80, 80, 131, 71))
        self.DDRA1.setFlat(False)
        self.DDRA1.setCheckable(False)
        self.DDRA1_output = QRadioButton(self.DDRA1)
        self.DDRA1_output.setObjectName(u"DDRA1_output")
        self.DDRA1_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRA1_output.setChecked(True)
        self.DDRA1_input = QRadioButton(self.DDRA1)
        self.DDRA1_input.setObjectName(u"DDRA1_input")
        self.DDRA1_input.setGeometry(QRect(10, 50, 82, 17))
        self.PORTA2 = QGroupBox(self.tab)
        self.PORTA2.setObjectName(u"PORTA2")
        self.PORTA2.setEnabled(True)
        self.PORTA2.setGeometry(QRect(210, 150, 131, 71))
        self.PORTA2_high = QRadioButton(self.PORTA2)
        self.PORTA2_high.setObjectName(u"PORTA2_high")
        self.PORTA2_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTA2_high.setChecked(True)
        self.PORTA2_low = QRadioButton(self.PORTA2)
        self.PORTA2_low.setObjectName(u"PORTA2_low")
        self.PORTA2_low.setGeometry(QRect(10, 50, 82, 17))
        self.PINA2 = QGroupBox(self.tab)
        self.PINA2.setObjectName(u"PINA2")
        self.PINA2.setEnabled(False)
        self.PINA2.setGeometry(QRect(340, 150, 131, 71))
        self.PINA2_pullup = QRadioButton(self.PINA2)
        self.PINA2_pullup.setObjectName(u"PINA2_pullup")
        self.PINA2_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINA2_highimp = QRadioButton(self.PINA2)
        self.PINA2_highimp.setObjectName(u"PINA2_highimp")
        self.PINA2_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINA2_highimp.setChecked(True)
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 180, 47, 13))
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setTextFormat(Qt.AutoText)
        self.DDRA2 = QGroupBox(self.tab)
        self.DDRA2.setObjectName(u"DDRA2")
        self.DDRA2.setGeometry(QRect(80, 150, 131, 71))
        self.DDRA2.setFlat(False)
        self.DDRA2.setCheckable(False)
        self.DDRA2_output = QRadioButton(self.DDRA2)
        self.DDRA2_output.setObjectName(u"DDRA2_output")
        self.DDRA2_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRA2_output.setChecked(True)
        self.DDRA2_input = QRadioButton(self.DDRA2)
        self.DDRA2_input.setObjectName(u"DDRA2_input")
        self.DDRA2_input.setGeometry(QRect(10, 50, 82, 17))
        self.PORTA3 = QGroupBox(self.tab)
        self.PORTA3.setObjectName(u"PORTA3")
        self.PORTA3.setEnabled(True)
        self.PORTA3.setGeometry(QRect(210, 220, 131, 71))
        self.PORTA3_high = QRadioButton(self.PORTA3)
        self.PORTA3_high.setObjectName(u"PORTA3_high")
        self.PORTA3_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTA3_high.setChecked(True)
        self.PORTA3_low = QRadioButton(self.PORTA3)
        self.PORTA3_low.setObjectName(u"PORTA3_low")
        self.PORTA3_low.setGeometry(QRect(10, 50, 82, 17))
        self.PINA3 = QGroupBox(self.tab)
        self.PINA3.setObjectName(u"PINA3")
        self.PINA3.setEnabled(False)
        self.PINA3.setGeometry(QRect(340, 220, 131, 71))
        self.PINA3_pullup = QRadioButton(self.PINA3)
        self.PINA3_pullup.setObjectName(u"PINA3_pullup")
        self.PINA3_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINA3_highimp = QRadioButton(self.PINA3)
        self.PINA3_highimp.setObjectName(u"PINA3_highimp")
        self.PINA3_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINA3_highimp.setChecked(True)
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 250, 47, 13))
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QFrame.NoFrame)
        self.label_4.setTextFormat(Qt.AutoText)
        self.DDRA3 = QGroupBox(self.tab)
        self.DDRA3.setObjectName(u"DDRA3")
        self.DDRA3.setGeometry(QRect(80, 220, 131, 71))
        self.DDRA3.setFlat(False)
        self.DDRA3.setCheckable(False)
        self.DDRA3_output = QRadioButton(self.DDRA3)
        self.DDRA3_output.setObjectName(u"DDRA3_output")
        self.DDRA3_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRA3_output.setChecked(True)
        self.DDRA3_input = QRadioButton(self.DDRA3)
        self.DDRA3_input.setObjectName(u"DDRA3_input")
        self.DDRA3_input.setGeometry(QRect(10, 50, 82, 17))
        self.PINA6 = QGroupBox(self.tab)
        self.PINA6.setObjectName(u"PINA6")
        self.PINA6.setEnabled(False)
        self.PINA6.setGeometry(QRect(810, 150, 131, 71))
        self.PINA6_pullup = QRadioButton(self.PINA6)
        self.PINA6_pullup.setObjectName(u"PINA6_pullup")
        self.PINA6_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINA6_highimp = QRadioButton(self.PINA6)
        self.PINA6_highimp.setObjectName(u"PINA6_highimp")
        self.PINA6_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINA6_highimp.setChecked(True)
        self.DDRA7 = QGroupBox(self.tab)
        self.DDRA7.setObjectName(u"DDRA7")
        self.DDRA7.setGeometry(QRect(550, 220, 131, 71))
        self.DDRA7.setFlat(False)
        self.DDRA7.setCheckable(False)
        self.DDRA7_output = QRadioButton(self.DDRA7)
        self.DDRA7_output.setObjectName(u"DDRA7_output")
        self.DDRA7_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRA7_output.setChecked(True)
        self.DDRA7_input = QRadioButton(self.DDRA7)
        self.DDRA7_input.setObjectName(u"DDRA7_input")
        self.DDRA7_input.setGeometry(QRect(10, 50, 82, 17))
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(480, 180, 47, 13))
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.label_5.setTextFormat(Qt.AutoText)
        self.PINA5 = QGroupBox(self.tab)
        self.PINA5.setObjectName(u"PINA5")
        self.PINA5.setEnabled(False)
        self.PINA5.setGeometry(QRect(810, 80, 131, 71))
        self.PINA5_pullup = QRadioButton(self.PINA5)
        self.PINA5_pullup.setObjectName(u"PINA5_pullup")
        self.PINA5_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINA5_highimp = QRadioButton(self.PINA5)
        self.PINA5_highimp.setObjectName(u"PINA5_highimp")
        self.PINA5_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINA5_highimp.setChecked(True)
        self.DDRA6 = QGroupBox(self.tab)
        self.DDRA6.setObjectName(u"DDRA6")
        self.DDRA6.setGeometry(QRect(550, 150, 131, 71))
        self.DDRA6.setFlat(False)
        self.DDRA6.setCheckable(False)
        self.DDRA6_output = QRadioButton(self.DDRA6)
        self.DDRA6_output.setObjectName(u"DDRA6_output")
        self.DDRA6_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRA6_output.setChecked(True)
        self.DDRA6_input = QRadioButton(self.DDRA6)
        self.DDRA6_input.setObjectName(u"DDRA6_input")
        self.DDRA6_input.setGeometry(QRect(10, 50, 82, 17))
        self.DDRA5 = QGroupBox(self.tab)
        self.DDRA5.setObjectName(u"DDRA5")
        self.DDRA5.setGeometry(QRect(550, 80, 131, 71))
        self.DDRA5.setFlat(False)
        self.DDRA5.setCheckable(False)
        self.DDRA5_output = QRadioButton(self.DDRA5)
        self.DDRA5_output.setObjectName(u"DDRA5_output")
        self.DDRA5_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRA5_output.setChecked(True)
        self.DDRA5_input = QRadioButton(self.DDRA5)
        self.DDRA5_input.setObjectName(u"DDRA5_input")
        self.DDRA5_input.setGeometry(QRect(10, 50, 82, 17))
        self.PINA7 = QGroupBox(self.tab)
        self.PINA7.setObjectName(u"PINA7")
        self.PINA7.setEnabled(False)
        self.PINA7.setGeometry(QRect(810, 220, 131, 71))
        self.PINA7_pullup = QRadioButton(self.PINA7)
        self.PINA7_pullup.setObjectName(u"PINA7_pullup")
        self.PINA7_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINA7_highimp = QRadioButton(self.PINA7)
        self.PINA7_highimp.setObjectName(u"PINA7_highimp")
        self.PINA7_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINA7_highimp.setChecked(True)
        self.PORTA4 = QGroupBox(self.tab)
        self.PORTA4.setObjectName(u"PORTA4")
        self.PORTA4.setEnabled(True)
        self.PORTA4.setGeometry(QRect(680, 10, 131, 71))
        self.PORTA4_high = QRadioButton(self.PORTA4)
        self.PORTA4_high.setObjectName(u"PORTA4_high")
        self.PORTA4_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTA4_high.setChecked(True)
        self.PORTA4_low = QRadioButton(self.PORTA4)
        self.PORTA4_low.setObjectName(u"PORTA4_low")
        self.PORTA4_low.setGeometry(QRect(10, 50, 82, 17))
        self.PORTA6 = QGroupBox(self.tab)
        self.PORTA6.setObjectName(u"PORTA6")
        self.PORTA6.setEnabled(True)
        self.PORTA6.setGeometry(QRect(680, 150, 131, 71))
        self.PORTA6_high = QRadioButton(self.PORTA6)
        self.PORTA6_high.setObjectName(u"PORTA6_high")
        self.PORTA6_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTA6_high.setChecked(True)
        self.PORTA6_low = QRadioButton(self.PORTA6)
        self.PORTA6_low.setObjectName(u"PORTA6_low")
        self.PORTA6_low.setGeometry(QRect(10, 50, 82, 17))
        self.PINA4 = QGroupBox(self.tab)
        self.PINA4.setObjectName(u"PINA4")
        self.PINA4.setEnabled(False)
        self.PINA4.setGeometry(QRect(810, 10, 131, 71))
        self.PINA4_pullup = QRadioButton(self.PINA4)
        self.PINA4_pullup.setObjectName(u"PINA4_pullup")
        self.PINA4_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINA4_highimp = QRadioButton(self.PINA4)
        self.PINA4_highimp.setObjectName(u"PINA4_highimp")
        self.PINA4_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINA4_highimp.setChecked(True)
        self.PORTA5 = QGroupBox(self.tab)
        self.PORTA5.setObjectName(u"PORTA5")
        self.PORTA5.setEnabled(True)
        self.PORTA5.setGeometry(QRect(680, 80, 131, 71))
        self.PORTA5_high = QRadioButton(self.PORTA5)
        self.PORTA5_high.setObjectName(u"PORTA5_high")
        self.PORTA5_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTA5_high.setChecked(True)
        self.PORTA5_low = QRadioButton(self.PORTA5)
        self.PORTA5_low.setObjectName(u"PORTA5_low")
        self.PORTA5_low.setGeometry(QRect(10, 50, 82, 17))
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(480, 40, 47, 13))
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QFrame.NoFrame)
        self.label_6.setTextFormat(Qt.AutoText)
        self.PORTA7 = QGroupBox(self.tab)
        self.PORTA7.setObjectName(u"PORTA7")
        self.PORTA7.setEnabled(True)
        self.PORTA7.setGeometry(QRect(680, 220, 131, 71))
        self.PORTA7_high = QRadioButton(self.PORTA7)
        self.PORTA7_high.setObjectName(u"PORTA7_high")
        self.PORTA7_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTA7_high.setChecked(True)
        self.PORTA7_low = QRadioButton(self.PORTA7)
        self.PORTA7_low.setObjectName(u"PORTA7_low")
        self.PORTA7_low.setGeometry(QRect(10, 50, 82, 17))
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(480, 250, 47, 13))
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QFrame.NoFrame)
        self.label_7.setTextFormat(Qt.AutoText)
        self.DDRA4 = QGroupBox(self.tab)
        self.DDRA4.setObjectName(u"DDRA4")
        self.DDRA4.setGeometry(QRect(550, 10, 131, 71))
        self.DDRA4.setFlat(False)
        self.DDRA4.setCheckable(False)
        self.DDRA4_output = QRadioButton(self.DDRA4)
        self.DDRA4_output.setObjectName(u"DDRA4_output")
        self.DDRA4_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRA4_output.setChecked(True)
        self.DDRA4_input = QRadioButton(self.DDRA4)
        self.DDRA4_input.setObjectName(u"DDRA4_input")
        self.DDRA4_input.setGeometry(QRect(10, 50, 82, 17))
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(480, 110, 47, 13))
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QFrame.NoFrame)
        self.label_8.setTextFormat(Qt.AutoText)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.DDRB4 = QGroupBox(self.tab_2)
        self.DDRB4.setObjectName(u"DDRB4")
        self.DDRB4.setGeometry(QRect(550, 10, 131, 71))
        self.DDRB4.setFlat(False)
        self.DDRB4.setCheckable(False)
        self.DDRB4_output = QRadioButton(self.DDRB4)
        self.DDRB4_output.setObjectName(u"DDRB4_output")
        self.DDRB4_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRB4_output.setChecked(True)
        self.DDRB4_input = QRadioButton(self.DDRB4)
        self.DDRB4_input.setObjectName(u"DDRB4_input")
        self.DDRB4_input.setGeometry(QRect(10, 50, 82, 17))
        self.PORTB6 = QGroupBox(self.tab_2)
        self.PORTB6.setObjectName(u"PORTB6")
        self.PORTB6.setEnabled(True)
        self.PORTB6.setGeometry(QRect(680, 150, 131, 71))
        self.PORTB6_high = QRadioButton(self.PORTB6)
        self.PORTB6_high.setObjectName(u"PORTB6_high")
        self.PORTB6_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTB6_high.setChecked(True)
        self.PORTB6_low = QRadioButton(self.PORTB6)
        self.PORTB6_low.setObjectName(u"PORTB6_low")
        self.PORTB6_low.setGeometry(QRect(10, 50, 82, 17))
        self.PINB4 = QGroupBox(self.tab_2)
        self.PINB4.setObjectName(u"PINB4")
        self.PINB4.setEnabled(False)
        self.PINB4.setGeometry(QRect(810, 10, 131, 71))
        self.PINB4_pullup = QRadioButton(self.PINB4)
        self.PINB4_pullup.setObjectName(u"PINB4_pullup")
        self.PINB4_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINB4_highimp = QRadioButton(self.PINB4)
        self.PINB4_highimp.setObjectName(u"PINB4_highimp")
        self.PINB4_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINB4_highimp.setChecked(True)
        self.PINB6 = QGroupBox(self.tab_2)
        self.PINB6.setObjectName(u"PINB6")
        self.PINB6.setEnabled(False)
        self.PINB6.setGeometry(QRect(810, 150, 131, 71))
        self.PINB6_pullup = QRadioButton(self.PINB6)
        self.PINB6_pullup.setObjectName(u"PINB6_pullup")
        self.PINB6_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINB6_highimp = QRadioButton(self.PINB6)
        self.PINB6_highimp.setObjectName(u"PINB6_highimp")
        self.PINB6_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINB6_highimp.setChecked(True)
        self.PINB0 = QGroupBox(self.tab_2)
        self.PINB0.setObjectName(u"PINB0")
        self.PINB0.setEnabled(False)
        self.PINB0.setGeometry(QRect(340, 10, 131, 71))
        self.PINB0_pullup = QRadioButton(self.PINB0)
        self.PINB0_pullup.setObjectName(u"PINB0_pullup")
        self.PINB0_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINB0_highimp = QRadioButton(self.PINB0)
        self.PINB0_highimp.setObjectName(u"PINB0_highimp")
        self.PINB0_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINB0_highimp.setChecked(True)
        self.DDRB5 = QGroupBox(self.tab_2)
        self.DDRB5.setObjectName(u"DDRB5")
        self.DDRB5.setGeometry(QRect(550, 80, 131, 71))
        self.DDRB5.setFlat(False)
        self.DDRB5.setCheckable(False)
        self.DDRB5_output = QRadioButton(self.DDRB5)
        self.DDRB5_output.setObjectName(u"DDRB5_output")
        self.DDRB5_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRB5_output.setChecked(True)
        self.DDRB5_input = QRadioButton(self.DDRB5)
        self.DDRB5_input.setObjectName(u"DDRB5_input")
        self.DDRB5_input.setGeometry(QRect(10, 50, 82, 17))
        self.DDRB7 = QGroupBox(self.tab_2)
        self.DDRB7.setObjectName(u"DDRB7")
        self.DDRB7.setGeometry(QRect(550, 220, 131, 71))
        self.DDRB7.setFlat(False)
        self.DDRB7.setCheckable(False)
        self.DDRB7_output = QRadioButton(self.DDRB7)
        self.DDRB7_output.setObjectName(u"DDRB7_output")
        self.DDRB7_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRB7_output.setChecked(True)
        self.DDRB7_input = QRadioButton(self.DDRB7)
        self.DDRB7_input.setObjectName(u"DDRB7_input")
        self.DDRB7_input.setGeometry(QRect(10, 50, 82, 17))
        self.PINB5 = QGroupBox(self.tab_2)
        self.PINB5.setObjectName(u"PINB5")
        self.PINB5.setEnabled(False)
        self.PINB5.setGeometry(QRect(810, 80, 131, 71))
        self.PINB5_pullup = QRadioButton(self.PINB5)
        self.PINB5_pullup.setObjectName(u"PINB5_pullup")
        self.PINB5_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINB5_highimp = QRadioButton(self.PINB5)
        self.PINB5_highimp.setObjectName(u"PINB5_highimp")
        self.PINB5_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINB5_highimp.setChecked(True)
        self.PORTB7 = QGroupBox(self.tab_2)
        self.PORTB7.setObjectName(u"PORTB7")
        self.PORTB7.setEnabled(True)
        self.PORTB7.setGeometry(QRect(680, 220, 131, 71))
        self.PORTB7_high = QRadioButton(self.PORTB7)
        self.PORTB7_high.setObjectName(u"PORTB7_high")
        self.PORTB7_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTB7_high.setChecked(True)
        self.PORTB7_low = QRadioButton(self.PORTB7)
        self.PORTB7_low.setObjectName(u"PORTB7_low")
        self.PORTB7_low.setGeometry(QRect(10, 50, 82, 17))
        self.PINB1 = QGroupBox(self.tab_2)
        self.PINB1.setObjectName(u"PINB1")
        self.PINB1.setEnabled(False)
        self.PINB1.setGeometry(QRect(340, 80, 131, 71))
        self.PINB1_pullup = QRadioButton(self.PINB1)
        self.PINB1_pullup.setObjectName(u"PINB1_pullup")
        self.PINB1_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINB1_highimp = QRadioButton(self.PINB1)
        self.PINB1_highimp.setObjectName(u"PINB1_highimp")
        self.PINB1_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINB1_highimp.setChecked(True)
        self.DDRB3 = QGroupBox(self.tab_2)
        self.DDRB3.setObjectName(u"DDRB3")
        self.DDRB3.setGeometry(QRect(80, 220, 131, 71))
        self.DDRB3.setFlat(False)
        self.DDRB3.setCheckable(False)
        self.DDRB3_output = QRadioButton(self.DDRB3)
        self.DDRB3_output.setObjectName(u"DDRB3_output")
        self.DDRB3_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRB3_output.setChecked(True)
        self.DDRB3_input = QRadioButton(self.DDRB3)
        self.DDRB3_input.setObjectName(u"DDRB3_input")
        self.DDRB3_input.setGeometry(QRect(10, 50, 82, 17))
        self.label_17 = QLabel(self.tab_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(480, 180, 47, 13))
        self.label_17.setFont(font)
        self.label_17.setFrameShape(QFrame.NoFrame)
        self.label_17.setTextFormat(Qt.AutoText)
        self.PINB7 = QGroupBox(self.tab_2)
        self.PINB7.setObjectName(u"PINB7")
        self.PINB7.setEnabled(False)
        self.PINB7.setGeometry(QRect(810, 220, 131, 71))
        self.PINB7_pullup = QRadioButton(self.PINB7)
        self.PINB7_pullup.setObjectName(u"PINB7_pullup")
        self.PINB7_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINB7_highimp = QRadioButton(self.PINB7)
        self.PINB7_highimp.setObjectName(u"PINB7_highimp")
        self.PINB7_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINB7_highimp.setChecked(True)
        self.PINB3 = QGroupBox(self.tab_2)
        self.PINB3.setObjectName(u"PINB3")
        self.PINB3.setEnabled(False)
        self.PINB3.setGeometry(QRect(340, 220, 131, 71))
        self.PINB3_pullup = QRadioButton(self.PINB3)
        self.PINB3_pullup.setObjectName(u"PINB3_pullup")
        self.PINB3_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINB3_highimp = QRadioButton(self.PINB3)
        self.PINB3_highimp.setObjectName(u"PINB3_highimp")
        self.PINB3_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINB3_highimp.setChecked(True)
        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(480, 110, 47, 13))
        self.label_18.setFont(font)
        self.label_18.setFrameShape(QFrame.NoFrame)
        self.label_18.setTextFormat(Qt.AutoText)
        self.label_19 = QLabel(self.tab_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 250, 47, 13))
        self.label_19.setFont(font)
        self.label_19.setFrameShape(QFrame.NoFrame)
        self.label_19.setTextFormat(Qt.AutoText)
        self.DDRB0 = QGroupBox(self.tab_2)
        self.DDRB0.setObjectName(u"DDRB0")
        self.DDRB0.setGeometry(QRect(80, 10, 131, 71))
        self.DDRB0.setFlat(False)
        self.DDRB0.setCheckable(False)
        self.DDRB0_output = QRadioButton(self.DDRB0)
        self.DDRB0_output.setObjectName(u"DDRB0_output")
        self.DDRB0_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRB0_output.setChecked(True)
        self.DDRB0_input = QRadioButton(self.DDRB0)
        self.DDRB0_input.setObjectName(u"DDRB0_input")
        self.DDRB0_input.setGeometry(QRect(10, 50, 82, 17))
        self.label_20 = QLabel(self.tab_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 110, 47, 13))
        self.label_20.setFont(font)
        self.label_20.setFrameShape(QFrame.NoFrame)
        self.label_20.setTextFormat(Qt.AutoText)
        self.PORTB0 = QGroupBox(self.tab_2)
        self.PORTB0.setObjectName(u"PORTB0")
        self.PORTB0.setEnabled(True)
        self.PORTB0.setGeometry(QRect(210, 10, 131, 71))
        self.PORTB0_high = QRadioButton(self.PORTB0)
        self.PORTB0_high.setObjectName(u"PORTB0_high")
        self.PORTB0_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTB0_high.setChecked(True)
        self.PORTB0_low = QRadioButton(self.PORTB0)
        self.PORTB0_low.setObjectName(u"PORTB0_low")
        self.PORTB0_low.setGeometry(QRect(10, 50, 82, 17))
        self.DDRB6 = QGroupBox(self.tab_2)
        self.DDRB6.setObjectName(u"DDRB6")
        self.DDRB6.setGeometry(QRect(550, 150, 131, 71))
        self.DDRB6.setFlat(False)
        self.DDRB6.setCheckable(False)
        self.DDRB6_output = QRadioButton(self.DDRB6)
        self.DDRB6_output.setObjectName(u"DDRB6_output")
        self.DDRB6_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRB6_output.setChecked(True)
        self.DDRB6_input = QRadioButton(self.DDRB6)
        self.DDRB6_input.setObjectName(u"DDRB6_input")
        self.DDRB6_input.setGeometry(QRect(10, 50, 82, 17))
        self.label_21 = QLabel(self.tab_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 180, 47, 13))
        self.label_21.setFont(font)
        self.label_21.setFrameShape(QFrame.NoFrame)
        self.label_21.setTextFormat(Qt.AutoText)
        self.DDRB1 = QGroupBox(self.tab_2)
        self.DDRB1.setObjectName(u"DDRB1")
        self.DDRB1.setGeometry(QRect(80, 80, 131, 71))
        self.DDRB1.setFlat(False)
        self.DDRB1.setCheckable(False)
        self.DDRB1_output = QRadioButton(self.DDRB1)
        self.DDRB1_output.setObjectName(u"DDRB1_output")
        self.DDRB1_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRB1_output.setChecked(True)
        self.DDRB1_input = QRadioButton(self.DDRB1)
        self.DDRB1_input.setObjectName(u"DDRB1_input")
        self.DDRB1_input.setGeometry(QRect(10, 50, 82, 17))
        self.PORTB1 = QGroupBox(self.tab_2)
        self.PORTB1.setObjectName(u"PORTB1")
        self.PORTB1.setEnabled(True)
        self.PORTB1.setGeometry(QRect(210, 80, 131, 71))
        self.PORTB1_high = QRadioButton(self.PORTB1)
        self.PORTB1_high.setObjectName(u"PORTB1_high")
        self.PORTB1_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTB1_high.setChecked(True)
        self.PORTB1_low = QRadioButton(self.PORTB1)
        self.PORTB1_low.setObjectName(u"PORTB1_low")
        self.PORTB1_low.setGeometry(QRect(10, 50, 82, 17))
        self.PORTB3 = QGroupBox(self.tab_2)
        self.PORTB3.setObjectName(u"PORTB3")
        self.PORTB3.setEnabled(True)
        self.PORTB3.setGeometry(QRect(210, 220, 131, 71))
        self.PORTB3_high = QRadioButton(self.PORTB3)
        self.PORTB3_high.setObjectName(u"PORTB3_high")
        self.PORTB3_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTB3_high.setChecked(True)
        self.PORTB3_low = QRadioButton(self.PORTB3)
        self.PORTB3_low.setObjectName(u"PORTB3_low")
        self.PORTB3_low.setGeometry(QRect(10, 50, 82, 17))
        self.DDRB2 = QGroupBox(self.tab_2)
        self.DDRB2.setObjectName(u"DDRB2")
        self.DDRB2.setGeometry(QRect(80, 150, 131, 71))
        self.DDRB2.setFlat(False)
        self.DDRB2.setCheckable(False)
        self.DDRB2_output = QRadioButton(self.DDRB2)
        self.DDRB2_output.setObjectName(u"DDRB2_output")
        self.DDRB2_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRB2_output.setChecked(True)
        self.DDRB2_input = QRadioButton(self.DDRB2)
        self.DDRB2_input.setObjectName(u"DDRB2_input")
        self.DDRB2_input.setGeometry(QRect(10, 50, 82, 17))
        self.label_22 = QLabel(self.tab_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(480, 40, 47, 13))
        self.label_22.setFont(font)
        self.label_22.setFrameShape(QFrame.NoFrame)
        self.label_22.setTextFormat(Qt.AutoText)
        self.label_23 = QLabel(self.tab_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 40, 47, 13))
        self.label_23.setFont(font)
        self.label_23.setFrameShape(QFrame.NoFrame)
        self.label_23.setTextFormat(Qt.AutoText)
        self.PORTB5 = QGroupBox(self.tab_2)
        self.PORTB5.setObjectName(u"PORTB5")
        self.PORTB5.setEnabled(True)
        self.PORTB5.setGeometry(QRect(680, 80, 131, 71))
        self.PORTB5_high = QRadioButton(self.PORTB5)
        self.PORTB5_high.setObjectName(u"PORTB5_high")
        self.PORTB5_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTB5_high.setChecked(True)
        self.PORTB5_low = QRadioButton(self.PORTB5)
        self.PORTB5_low.setObjectName(u"PORTB5_low")
        self.PORTB5_low.setGeometry(QRect(10, 50, 82, 17))
        self.PINB2 = QGroupBox(self.tab_2)
        self.PINB2.setObjectName(u"PINB2")
        self.PINB2.setEnabled(False)
        self.PINB2.setGeometry(QRect(340, 150, 131, 71))
        self.PINB2_pullup = QRadioButton(self.PINB2)
        self.PINB2_pullup.setObjectName(u"PINB2_pullup")
        self.PINB2_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINB2_highimp = QRadioButton(self.PINB2)
        self.PINB2_highimp.setObjectName(u"PINB2_highimp")
        self.PINB2_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINB2_highimp.setChecked(True)
        self.label_24 = QLabel(self.tab_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(480, 250, 47, 13))
        self.label_24.setFont(font)
        self.label_24.setFrameShape(QFrame.NoFrame)
        self.label_24.setTextFormat(Qt.AutoText)
        self.PORTB4 = QGroupBox(self.tab_2)
        self.PORTB4.setObjectName(u"PORTB4")
        self.PORTB4.setEnabled(True)
        self.PORTB4.setGeometry(QRect(680, 10, 131, 71))
        self.PORTB4_high = QRadioButton(self.PORTB4)
        self.PORTB4_high.setObjectName(u"PORTB4_high")
        self.PORTB4_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTB4_high.setChecked(True)
        self.PORTB4_low = QRadioButton(self.PORTB4)
        self.PORTB4_low.setObjectName(u"PORTB4_low")
        self.PORTB4_low.setGeometry(QRect(10, 50, 82, 17))
        self.PORTB2 = QGroupBox(self.tab_2)
        self.PORTB2.setObjectName(u"PORTB2")
        self.PORTB2.setEnabled(True)
        self.PORTB2.setGeometry(QRect(210, 150, 131, 71))
        self.PORTB2_high = QRadioButton(self.PORTB2)
        self.PORTB2_high.setObjectName(u"PORTB2_high")
        self.PORTB2_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTB2_high.setChecked(True)
        self.PORTB2_low = QRadioButton(self.PORTB2)
        self.PORTB2_low.setObjectName(u"PORTB2_low")
        self.PORTB2_low.setGeometry(QRect(10, 50, 82, 17))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.DDRC4 = QGroupBox(self.tab_4)
        self.DDRC4.setObjectName(u"DDRC4")
        self.DDRC4.setGeometry(QRect(550, 10, 131, 71))
        self.DDRC4.setFlat(False)
        self.DDRC4.setCheckable(False)
        self.DDRC4_output = QRadioButton(self.DDRC4)
        self.DDRC4_output.setObjectName(u"DDRC4_output")
        self.DDRC4_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRC4_output.setChecked(True)
        self.DDRC4_input = QRadioButton(self.DDRC4)
        self.DDRC4_input.setObjectName(u"DDRC4_input")
        self.DDRC4_input.setGeometry(QRect(10, 50, 82, 17))
        self.PORTC6 = QGroupBox(self.tab_4)
        self.PORTC6.setObjectName(u"PORTC6")
        self.PORTC6.setEnabled(True)
        self.PORTC6.setGeometry(QRect(680, 150, 131, 71))
        self.PORTC6_high = QRadioButton(self.PORTC6)
        self.PORTC6_high.setObjectName(u"PORTC6_high")
        self.PORTC6_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTC6_high.setChecked(True)
        self.PORTC6_low = QRadioButton(self.PORTC6)
        self.PORTC6_low.setObjectName(u"PORTC6_low")
        self.PORTC6_low.setGeometry(QRect(10, 50, 82, 17))
        self.PINC4 = QGroupBox(self.tab_4)
        self.PINC4.setObjectName(u"PINC4")
        self.PINC4.setEnabled(False)
        self.PINC4.setGeometry(QRect(810, 10, 131, 71))
        self.PINC4_pullup = QRadioButton(self.PINC4)
        self.PINC4_pullup.setObjectName(u"PINC4_pullup")
        self.PINC4_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINC4_highimp = QRadioButton(self.PINC4)
        self.PINC4_highimp.setObjectName(u"PINC4_highimp")
        self.PINC4_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINC4_highimp.setChecked(True)
        self.PINC6 = QGroupBox(self.tab_4)
        self.PINC6.setObjectName(u"PINC6")
        self.PINC6.setEnabled(False)
        self.PINC6.setGeometry(QRect(810, 150, 131, 71))
        self.PINC6_pullup = QRadioButton(self.PINC6)
        self.PINC6_pullup.setObjectName(u"PINC6_pullup")
        self.PINC6_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINC6_highimp = QRadioButton(self.PINC6)
        self.PINC6_highimp.setObjectName(u"PINC6_highimp")
        self.PINC6_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINC6_highimp.setChecked(True)
        self.PINC0 = QGroupBox(self.tab_4)
        self.PINC0.setObjectName(u"PINC0")
        self.PINC0.setEnabled(False)
        self.PINC0.setGeometry(QRect(340, 10, 131, 71))
        self.PINC0_pullup = QRadioButton(self.PINC0)
        self.PINC0_pullup.setObjectName(u"PINC0_pullup")
        self.PINC0_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINC0_highimp = QRadioButton(self.PINC0)
        self.PINC0_highimp.setObjectName(u"PINC0_highimp")
        self.PINC0_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINC0_highimp.setChecked(True)
        self.DDRC5 = QGroupBox(self.tab_4)
        self.DDRC5.setObjectName(u"DDRC5")
        self.DDRC5.setGeometry(QRect(550, 80, 131, 71))
        self.DDRC5.setFlat(False)
        self.DDRC5.setCheckable(False)
        self.DDRC5_output = QRadioButton(self.DDRC5)
        self.DDRC5_output.setObjectName(u"DDRC5_output")
        self.DDRC5_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRC5_output.setChecked(True)
        self.DDRC5_input = QRadioButton(self.DDRC5)
        self.DDRC5_input.setObjectName(u"DDRC5_input")
        self.DDRC5_input.setGeometry(QRect(10, 50, 82, 17))
        self.DDRC7 = QGroupBox(self.tab_4)
        self.DDRC7.setObjectName(u"DDRC7")
        self.DDRC7.setGeometry(QRect(550, 220, 131, 71))
        self.DDRC7.setFlat(False)
        self.DDRC7.setCheckable(False)
        self.DDRC7_output = QRadioButton(self.DDRC7)
        self.DDRC7_output.setObjectName(u"DDRC7_output")
        self.DDRC7_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRC7_output.setChecked(True)
        self.DDRC7_input = QRadioButton(self.DDRC7)
        self.DDRC7_input.setObjectName(u"DDRC7_input")
        self.DDRC7_input.setGeometry(QRect(10, 50, 82, 17))
        self.PINC5 = QGroupBox(self.tab_4)
        self.PINC5.setObjectName(u"PINC5")
        self.PINC5.setEnabled(False)
        self.PINC5.setGeometry(QRect(810, 80, 131, 71))
        self.PINC5_pullup = QRadioButton(self.PINC5)
        self.PINC5_pullup.setObjectName(u"PINC5_pullup")
        self.PINC5_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINC5_highimp = QRadioButton(self.PINC5)
        self.PINC5_highimp.setObjectName(u"PINC5_highimp")
        self.PINC5_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINC5_highimp.setChecked(True)
        self.PORTC7 = QGroupBox(self.tab_4)
        self.PORTC7.setObjectName(u"PORTC7")
        self.PORTC7.setEnabled(True)
        self.PORTC7.setGeometry(QRect(680, 220, 131, 71))
        self.PORTC7_high = QRadioButton(self.PORTC7)
        self.PORTC7_high.setObjectName(u"PORTC7_high")
        self.PORTC7_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTC7_high.setChecked(True)
        self.PORTC7_low = QRadioButton(self.PORTC7)
        self.PORTC7_low.setObjectName(u"PORTC7_low")
        self.PORTC7_low.setGeometry(QRect(10, 50, 82, 17))
        self.PINC1 = QGroupBox(self.tab_4)
        self.PINC1.setObjectName(u"PINC1")
        self.PINC1.setEnabled(False)
        self.PINC1.setGeometry(QRect(340, 80, 131, 71))
        self.PINC1_pullup = QRadioButton(self.PINC1)
        self.PINC1_pullup.setObjectName(u"PINC1_pullup")
        self.PINC1_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINC1_highimp = QRadioButton(self.PINC1)
        self.PINC1_highimp.setObjectName(u"PINC1_highimp")
        self.PINC1_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINC1_highimp.setChecked(True)
        self.DDRC3 = QGroupBox(self.tab_4)
        self.DDRC3.setObjectName(u"DDRC3")
        self.DDRC3.setGeometry(QRect(80, 220, 131, 71))
        self.DDRC3.setFlat(False)
        self.DDRC3.setCheckable(False)
        self.DDRC3_output = QRadioButton(self.DDRC3)
        self.DDRC3_output.setObjectName(u"DDRC3_output")
        self.DDRC3_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRC3_output.setChecked(True)
        self.DDRC3_input = QRadioButton(self.DDRC3)
        self.DDRC3_input.setObjectName(u"DDRC3_input")
        self.DDRC3_input.setGeometry(QRect(10, 50, 82, 17))
        self.label_25 = QLabel(self.tab_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(480, 180, 47, 13))
        self.label_25.setFont(font)
        self.label_25.setFrameShape(QFrame.NoFrame)
        self.label_25.setTextFormat(Qt.AutoText)
        self.PINC7 = QGroupBox(self.tab_4)
        self.PINC7.setObjectName(u"PINC7")
        self.PINC7.setEnabled(False)
        self.PINC7.setGeometry(QRect(810, 220, 131, 71))
        self.PINC7_pullup = QRadioButton(self.PINC7)
        self.PINC7_pullup.setObjectName(u"PINC7_pullup")
        self.PINC7_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINC7_highimp = QRadioButton(self.PINC7)
        self.PINC7_highimp.setObjectName(u"PINC7_highimp")
        self.PINC7_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINC7_highimp.setChecked(True)
        self.PINC3 = QGroupBox(self.tab_4)
        self.PINC3.setObjectName(u"PINC3")
        self.PINC3.setEnabled(False)
        self.PINC3.setGeometry(QRect(340, 220, 131, 71))
        self.PINC3_pullup = QRadioButton(self.PINC3)
        self.PINC3_pullup.setObjectName(u"PINC3_pullup")
        self.PINC3_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINC3_highimp = QRadioButton(self.PINC3)
        self.PINC3_highimp.setObjectName(u"PINC3_highimp")
        self.PINC3_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINC3_highimp.setChecked(True)
        self.label_26 = QLabel(self.tab_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(480, 110, 47, 13))
        self.label_26.setFont(font)
        self.label_26.setFrameShape(QFrame.NoFrame)
        self.label_26.setTextFormat(Qt.AutoText)
        self.label_27 = QLabel(self.tab_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 250, 47, 13))
        self.label_27.setFont(font)
        self.label_27.setFrameShape(QFrame.NoFrame)
        self.label_27.setTextFormat(Qt.AutoText)
        self.DDRC0 = QGroupBox(self.tab_4)
        self.DDRC0.setObjectName(u"DDRC0")
        self.DDRC0.setGeometry(QRect(80, 10, 131, 71))
        self.DDRC0.setFlat(False)
        self.DDRC0.setCheckable(False)
        self.DDRC0_output = QRadioButton(self.DDRC0)
        self.DDRC0_output.setObjectName(u"DDRC0_output")
        self.DDRC0_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRC0_output.setChecked(True)
        self.DDRC0_input = QRadioButton(self.DDRC0)
        self.DDRC0_input.setObjectName(u"DDRC0_input")
        self.DDRC0_input.setGeometry(QRect(10, 50, 82, 17))
        self.label_28 = QLabel(self.tab_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 110, 47, 13))
        self.label_28.setFont(font)
        self.label_28.setFrameShape(QFrame.NoFrame)
        self.label_28.setTextFormat(Qt.AutoText)
        self.PORTC0 = QGroupBox(self.tab_4)
        self.PORTC0.setObjectName(u"PORTC0")
        self.PORTC0.setEnabled(True)
        self.PORTC0.setGeometry(QRect(210, 10, 131, 71))
        self.PORTC0_high = QRadioButton(self.PORTC0)
        self.PORTC0_high.setObjectName(u"PORTC0_high")
        self.PORTC0_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTC0_high.setChecked(True)
        self.PORTC0_low = QRadioButton(self.PORTC0)
        self.PORTC0_low.setObjectName(u"PORTC0_low")
        self.PORTC0_low.setGeometry(QRect(10, 50, 82, 17))
        self.DDRC6 = QGroupBox(self.tab_4)
        self.DDRC6.setObjectName(u"DDRC6")
        self.DDRC6.setGeometry(QRect(550, 150, 131, 71))
        self.DDRC6.setFlat(False)
        self.DDRC6.setCheckable(False)
        self.DDRC6_output = QRadioButton(self.DDRC6)
        self.DDRC6_output.setObjectName(u"DDRC6_output")
        self.DDRC6_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRC6_output.setChecked(True)
        self.DDRC6_input = QRadioButton(self.DDRC6)
        self.DDRC6_input.setObjectName(u"DDRC6_input")
        self.DDRC6_input.setGeometry(QRect(10, 50, 82, 17))
        self.label_29 = QLabel(self.tab_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 180, 47, 13))
        self.label_29.setFont(font)
        self.label_29.setFrameShape(QFrame.NoFrame)
        self.label_29.setTextFormat(Qt.AutoText)
        self.DDRC1 = QGroupBox(self.tab_4)
        self.DDRC1.setObjectName(u"DDRC1")
        self.DDRC1.setGeometry(QRect(80, 80, 131, 71))
        self.DDRC1.setFlat(False)
        self.DDRC1.setCheckable(False)
        self.DDRC1_output = QRadioButton(self.DDRC1)
        self.DDRC1_output.setObjectName(u"DDRC1_output")
        self.DDRC1_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRC1_output.setChecked(True)
        self.DDRC1_input = QRadioButton(self.DDRC1)
        self.DDRC1_input.setObjectName(u"DDRC1_input")
        self.DDRC1_input.setGeometry(QRect(10, 50, 82, 17))
        self.PORTC1 = QGroupBox(self.tab_4)
        self.PORTC1.setObjectName(u"PORTC1")
        self.PORTC1.setEnabled(True)
        self.PORTC1.setGeometry(QRect(210, 80, 131, 71))
        self.PORTC1_high = QRadioButton(self.PORTC1)
        self.PORTC1_high.setObjectName(u"PORTC1_high")
        self.PORTC1_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTC1_high.setChecked(True)
        self.PORTC1_low = QRadioButton(self.PORTC1)
        self.PORTC1_low.setObjectName(u"PORTC1_low")
        self.PORTC1_low.setGeometry(QRect(10, 50, 82, 17))
        self.PORTC3 = QGroupBox(self.tab_4)
        self.PORTC3.setObjectName(u"PORTC3")
        self.PORTC3.setEnabled(True)
        self.PORTC3.setGeometry(QRect(210, 220, 131, 71))
        self.PORTC3_high = QRadioButton(self.PORTC3)
        self.PORTC3_high.setObjectName(u"PORTC3_high")
        self.PORTC3_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTC3_high.setChecked(True)
        self.PORTC3_low = QRadioButton(self.PORTC3)
        self.PORTC3_low.setObjectName(u"PORTC3_low")
        self.PORTC3_low.setGeometry(QRect(10, 50, 82, 17))
        self.DDRC2 = QGroupBox(self.tab_4)
        self.DDRC2.setObjectName(u"DDRC2")
        self.DDRC2.setGeometry(QRect(80, 150, 131, 71))
        self.DDRC2.setFlat(False)
        self.DDRC2.setCheckable(False)
        self.DDRC2_output = QRadioButton(self.DDRC2)
        self.DDRC2_output.setObjectName(u"DDRC2_output")
        self.DDRC2_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRC2_output.setChecked(True)
        self.DDRC2_input = QRadioButton(self.DDRC2)
        self.DDRC2_input.setObjectName(u"DDRC2_input")
        self.DDRC2_input.setGeometry(QRect(10, 50, 82, 17))
        self.label_30 = QLabel(self.tab_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(480, 40, 47, 13))
        self.label_30.setFont(font)
        self.label_30.setFrameShape(QFrame.NoFrame)
        self.label_30.setTextFormat(Qt.AutoText)
        self.label_31 = QLabel(self.tab_4)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 40, 47, 13))
        self.label_31.setFont(font)
        self.label_31.setFrameShape(QFrame.NoFrame)
        self.label_31.setTextFormat(Qt.AutoText)
        self.PORTC5 = QGroupBox(self.tab_4)
        self.PORTC5.setObjectName(u"PORTC5")
        self.PORTC5.setEnabled(True)
        self.PORTC5.setGeometry(QRect(680, 80, 131, 71))
        self.PORTC5_high = QRadioButton(self.PORTC5)
        self.PORTC5_high.setObjectName(u"PORTC5_high")
        self.PORTC5_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTC5_high.setChecked(True)
        self.PORTC5_low = QRadioButton(self.PORTC5)
        self.PORTC5_low.setObjectName(u"PORTC5_low")
        self.PORTC5_low.setGeometry(QRect(10, 50, 82, 17))
        self.PINC2 = QGroupBox(self.tab_4)
        self.PINC2.setObjectName(u"PINC2")
        self.PINC2.setEnabled(False)
        self.PINC2.setGeometry(QRect(340, 150, 131, 71))
        self.PINC2_pullup = QRadioButton(self.PINC2)
        self.PINC2_pullup.setObjectName(u"PINC2_pullup")
        self.PINC2_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PINC2_highimp = QRadioButton(self.PINC2)
        self.PINC2_highimp.setObjectName(u"PINC2_highimp")
        self.PINC2_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PINC2_highimp.setChecked(True)
        self.label_32 = QLabel(self.tab_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(480, 250, 47, 13))
        self.label_32.setFont(font)
        self.label_32.setFrameShape(QFrame.NoFrame)
        self.label_32.setTextFormat(Qt.AutoText)
        self.PORTC4 = QGroupBox(self.tab_4)
        self.PORTC4.setObjectName(u"PORTC4")
        self.PORTC4.setEnabled(True)
        self.PORTC4.setGeometry(QRect(680, 10, 131, 71))
        self.PORTC4_high = QRadioButton(self.PORTC4)
        self.PORTC4_high.setObjectName(u"PORTC4_high")
        self.PORTC4_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTC4_high.setChecked(True)
        self.PORTC4_low = QRadioButton(self.PORTC4)
        self.PORTC4_low.setObjectName(u"PORTC4_low")
        self.PORTC4_low.setGeometry(QRect(10, 50, 82, 17))
        self.PORTC2 = QGroupBox(self.tab_4)
        self.PORTC2.setObjectName(u"PORTC2")
        self.PORTC2.setEnabled(True)
        self.PORTC2.setGeometry(QRect(210, 150, 131, 71))
        self.PORTC2_high = QRadioButton(self.PORTC2)
        self.PORTC2_high.setObjectName(u"PORTC2_high")
        self.PORTC2_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTC2_high.setChecked(True)
        self.PORTC2_low = QRadioButton(self.PORTC2)
        self.PORTC2_low.setObjectName(u"PORTC2_low")
        self.PORTC2_low.setGeometry(QRect(10, 50, 82, 17))
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.DDRD4 = QGroupBox(self.tab_5)
        self.DDRD4.setObjectName(u"DDRD4")
        self.DDRD4.setGeometry(QRect(550, 10, 131, 71))
        self.DDRD4.setFlat(False)
        self.DDRD4.setCheckable(False)
        self.DDRD4_output = QRadioButton(self.DDRD4)
        self.DDRD4_output.setObjectName(u"DDRD4_output")
        self.DDRD4_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRD4_output.setChecked(True)
        self.DDRD4_input = QRadioButton(self.DDRD4)
        self.DDRD4_input.setObjectName(u"DDRD4_input")
        self.DDRD4_input.setGeometry(QRect(10, 50, 82, 17))
        self.PORTD6 = QGroupBox(self.tab_5)
        self.PORTD6.setObjectName(u"PORTD6")
        self.PORTD6.setEnabled(True)
        self.PORTD6.setGeometry(QRect(680, 150, 131, 71))
        self.PORTD6_high = QRadioButton(self.PORTD6)
        self.PORTD6_high.setObjectName(u"PORTD6_high")
        self.PORTD6_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTD6_high.setChecked(True)
        self.PORTD6_low = QRadioButton(self.PORTD6)
        self.PORTD6_low.setObjectName(u"PORTD6_low")
        self.PORTD6_low.setGeometry(QRect(10, 50, 82, 17))
        self.PIND4 = QGroupBox(self.tab_5)
        self.PIND4.setObjectName(u"PIND4")
        self.PIND4.setEnabled(False)
        self.PIND4.setGeometry(QRect(810, 10, 131, 71))
        self.PIND4_pullup = QRadioButton(self.PIND4)
        self.PIND4_pullup.setObjectName(u"PIND4_pullup")
        self.PIND4_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PIND4_highimp = QRadioButton(self.PIND4)
        self.PIND4_highimp.setObjectName(u"PIND4_highimp")
        self.PIND4_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PIND4_highimp.setChecked(True)
        self.PIND6 = QGroupBox(self.tab_5)
        self.PIND6.setObjectName(u"PIND6")
        self.PIND6.setEnabled(False)
        self.PIND6.setGeometry(QRect(810, 150, 131, 71))
        self.PIND6_pullup = QRadioButton(self.PIND6)
        self.PIND6_pullup.setObjectName(u"PIND6_pullup")
        self.PIND6_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PIND6_highimp = QRadioButton(self.PIND6)
        self.PIND6_highimp.setObjectName(u"PIND6_highimp")
        self.PIND6_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PIND6_highimp.setChecked(True)
        self.PIND0 = QGroupBox(self.tab_5)
        self.PIND0.setObjectName(u"PIND0")
        self.PIND0.setEnabled(False)
        self.PIND0.setGeometry(QRect(340, 10, 131, 71))
        self.PIND0_pullup = QRadioButton(self.PIND0)
        self.PIND0_pullup.setObjectName(u"PIND0_pullup")
        self.PIND0_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PIND0_highimp = QRadioButton(self.PIND0)
        self.PIND0_highimp.setObjectName(u"PIND0_highimp")
        self.PIND0_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PIND0_highimp.setChecked(True)
        self.DDRD5 = QGroupBox(self.tab_5)
        self.DDRD5.setObjectName(u"DDRD5")
        self.DDRD5.setGeometry(QRect(550, 80, 131, 71))
        self.DDRD5.setFlat(False)
        self.DDRD5.setCheckable(False)
        self.DDRD5_output = QRadioButton(self.DDRD5)
        self.DDRD5_output.setObjectName(u"DDRD5_output")
        self.DDRD5_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRD5_output.setChecked(True)
        self.DDRD5_input = QRadioButton(self.DDRD5)
        self.DDRD5_input.setObjectName(u"DDRD5_input")
        self.DDRD5_input.setGeometry(QRect(10, 50, 82, 17))
        self.DDRD7 = QGroupBox(self.tab_5)
        self.DDRD7.setObjectName(u"DDRD7")
        self.DDRD7.setGeometry(QRect(550, 220, 131, 71))
        self.DDRD7.setFlat(False)
        self.DDRD7.setCheckable(False)
        self.DDRD7_output = QRadioButton(self.DDRD7)
        self.DDRD7_output.setObjectName(u"DDRD7_output")
        self.DDRD7_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRD7_output.setChecked(True)
        self.DDRD7_input = QRadioButton(self.DDRD7)
        self.DDRD7_input.setObjectName(u"DDRD7_input")
        self.DDRD7_input.setGeometry(QRect(10, 50, 82, 17))
        self.PIND5 = QGroupBox(self.tab_5)
        self.PIND5.setObjectName(u"PIND5")
        self.PIND5.setEnabled(False)
        self.PIND5.setGeometry(QRect(810, 80, 131, 71))
        self.PIND5_pullup = QRadioButton(self.PIND5)
        self.PIND5_pullup.setObjectName(u"PIND5_pullup")
        self.PIND5_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PIND5_highimp = QRadioButton(self.PIND5)
        self.PIND5_highimp.setObjectName(u"PIND5_highimp")
        self.PIND5_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PIND5_highimp.setChecked(True)
        self.PORTD7 = QGroupBox(self.tab_5)
        self.PORTD7.setObjectName(u"PORTD7")
        self.PORTD7.setEnabled(True)
        self.PORTD7.setGeometry(QRect(680, 220, 131, 71))
        self.PORTD7_high = QRadioButton(self.PORTD7)
        self.PORTD7_high.setObjectName(u"PORTD7_high")
        self.PORTD7_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTD7_high.setChecked(True)
        self.PORTD7_low = QRadioButton(self.PORTD7)
        self.PORTD7_low.setObjectName(u"PORTD7_low")
        self.PORTD7_low.setGeometry(QRect(10, 50, 82, 17))
        self.PIND1 = QGroupBox(self.tab_5)
        self.PIND1.setObjectName(u"PIND1")
        self.PIND1.setEnabled(False)
        self.PIND1.setGeometry(QRect(340, 80, 131, 71))
        self.PIND1_pullup = QRadioButton(self.PIND1)
        self.PIND1_pullup.setObjectName(u"PIND1_pullup")
        self.PIND1_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PIND1_highimp = QRadioButton(self.PIND1)
        self.PIND1_highimp.setObjectName(u"PIND1_highimp")
        self.PIND1_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PIND1_highimp.setChecked(True)
        self.DDRD3 = QGroupBox(self.tab_5)
        self.DDRD3.setObjectName(u"DDRD3")
        self.DDRD3.setGeometry(QRect(80, 220, 131, 71))
        self.DDRD3.setFlat(False)
        self.DDRD3.setCheckable(False)
        self.DDRD3_output = QRadioButton(self.DDRD3)
        self.DDRD3_output.setObjectName(u"DDRD3_output")
        self.DDRD3_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRD3_output.setChecked(True)
        self.DDRD3_input = QRadioButton(self.DDRD3)
        self.DDRD3_input.setObjectName(u"DDRD3_input")
        self.DDRD3_input.setGeometry(QRect(10, 50, 82, 17))
        self.label_33 = QLabel(self.tab_5)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(480, 180, 47, 13))
        self.label_33.setFont(font)
        self.label_33.setFrameShape(QFrame.NoFrame)
        self.label_33.setTextFormat(Qt.AutoText)
        self.PIND7 = QGroupBox(self.tab_5)
        self.PIND7.setObjectName(u"PIND7")
        self.PIND7.setEnabled(False)
        self.PIND7.setGeometry(QRect(810, 220, 131, 71))
        self.PIND7_pullup = QRadioButton(self.PIND7)
        self.PIND7_pullup.setObjectName(u"PIND7_pullup")
        self.PIND7_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PIND7_highimp = QRadioButton(self.PIND7)
        self.PIND7_highimp.setObjectName(u"PIND7_highimp")
        self.PIND7_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PIND7_highimp.setChecked(True)
        self.PIND3 = QGroupBox(self.tab_5)
        self.PIND3.setObjectName(u"PIND3")
        self.PIND3.setEnabled(False)
        self.PIND3.setGeometry(QRect(340, 220, 131, 71))
        self.PIND3_pullup = QRadioButton(self.PIND3)
        self.PIND3_pullup.setObjectName(u"PIND3_pullup")
        self.PIND3_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PIND3_highimp = QRadioButton(self.PIND3)
        self.PIND3_highimp.setObjectName(u"PIND3_highimp")
        self.PIND3_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PIND3_highimp.setChecked(True)
        self.label_34 = QLabel(self.tab_5)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(480, 110, 47, 13))
        self.label_34.setFont(font)
        self.label_34.setFrameShape(QFrame.NoFrame)
        self.label_34.setTextFormat(Qt.AutoText)
        self.label_35 = QLabel(self.tab_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 250, 47, 13))
        self.label_35.setFont(font)
        self.label_35.setFrameShape(QFrame.NoFrame)
        self.label_35.setTextFormat(Qt.AutoText)
        self.DDRD0 = QGroupBox(self.tab_5)
        self.DDRD0.setObjectName(u"DDRD0")
        self.DDRD0.setGeometry(QRect(80, 10, 131, 71))
        self.DDRD0.setFlat(False)
        self.DDRD0.setCheckable(False)
        self.DDRD0_output = QRadioButton(self.DDRD0)
        self.DDRD0_output.setObjectName(u"DDRD0_output")
        self.DDRD0_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRD0_output.setChecked(True)
        self.DDRD0_input = QRadioButton(self.DDRD0)
        self.DDRD0_input.setObjectName(u"DDRD0_input")
        self.DDRD0_input.setGeometry(QRect(10, 50, 82, 17))
        self.label_36 = QLabel(self.tab_5)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(10, 110, 47, 13))
        self.label_36.setFont(font)
        self.label_36.setFrameShape(QFrame.NoFrame)
        self.label_36.setTextFormat(Qt.AutoText)
        self.PORTD0 = QGroupBox(self.tab_5)
        self.PORTD0.setObjectName(u"PORTD0")
        self.PORTD0.setEnabled(True)
        self.PORTD0.setGeometry(QRect(210, 10, 131, 71))
        self.PORTD0_high = QRadioButton(self.PORTD0)
        self.PORTD0_high.setObjectName(u"PORTD0_high")
        self.PORTD0_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTD0_high.setChecked(True)
        self.PORTD0_low = QRadioButton(self.PORTD0)
        self.PORTD0_low.setObjectName(u"PORTD0_low")
        self.PORTD0_low.setGeometry(QRect(10, 50, 82, 17))
        self.DDRD6 = QGroupBox(self.tab_5)
        self.DDRD6.setObjectName(u"DDRD6")
        self.DDRD6.setGeometry(QRect(550, 150, 131, 71))
        self.DDRD6.setFlat(False)
        self.DDRD6.setCheckable(False)
        self.DDRD6_output = QRadioButton(self.DDRD6)
        self.DDRD6_output.setObjectName(u"DDRD6_output")
        self.DDRD6_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRD6_output.setChecked(True)
        self.DDRD6_input = QRadioButton(self.DDRD6)
        self.DDRD6_input.setObjectName(u"DDRD6_input")
        self.DDRD6_input.setGeometry(QRect(10, 50, 82, 17))
        self.label_37 = QLabel(self.tab_5)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 180, 47, 13))
        self.label_37.setFont(font)
        self.label_37.setFrameShape(QFrame.NoFrame)
        self.label_37.setTextFormat(Qt.AutoText)
        self.DDRD1 = QGroupBox(self.tab_5)
        self.DDRD1.setObjectName(u"DDRD1")
        self.DDRD1.setGeometry(QRect(80, 80, 131, 71))
        self.DDRD1.setFlat(False)
        self.DDRD1.setCheckable(False)
        self.DDRD1_output = QRadioButton(self.DDRD1)
        self.DDRD1_output.setObjectName(u"DDRD1_output")
        self.DDRD1_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRD1_output.setChecked(True)
        self.DDRD1_input = QRadioButton(self.DDRD1)
        self.DDRD1_input.setObjectName(u"DDRD1_input")
        self.DDRD1_input.setGeometry(QRect(10, 50, 82, 17))
        self.PORTD1 = QGroupBox(self.tab_5)
        self.PORTD1.setObjectName(u"PORTD1")
        self.PORTD1.setEnabled(True)
        self.PORTD1.setGeometry(QRect(210, 80, 131, 71))
        self.PORTD1_high = QRadioButton(self.PORTD1)
        self.PORTD1_high.setObjectName(u"PORTD1_high")
        self.PORTD1_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTD1_high.setChecked(True)
        self.PORTD1_low = QRadioButton(self.PORTD1)
        self.PORTD1_low.setObjectName(u"PORTD1_low")
        self.PORTD1_low.setGeometry(QRect(10, 50, 82, 17))
        self.PORTD3 = QGroupBox(self.tab_5)
        self.PORTD3.setObjectName(u"PORTD3")
        self.PORTD3.setEnabled(True)
        self.PORTD3.setGeometry(QRect(210, 220, 131, 71))
        self.PORTD3_high = QRadioButton(self.PORTD3)
        self.PORTD3_high.setObjectName(u"PORTD3_high")
        self.PORTD3_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTD3_high.setChecked(True)
        self.PORTD3_low = QRadioButton(self.PORTD3)
        self.PORTD3_low.setObjectName(u"PORTD3_low")
        self.PORTD3_low.setGeometry(QRect(10, 50, 82, 17))
        self.DDRD2 = QGroupBox(self.tab_5)
        self.DDRD2.setObjectName(u"DDRD2")
        self.DDRD2.setGeometry(QRect(80, 150, 131, 71))
        self.DDRD2.setFlat(False)
        self.DDRD2.setCheckable(False)
        self.DDRD2_output = QRadioButton(self.DDRD2)
        self.DDRD2_output.setObjectName(u"DDRD2_output")
        self.DDRD2_output.setGeometry(QRect(10, 30, 82, 17))
        self.DDRD2_output.setChecked(True)
        self.DDRD2_input = QRadioButton(self.DDRD2)
        self.DDRD2_input.setObjectName(u"DDRD2_input")
        self.DDRD2_input.setGeometry(QRect(10, 50, 82, 17))
        self.label_38 = QLabel(self.tab_5)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(480, 40, 47, 13))
        self.label_38.setFont(font)
        self.label_38.setFrameShape(QFrame.NoFrame)
        self.label_38.setTextFormat(Qt.AutoText)
        self.label_39 = QLabel(self.tab_5)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 40, 47, 13))
        self.label_39.setFont(font)
        self.label_39.setFrameShape(QFrame.NoFrame)
        self.label_39.setTextFormat(Qt.AutoText)
        self.PORTD5 = QGroupBox(self.tab_5)
        self.PORTD5.setObjectName(u"PORTD5")
        self.PORTD5.setEnabled(True)
        self.PORTD5.setGeometry(QRect(680, 80, 131, 71))
        self.PORTD5_high = QRadioButton(self.PORTD5)
        self.PORTD5_high.setObjectName(u"PORTD5_high")
        self.PORTD5_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTD5_high.setChecked(True)
        self.PORTD5_low = QRadioButton(self.PORTD5)
        self.PORTD5_low.setObjectName(u"PORTD5_low")
        self.PORTD5_low.setGeometry(QRect(10, 50, 82, 17))
        self.PIND2 = QGroupBox(self.tab_5)
        self.PIND2.setObjectName(u"PIND2")
        self.PIND2.setEnabled(False)
        self.PIND2.setGeometry(QRect(340, 150, 131, 71))
        self.PIND2_pullup = QRadioButton(self.PIND2)
        self.PIND2_pullup.setObjectName(u"PIND2_pullup")
        self.PIND2_pullup.setGeometry(QRect(10, 30, 82, 17))
        self.PIND2_highimp = QRadioButton(self.PIND2)
        self.PIND2_highimp.setObjectName(u"PIND2_highimp")
        self.PIND2_highimp.setGeometry(QRect(10, 50, 82, 17))
        self.PIND2_highimp.setChecked(True)
        self.label_40 = QLabel(self.tab_5)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(480, 250, 47, 13))
        self.label_40.setFont(font)
        self.label_40.setFrameShape(QFrame.NoFrame)
        self.label_40.setTextFormat(Qt.AutoText)
        self.PORTD4 = QGroupBox(self.tab_5)
        self.PORTD4.setObjectName(u"PORTD4")
        self.PORTD4.setEnabled(True)
        self.PORTD4.setGeometry(QRect(680, 10, 131, 71))
        self.PORTD4_high = QRadioButton(self.PORTD4)
        self.PORTD4_high.setObjectName(u"PORTD4_high")
        self.PORTD4_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTD4_high.setChecked(True)
        self.PORTD4_low = QRadioButton(self.PORTD4)
        self.PORTD4_low.setObjectName(u"PORTD4_low")
        self.PORTD4_low.setGeometry(QRect(10, 50, 82, 17))
        self.PORTD2 = QGroupBox(self.tab_5)
        self.PORTD2.setObjectName(u"PORTD2")
        self.PORTD2.setEnabled(True)
        self.PORTD2.setGeometry(QRect(210, 150, 131, 71))
        self.PORTD2_high = QRadioButton(self.PORTD2)
        self.PORTD2_high.setObjectName(u"PORTD2_high")
        self.PORTD2_high.setGeometry(QRect(10, 30, 82, 17))
        self.PORTD2_high.setChecked(True)
        self.PORTD2_low = QRadioButton(self.PORTD2)
        self.PORTD2_low.setObjectName(u"PORTD2_low")
        self.PORTD2_low.setGeometry(QRect(10, 50, 82, 17))
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.lineEdit = QLineEdit(self.tab_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(240, 160, 281, 20))
        self.generate = QPushButton(self.tab_3)
        self.generate.setObjectName(u"generate")
        self.generate.setGeometry(QRect(530, 160, 61, 21))
        self.label_41 = QLabel(self.tab_3)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(240, 30, 421, 121))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_41.setFont(font1)
        self.label_41.setFrameShape(QFrame.NoFrame)
        self.label_41.setTextFormat(Qt.AutoText)
        self.label_41.setAlignment(Qt.AlignCenter)
        self.lineEdit_save = QLineEdit(self.tab_3)
        self.lineEdit_save.setObjectName(u"lineEdit_save")
        self.lineEdit_save.setGeometry(QRect(240, 190, 281, 20))
        self.save = QPushButton(self.tab_3)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(530, 190, 61, 21))
        self.lineEdit_load = QLineEdit(self.tab_3)
        self.lineEdit_load.setObjectName(u"lineEdit_load")
        self.lineEdit_load.setGeometry(QRect(240, 220, 281, 20))
        self.load = QPushButton(self.tab_3)
        self.load.setObjectName(u"load")
        self.load.setGeometry(QRect(530, 220, 61, 21))
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        
        '''''''''''''''''''''''''PORTA'''''''''''''''''''''''''''''''''''''
        QObject.connect(self.DDRA0_output,SIGNAL("clicked(bool)"),self.PINA0.setDisabled)
        QObject.connect(self.DDRA0_output,SIGNAL("clicked(bool)"),self.PORTA0.setEnabled)
        QObject.connect(self.DDRA0_input,SIGNAL("clicked(bool)"),self.PINA0.setEnabled)
        QObject.connect(self.DDRA0_input,SIGNAL("clicked(bool)"),self.PORTA0.setDisabled)
        QObject.connect(self.DDRA1_output,SIGNAL("clicked(bool)"),self.PINA1.setDisabled)
        QObject.connect(self.DDRA1_output,SIGNAL("clicked(bool)"),self.PORTA1.setEnabled)
        QObject.connect(self.DDRA1_input,SIGNAL("clicked(bool)"),self.PINA1.setEnabled)
        QObject.connect(self.DDRA1_input,SIGNAL("clicked(bool)"),self.PORTA1.setDisabled)
        QObject.connect(self.DDRA2_output,SIGNAL("clicked(bool)"),self.PINA2.setDisabled)
        QObject.connect(self.DDRA2_output,SIGNAL("clicked(bool)"),self.PORTA2.setEnabled)
        QObject.connect(self.DDRA2_input,SIGNAL("clicked(bool)"),self.PINA2.setEnabled)
        QObject.connect(self.DDRA2_input,SIGNAL("clicked(bool)"),self.PORTA2.setDisabled)
        QObject.connect(self.DDRA3_output,SIGNAL("clicked(bool)"),self.PINA3.setDisabled)
        QObject.connect(self.DDRA3_output,SIGNAL("clicked(bool)"),self.PORTA3.setEnabled)
        QObject.connect(self.DDRA3_input,SIGNAL("clicked(bool)"),self.PINA3.setEnabled)
        QObject.connect(self.DDRA3_input,SIGNAL("clicked(bool)"),self.PORTA3.setDisabled)
        QObject.connect(self.DDRA4_output,SIGNAL("clicked(bool)"),self.PINA4.setDisabled)
        QObject.connect(self.DDRA4_output,SIGNAL("clicked(bool)"),self.PORTA4.setEnabled)
        QObject.connect(self.DDRA4_input,SIGNAL("clicked(bool)"),self.PINA4.setEnabled)
        QObject.connect(self.DDRA4_input,SIGNAL("clicked(bool)"),self.PORTA4.setDisabled)
        QObject.connect(self.DDRA5_output,SIGNAL("clicked(bool)"),self.PINA5.setDisabled)
        QObject.connect(self.DDRA5_output,SIGNAL("clicked(bool)"),self.PORTA5.setEnabled)
        QObject.connect(self.DDRA5_input,SIGNAL("clicked(bool)"),self.PINA5.setEnabled)
        QObject.connect(self.DDRA5_input,SIGNAL("clicked(bool)"),self.PORTA5.setDisabled)
        QObject.connect(self.DDRA6_output,SIGNAL("clicked(bool)"),self.PINA6.setDisabled)
        QObject.connect(self.DDRA6_output,SIGNAL("clicked(bool)"),self.PORTA6.setEnabled)
        QObject.connect(self.DDRA6_input,SIGNAL("clicked(bool)"),self.PINA6.setEnabled)
        QObject.connect(self.DDRA6_input,SIGNAL("clicked(bool)"),self.PORTA6.setDisabled)
        QObject.connect(self.DDRA7_output,SIGNAL("clicked(bool)"),self.PINA7.setDisabled)
        QObject.connect(self.DDRA7_output,SIGNAL("clicked(bool)"),self.PORTA7.setEnabled)
        QObject.connect(self.DDRA7_input,SIGNAL("clicked(bool)"),self.PINA7.setEnabled)
        QObject.connect(self.DDRA7_input,SIGNAL("clicked(bool)"),self.PORTA7.setDisabled)
        '''''''''''''''''''''''''PORTB'''''''''''''''''''''''''''''''''''''
        QObject.connect(self.DDRB0_output,SIGNAL("clicked(bool)"),self.PINB0.setDisabled)
        QObject.connect(self.DDRB0_output,SIGNAL("clicked(bool)"),self.PORTB0.setEnabled)
        QObject.connect(self.DDRB0_input,SIGNAL("clicked(bool)"),self.PINB0.setEnabled)
        QObject.connect(self.DDRB0_input,SIGNAL("clicked(bool)"),self.PORTB0.setDisabled)
        QObject.connect(self.DDRB1_output,SIGNAL("clicked(bool)"),self.PINB1.setDisabled)
        QObject.connect(self.DDRB1_output,SIGNAL("clicked(bool)"),self.PORTB1.setEnabled)
        QObject.connect(self.DDRB1_input,SIGNAL("clicked(bool)"),self.PINB1.setEnabled)
        QObject.connect(self.DDRB1_input,SIGNAL("clicked(bool)"),self.PORTB1.setDisabled)
        QObject.connect(self.DDRB2_output,SIGNAL("clicked(bool)"),self.PINB2.setDisabled)
        QObject.connect(self.DDRB2_output,SIGNAL("clicked(bool)"),self.PORTB2.setEnabled)
        QObject.connect(self.DDRB2_input,SIGNAL("clicked(bool)"),self.PINB2.setEnabled)
        QObject.connect(self.DDRB2_input,SIGNAL("clicked(bool)"),self.PORTB2.setDisabled)
        QObject.connect(self.DDRB3_output,SIGNAL("clicked(bool)"),self.PINB3.setDisabled)
        QObject.connect(self.DDRB3_output,SIGNAL("clicked(bool)"),self.PORTB3.setEnabled)
        QObject.connect(self.DDRB3_input,SIGNAL("clicked(bool)"),self.PINB3.setEnabled)
        QObject.connect(self.DDRB3_input,SIGNAL("clicked(bool)"),self.PORTB3.setDisabled)
        QObject.connect(self.DDRB4_output,SIGNAL("clicked(bool)"),self.PINB4.setDisabled)
        QObject.connect(self.DDRB4_output,SIGNAL("clicked(bool)"),self.PORTB4.setEnabled)
        QObject.connect(self.DDRB4_input,SIGNAL("clicked(bool)"),self.PINB4.setEnabled)
        QObject.connect(self.DDRB4_input,SIGNAL("clicked(bool)"),self.PORTB4.setDisabled)
        QObject.connect(self.DDRB5_output,SIGNAL("clicked(bool)"),self.PINB5.setDisabled)
        QObject.connect(self.DDRB5_output,SIGNAL("clicked(bool)"),self.PORTB5.setEnabled)
        QObject.connect(self.DDRB5_input,SIGNAL("clicked(bool)"),self.PINB5.setEnabled)
        QObject.connect(self.DDRB5_input,SIGNAL("clicked(bool)"),self.PORTB5.setDisabled)
        QObject.connect(self.DDRB6_output,SIGNAL("clicked(bool)"),self.PINB6.setDisabled)
        QObject.connect(self.DDRB6_output,SIGNAL("clicked(bool)"),self.PORTB6.setEnabled)
        QObject.connect(self.DDRB6_input,SIGNAL("clicked(bool)"),self.PINB6.setEnabled)
        QObject.connect(self.DDRB6_input,SIGNAL("clicked(bool)"),self.PORTB6.setDisabled)
        QObject.connect(self.DDRB7_output,SIGNAL("clicked(bool)"),self.PINB7.setDisabled)
        QObject.connect(self.DDRB7_output,SIGNAL("clicked(bool)"),self.PORTB7.setEnabled)
        QObject.connect(self.DDRB7_input,SIGNAL("clicked(bool)"),self.PINB7.setEnabled)
        QObject.connect(self.DDRB7_input,SIGNAL("clicked(bool)"),self.PORTB7.setDisabled)
        '''''''''''''''''''''''''PORTC'''''''''''''''''''''''''''''''''''''
        QObject.connect(self.DDRC0_output,SIGNAL("clicked(bool)"),self.PINC0.setDisabled)
        QObject.connect(self.DDRC0_output,SIGNAL("clicked(bool)"),self.PORTC0.setEnabled)
        QObject.connect(self.DDRC0_input,SIGNAL("clicked(bool)"),self.PINC0.setEnabled)
        QObject.connect(self.DDRC0_input,SIGNAL("clicked(bool)"),self.PORTC0.setDisabled)
        QObject.connect(self.DDRC1_output,SIGNAL("clicked(bool)"),self.PINC1.setDisabled)
        QObject.connect(self.DDRC1_output,SIGNAL("clicked(bool)"),self.PORTC1.setEnabled)
        QObject.connect(self.DDRC1_input,SIGNAL("clicked(bool)"),self.PINC1.setEnabled)
        QObject.connect(self.DDRC1_input,SIGNAL("clicked(bool)"),self.PORTC1.setDisabled)
        QObject.connect(self.DDRC2_output,SIGNAL("clicked(bool)"),self.PINC2.setDisabled)
        QObject.connect(self.DDRC2_output,SIGNAL("clicked(bool)"),self.PORTC2.setEnabled)
        QObject.connect(self.DDRC2_input,SIGNAL("clicked(bool)"),self.PINC2.setEnabled)
        QObject.connect(self.DDRC2_input,SIGNAL("clicked(bool)"),self.PORTC2.setDisabled)
        QObject.connect(self.DDRC3_output,SIGNAL("clicked(bool)"),self.PINC3.setDisabled)
        QObject.connect(self.DDRC3_output,SIGNAL("clicked(bool)"),self.PORTC3.setEnabled)
        QObject.connect(self.DDRC3_input,SIGNAL("clicked(bool)"),self.PINC3.setEnabled)
        QObject.connect(self.DDRC3_input,SIGNAL("clicked(bool)"),self.PORTC3.setDisabled)
        QObject.connect(self.DDRC4_output,SIGNAL("clicked(bool)"),self.PINC4.setDisabled)
        QObject.connect(self.DDRC4_output,SIGNAL("clicked(bool)"),self.PORTC4.setEnabled)
        QObject.connect(self.DDRC4_input,SIGNAL("clicked(bool)"),self.PINC4.setEnabled)
        QObject.connect(self.DDRC4_input,SIGNAL("clicked(bool)"),self.PORTC4.setDisabled)
        QObject.connect(self.DDRC5_output,SIGNAL("clicked(bool)"),self.PINC5.setDisabled)
        QObject.connect(self.DDRC5_output,SIGNAL("clicked(bool)"),self.PORTC5.setEnabled)
        QObject.connect(self.DDRC5_input,SIGNAL("clicked(bool)"),self.PINC5.setEnabled)
        QObject.connect(self.DDRC5_input,SIGNAL("clicked(bool)"),self.PORTC5.setDisabled)
        QObject.connect(self.DDRC6_output,SIGNAL("clicked(bool)"),self.PINC6.setDisabled)
        QObject.connect(self.DDRC6_output,SIGNAL("clicked(bool)"),self.PORTC6.setEnabled)
        QObject.connect(self.DDRC6_input,SIGNAL("clicked(bool)"),self.PINC6.setEnabled)
        QObject.connect(self.DDRC6_input,SIGNAL("clicked(bool)"),self.PORTC6.setDisabled)
        QObject.connect(self.DDRC7_output,SIGNAL("clicked(bool)"),self.PINC7.setDisabled)
        QObject.connect(self.DDRC7_output,SIGNAL("clicked(bool)"),self.PORTC7.setEnabled)
        QObject.connect(self.DDRC7_input,SIGNAL("clicked(bool)"),self.PINC7.setEnabled)
        QObject.connect(self.DDRC7_input,SIGNAL("clicked(bool)"),self.PORTC7.setDisabled)
        '''''''''''''''''''''''''PORTD'''''''''''''''''''''''''''''''''''''
        QObject.connect(self.DDRD0_output,SIGNAL("clicked(bool)"),self.PIND0.setDisabled)
        QObject.connect(self.DDRD0_output,SIGNAL("clicked(bool)"),self.PORTD0.setEnabled)
        QObject.connect(self.DDRD0_input,SIGNAL("clicked(bool)"),self.PIND0.setEnabled)
        QObject.connect(self.DDRD0_input,SIGNAL("clicked(bool)"),self.PORTD0.setDisabled)
        QObject.connect(self.DDRD1_output,SIGNAL("clicked(bool)"),self.PIND1.setDisabled)
        QObject.connect(self.DDRD1_output,SIGNAL("clicked(bool)"),self.PORTD1.setEnabled)
        QObject.connect(self.DDRD1_input,SIGNAL("clicked(bool)"),self.PIND1.setEnabled)
        QObject.connect(self.DDRD1_input,SIGNAL("clicked(bool)"),self.PORTD1.setDisabled)
        QObject.connect(self.DDRD2_output,SIGNAL("clicked(bool)"),self.PIND2.setDisabled)
        QObject.connect(self.DDRD2_output,SIGNAL("clicked(bool)"),self.PORTD2.setEnabled)
        QObject.connect(self.DDRD2_input,SIGNAL("clicked(bool)"),self.PIND2.setEnabled)
        QObject.connect(self.DDRD2_input,SIGNAL("clicked(bool)"),self.PORTD2.setDisabled)
        QObject.connect(self.DDRD3_output,SIGNAL("clicked(bool)"),self.PIND3.setDisabled)
        QObject.connect(self.DDRD3_output,SIGNAL("clicked(bool)"),self.PORTD3.setEnabled)
        QObject.connect(self.DDRD3_input,SIGNAL("clicked(bool)"),self.PIND3.setEnabled)
        QObject.connect(self.DDRD3_input,SIGNAL("clicked(bool)"),self.PORTD3.setDisabled)
        QObject.connect(self.DDRD4_output,SIGNAL("clicked(bool)"),self.PIND4.setDisabled)
        QObject.connect(self.DDRD4_output,SIGNAL("clicked(bool)"),self.PORTD4.setEnabled)
        QObject.connect(self.DDRD4_input,SIGNAL("clicked(bool)"),self.PIND4.setEnabled)
        QObject.connect(self.DDRD4_input,SIGNAL("clicked(bool)"),self.PORTD4.setDisabled)
        QObject.connect(self.DDRD5_output,SIGNAL("clicked(bool)"),self.PIND5.setDisabled)
        QObject.connect(self.DDRD5_output,SIGNAL("clicked(bool)"),self.PORTD5.setEnabled)
        QObject.connect(self.DDRD5_input,SIGNAL("clicked(bool)"),self.PIND5.setEnabled)
        QObject.connect(self.DDRD5_input,SIGNAL("clicked(bool)"),self.PORTD5.setDisabled)
        QObject.connect(self.DDRD6_output,SIGNAL("clicked(bool)"),self.PIND6.setDisabled)
        QObject.connect(self.DDRD6_output,SIGNAL("clicked(bool)"),self.PORTD6.setEnabled)
        QObject.connect(self.DDRD6_input,SIGNAL("clicked(bool)"),self.PIND6.setEnabled)
        QObject.connect(self.DDRD6_input,SIGNAL("clicked(bool)"),self.PORTD6.setDisabled)
        QObject.connect(self.DDRD7_output,SIGNAL("clicked(bool)"),self.PIND7.setDisabled)
        QObject.connect(self.DDRD7_output,SIGNAL("clicked(bool)"),self.PORTD7.setEnabled)
        QObject.connect(self.DDRD7_input,SIGNAL("clicked(bool)"),self.PIND7.setEnabled)
        QObject.connect(self.DDRD7_input,SIGNAL("clicked(bool)"),self.PORTD7.setDisabled)
        
        self.generate.clicked.connect(self.generatefun)
        self.save.clicked.connect(self.savefun)
        self.load.clicked.connect(self.loadfun)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi
    def generatefun(self):
      Path = self.lineEdit.text() + r'\DIO_Cfg.h'
      File_Handler = open(Path ,'w')
      
      File_Handler.write("/**************************************************/\n")
      File_Handler.write("/**************** AVR32 CONFIG ********************/\n")
      File_Handler.write("/**************  Author: Karim Mourad **************/\n")
      File_Handler.write("/**************************************************/\n")
      File_Handler.write("\n")
      File_Handler.write("#ifndef _DIO_CONFIG_H\n")
      File_Handler.write("#define _DIO_CONFIG_H\n")
      File_Handler.write("\n")
      File_Handler.write("\n")
      '''''''''''''''''''''''''''''''PORTA'''''''''''''''''''''''''''''''''''''
      if self.DDRA0_output.isChecked() :
        if self.PORTA0_high.isChecked():
          File_Handler.write("#define     DIO_PINA_0_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINA_0_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINA0_pullup.isChecked():
          File_Handler.write("#define     DIO_PINA_0_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINA_0_MODE     DIO_INPUT_HIGH_IMP\n")
      
      if self.DDRA1_output.isChecked() :
        if self.PORTA1_high.isChecked():  
          File_Handler.write("#define     DIO_PINA_1_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINA_1_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINA1_pullup.isChecked():
          File_Handler.write("#define     DIO_PINA_1_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINA_1_MODE     DIO_INPUT_HIGH_IMP\n") 
      
      if self.DDRA2_output.isChecked() :
        if self.PORTA2_high.isChecked():
          File_Handler.write("#define     DIO_PINA_2_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINA_2_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINA2_pullup.isChecked():
          File_Handler.write("#define     DIO_PINA_2_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINA_2_MODE     DIO_INPUT_HIGH_IMP\n")
      
      if self.DDRA3_output.isChecked() :
        if self.PORTA3_high.isChecked():
          File_Handler.write("#define     DIO_PINA_3_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINA_3_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINA3_pullup.isChecked():
          File_Handler.write("#define     DIO_PINA_3_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINA_3_MODE     DIO_INPUT_HIGH_IMP\n") 
      
      if self.DDRA4_output.isChecked() :
        if self.PORTA4_high.isChecked():
          File_Handler.write("#define     DIO_PINA_4_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINA_4_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINA4_pullup.isChecked():
          File_Handler.write("#define     DIO_PINA_4_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINA_4_MODE     DIO_INPUT_HIGH_IMP\n")
      
      
      if self.DDRA5_output.isChecked() :
        if self.PORTA5_high.isChecked():
          File_Handler.write("#define     DIO_PINA_5_MODE     DIO_OUTPUT_HIGH\n")
        else : 
          File_Handler.write("#define     DIO_PINA_5_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINA5_pullup.isChecked():
          File_Handler.write("#define     DIO_PINA_5_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINA_5_MODE     DIO_INPUT_HIGH_IMP\n")
      
      
      if self.DDRA6_output.isChecked() :
        if self.PORTA6_high.isChecked():
          File_Handler.write("#define     DIO_PINA_6_MODE     DIO_OUTPUT_HIGH\n")
        else :  
          File_Handler.write("#define     DIO_PINA_6_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINA6_pullup.isChecked():
          File_Handler.write("#define     DIO_PINA_6_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINA_6_MODE     DIO_INPUT_HIGH_IMP\n")
      
      
      if self.DDRA7_output.isChecked() :
        if self.PORTA7_high.isChecked():
          File_Handler.write("#define     DIO_PINA_7_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINA_7_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINA7_pullup.isChecked():
          File_Handler.write("#define     DIO_PINA_7_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINA_7_MODE     DIO_INPUT_HIGH_IMP\n")
          
          
      File_Handler.write("\n")
      File_Handler.write("\n")
          
      '''''''''''''''''''''''''''''''PORTB'''''''''''''''''''''''''''''''''''''
      if self.DDRB0_output.isChecked() :
        if self.PORTB0_high.isChecked():
          File_Handler.write("#define     DIO_PINB_0_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINB_0_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINB0_pullup.isChecked():
          File_Handler.write("#define     DIO_PINB_0_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINB_0_MODE     DIO_INPUT_HIGH_IMP\n")
      
      if self.DDRB1_output.isChecked() :
        if self.PORTB1_high.isChecked():  
          File_Handler.write("#define     DIO_PINB_1_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINB_1_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINB1_pullup.isChecked():
          File_Handler.write("#define     DIO_PINB_1_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINB_1_MODE     DIO_INPUT_HIGH_IMP\n") 
      
      if self.DDRB2_output.isChecked() :
        if self.PORTB2_high.isChecked():
          File_Handler.write("#define     DIO_PINB_2_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINB_2_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINB2_pullup.isChecked():
          File_Handler.write("#define     DIO_PINB_2_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINB_2_MODE     DIO_INPUT_HIGH_IMP\n")
      
      if self.DDRB3_output.isChecked() :
        if self.PORTB3_high.isChecked():
          File_Handler.write("#define     DIO_PINB_3_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINB_3_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINB3_pullup.isChecked():
          File_Handler.write("#define     DIO_PINB_3_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINB_3_MODE     DIO_INPUT_HIGH_IMP\n") 
      
      if self.DDRB4_output.isChecked() :
        if self.PORTB4_high.isChecked():
          File_Handler.write("#define     DIO_PINB_4_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINB_4_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINB4_pullup.isChecked():
          File_Handler.write("#define     DIO_PINB_4_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINB_4_MODE     DIO_INPUT_HIGH_IMP\n")
      
      
      if self.DDRB5_output.isChecked() :
        if self.PORTB5_high.isChecked():
          File_Handler.write("#define     DIO_PINB_5_MODE     DIO_OUTPUT_HIGH\n")
        else : 
          File_Handler.write("#define     DIO_PINB_5_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINB5_pullup.isChecked():
          File_Handler.write("#define     DIO_PINB_5_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINB_5_MODE     DIO_INPUT_HIGH_IMP\n")
      
      
      if self.DDRB6_output.isChecked() :
        if self.PORTB6_high.isChecked():
          File_Handler.write("#define     DIO_PINB_6_MODE     DIO_OUTPUT_HIGH\n")
        else :  
          File_Handler.write("#define     DIO_PINB_6_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINB6_pullup.isChecked():
          File_Handler.write("#define     DIO_PINB_6_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINB_6_MODE     DIO_INPUT_HIGH_IMP\n")
      
      
      if self.DDRB7_output.isChecked() :
        if self.PORTB7_high.isChecked():
          File_Handler.write("#define     DIO_PINB_7_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINB_7_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINB7_pullup.isChecked():
          File_Handler.write("#define     DIO_PINB_7_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINB_7_MODE     DIO_INPUT_HIGH_IMP\n")
          
          
      File_Handler.write("\n")
      File_Handler.write("\n")
      '''''''''''''''''''''''''''''''PORTC'''''''''''''''''''''''''''''''''''''
      if self.DDRC0_output.isChecked() :
        if self.PORTC0_high.isChecked():
          File_Handler.write("#define     DIO_PINC_0_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINC_0_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINC0_pullup.isChecked():
          File_Handler.write("#define     DIO_PINC_0_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINC_0_MODE     DIO_INPUT_HIGH_IMP\n")
      
      if self.DDRC1_output.isChecked() :
        if self.PORTC1_high.isChecked():  
          File_Handler.write("#define     DIO_PINC_1_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINC_1_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINC1_pullup.isChecked():
          File_Handler.write("#define     DIO_PINC_1_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINC_1_MODE     DIO_INPUT_HIGH_IMP\n") 
      
      if self.DDRC2_output.isChecked() :
        if self.PORTC2_high.isChecked():
          File_Handler.write("#define     DIO_PINC_2_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINC_2_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINC2_pullup.isChecked():
          File_Handler.write("#define     DIO_PINC_2_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINC_2_MODE     DIO_INPUT_HIGH_IMP\n")
      
      if self.DDRC3_output.isChecked() :
        if self.PORTC3_high.isChecked():
          File_Handler.write("#define     DIO_PINC_3_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINC_3_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINC3_pullup.isChecked():
          File_Handler.write("#define     DIO_PINC_3_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINC_3_MODE     DIO_INPUT_HIGH_IMP\n") 
      
      if self.DDRC4_output.isChecked() :
        if self.PORTC4_high.isChecked():
          File_Handler.write("#define     DIO_PINC_4_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINC_4_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINC4_pullup.isChecked():
          File_Handler.write("#define     DIO_PINC_4_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINC_4_MODE     DIO_INPUT_HIGH_IMP\n")
      
      
      if self.DDRC5_output.isChecked() :
        if self.PORTC5_high.isChecked():
          File_Handler.write("#define     DIO_PINC_5_MODE     DIO_OUTPUT_HIGH\n")
        else : 
          File_Handler.write("#define     DIO_PINC_5_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINC5_pullup.isChecked():
          File_Handler.write("#define     DIO_PINC_5_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINC_5_MODE     DIO_INPUT_HIGH_IMP\n")
      
      
      if self.DDRC6_output.isChecked() :
        if self.PORTC6_high.isChecked():
          File_Handler.write("#define     DIO_PINC_6_MODE     DIO_OUTPUT_HIGH\n")
        else :  
          File_Handler.write("#define     DIO_PINC_6_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINC6_pullup.isChecked():
          File_Handler.write("#define     DIO_PINC_6_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINC_6_MODE     DIO_INPUT_HIGH_IMP\n")
      
      
      if self.DDRC7_output.isChecked() :
        if self.PORTC7_high.isChecked():
          File_Handler.write("#define     DIO_PINC_7_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PINC_7_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PINC7_pullup.isChecked():
          File_Handler.write("#define     DIO_PINC_7_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PINC_7_MODE     DIO_INPUT_HIGH_IMP\n")
          
          
          
      File_Handler.write("\n")    
      File_Handler.write("\n")    
      '''''''''''''''''''''''''''''''PORTD'''''''''''''''''''''''''''''''''''''
      if self.DDRD0_output.isChecked() :
        if self.PORTD0_high.isChecked():
          File_Handler.write("#define     DIO_PIND_0_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PIND_0_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PIND0_pullup.isChecked():
          File_Handler.write("#define     DIO_PIND_0_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PIND_0_MODE     DIO_INPUT_HIGH_IMP\n")
      
      if self.DDRD1_output.isChecked() :
        if self.PORTD1_high.isChecked():  
          File_Handler.write("#define     DIO_PIND_1_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PIND_1_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PIND1_pullup.isChecked():
          File_Handler.write("#define     DIO_PIND_1_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PIND_1_MODE     DIO_INPUT_HIGH_IMP\n") 
      
      if self.DDRD2_output.isChecked() :
        if self.PORTD2_high.isChecked():
          File_Handler.write("#define     DIO_PIND_2_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PIND_2_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PIND2_pullup.isChecked():
          File_Handler.write("#define     DIO_PIND_2_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PIND_2_MODE     DIO_INPUT_HIGH_IMP\n")
      
      if self.DDRD3_output.isChecked() :
        if self.PORTD3_high.isChecked():
          File_Handler.write("#define     DIO_PIND_3_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PIND_3_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PIND3_pullup.isChecked():
          File_Handler.write("#define     DIO_PIND_3_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PIND_3_MODE     DIO_INPUT_HIGH_IMP\n") 
      
      if self.DDRD4_output.isChecked() :
        if self.PORTD4_high.isChecked():
          File_Handler.write("#define     DIO_PIND_4_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PIND_4_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PIND4_pullup.isChecked():
          File_Handler.write("#define     DIO_PIND_4_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PIND_4_MODE     DIO_INPUT_HIGH_IMP\n")
      
      
      if self.DDRD5_output.isChecked() :
        if self.PORTD5_high.isChecked():
          File_Handler.write("#define     DIO_PIND_5_MODE     DIO_OUTPUT_HIGH\n")
        else : 
          File_Handler.write("#define     DIO_PIND_5_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PIND5_pullup.isChecked():
          File_Handler.write("#define     DIO_PIND_5_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PIND_5_MODE     DIO_INPUT_HIGH_IMP\n")
      
      
      if self.DDRD6_output.isChecked() :
        if self.PORTD6_high.isChecked():
          File_Handler.write("#define     DIO_PIND_6_MODE     DIO_OUTPUT_HIGH\n")
        else :  
          File_Handler.write("#define     DIO_PIND_6_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PIND6_pullup.isChecked():
          File_Handler.write("#define     DIO_PIND_6_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PIND_6_MODE     DIO_INPUT_HIGH_IMP\n")
      
      
      if self.DDRD7_output.isChecked() :
        if self.PORTD7_high.isChecked():
          File_Handler.write("#define     DIO_PIND_7_MODE     DIO_OUTPUT_HIGH\n")
        else :
          File_Handler.write("#define     DIO_PIND_7_MODE     DIO_OUTPUT_LOW\n")
      else : 
        if self.PIND7_pullup.isChecked():
          File_Handler.write("#define     DIO_PIND_7_MODE     DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define     DIO_PIND_7_MODE     DIO_INPUT_HIGH_IMP\n")
        
        
      File_Handler.write("\n")
      File_Handler.write("\n")
      File_Handler.write("#endif /*_DIO_CONFIG_H*/\n")
    
    def savefun(self):
      DIO = ET.Element("DIO")
      '''''''''''''''''''''''''''''''PORTA'''''''''''''''''''''''''''''''''''''
      PORTA = ET.Element("PORTA")
      PORTA_PIN0 = ET.Element("PIN0")
      PORTA_PIN1 = ET.Element("PIN1")
      PORTA_PIN2 = ET.Element("PIN2")
      PORTA_PIN3 = ET.Element("PIN3")
      PORTA_PIN4 = ET.Element("PIN4")
      PORTA_PIN5 = ET.Element("PIN5")
      PORTA_PIN6 = ET.Element("PIN6")
      PORTA_PIN7 = ET.Element("PIN7")
      
      PORTA_PIN0_DIR = ET.Element("DIR")
      PORTA_PIN0_CONFIG = ET.Element("CONFIG")
      PORTA_PIN1_DIR = ET.Element("DIR")
      PORTA_PIN1_CONFIG = ET.Element("CONFIG")
      PORTA_PIN2_DIR = ET.Element("DIR")
      PORTA_PIN2_CONFIG = ET.Element("CONFIG")
      PORTA_PIN3_DIR = ET.Element("DIR")
      PORTA_PIN3_CONFIG = ET.Element("CONFIG")
      PORTA_PIN4_DIR = ET.Element("DIR")
      PORTA_PIN4_CONFIG = ET.Element("CONFIG")
      PORTA_PIN5_DIR = ET.Element("DIR")
      PORTA_PIN5_CONFIG = ET.Element("CONFIG")
      PORTA_PIN6_DIR = ET.Element("DIR")
      PORTA_PIN6_CONFIG = ET.Element("CONFIG")
      PORTA_PIN7_DIR = ET.Element("DIR")
      PORTA_PIN7_CONFIG = ET.Element("CONFIG")
      
      if self.DDRA0_input.isChecked():
        PORTA_PIN0_DIR.text = 'INPUT'
        if self.PINA0_pullup.isChecked():
          PORTA_PIN0_CONFIG.text = 'PullUP'
        else:
          PORTA_PIN0_CONFIG.text = 'High-Imp'
      else:
        PORTA_PIN0_DIR.text = 'OUTPUT'
        if self.PORTA0_high.isChecked():
          PORTA_PIN0_CONFIG.text = 'High'
        else:
          PORTA_PIN0_CONFIG.text = 'Low'
          
      if self.DDRA1_input.isChecked():
        PORTA_PIN1_DIR.text = 'INPUT'
        if self.PINA1_pullup.isChecked():
          PORTA_PIN1_CONFIG.text = 'PullUP'
        else:
          PORTA_PIN1_CONFIG.text = 'High-Imp'
      else:
        PORTA_PIN1_DIR.text = 'OUTPUT'
        if self.PORTA1_high.isChecked():
          PORTA_PIN1_CONFIG.text = 'High'
        else:
          PORTA_PIN1_CONFIG.text = 'Low'
          
      if self.DDRA2_input.isChecked():
        PORTA_PIN2_DIR.text = 'INPUT'
        if self.PINA2_pullup.isChecked():
          PORTA_PIN2_CONFIG.text = 'PullUP'
        else:
          PORTA_PIN2_CONFIG.text = 'High-Imp'
      else:
        PORTA_PIN2_DIR.text = 'OUTPUT'
        if self.PORTA2_high.isChecked():
          PORTA_PIN2_CONFIG.text = 'High'
        else:
          PORTA_PIN2_CONFIG.text = 'Low'
          
      if self.DDRA3_input.isChecked():
        PORTA_PIN3_DIR.text = 'INPUT'
        if self.PINA3_pullup.isChecked():
          PORTA_PIN3_CONFIG.text = 'PullUP'
        else:
          PORTA_PIN3_CONFIG.text = 'High-Imp'
      else:
        PORTA_PIN3_DIR.text = 'OUTPUT'
        if self.PORTA3_high.isChecked():
          PORTA_PIN3_CONFIG.text = 'High'
        else:
          PORTA_PIN3_CONFIG.text = 'Low'
          
      if self.DDRA4_input.isChecked():
        PORTA_PIN4_DIR.text = 'INPUT'
        if self.PINA4_pullup.isChecked():
          PORTA_PIN4_CONFIG.text = 'PullUP'
        else:
          PORTA_PIN4_CONFIG.text = 'High-Imp'
      else:
        PORTA_PIN4_DIR.text = 'OUTPUT'
        if self.PORTA4_high.isChecked():
          PORTA_PIN4_CONFIG.text = 'High'
        else:
          PORTA_PIN4_CONFIG.text = 'Low'
          
      if self.DDRA5_input.isChecked():
        PORTA_PIN5_DIR.text = 'INPUT'
        if self.PINA5_pullup.isChecked():
          PORTA_PIN5_CONFIG.text = 'PullUP'
        else:
          PORTA_PIN5_CONFIG.text = 'High-Imp'
      else:
        PORTA_PIN5_DIR.text = 'OUTPUT'
        if self.PORTA5_high.isChecked():
          PORTA_PIN5_CONFIG.text = 'High'
        else:
          PORTA_PIN5_CONFIG.text = 'Low'
          
      if self.DDRA6_input.isChecked():
        PORTA_PIN6_DIR.text = 'INPUT'
        if self.PINA6_pullup.isChecked():
          PORTA_PIN6_CONFIG.text = 'PullUP'
        else:
          PORTA_PIN6_CONFIG.text = 'High-Imp'
      else:
        PORTA_PIN6_DIR.text = 'OUTPUT'
        if self.PORTA6_high.isChecked():
          PORTA_PIN6_CONFIG.text = 'High'
        else:
          PORTA_PIN6_CONFIG.text = 'Low'
          
      if self.DDRA7_input.isChecked():
        PORTA_PIN7_DIR.text = 'INPUT'
        if self.PINA7_pullup.isChecked():
          PORTA_PIN7_CONFIG.text = 'PullUP'
        else:
          PORTA_PIN7_CONFIG.text = 'High-Imp'
      else:
        PORTA_PIN7_DIR.text = 'OUTPUT'
        if self.PORTA7_high.isChecked():
          PORTA_PIN7_CONFIG.text = 'High'
        else:
          PORTA_PIN7_CONFIG.text = 'Low'
          
      DIO.append(PORTA)
        
      PORTA.append(PORTA_PIN0)
      PORTA_PIN0.append(PORTA_PIN0_DIR)
      PORTA_PIN0.append(PORTA_PIN0_CONFIG)
      PORTA.append(PORTA_PIN1)
      PORTA_PIN1.append(PORTA_PIN1_DIR)
      PORTA_PIN1.append(PORTA_PIN1_CONFIG)
      PORTA.append(PORTA_PIN2)
      PORTA_PIN2.append(PORTA_PIN2_DIR)
      PORTA_PIN2.append(PORTA_PIN2_CONFIG)
      PORTA.append(PORTA_PIN3)
      PORTA_PIN3.append(PORTA_PIN3_DIR)
      PORTA_PIN3.append(PORTA_PIN3_CONFIG)
      PORTA.append(PORTA_PIN4)
      PORTA_PIN4.append(PORTA_PIN4_DIR)
      PORTA_PIN4.append(PORTA_PIN4_CONFIG)
      PORTA.append(PORTA_PIN5)
      PORTA_PIN5.append(PORTA_PIN5_DIR)
      PORTA_PIN5.append(PORTA_PIN5_CONFIG)
      PORTA.append(PORTA_PIN6)
      PORTA_PIN6.append(PORTA_PIN6_DIR)
      PORTA_PIN6.append(PORTA_PIN6_CONFIG)
      PORTA.append(PORTA_PIN7)
      PORTA_PIN7.append(PORTA_PIN7_DIR)
      PORTA_PIN7.append(PORTA_PIN7_CONFIG)
      
      '''''''''''''''''''''''''''''''PORTB'''''''''''''''''''''''''''''''''''''
      PORTB = ET.Element("PORTB")
      PORTB_PIN0 = ET.Element("PIN0")
      PORTB_PIN1 = ET.Element("PIN1")
      PORTB_PIN2 = ET.Element("PIN2")
      PORTB_PIN3 = ET.Element("PIN3")
      PORTB_PIN4 = ET.Element("PIN4")
      PORTB_PIN5 = ET.Element("PIN5")
      PORTB_PIN6 = ET.Element("PIN6")
      PORTB_PIN7 = ET.Element("PIN7")
          
      PORTB_PIN0_DIR = ET.Element("DIR")
      PORTB_PIN0_CONFIG = ET.Element("CONFIG")
      PORTB_PIN1_DIR = ET.Element("DIR")
      PORTB_PIN1_CONFIG = ET.Element("CONFIG")
      PORTB_PIN2_DIR = ET.Element("DIR")
      PORTB_PIN2_CONFIG = ET.Element("CONFIG")
      PORTB_PIN3_DIR = ET.Element("DIR")
      PORTB_PIN3_CONFIG = ET.Element("CONFIG")
      PORTB_PIN4_DIR = ET.Element("DIR")
      PORTB_PIN4_CONFIG = ET.Element("CONFIG")
      PORTB_PIN5_DIR = ET.Element("DIR")
      PORTB_PIN5_CONFIG = ET.Element("CONFIG")
      PORTB_PIN6_DIR = ET.Element("DIR")
      PORTB_PIN6_CONFIG = ET.Element("CONFIG")
      PORTB_PIN7_DIR = ET.Element("DIR")
      PORTB_PIN7_CONFIG = ET.Element("CONFIG")
      
      if self.DDRB0_input.isChecked():
        PORTB_PIN0_DIR.text = 'INPUT'
        if self.PINB0_pullup.isChecked():
          PORTB_PIN0_CONFIG.text = 'PullUP'
        else:
          PORTB_PIN0_CONFIG.text = 'High-Imp'
      else:
        PORTB_PIN0_DIR.text = 'OUTPUT'
        if self.PORTB0_high.isChecked():
          PORTB_PIN0_CONFIG.text = 'High'
        else:
          PORTB_PIN0_CONFIG.text = 'Low'
          
      if self.DDRB1_input.isChecked():
        PORTB_PIN1_DIR.text = 'INPUT'
        if self.PINB1_pullup.isChecked():
          PORTB_PIN1_CONFIG.text = 'PullUP'
        else:
          PORTB_PIN1_CONFIG.text = 'High-Imp'
      else:
        PORTB_PIN1_DIR.text = 'OUTPUT'
        if self.PORTB1_high.isChecked():
          PORTB_PIN1_CONFIG.text = 'High'
        else:
          PORTB_PIN1_CONFIG.text = 'Low'
          
      if self.DDRB2_input.isChecked():
        PORTB_PIN2_DIR.text = 'INPUT'
        if self.PINB2_pullup.isChecked():
          PORTB_PIN2_CONFIG.text = 'PullUP'
        else:
          PORTB_PIN2_CONFIG.text = 'High-Imp'
      else:
        PORTB_PIN2_DIR.text = 'OUTPUT'
        if self.PORTB2_high.isChecked():
          PORTB_PIN2_CONFIG.text = 'High'
        else:
          PORTB_PIN2_CONFIG.text = 'Low'
          
      if self.DDRB3_input.isChecked():
        PORTB_PIN3_DIR.text = 'INPUT'
        if self.PINB3_pullup.isChecked():
          PORTB_PIN3_CONFIG.text = 'PullUP'
        else:
          PORTB_PIN3_CONFIG.text = 'High-Imp'
      else:
        PORTB_PIN3_DIR.text = 'OUTPUT'
        if self.PORTB3_high.isChecked():
          PORTB_PIN3_CONFIG.text = 'High'
        else:
          PORTB_PIN3_CONFIG.text = 'Low'
          
      if self.DDRB4_input.isChecked():
        PORTB_PIN4_DIR.text = 'INPUT'
        if self.PINB4_pullup.isChecked():
          PORTB_PIN4_CONFIG.text = 'PullUP'
        else:
          PORTB_PIN4_CONFIG.text = 'High-Imp'
      else:
        PORTB_PIN4_DIR.text = 'OUTPUT'
        if self.PORTB4_high.isChecked():
          PORTB_PIN4_CONFIG.text = 'High'
        else:
          PORTB_PIN4_CONFIG.text = 'Low'
          
      if self.DDRB5_input.isChecked():
        PORTB_PIN5_DIR.text = 'INPUT'
        if self.PINB5_pullup.isChecked():
          PORTB_PIN5_CONFIG.text = 'PullUP'
        else:
          PORTB_PIN5_CONFIG.text = 'High-Imp'
      else:
        PORTB_PIN5_DIR.text = 'OUTPUT'
        if self.PORTB5_high.isChecked():
          PORTB_PIN5_CONFIG.text = 'High'
        else:
          PORTB_PIN5_CONFIG.text = 'Low'
          
      if self.DDRB6_input.isChecked():
        PORTB_PIN6_DIR.text = 'INPUT'
        if self.PINB6_pullup.isChecked():
          PORTB_PIN6_CONFIG.text = 'PullUP'
        else:
          PORTB_PIN6_CONFIG.text = 'High-Imp'
      else:
        PORTB_PIN6_DIR.text = 'OUTPUT'
        if self.PORTB6_high.isChecked():
          PORTB_PIN6_CONFIG.text = 'High'
        else:
          PORTB_PIN6_CONFIG.text = 'Low'
          
      if self.DDRB7_input.isChecked():
        PORTB_PIN7_DIR.text = 'INPUT'
        if self.PINB7_pullup.isChecked():
          PORTB_PIN7_CONFIG.text = 'PullUP'
        else:
          PORTB_PIN7_CONFIG.text = 'High-Imp'
      else:
        PORTB_PIN7_DIR.text = 'OUTPUT'
        if self.PORTB7_high.isChecked():
          PORTB_PIN7_CONFIG.text = 'High'
        else:
          PORTB_PIN7_CONFIG.text = 'Low'
          
      DIO.append(PORTB)
        
      PORTB.append(PORTB_PIN0)
      PORTB_PIN0.append(PORTB_PIN0_DIR)
      PORTB_PIN0.append(PORTB_PIN0_CONFIG)
      PORTB.append(PORTB_PIN1)
      PORTB_PIN1.append(PORTB_PIN1_DIR)
      PORTB_PIN1.append(PORTB_PIN1_CONFIG)
      PORTB.append(PORTB_PIN2)
      PORTB_PIN2.append(PORTB_PIN2_DIR)
      PORTB_PIN2.append(PORTB_PIN2_CONFIG)
      PORTB.append(PORTB_PIN3)
      PORTB_PIN3.append(PORTB_PIN3_DIR)
      PORTB_PIN3.append(PORTB_PIN3_CONFIG)
      PORTB.append(PORTB_PIN4)
      PORTB_PIN4.append(PORTB_PIN4_DIR)
      PORTB_PIN4.append(PORTB_PIN4_CONFIG)
      PORTB.append(PORTB_PIN5)
      PORTB_PIN5.append(PORTB_PIN5_DIR)
      PORTB_PIN5.append(PORTB_PIN5_CONFIG)
      PORTB.append(PORTB_PIN6)
      PORTB_PIN6.append(PORTB_PIN6_DIR)
      PORTB_PIN6.append(PORTB_PIN6_CONFIG)
      PORTB.append(PORTB_PIN7)
      PORTB_PIN7.append(PORTB_PIN7_DIR)
      PORTB_PIN7.append(PORTB_PIN7_CONFIG)
      
      '''''''''''''''''''''''''''''''PORTC'''''''''''''''''''''''''''''''''''''
      PORTC = ET.Element("PORTC")
      PORTC_PIN0 = ET.Element("PIN0")
      PORTC_PIN1 = ET.Element("PIN1")
      PORTC_PIN2 = ET.Element("PIN2")
      PORTC_PIN3 = ET.Element("PIN3")
      PORTC_PIN4 = ET.Element("PIN4")
      PORTC_PIN5 = ET.Element("PIN5")
      PORTC_PIN6 = ET.Element("PIN6")
      PORTC_PIN7 = ET.Element("PIN7")
          
      PORTC_PIN0_DIR = ET.Element("DIR")
      PORTC_PIN0_CONFIG = ET.Element("CONFIG")
      PORTC_PIN1_DIR = ET.Element("DIR")
      PORTC_PIN1_CONFIG = ET.Element("CONFIG")
      PORTC_PIN2_DIR = ET.Element("DIR")
      PORTC_PIN2_CONFIG = ET.Element("CONFIG")
      PORTC_PIN3_DIR = ET.Element("DIR")
      PORTC_PIN3_CONFIG = ET.Element("CONFIG")
      PORTC_PIN4_DIR = ET.Element("DIR")
      PORTC_PIN4_CONFIG = ET.Element("CONFIG")
      PORTC_PIN5_DIR = ET.Element("DIR")
      PORTC_PIN5_CONFIG = ET.Element("CONFIG")
      PORTC_PIN6_DIR = ET.Element("DIR")
      PORTC_PIN6_CONFIG = ET.Element("CONFIG")
      PORTC_PIN7_DIR = ET.Element("DIR")
      PORTC_PIN7_CONFIG = ET.Element("CONFIG")
      
      if self.DDRC0_input.isChecked():
        PORTC_PIN0_DIR.text = 'INPUT'
        if self.PINC0_pullup.isChecked():
          PORTC_PIN0_CONFIG.text = 'PullUP'
        else:
          PORTC_PIN0_CONFIG.text = 'High-Imp'
      else:
        PORTC_PIN0_DIR.text = 'OUTPUT'
        if self.PORTC0_high.isChecked():
          PORTC_PIN0_CONFIG.text = 'High'
        else:
          PORTC_PIN0_CONFIG.text = 'Low'
          
      if self.DDRC1_input.isChecked():
        PORTC_PIN1_DIR.text = 'INPUT'
        if self.PINC1_pullup.isChecked():
          PORTC_PIN1_CONFIG.text = 'PullUP'
        else:
          PORTC_PIN1_CONFIG.text = 'High-Imp'
      else:
        PORTC_PIN1_DIR.text = 'OUTPUT'
        if self.PORTC1_high.isChecked():
          PORTC_PIN1_CONFIG.text = 'High'
        else:
          PORTC_PIN1_CONFIG.text = 'Low'
          
      if self.DDRC2_input.isChecked():
        PORTC_PIN2_DIR.text = 'INPUT'
        if self.PINC2_pullup.isChecked():
          PORTC_PIN2_CONFIG.text = 'PullUP'
        else:
          PORTC_PIN2_CONFIG.text = 'High-Imp'
      else:
        PORTC_PIN2_DIR.text = 'OUTPUT'
        if self.PORTC2_high.isChecked():
          PORTC_PIN2_CONFIG.text = 'High'
        else:
          PORTC_PIN2_CONFIG.text = 'Low'
          
      if self.DDRC3_input.isChecked():
        PORTC_PIN3_DIR.text = 'INPUT'
        if self.PINC3_pullup.isChecked():
          PORTC_PIN3_CONFIG.text = 'PullUP'
        else:
          PORTC_PIN3_CONFIG.text = 'High-Imp'
      else:
        PORTC_PIN3_DIR.text = 'OUTPUT'
        if self.PORTC3_high.isChecked():
          PORTC_PIN3_CONFIG.text = 'High'
        else:
          PORTC_PIN3_CONFIG.text = 'Low'
          
      if self.DDRC4_input.isChecked():
        PORTC_PIN4_DIR.text = 'INPUT'
        if self.PINC4_pullup.isChecked():
          PORTC_PIN4_CONFIG.text = 'PullUP'
        else:
          PORTC_PIN4_CONFIG.text = 'High-Imp'
      else:
        PORTC_PIN4_DIR.text = 'OUTPUT'
        if self.PORTC4_high.isChecked():
          PORTC_PIN4_CONFIG.text = 'High'
        else:
          PORTC_PIN4_CONFIG.text = 'Low'
          
      if self.DDRC5_input.isChecked():
        PORTC_PIN5_DIR.text = 'INPUT'
        if self.PINC5_pullup.isChecked():
          PORTC_PIN5_CONFIG.text = 'PullUP'
        else:
          PORTC_PIN5_CONFIG.text = 'High-Imp'
      else:
        PORTC_PIN5_DIR.text = 'OUTPUT'
        if self.PORTC5_high.isChecked():
          PORTC_PIN5_CONFIG.text = 'High'
        else:
          PORTC_PIN5_CONFIG.text = 'Low'
          
      if self.DDRC6_input.isChecked():
        PORTC_PIN6_DIR.text = 'INPUT'
        if self.PINC6_pullup.isChecked():
          PORTC_PIN6_CONFIG.text = 'PullUP'
        else:
          PORTC_PIN6_CONFIG.text = 'High-Imp'
      else:
        PORTC_PIN6_DIR.text = 'OUTPUT'
        if self.PORTC6_high.isChecked():
          PORTC_PIN6_CONFIG.text = 'High'
        else:
          PORTC_PIN6_CONFIG.text = 'Low'
          
      if self.DDRC7_input.isChecked():
        PORTC_PIN7_DIR.text = 'INPUT'
        if self.PINC7_pullup.isChecked():
          PORTC_PIN7_CONFIG.text = 'PullUP'
        else:
          PORTC_PIN7_CONFIG.text = 'High-Imp'
      else:
        PORTC_PIN7_DIR.text = 'OUTPUT'
        if self.PORTC7_high.isChecked():
          PORTC_PIN7_CONFIG.text = 'High'
        else:
          PORTC_PIN7_CONFIG.text = 'Low'
          
      DIO.append(PORTC)
        
      PORTC.append(PORTC_PIN0)
      PORTC_PIN0.append(PORTC_PIN0_DIR)
      PORTC_PIN0.append(PORTC_PIN0_CONFIG)
      PORTC.append(PORTC_PIN1)
      PORTC_PIN1.append(PORTC_PIN1_DIR)
      PORTC_PIN1.append(PORTC_PIN1_CONFIG)
      PORTC.append(PORTC_PIN2)
      PORTC_PIN2.append(PORTC_PIN2_DIR)
      PORTC_PIN2.append(PORTC_PIN2_CONFIG)
      PORTC.append(PORTC_PIN3)
      PORTC_PIN3.append(PORTC_PIN3_DIR)
      PORTC_PIN3.append(PORTC_PIN3_CONFIG)
      PORTC.append(PORTC_PIN4)
      PORTC_PIN4.append(PORTC_PIN4_DIR)
      PORTC_PIN4.append(PORTC_PIN4_CONFIG)
      PORTC.append(PORTC_PIN5)
      PORTC_PIN5.append(PORTC_PIN5_DIR)
      PORTC_PIN5.append(PORTC_PIN5_CONFIG)
      PORTC.append(PORTC_PIN6)
      PORTC_PIN6.append(PORTC_PIN6_DIR)
      PORTC_PIN6.append(PORTC_PIN6_CONFIG)
      PORTC.append(PORTC_PIN7)
      PORTC_PIN7.append(PORTC_PIN7_DIR)
      PORTC_PIN7.append(PORTC_PIN7_CONFIG)
      '''''''''''''''''''''''''''''''PORTD'''''''''''''''''''''''''''''''''''''
      PORTD = ET.Element("PORTD")
      PORTD_PIN0 = ET.Element("PIN0")
      PORTD_PIN1 = ET.Element("PIN1")
      PORTD_PIN2 = ET.Element("PIN2")
      PORTD_PIN3 = ET.Element("PIN3")
      PORTD_PIN4 = ET.Element("PIN4")
      PORTD_PIN5 = ET.Element("PIN5")
      PORTD_PIN6 = ET.Element("PIN6")
      PORTD_PIN7 = ET.Element("PIN7")
          
      PORTD_PIN0_DIR = ET.Element("DIR")
      PORTD_PIN0_CONFIG = ET.Element("CONFIG")
      PORTD_PIN1_DIR = ET.Element("DIR")
      PORTD_PIN1_CONFIG = ET.Element("CONFIG")
      PORTD_PIN2_DIR = ET.Element("DIR")
      PORTD_PIN2_CONFIG = ET.Element("CONFIG")
      PORTD_PIN3_DIR = ET.Element("DIR")
      PORTD_PIN3_CONFIG = ET.Element("CONFIG")
      PORTD_PIN4_DIR = ET.Element("DIR")
      PORTD_PIN4_CONFIG = ET.Element("CONFIG")
      PORTD_PIN5_DIR = ET.Element("DIR")
      PORTD_PIN5_CONFIG = ET.Element("CONFIG")
      PORTD_PIN6_DIR = ET.Element("DIR")
      PORTD_PIN6_CONFIG = ET.Element("CONFIG")
      PORTD_PIN7_DIR = ET.Element("DIR")
      PORTD_PIN7_CONFIG = ET.Element("CONFIG")
      
      if self.DDRD0_input.isChecked():
        PORTD_PIN0_DIR.text = 'INPUT'
        if self.PIND0_pullup.isChecked():
          PORTD_PIN0_CONFIG.text = 'PullUP'
        else:
          PORTD_PIN0_CONFIG.text = 'High-Imp'
      else:
        PORTD_PIN0_DIR.text = 'OUTPUT'
        if self.PORTD0_high.isChecked():
          PORTD_PIN0_CONFIG.text = 'High'
        else:
          PORTD_PIN0_CONFIG.text = 'Low'
          
      if self.DDRD1_input.isChecked():
        PORTD_PIN1_DIR.text = 'INPUT'
        if self.PIND1_pullup.isChecked():
          PORTD_PIN1_CONFIG.text = 'PullUP'
        else:
          PORTD_PIN1_CONFIG.text = 'High-Imp'
      else:
        PORTD_PIN1_DIR.text = 'OUTPUT'
        if self.PORTD1_high.isChecked():
          PORTD_PIN1_CONFIG.text = 'High'
        else:
          PORTD_PIN1_CONFIG.text = 'Low'
          
      if self.DDRD2_input.isChecked():
        PORTD_PIN2_DIR.text = 'INPUT'
        if self.PIND2_pullup.isChecked():
          PORTD_PIN2_CONFIG.text = 'PullUP'
        else:
          PORTD_PIN2_CONFIG.text = 'High-Imp'
      else:
        PORTD_PIN2_DIR.text = 'OUTPUT'
        if self.PORTD2_high.isChecked():
          PORTD_PIN2_CONFIG.text = 'High'
        else:
          PORTD_PIN2_CONFIG.text = 'Low'
          
      if self.DDRD3_input.isChecked():
        PORTD_PIN3_DIR.text = 'INPUT'
        if self.PIND3_pullup.isChecked():
          PORTD_PIN3_CONFIG.text = 'PullUP'
        else:
          PORTD_PIN3_CONFIG.text = 'High-Imp'
      else:
        PORTD_PIN3_DIR.text = 'OUTPUT'
        if self.PORTD3_high.isChecked():
          PORTD_PIN3_CONFIG.text = 'High'
        else:
          PORTD_PIN3_CONFIG.text = 'Low'
          
      if self.DDRD4_input.isChecked():
        PORTD_PIN4_DIR.text = 'INPUT'
        if self.PIND4_pullup.isChecked():
          PORTD_PIN4_CONFIG.text = 'PullUP'
        else:
          PORTD_PIN4_CONFIG.text = 'High-Imp'
      else:
        PORTD_PIN4_DIR.text = 'OUTPUT'
        if self.PORTD4_high.isChecked():
          PORTD_PIN4_CONFIG.text = 'High'
        else:
          PORTD_PIN4_CONFIG.text = 'Low'
          
      if self.DDRD5_input.isChecked():
        PORTD_PIN5_DIR.text = 'INPUT'
        if self.PIND5_pullup.isChecked():
          PORTD_PIN5_CONFIG.text = 'PullUP'
        else:
          PORTD_PIN5_CONFIG.text = 'High-Imp'
      else:
        PORTD_PIN5_DIR.text = 'OUTPUT'
        if self.PORTD5_high.isChecked():
          PORTD_PIN5_CONFIG.text = 'High'
        else:
          PORTD_PIN5_CONFIG.text = 'Low'
          
      if self.DDRD6_input.isChecked():
        PORTD_PIN6_DIR.text = 'INPUT'
        if self.PIND6_pullup.isChecked():
          PORTD_PIN6_CONFIG.text = 'PullUP'
        else:
          PORTD_PIN6_CONFIG.text = 'High-Imp'
      else:
        PORTD_PIN6_DIR.text = 'OUTPUT'
        if self.PORTD6_high.isChecked():
          PORTD_PIN6_CONFIG.text = 'High'
        else:
          PORTD_PIN6_CONFIG.text = 'Low'
          
      if self.DDRD7_input.isChecked():
        PORTD_PIN7_DIR.text = 'INPUT'
        if self.PIND7_pullup.isChecked():
          PORTD_PIN7_CONFIG.text = 'PullUP'
        else:
          PORTD_PIN7_CONFIG.text = 'High-Imp'
      else:
        PORTD_PIN7_DIR.text = 'OUTPUT'
        if self.PORTD7_high.isChecked():
          PORTD_PIN7_CONFIG.text = 'High'
        else:
          PORTD_PIN7_CONFIG.text = 'Low'
          
      DIO.append(PORTD)
        
      PORTD.append(PORTD_PIN0)
      PORTD_PIN0.append(PORTD_PIN0_DIR)
      PORTD_PIN0.append(PORTD_PIN0_CONFIG)
      PORTD.append(PORTD_PIN1)
      PORTD_PIN1.append(PORTD_PIN1_DIR)
      PORTD_PIN1.append(PORTD_PIN1_CONFIG)
      PORTD.append(PORTD_PIN2)
      PORTD_PIN2.append(PORTD_PIN2_DIR)
      PORTD_PIN2.append(PORTD_PIN2_CONFIG)
      PORTD.append(PORTD_PIN3)
      PORTD_PIN3.append(PORTD_PIN3_DIR)
      PORTD_PIN3.append(PORTD_PIN3_CONFIG)
      PORTD.append(PORTD_PIN4)
      PORTD_PIN4.append(PORTD_PIN4_DIR)
      PORTD_PIN4.append(PORTD_PIN4_CONFIG)
      PORTD.append(PORTD_PIN5)
      PORTD_PIN5.append(PORTD_PIN5_DIR)
      PORTD_PIN5.append(PORTD_PIN5_CONFIG)
      PORTD.append(PORTD_PIN6)
      PORTD_PIN6.append(PORTD_PIN6_DIR)
      PORTD_PIN6.append(PORTD_PIN6_CONFIG)
      PORTD.append(PORTD_PIN7)
      PORTD_PIN7.append(PORTD_PIN7_DIR)
      PORTD_PIN7.append(PORTD_PIN7_CONFIG)
      
      path = self.lineEdit_save.text()+r'\DIO_Cfg.xml'
      File_Handler=open(path,'w')
      File_Handler.write(ET.tostring(DIO, pretty_print=True).decode())
      File_Handler.close()
    
    
    
    def loadfun(self):
      path = self.lineEdit_load.text()+r'\DIO_Cfg.xml'
      
      tree = ET.parse(path)
      DIO=tree.getroot()
      '''''''''''''''''''''''''''''''PORTA'''''''''''''''''''''''''''''''''''''
      PORT=DIO.find('PORTA')
      
      PIN0=PORT.find('PIN0')
      DIR = PIN0.find('DIR').text
      Cfg = PIN0.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRA0_input.setChecked(True)
          self.PORTA0.setDisabled(True)
          self.PINA0.setEnabled(True)
          if Cfg == "PullUP":
              self.PINA0_pullup.setChecked(True)
          else:
              self.PINA0_highimp.setChecked(True)
      else:
          self.DDRA0_output.setChecked(True)
          self.PINA0.setDisabled(True)
          self.PORTA0.setEnabled(True)
          if Cfg == "Low":
              self.PORTA0_low.setChecked(True)
          else:
              self.PORTA0_high.setChecked(True)
              
      PIN1=PORT.find('PIN1')
      DIR = PIN1.find('DIR').text
      Cfg = PIN1.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRA1_input.setChecked(True)
          self.PORTA1.setDisabled(True)
          self.PINA1.setEnabled(True)
          if Cfg == "PullUP":
              self.PINA1_pullup.setChecked(True)
          else:
              self.PINA1_highimp.setChecked(True)
      else:
          self.DDRA1_output.setChecked(True)
          self.PINA1.setDisabled(True)
          self.PORTA1.setEnabled(True)
          if Cfg == "Low":
              self.PORTA1_low.setChecked(True)
          else:
              self.PORTA1_high.setChecked(True)
      
      PIN2=PORT.find('PIN2')
      DIR = PIN2.find('DIR').text
      Cfg = PIN2.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRA2_input.setChecked(True)
          self.PORTA2.setDisabled(True)
          self.PINA2.setEnabled(True)
          if Cfg == "PullUP":
              self.PINA2_pullup.setChecked(True)
          else:
              self.PINA2_highimp.setChecked(True)
      else:
          self.DDRA2_output.setChecked(True)
          self.PINA2.setDisabled(True)
          self.PORTA2.setEnabled(True)
          if Cfg == "Low":
              self.PORTA2_low.setChecked(True)
          else:
              self.PORTA2_high.setChecked(True)
              
      PIN3=PORT.find('PIN3')
      DIR = PIN3.find('DIR').text
      Cfg = PIN3.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRA3_input.setChecked(True)
          self.PORTA3.setDisabled(True)
          self.PINA3.setEnabled(True)
          if Cfg == "PullUP":
              self.PINA3_pullup.setChecked(True)
          else:
              self.PINA3_highimp.setChecked(True)
      else:
          self.DDRA3_output.setChecked(True)
          self.PINA3.setDisabled(True)
          self.PORTA3.setEnabled(True)
          if Cfg == "Low":
              self.PORTA3_low.setChecked(True)
          else:
              self.PORTA3_high.setChecked(True)
              
      PIN4=PORT.find('PIN4')
      DIR = PIN4.find('DIR').text
      Cfg = PIN4.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRA4_input.setChecked(True)
          self.PORTA4.setDisabled(True)
          self.PINA4.setEnabled(True)
          if Cfg == "PullUP":
              self.PINA4_pullup.setChecked(True)
          else:
              self.PINA4_highimp.setChecked(True)
      else:
          self.DDRA4_output.setChecked(True)
          self.PINA4.setDisabled(True)
          self.PORTA4.setEnabled(True)
          if Cfg == "Low":
              self.PORTA4_low.setChecked(True)
          else:
              self.PORTA4_high.setChecked(True)
              
      PIN5=PORT.find('PIN5')        
      DIR = PIN5.find('DIR').text
      Cfg = PIN5.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRA5_input.setChecked(True)
          self.PORTA5.setDisabled(True)
          self.PINA5.setEnabled(True)
          if Cfg == "PullUP":
              self.PINA5_pullup.setChecked(True)
          else:
              self.PINA5_highimp.setChecked(True)
      else:
          self.DDRA5_output.setChecked(True)
          self.PINA5.setDisabled(True)
          self.PORTA5.setEnabled(True)
          if Cfg == "Low":
              self.PORTA5_low.setChecked(True)
          else:
              self.PORTA5_high.setChecked(True)
              
      PIN6=PORT.find('PIN6')
      DIR = PIN6.find('DIR').text
      Cfg = PIN6.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRA6_input.setChecked(True)
          self.PORTA6.setDisabled(True)
          self.PINA6.setEnabled(True)
          if Cfg == "PullUP":
              self.PINA6_pullup.setChecked(True)
          else:
              self.PINA6_highimp.setChecked(True)
      else:
          self.DDRA6_output.setChecked(True)
          self.PINA6.setDisabled(True)
          self.PORTA6.setEnabled(True)
          if Cfg == "Low":
              self.PORTA6_low.setChecked(True)
          else:
              self.PORTA6_high.setChecked(True)
              
      PIN7=PORT.find('PIN7')
      DIR = PIN7.find('DIR').text
      Cfg = PIN7.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRA7_input.setChecked(True)
          self.PORTA7.setDisabled(True)
          self.PINA7.setEnabled(True)
          if Cfg == "PullUP":
              self.PINA7_pullup.setChecked(True)
          else:
              self.PINA7_highimp.setChecked(True)
      else:
          self.DDRA7_output.setChecked(True)
          self.PINA7.setDisabled(True)
          self.PORTA7.setEnabled(True)
          if Cfg == "Low":
              self.PORTA7_low.setChecked(True)
          else:
              self.PORTA7_high.setChecked(True)
              
      '''''''''''''''''''''''''''''''PORTB'''''''''''''''''''''''''''''''''''''
      PORT=DIO.find('PORTB')
      
      PIN0=PORT.find('PIN0')
      DIR = PIN0.find('DIR').text
      Cfg = PIN0.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRB0_input.setChecked(True)
          self.PORTB0.setDisabled(True)
          self.PINB0.setEnabled(True)
          if Cfg == "PullUP":
              self.PINB0_pullup.setChecked(True)
          else:
              self.PINB0_highimp.setChecked(True)
      else:
          self.DDRB0_output.setChecked(True)
          self.PINB0.setDisabled(True)
          self.PORTB0.setEnabled(True)
          if Cfg == "Low":
              self.PORTB0_low.setChecked(True)
          else:
              self.PORTB0_high.setChecked(True)
              
      PIN1=PORT.find('PIN1')
      DIR = PIN1.find('DIR').text
      Cfg = PIN1.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRB1_input.setChecked(True)
          self.PORTB1.setDisabled(True)
          self.PINB1.setEnabled(True)
          if Cfg == "PullUP":
              self.PINB1_pullup.setChecked(True)
          else:
              self.PINB1_highimp.setChecked(True)
      else:
          self.DDRB1_output.setChecked(True)
          self.PINB1.setDisabled(True)
          self.PORTB1.setEnabled(True)
          if Cfg == "Low":
              self.PORTB1_low.setChecked(True)
          else:
              self.PORTB1_high.setChecked(True)
      
      PIN2=PORT.find('PIN2')
      DIR = PIN2.find('DIR').text
      Cfg = PIN2.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRB2_input.setChecked(True)
          self.PORTB2.setDisabled(True)
          self.PINB2.setEnabled(True)
          if Cfg == "PullUP":
              self.PINB2_pullup.setChecked(True)
          else:
              self.PINB2_highimp.setChecked(True)
      else:
          self.DDRB2_output.setChecked(True)
          self.PINB2.setDisabled(True)
          self.PORTB2.setEnabled(True)
          if Cfg == "Low":
              self.PORTB2_low.setChecked(True)
          else:
              self.PORTB2_high.setChecked(True)
              
      PIN3=PORT.find('PIN3')
      DIR = PIN3.find('DIR').text
      Cfg = PIN3.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRB3_input.setChecked(True)
          self.PORTB3.setDisabled(True)
          self.PINB3.setEnabled(True)
          if Cfg == "PullUP":
              self.PINB3_pullup.setChecked(True)
          else:
              self.PINB3_highimp.setChecked(True)
      else:
          self.DDRB3_output.setChecked(True)
          self.PINB3.setDisabled(True)
          self.PORTB3.setEnabled(True)
          if Cfg == "Low":
              self.PORTB3_low.setChecked(True)
          else:
              self.PORTB3_high.setChecked(True)
              
      PIN4=PORT.find('PIN4')
      DIR = PIN4.find('DIR').text
      Cfg = PIN4.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRB4_input.setChecked(True)
          self.PORTB4.setDisabled(True)
          self.PINB4.setEnabled(True)
          if Cfg == "PullUP":
              self.PINB4_pullup.setChecked(True)
          else:
              self.PINB4_highimp.setChecked(True)
      else:
          self.DDRB4_output.setChecked(True)
          self.PINB4.setDisabled(True)
          self.PORTB4.setEnabled(True)
          if Cfg == "Low":
              self.PORTB4_low.setChecked(True)
          else:
              self.PORTB4_high.setChecked(True)
              
      PIN5=PORT.find('PIN5')        
      DIR = PIN5.find('DIR').text
      Cfg = PIN5.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRB5_input.setChecked(True)
          self.PORTB5.setDisabled(True)
          self.PINB5.setEnabled(True)
          if Cfg == "PullUP":
              self.PINB5_pullup.setChecked(True)
          else:
              self.PINB5_highimp.setChecked(True)
      else:
          self.DDRB5_output.setChecked(True)
          self.PINB5.setDisabled(True)
          self.PORTB5.setEnabled(True)
          if Cfg == "Low":
              self.PORTB5_low.setChecked(True)
          else:
              self.PORTB5_high.setChecked(True)
              
      PIN6=PORT.find('PIN6')
      DIR = PIN6.find('DIR').text
      Cfg = PIN6.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRB6_input.setChecked(True)
          self.PORTB6.setDisabled(True)
          self.PINB6.setEnabled(True)
          if Cfg == "PullUP":
              self.PINB6_pullup.setChecked(True)
          else:
              self.PINB6_highimp.setChecked(True)
      else:
          self.DDRB6_output.setChecked(True)
          self.PINB6.setDisabled(True)
          self.PORTB6.setEnabled(True)
          if Cfg == "Low":
              self.PORTB6_low.setChecked(True)
          else:
              self.PORTB6_high.setChecked(True)
              
      PIN7=PORT.find('PIN7')
      DIR = PIN7.find('DIR').text
      Cfg = PIN7.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRB7_input.setChecked(True)
          self.PORTB7.setDisabled(True)
          self.PINB7.setEnabled(True)
          if Cfg == "PullUP":
              self.PINB7_pullup.setChecked(True)
          else:
              self.PINB7_highimp.setChecked(True)
      else:
          self.DDRB7_output.setChecked(True)
          self.PINB7.setDisabled(True)
          self.PORTB7.setEnabled(True)
          if Cfg == "Low":
              self.PORTB7_low.setChecked(True)
          else:
              self.PORTB7_high.setChecked(True)
              
      '''''''''''''''''''''''''''''''PORTC'''''''''''''''''''''''''''''''''''''
      PORT=DIO.find('PORTC')        
              
      PIN0=PORT.find('PIN0')        
      DIR = PIN0.find('DIR').text        
      Cfg = PIN0.find('CONFIG').text        
      if DIR == "INPUT":        
          self.DDRC0_input.setChecked(True)        
          self.PORTC0.setDisabled(True)        
          self.PINC0.setEnabled(True)        
          if Cfg == "PullUP":        
              self.PINC0_pullup.setChecked(True)        
          else:        
              self.PINC0_highimp.setChecked(True)        
      else:        
          self.DDRC0_output.setChecked(True)        
          self.PINC0.setDisabled(True)        
          self.PORTC0.setEnabled(True)        
          if Cfg == "Low":        
              self.PORTC0_low.setChecked(True)        
          else:        
              self.PORTC0_high.setChecked(True)        
                      
      PIN1=PORT.find('PIN1')        
      DIR = PIN1.find('DIR').text        
      Cfg = PIN1.find('CONFIG').text        
      if DIR == "INPUT":        
          self.DDRC1_input.setChecked(True)        
          self.PORTC1.setDisabled(True)        
          self.PINC1.setEnabled(True)        
          if Cfg == "PullUP":        
              self.PINC1_pullup.setChecked(True)        
          else:        
              self.PINC1_highimp.setChecked(True)        
      else:        
          self.DDRC1_output.setChecked(True)        
          self.PINC1.setDisabled(True)        
          self.PORTC1.setEnabled(True)        
          if Cfg == "Low":        
              self.PORTC1_low.setChecked(True)        
          else:        
              self.PORTC1_high.setChecked(True)        
              
      PIN2=PORT.find('PIN2')        
      DIR = PIN2.find('DIR').text        
      Cfg = PIN2.find('CONFIG').text        
      if DIR == "INPUT":        
          self.DDRC2_input.setChecked(True)        
          self.PORTC2.setDisabled(True)        
          self.PINC2.setEnabled(True)        
          if Cfg == "PullUP":        
              self.PINC2_pullup.setChecked(True)        
          else:        
              self.PINC2_highimp.setChecked(True)        
      else:        
          self.DDRC2_output.setChecked(True)        
          self.PINC2.setDisabled(True)        
          self.PORTC2.setEnabled(True)        
          if Cfg == "Low":        
              self.PORTC2_low.setChecked(True)        
          else:        
              self.PORTC2_high.setChecked(True)        
                      
      PIN3=PORT.find('PIN3')        
      DIR = PIN3.find('DIR').text        
      Cfg = PIN3.find('CONFIG').text        
      if DIR == "INPUT":        
          self.DDRC3_input.setChecked(True)        
          self.PORTC3.setDisabled(True)        
          self.PINC3.setEnabled(True)        
          if Cfg == "PullUP":        
              self.PINC3_pullup.setChecked(True)        
          else:        
              self.PINC3_highimp.setChecked(True)        
      else:        
          self.DDRC3_output.setChecked(True)        
          self.PINC3.setDisabled(True)        
          self.PORTC3.setEnabled(True)        
          if Cfg == "Low":        
              self.PORTC3_low.setChecked(True)        
          else:        
              self.PORTC3_high.setChecked(True)        
                      
      PIN4=PORT.find('PIN4')        
      DIR = PIN4.find('DIR').text        
      Cfg = PIN4.find('CONFIG').text        
      if DIR == "INPUT":        
          self.DDRC4_input.setChecked(True)        
          self.PORTC4.setDisabled(True)        
          self.PINC4.setEnabled(True)        
          if Cfg == "PullUP":        
              self.PINC4_pullup.setChecked(True)        
          else:        
              self.PINC4_highimp.setChecked(True)        
      else:        
          self.DDRC4_output.setChecked(True)        
          self.PINC4.setDisabled(True)        
          self.PORTC4.setEnabled(True)        
          if Cfg == "Low":        
              self.PORTC4_low.setChecked(True)        
          else:        
              self.PORTC4_high.setChecked(True)        
                      
      PIN5=PORT.find('PIN5')                
      DIR = PIN5.find('DIR').text        
      Cfg = PIN5.find('CONFIG').text        
      if DIR == "INPUT":        
          self.DDRC5_input.setChecked(True)        
          self.PORTC5.setDisabled(True)        
          self.PINC5.setEnabled(True)        
          if Cfg == "PullUP":        
              self.PINC5_pullup.setChecked(True)        
          else:        
              self.PINC5_highimp.setChecked(True)        
      else:        
          self.DDRC5_output.setChecked(True)        
          self.PINC5.setDisabled(True)        
          self.PORTC5.setEnabled(True)        
          if Cfg == "Low":        
              self.PORTC5_low.setChecked(True)        
          else:        
              self.PORTC5_high.setChecked(True)        
                      
      PIN6=PORT.find('PIN6')        
      DIR = PIN6.find('DIR').text        
      Cfg = PIN6.find('CONFIG').text        
      if DIR == "INPUT":        
          self.DDRC6_input.setChecked(True)        
          self.PORTC6.setDisabled(True)        
          self.PINC6.setEnabled(True)        
          if Cfg == "PullUP":        
              self.PINC6_pullup.setChecked(True)        
          else:        
              self.PINC6_highimp.setChecked(True)        
      else:        
          self.DDRC6_output.setChecked(True)        
          self.PINC6.setDisabled(True)        
          self.PORTC6.setEnabled(True)        
          if Cfg == "Low":        
              self.PORTC6_low.setChecked(True)        
          else:        
              self.PORTC6_high.setChecked(True)        
                      
      PIN7=PORT.find('PIN7')        
      DIR = PIN7.find('DIR').text        
      Cfg = PIN7.find('CONFIG').text        
      if DIR == "INPUT":        
          self.DDRC7_input.setChecked(True)        
          self.PORTC7.setDisabled(True)        
          self.PINC7.setEnabled(True)        
          if Cfg == "PullUP":        
              self.PINC7_pullup.setChecked(True)        
          else:        
              self.PINC7_highimp.setChecked(True)        
      else:        
          self.DDRC7_output.setChecked(True)        
          self.PINC7.setDisabled(True)        
          self.PORTC7.setEnabled(True)        
          if Cfg == "Low":        
              self.PORTC7_low.setChecked(True)        
          else:        
              self.PORTC7_high.setChecked(True) 

      '''''''''''''''''''''''''''''''PORTD'''''''''''''''''''''''''''''''''''''             
      PORT=DIO.find('PORTD')        
              
      PIN0=PORT.find('PIN0')        
      DIR = PIN0.find('DIR').text        
      Cfg = PIN0.find('CONFIG').text        
      if DIR == "INPUT":        
          self.DDRD0_input.setChecked(True)        
          self.PORTD0.setDisabled(True)        
          self.PIND0.setEnabled(True)        
          if Cfg == "PullUP":        
              self.PIND0_pullup.setChecked(True)        
          else:        
              self.PIND0_highimp.setChecked(True)        
      else:        
          self.DDRD0_output.setChecked(True)        
          self.PIND0.setDisabled(True)        
          self.PORTD0.setEnabled(True)        
          if Cfg == "Low":        
              self.PORTD0_low.setChecked(True)        
          else:        
              self.PORTD0_high.setChecked(True)        
                      
      PIN1=PORT.find('PIN1')        
      DIR = PIN1.find('DIR').text        
      Cfg = PIN1.find('CONFIG').text        
      if DIR == "INPUT":        
          self.DDRD1_input.setChecked(True)        
          self.PORTD1.setDisabled(True)        
          self.PIND1.setEnabled(True)        
          if Cfg == "PullUP":        
              self.PIND1_pullup.setChecked(True)        
          else:        
              self.PIND1_highimp.setChecked(True)        
      else:        
          self.DDRD1_output.setChecked(True)        
          self.PIND1.setDisabled(True)        
          self.PORTD1.setEnabled(True)        
          if Cfg == "Low":        
              self.PORTD1_low.setChecked(True)        
          else:        
              self.PORTD1_high.setChecked(True)        
              
      PIN2=PORT.find('PIN2')        
      DIR = PIN2.find('DIR').text        
      Cfg = PIN2.find('CONFIG').text        
      if DIR == "INPUT":        
          self.DDRD2_input.setChecked(True)        
          self.PORTD2.setDisabled(True)        
          self.PIND2.setEnabled(True)        
          if Cfg == "PullUP":        
              self.PIND2_pullup.setChecked(True)        
          else:        
              self.PIND2_highimp.setChecked(True)        
      else:        
          self.DDRD2_output.setChecked(True)        
          self.PIND2.setDisabled(True)        
          self.PORTD2.setEnabled(True)        
          if Cfg == "Low":        
              self.PORTD2_low.setChecked(True)        
          else:        
              self.PORTD2_high.setChecked(True)        
                      
      PIN3=PORT.find('PIN3')        
      DIR = PIN3.find('DIR').text        
      Cfg = PIN3.find('CONFIG').text        
      if DIR == "INPUT":        
          self.DDRD3_input.setChecked(True)        
          self.PORTD3.setDisabled(True)        
          self.PIND3.setEnabled(True)        
          if Cfg == "PullUP":        
              self.PIND3_pullup.setChecked(True)
          else:
              self.PIND3_highimp.setChecked(True)
      else:
          self.DDRD3_output.setChecked(True)
          self.PIND3.setDisabled(True)
          self.PORTD3.setEnabled(True)
          if Cfg == "Low":
              self.PORTD3_low.setChecked(True)
          else:
              self.PORTD3_high.setChecked(True)
              
      PIN4=PORT.find('PIN4')
      DIR = PIN4.find('DIR').text
      Cfg = PIN4.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRD4_input.setChecked(True)
          self.PORTD4.setDisabled(True)
          self.PIND4.setEnabled(True)
          if Cfg == "PullUP":
              self.PIND4_pullup.setChecked(True)
          else:
              self.PIND4_highimp.setChecked(True)
      else:
          self.DDRD4_output.setChecked(True)
          self.PIND4.setDisabled(True)
          self.PORTD4.setEnabled(True)
          if Cfg == "Low":
              self.PORTD4_low.setChecked(True)
          else:
              self.PORTD4_high.setChecked(True)
              
      PIN5=PORT.find('PIN5')        
      DIR = PIN5.find('DIR').text
      Cfg = PIN5.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRD5_input.setChecked(True)
          self.PORTD5.setDisabled(True)
          self.PIND5.setEnabled(True)
          if Cfg == "PullUP":
              self.PIND5_pullup.setChecked(True)
          else:
              self.PIND5_highimp.setChecked(True)
      else:
          self.DDRD5_output.setChecked(True)
          self.PIND5.setDisabled(True)
          self.PORTD5.setEnabled(True)
          if Cfg == "Low":
              self.PORTD5_low.setChecked(True)
          else:
              self.PORTD5_high.setChecked(True)
              
      PIN6=PORT.find('PIN6')
      DIR = PIN6.find('DIR').text
      Cfg = PIN6.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRD6_input.setChecked(True)
          self.PORTD6.setDisabled(True)
          self.PIND6.setEnabled(True)
          if Cfg == "PullUP":
              self.PIND6_pullup.setChecked(True)
          else:
              self.PIND6_highimp.setChecked(True)
      else:
          self.DDRD6_output.setChecked(True)
          self.PIND6.setDisabled(True)
          self.PORTD6.setEnabled(True)
          if Cfg == "Low":
              self.PORTD6_low.setChecked(True)
          else:
              self.PORTD6_high.setChecked(True)
              
      PIN7=PORT.find('PIN7')
      DIR = PIN7.find('DIR').text
      Cfg = PIN7.find('CONFIG').text
      if DIR == "INPUT":
          self.DDRD7_input.setChecked(True)
          self.PORTD7.setDisabled(True)
          self.PIND7.setEnabled(True)
          if Cfg == "PullUP":
              self.PIND7_pullup.setChecked(True)
          else:
              self.PIND7_highimp.setChecked(True)
      else:
          self.DDRD7_output.setChecked(True)
          self.PIND7.setDisabled(True)
          self.PORTD7.setEnabled(True)
          if Cfg == "Low":
              self.PORTD7_low.setChecked(True)
          else:
              self.PORTD7_high.setChecked(True)
     
    
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.PORTA0.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTA0_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTA0_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PINA0.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINA0_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINA0_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.DDRA0.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRA0_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRA0_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.label.setText(QCoreApplication.translate("Form", u"PIN0", None))
        self.PORTA1.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTA1_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTA1_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PINA1.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINA1_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINA1_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"PIN1", None))
        self.DDRA1.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRA1_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRA1_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PORTA2.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTA2_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTA2_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PINA2.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINA2_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINA2_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"PIN2", None))
        self.DDRA2.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRA2_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRA2_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PORTA3.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTA3_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTA3_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PINA3.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINA3_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINA3_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"PIN3", None))
        self.DDRA3.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRA3_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRA3_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PINA6.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINA6_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINA6_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.DDRA7.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRA7_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRA7_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"PIN6", None))
        self.PINA5.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINA5_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINA5_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.DDRA6.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRA6_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRA6_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.DDRA5.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRA5_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRA5_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PINA7.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINA7_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINA7_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.PORTA4.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTA4_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTA4_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PORTA6.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTA6_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTA6_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PINA4.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINA4_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINA4_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.PORTA5.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTA5_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTA5_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"PIN4", None))
        self.PORTA7.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTA7_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTA7_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"PIN7", None))
        self.DDRA4.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRA4_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRA4_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"PIN5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"PORTA", None))
        self.DDRB4.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRB4_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRB4_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PORTB6.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTB6_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTB6_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PINB4.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINB4_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINB4_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.PINB6.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINB6_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINB6_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.PINB0.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINB0_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINB0_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.DDRB5.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRB5_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRB5_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.DDRB7.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRB7_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRB7_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PINB5.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINB5_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINB5_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.PORTB7.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTB7_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTB7_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PINB1.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINB1_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINB1_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.DDRB3.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRB3_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRB3_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"PIN6", None))
        self.PINB7.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINB7_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINB7_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.PINB3.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINB3_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINB3_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"PIN5", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"PIN3", None))
        self.DDRB0.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRB0_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRB0_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"PIN1", None))
        self.PORTB0.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTB0_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTB0_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.DDRB6.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRB6_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRB6_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"PIN2", None))
        self.DDRB1.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRB1_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRB1_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PORTB1.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTB1_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTB1_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PORTB3.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTB3_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTB3_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.DDRB2.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRB2_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRB2_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"PIN4", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"PIN0", None))
        self.PORTB5.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTB5_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTB5_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PINB2.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINB2_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINB2_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"PIN7", None))
        self.PORTB4.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTB4_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTB4_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PORTB2.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTB2_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTB2_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"PORTB", None))
        self.DDRC4.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRC4_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRC4_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PORTC6.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTC6_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTC6_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PINC4.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINC4_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINC4_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.PINC6.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINC6_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINC6_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.PINC0.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINC0_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINC0_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.DDRC5.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRC5_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRC5_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.DDRC7.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRC7_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRC7_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PINC5.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINC5_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINC5_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.PORTC7.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTC7_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTC7_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PINC1.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINC1_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINC1_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.DDRC3.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRC3_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRC3_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"PIN6", None))
        self.PINC7.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINC7_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINC7_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.PINC3.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINC3_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINC3_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"PIN5", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"PIN3", None))
        self.DDRC0.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRC0_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRC0_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"PIN1", None))
        self.PORTC0.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTC0_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTC0_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.DDRC6.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRC6_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRC6_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"PIN2", None))
        self.DDRC1.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRC1_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRC1_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PORTC1.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTC1_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTC1_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PORTC3.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTC3_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTC3_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.DDRC2.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRC2_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRC2_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"PIN4", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"PIN0", None))
        self.PORTC5.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTC5_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTC5_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PINC2.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PINC2_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PINC2_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"PIN7", None))
        self.PORTC4.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTC4_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTC4_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PORTC2.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTC2_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTC2_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"PORTC", None))
        self.DDRD4.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRD4_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRD4_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PORTD6.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTD6_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTD6_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PIND4.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PIND4_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PIND4_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.PIND6.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PIND6_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PIND6_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.PIND0.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PIND0_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PIND0_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.DDRD5.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRD5_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRD5_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.DDRD7.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRD7_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRD7_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PIND5.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PIND5_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PIND5_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.PORTD7.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTD7_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTD7_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PIND1.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PIND1_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PIND1_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.DDRD3.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRD3_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRD3_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"PIN6", None))
        self.PIND7.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PIND7_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PIND7_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.PIND3.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PIND3_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PIND3_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"PIN5", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"PIN3", None))
        self.DDRD0.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRD0_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRD0_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"PIN1", None))
        self.PORTD0.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTD0_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTD0_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.DDRD6.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRD6_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRD6_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"PIN2", None))
        self.DDRD1.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRD1_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRD1_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PORTD1.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTD1_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTD1_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PORTD3.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTD3_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTD3_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.DDRD2.setTitle(QCoreApplication.translate("Form", u"Direction", None))
        self.DDRD2_output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.DDRD2_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"PIN4", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"PIN0", None))
        self.PORTD5.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTD5_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTD5_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PIND2.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PIND2_pullup.setText(QCoreApplication.translate("Form", u"Pull-up", None))
        self.PIND2_highimp.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.label_40.setText(QCoreApplication.translate("Form", u"PIN7", None))
        self.PORTD4.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTD4_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTD4_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PORTD2.setTitle(QCoreApplication.translate("Form", u"Output Configuraion", None))
        self.PORTD2_high.setText(QCoreApplication.translate("Form", u"High", None))
        self.PORTD2_low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Form", u"PORTD", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"Enter the path to generate the configuration file", None))
        self.generate.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.label_41.setText(QCoreApplication.translate("Form", u"Choose from the below options", None))
        self.lineEdit_save.setText(QCoreApplication.translate("Form", u"Enter the path to save the configuration in an xml file", None))
        self.save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.lineEdit_load.setText(QCoreApplication.translate("Form", u"Enter the path to load the configuration from an xml file", None))
        self.load.setText(QCoreApplication.translate("Form", u"Load", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"OUTPUT", None))
    # retranslateUi

app=QApplication(sys.argv)
Widget=QWidget()
Form=Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())