# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenutXHLv.ui'
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


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(700, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
"	background-color:#2d2d31;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* #a8a192 */")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 60, 661, 81))
        font = QFont()
        font.setFamily(u"Nasalization Rg")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: #a8a192;\n"
"font: 40pt \"Nasalization Rg\";")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 150, 661, 31))
        font1 = QFont()
        font1.setFamily(u"Nasalization Rg")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: #a8a192;\n"
"font: 10pt \"Nasalization Rg\";")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(60, 230, 561, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: #a8a192;\n"
"	color: #000;\n"
"	border-style: none;\n"
"	border-radius: 5px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	background-color: #c2c1bd;\n"
"}\n"
"")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 270, 661, 21))
        font2 = QFont()
        font2.setFamily(u"Nasalization Rg")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"color: #a8a192;\n"
"font: 12pt \"Nasalization Rg\";")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(30, 330, 621, 21))
        self.label_credits.setFont(font1)
        self.label_credits.setStyleSheet(u"color: #a8a192;\n"
"font: 10pt \"Nasalization Rg\";")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_credits_2 = QLabel(self.dropShadowFrame)
        self.label_credits_2.setObjectName(u"label_credits_2")
        self.label_credits_2.setGeometry(QRect(30, 350, 621, 21))
        self.label_credits_2.setFont(font1)
        self.label_credits_2.setStyleSheet(u"color:#a8a192;\n"
"font: 10pt \"Nasalization Rg\";")
        self.label_credits_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<strong>M.A.R.S</strong>", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"<strong>Work Like</strong> Speed", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.label_credits.setText(QCoreApplication.translate("SplashScreen", u"<strong>\u00a9</strong>:Developed & Innovated By", None))
        self.label_credits_2.setText(QCoreApplication.translate("SplashScreen", u"<strong>_sh\u039bdoww, PiDPyd , Trilogical</strong>", None))
    # retranslateUi

