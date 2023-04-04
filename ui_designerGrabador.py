# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerGrabadoryOgdQj.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(189, 74)
        self.frmMain = QWidget(MainWindow)
        self.frmMain.setObjectName(u"frmMain")
        self.frmMain.setStyleSheet(u"\n"
"background-color: rgb(227, 221, 205);")
        self.verticalLayout_2 = QVBoxLayout(self.frmMain)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frmdefrms = QHBoxLayout()
        self.frmdefrms.setObjectName(u"frmdefrms")
        self.frmGrabar = QHBoxLayout()
        self.frmGrabar.setObjectName(u"frmGrabar")
        self.frmGrabar.setContentsMargins(3, 4, 6, 6)
        self.btnGrabar = QPushButton(self.frmMain)
        self.btnGrabar.setObjectName(u"btnGrabar")
        self.btnGrabar.setMaximumSize(QSize(40, 40))
        self.btnGrabar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnGrabar.setStyleSheet(u"QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/boton-rec_black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnGrabar.setIcon(icon)
        self.btnGrabar.setIconSize(QSize(38, 38))

        self.frmGrabar.addWidget(self.btnGrabar)


        self.frmdefrms.addLayout(self.frmGrabar)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.frmdefrms.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btnConfig = QPushButton(self.frmMain)
        self.btnConfig.setObjectName(u"btnConfig")
        self.btnConfig.setMaximumSize(QSize(40, 40))
        self.btnConfig.setStyleSheet(u"QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/configuraciones.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnConfig.setIcon(icon1)
        self.btnConfig.setIconSize(QSize(40, 40))
        self.btnConfig.setFlat(True)

        self.verticalLayout_4.addWidget(self.btnConfig)


        self.frmdefrms.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addLayout(self.frmdefrms)

        MainWindow.setCentralWidget(self.frmMain)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 189, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnGrabar.setText("")
        self.btnConfig.setText("")
    # retranslateUi

