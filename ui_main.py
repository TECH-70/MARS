# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainBNrrFB.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1020, 520)
        MainWindow.setMinimumSize(QSize(1020, 520))
        MainWindow.setMaximumSize(QSize(1020, 520))
        MainWindow.setStyleSheet(u"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.drop_shadow_frame = QWidget(MainWindow)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"background-color: none;")
        self.drop_shadow_layout = QVBoxLayout(self.drop_shadow_frame)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.top_bar = QFrame(self.drop_shadow_frame)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 40))
        self.top_bar.setStyleSheet(u"background-color: #2E3440;\n"
"border-top-right-radius: 13px;\n"
"border-top-left-radius: 10px;")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.top_bar)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(50, 40))
        self.frame.setCursor(QCursor(Qt.ArrowCursor))
        self.frame.setStyleSheet(u"background-color: rgb(46, 52, 64);\n"
"border-top-left-radius: 10px;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_butt = QPushButton(self.frame)
        self.menu_butt.setObjectName(u"menu_butt")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_butt.sizePolicy().hasHeightForWidth())
        self.menu_butt.setSizePolicy(sizePolicy)
        self.menu_butt.setMinimumSize(QSize(0, 40))
        self.menu_butt.setStyleSheet(u"border: 0px solid;\n"
"border-top-right-radius: 0px;\n"
"background-color: #141518;\n"
"")
        icon = QIcon()
        icon.addFile(u"V2 Icons/menu_4px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_butt.setIcon(icon)
        self.menu_butt.setIconSize(QSize(100, 100))

        self.verticalLayout_2.addWidget(self.menu_butt)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_40 = QFrame(self.top_bar)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_40.setStyleSheet(u"\n"
"background-color: #474b56;")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.frame_40.setLineWidth(0)

        self.horizontalLayout.addWidget(self.frame_40)

        self.frame_top = QFrame(self.top_bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(100, 40))
        self.frame_top.setStyleSheet(u"")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_top)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(20, 20))
        self.btn_minimize.setMaximumSize(QSize(20, 20))
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minimize.setToolTipDuration(1)
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	background-color: #050505;\n"
"	border: 0px;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 255, 0);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_minimize)

        self.btn_minimize_2 = QPushButton(self.frame_top)
        self.btn_minimize_2.setObjectName(u"btn_minimize_2")
        self.btn_minimize_2.setMinimumSize(QSize(20, 20))
        self.btn_minimize_2.setMaximumSize(QSize(20, 20))
        self.btn_minimize_2.setToolTipDuration(1)
        self.btn_minimize_2.setStyleSheet(u"QPushButton{\n"
"	background-color: #050505;\n"
"	border: 0px;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 191, 0);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_minimize_2)

        self.btn_close = QPushButton(self.frame_top)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(20, 20))
        self.btn_close.setMaximumSize(QSize(20, 20))
        self.btn_close.setToolTipDuration(1)
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	background-color: #050505;\n"
"	border: 0px;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_top)


        self.drop_shadow_layout.addWidget(self.top_bar)

        self.Content = QFrame(self.drop_shadow_frame)
        self.Content.setObjectName(u"Content")
        self.Content.setStyleSheet(u"")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(50, 0))
        self.frame_left_menu.setMaximumSize(QSize(50, 498))
        self.frame_left_menu.setStyleSheet(u"background-color: #2E3440;\n"
"border-bottom-left-radius: 13px;\n"
"\n"
"")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_left_menu)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Sidebar = QFrame(self.frame_left_menu)
        self.Sidebar.setObjectName(u"Sidebar")
        self.Sidebar.setMinimumSize(QSize(50, 0))
        self.Sidebar.setMaximumSize(QSize(50, 200))
        self.Sidebar.setStyleSheet(u"background-color: #474b56;")
        self.Sidebar.setFrameShape(QFrame.NoFrame)
        self.Sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Sidebar)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.V2 = QPushButton(self.Sidebar)
        self.V2.setObjectName(u"V2")
        self.V2.setMinimumSize(QSize(170, 40))
        self.V2.setMaximumSize(QSize(50, 40))
        self.V2.setCursor(QCursor(Qt.PointingHandCursor))
        self.V2.setStyleSheet(u"QPushButton{\n"
" 	border: 0px solid;\n"
"	background-color: #474b56;\n"
"	color: #00dc82;\n"
"	font-size: 19px;\n"
"	border-radius: 0px;\n"
"	font-family: Nasalization Rg;\n"
"	padding-left: -60px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #0f111e;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"V2 Icons/image-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.V2.setIcon(icon1)
        self.V2.setIconSize(QSize(60, 60))

        self.verticalLayout_3.addWidget(self.V2)

        self.Desktop = QPushButton(self.Sidebar)
        self.Desktop.setObjectName(u"Desktop")
        self.Desktop.setMinimumSize(QSize(200, 40))
        self.Desktop.setMaximumSize(QSize(200, 40))
        self.Desktop.setCursor(QCursor(Qt.PointingHandCursor))
        self.Desktop.setStyleSheet(u"QPushButton{\n"
" 	border: 0px solid;\n"
"	background-color: #474b56;\n"
"	color: #00dc82;\n"
"	border-radius: 0px;\n"
"	font-size: 18px;\n"
"	font-family: Nasalization Rg;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #0f111e;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"V2 Icons/monitor30px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Desktop.setIcon(icon2)
        self.Desktop.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.Desktop)

        self.profile = QPushButton(self.Sidebar)
        self.profile.setObjectName(u"profile")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.profile.sizePolicy().hasHeightForWidth())
        self.profile.setSizePolicy(sizePolicy1)
        self.profile.setMinimumSize(QSize(140, 40))
        self.profile.setMaximumSize(QSize(50, 40))
        self.profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.profile.setStyleSheet(u"QPushButton{\n"
" 	border: 0px solid;\n"
"	background-color: #474b56;\n"
"	color: #00dc82;\n"
"	border-radius: 0px;\n"
"	font-size: 20px;\n"
"	font-family: Nasalization Rg;\n"
"	padding-right: -4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #0f111e;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"V2 Icons/male_user_2px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profile.setIcon(icon3)
        self.profile.setIconSize(QSize(50, 50))

        self.verticalLayout_3.addWidget(self.profile)


        self.gridLayout.addWidget(self.Sidebar, 0, 0, 1, 1)

        self.frame_14 = QFrame(self.frame_left_menu)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"background-color: #474b56;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_14, 1, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setStyleSheet(u"border-bottom-right-radius: 13px")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.frame_pages)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"")
        self.v2 = QWidget()
        self.v2.setObjectName(u"v2")
        self.v2.setStyleSheet(u"boder-bottom-right-radius: 25px;")
        self.verticalLayout_4 = QVBoxLayout(self.v2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.chat_screem = QFrame(self.v2)
        self.chat_screem.setObjectName(u"chat_screem")
        self.chat_screem.setStyleSheet(u"background-color: #141518\n"
";")
        self.chat_screem.setFrameShape(QFrame.NoFrame)
        self.chat_screem.setFrameShadow(QFrame.Raised)
        self.chat_screem.setLineWidth(0)
        self.v2logo = QPushButton(self.chat_screem)
        self.v2logo.setObjectName(u"v2logo")
        self.v2logo.setGeometry(QRect(260, 30, 411, 311))
        self.v2logo.setStyleSheet(u"border: 0 solid;\n"
"")
        self.v2logo.setIcon(icon1)
        self.v2logo.setIconSize(QSize(300, 300))
        self.recomended_tab = QFrame(self.chat_screem)
        self.recomended_tab.setObjectName(u"recomended_tab")
        self.recomended_tab.setGeometry(QRect(0, 390, 951, 35))
        self.recomended_tab.setMinimumSize(QSize(30, 25))
        self.recomended_tab.setMaximumSize(QSize(16777215, 35))
        self.recomended_tab.setStyleSheet(u"background-color: #474b56;\n"
"border-radius: 0px")
        self.recomended_tab.setFrameShape(QFrame.NoFrame)
        self.recomended_tab.setFrameShadow(QFrame.Raised)
        self.recomended_tab.setLineWidth(0)
        self.recomended_5 = QFrame(self.recomended_tab)
        self.recomended_5.setObjectName(u"recomended_5")
        self.recomended_5.setGeometry(QRect(20, 10, 120, 20))
        self.recomended_5.setStyleSheet(u"QFrame{\n"
"	background-color:#00dc82;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.recomended_5.setFrameShape(QFrame.StyledPanel)
        self.recomended_5.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.recomended_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 121, 20))
        font = QFont()
        font.setFamily(u"Nasalization Rg")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(43, 43, 43);\n"
"font-size: 11px;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.recomended_1 = QFrame(self.recomended_tab)
        self.recomended_1.setObjectName(u"recomended_1")
        self.recomended_1.setGeometry(QRect(160, 10, 120, 20))
        self.recomended_1.setStyleSheet(u"QFrame{\n"
"	background-color: #00dc82;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.recomended_1.setFrameShape(QFrame.StyledPanel)
        self.recomended_1.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.recomended_1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 121, 20))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(43, 43, 43);\n"
"font-size: 11px;\n"
"background-color: #00dc82\n"
"")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.recomended_7 = QFrame(self.recomended_tab)
        self.recomended_7.setObjectName(u"recomended_7")
        self.recomended_7.setGeometry(QRect(300, 10, 120, 20))
        self.recomended_7.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 191, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.recomended_7.setFrameShape(QFrame.StyledPanel)
        self.recomended_7.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.recomended_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 121, 20))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(43, 43, 43);\n"
"font-size: 10px;\n"
"background-color: #00dc82\n"
"")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.recomended_2 = QFrame(self.recomended_tab)
        self.recomended_2.setObjectName(u"recomended_2")
        self.recomended_2.setGeometry(QRect(430, 10, 120, 20))
        self.recomended_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 191, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.recomended_2.setFrameShape(QFrame.StyledPanel)
        self.recomended_2.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.recomended_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 0, 121, 20))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(43, 43, 43);\n"
"font-size: 11px;\n"
"background-color: #00dc82\n"
";")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.recomended_4 = QFrame(self.recomended_tab)
        self.recomended_4.setObjectName(u"recomended_4")
        self.recomended_4.setGeometry(QRect(560, 10, 120, 20))
        self.recomended_4.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 191, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.recomended_4.setFrameShape(QFrame.StyledPanel)
        self.recomended_4.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.recomended_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 0, 121, 20))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(43, 43, 43);\n"
"font-size: 11px;\n"
"background-color: #00dc82\n"
";")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.recomended_3 = QFrame(self.recomended_tab)
        self.recomended_3.setObjectName(u"recomended_3")
        self.recomended_3.setGeometry(QRect(690, 10, 120, 20))
        self.recomended_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 191, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.recomended_3.setFrameShape(QFrame.StyledPanel)
        self.recomended_3.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.recomended_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 0, 121, 20))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: rgb(43, 43, 43);\n"
"font-size: 11px;\n"
"background-color:#00dc82\n"
";")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.recomended_6 = QFrame(self.recomended_tab)
        self.recomended_6.setObjectName(u"recomended_6")
        self.recomended_6.setGeometry(QRect(820, 10, 120, 20))
        self.recomended_6.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 191, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.recomended_6.setFrameShape(QFrame.StyledPanel)
        self.recomended_6.setFrameShadow(QFrame.Raised)
        self.label_13 = QLabel(self.recomended_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 0, 121, 20))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(43, 43, 43);\n"
"font-size: 10px;\n"
"background-color: #00dc82\n"
";")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.chat_screem)

        self.down_bar = QFrame(self.v2)
        self.down_bar.setObjectName(u"down_bar")
        self.down_bar.setMaximumSize(QSize(16777215, 40))
        self.down_bar.setStyleSheet(u"background: none;\n"
"border-bottom-right-radius: 13px;")
        self.down_bar.setFrameShape(QFrame.NoFrame)
        self.down_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.down_bar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.help_bar_1 = QFrame(self.down_bar)
        self.help_bar_1.setObjectName(u"help_bar_1")
        self.help_bar_1.setMinimumSize(QSize(0, 0))
        self.help_bar_1.setStyleSheet(u"background-color:#474b56;\n"
"border-radius: 0px;\n"
"height: 50px;")
        self.help_bar_1.setFrameShape(QFrame.NoFrame)
        self.help_bar_1.setFrameShadow(QFrame.Raised)
        self.help_bar_1.setLineWidth(0)

        self.horizontalLayout_4.addWidget(self.help_bar_1)

        self.mic = QPushButton(self.down_bar)
        self.mic.setObjectName(u"mic")
        self.mic.setMinimumSize(QSize(50, 40))
        self.mic.setMaximumSize(QSize(50, 40))
        self.mic.setCursor(QCursor(Qt.PointingHandCursor))
        self.mic.setStyleSheet(u"QPushButton{\n"
"	border: 0 solid;\n"
"	border-radius: 0px;\n"
"	background-color: #474b56;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #141518;\n"
"	border-radius: 5px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"V2 Icons/microphone_2px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mic.setIcon(icon4)
        self.mic.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.mic)

        self.help_bar_2 = QFrame(self.down_bar)
        self.help_bar_2.setObjectName(u"help_bar_2")
        self.help_bar_2.setStyleSheet(u"background-color:#474b56;\n"
"border-bottom-right-radius: 16px;\n"
"height: 50px;")
        self.help_bar_2.setFrameShape(QFrame.NoFrame)
        self.help_bar_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.help_bar_2)


        self.verticalLayout_4.addWidget(self.down_bar)

        self.pages.addWidget(self.v2)
        self.theme = QWidget()
        self.theme.setObjectName(u"theme")
        self.theme_window = QFrame(self.theme)
        self.theme_window.setObjectName(u"theme_window")
        self.theme_window.setGeometry(QRect(0, 0, 951, 461))
        self.theme_window.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: #0f111e;")
        self.theme_window.setFrameShape(QFrame.StyledPanel)
        self.theme_window.setFrameShadow(QFrame.Raised)
        self.themes_label = QLabel(self.theme_window)
        self.themes_label.setObjectName(u"themes_label")
        self.themes_label.setGeometry(QRect(10, 10, 211, 31))
        self.themes_label.setFont(font)
        self.themes_label.setStyleSheet(u"color: #00dc82;\n"
"font-size: 25px;\n"
"background-color: #2E3440;\n"
"border-radius:15px;")
        self.themes_label.setFrameShadow(QFrame.Plain)
        self.themes_label.setAlignment(Qt.AlignCenter)
        self.theme_main_window = QFrame(self.theme_window)
        self.theme_main_window.setObjectName(u"theme_main_window")
        self.theme_main_window.setGeometry(QRect(10, 50, 921, 231))
        self.theme_main_window.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #2E3440;")
        self.theme_main_window.setFrameShape(QFrame.StyledPanel)
        self.theme_main_window.setFrameShadow(QFrame.Raised)
        self.light_theme = QFrame(self.theme_main_window)
        self.light_theme.setObjectName(u"light_theme")
        self.light_theme.setGeometry(QRect(320, 20, 120, 190))
        self.light_theme.setMinimumSize(QSize(120, 190))
        self.light_theme.setMaximumSize(QSize(120, 170))
        self.light_theme.setStyleSheet(u"QFrame{\n"
"	background-color:#00dc82;\n"
"	border-radius: 10px;	\n"
"}\n"
"QFrame:hover{\n"
"	\n"
"}")
        self.light_theme.setFrameShape(QFrame.StyledPanel)
        self.light_theme.setFrameShadow(QFrame.Raised)
        self.label_15 = QLabel(self.light_theme)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 110, 121, 31))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color: rgb(43, 43, 43);\n"
"font-size: 15px;")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.frame_26 = QFrame(self.light_theme)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(10, 10, 101, 91))
        self.frame_26.setStyleSheet(u"background-color:#aba8a7;")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_29 = QFrame(self.frame_26)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"background-color: #0f111e;")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_26)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_30)

        self.pushButton_17 = QPushButton(self.light_theme)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(20, 150, 81, 23))
        self.pushButton_17.setStyleSheet(u"border-radius:10px;\n"
"font: 8pt \"Nasalization Rg\";\n"
"color:#0f111e;")
        self.element_theme = QFrame(self.theme_main_window)
        self.element_theme.setObjectName(u"element_theme")
        self.element_theme.setGeometry(QRect(190, 20, 120, 190))
        self.element_theme.setMinimumSize(QSize(120, 190))
        self.element_theme.setMaximumSize(QSize(120, 190))
        self.element_theme.setStyleSheet(u"QFrame{\n"
"	background-color: #00dc82;\n"
"	border-radius: 10px;	\n"
"}\n"
"QFrame:hover{\n"
"	\n"
"}")
        self.element_theme.setFrameShape(QFrame.StyledPanel)
        self.element_theme.setFrameShadow(QFrame.Raised)
        self.frame_25 = QFrame(self.element_theme)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(10, 10, 101, 91))
        self.frame_25.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.170455 rgba(162, 0, 255, 255), stop:1 rgba(0, 81, 255, 255))")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.element_theme)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 110, 121, 31))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: rgb(43, 43, 43);\n"
"font-size: 14px;")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.pushButton_16 = QPushButton(self.element_theme)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(20, 150, 81, 23))
        self.pushButton_16.setStyleSheet(u"border-radius:10px;\n"
"font: 8pt \"Nasalization Rg\";\n"
"color: #0f111e;\n"
"")
        self.deafult_theme = QFrame(self.theme_main_window)
        self.deafult_theme.setObjectName(u"deafult_theme")
        self.deafult_theme.setGeometry(QRect(60, 20, 120, 190))
        self.deafult_theme.setMinimumSize(QSize(120, 190))
        self.deafult_theme.setMaximumSize(QSize(120, 190))
        self.deafult_theme.setStyleSheet(u"QFrame{\n"
"	background-color: #00dc82;\n"
"	border-radius: 10px;	\n"
"}\n"
"QFrame:hover{\n"
"	\n"
"}")
        self.deafult_theme.setFrameShape(QFrame.StyledPanel)
        self.deafult_theme.setFrameShadow(QFrame.Raised)
        self.frame_24 = QFrame(self.deafult_theme)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(10, 9, 101, 91))
        self.frame_24.setStyleSheet(u"background-color: #aba8a7;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_27 = QFrame(self.frame_24)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"background-color:#0f111e;")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_24)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"background-color: #2E3440;")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_28)

        self.label_2 = QLabel(self.deafult_theme)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 110, 121, 31))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(43, 43, 43);\n"
"font-size: 15px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.pushButton_15 = QPushButton(self.deafult_theme)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(20, 150, 81, 23))
        self.pushButton_15.setStyleSheet(u"border-radius:10px;\n"
"font: 8pt \"Nasalization Rg\";\n"
"color: #0f111e;")
        self.coming_soom_theme = QFrame(self.theme_main_window)
        self.coming_soom_theme.setObjectName(u"coming_soom_theme")
        self.coming_soom_theme.setGeometry(QRect(470, 30, 421, 171))
        self.coming_soom_theme.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #00dc82")
        self.coming_soom_theme.setFrameShape(QFrame.StyledPanel)
        self.coming_soom_theme.setFrameShadow(QFrame.Raised)
        self.label_20 = QLabel(self.coming_soom_theme)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(110, 70, 241, 41))
        self.label_20.setStyleSheet(u"color: #0f111e;\n"
"font-size: 25px;\n"
"font: 10pt \"Nasalization Rg\";")
        self.font_window = QFrame(self.theme_window)
        self.font_window.setObjectName(u"font_window")
        self.font_window.setGeometry(QRect(9, 289, 921, 161))
        self.font_window.setMaximumSize(QSize(16777215, 16777215))
        self.font_window.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #2E3440;")
        self.font_window.setFrameShape(QFrame.StyledPanel)
        self.font_window.setFrameShadow(QFrame.Raised)
        self.v2deafault_font = QFrame(self.font_window)
        self.v2deafault_font.setObjectName(u"v2deafault_font")
        self.v2deafault_font.setGeometry(QRect(30, 5, 150, 150))
        self.v2deafault_font.setMinimumSize(QSize(150, 150))
        self.v2deafault_font.setMaximumSize(QSize(150, 150))
        self.v2deafault_font.setStyleSheet(u"QFrame{\n"
"	background-color: #00dc82;\n"
"	border-radius: 10px;	\n"
"}\n"
"QFrame:hover{\n"
"	\n"
"}")
        self.v2deafault_font.setFrameShape(QFrame.StyledPanel)
        self.v2deafault_font.setFrameShadow(QFrame.Raised)
        self.frame_37 = QFrame(self.v2deafault_font)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setGeometry(QRect(10, 9, 131, 61))
        self.frame_37.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.pushButton_19 = QPushButton(self.frame_37)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(0, 0, 131, 61))
        self.pushButton_19.setStyleSheet(u"border-radius:10px;\n"
"font: 8pt \"Nasalization Rg\";\n"
"color: #0f111e;\n"
"background-color: #aba8a7;")
        self.label_17 = QLabel(self.v2deafault_font)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(0, 80, 151, 31))
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"color: rgb(43, 43, 43);\n"
"font-size: 15px;")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.pushButton_18 = QPushButton(self.v2deafault_font)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(20, 120, 111, 23))
        self.pushButton_18.setStyleSheet(u"border-radius:10px;\n"
"font: 8pt \"Nasalization Rg\";\n"
"color:#0f111e;")
        self.v2square_font = QFrame(self.font_window)
        self.v2square_font.setObjectName(u"v2square_font")
        self.v2square_font.setGeometry(QRect(190, 5, 150, 150))
        self.v2square_font.setMinimumSize(QSize(150, 150))
        self.v2square_font.setMaximumSize(QSize(150, 150))
        self.v2square_font.setStyleSheet(u"QFrame{\n"
"	background-color: #00dc82;\n"
"	border-radius: 10px;	\n"
"}\n"
"QFrame:hover{\n"
"	\n"
"}")
        self.v2square_font.setFrameShape(QFrame.StyledPanel)
        self.v2square_font.setFrameShadow(QFrame.Raised)
        self.frame_38 = QFrame(self.v2square_font)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setGeometry(QRect(10, 9, 131, 61))
        self.frame_38.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.pushButton_20 = QPushButton(self.frame_38)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(0, 0, 131, 61))
        self.pushButton_20.setStyleSheet(u"border-radius:10px;\n"
"font: 15pt \"Agency FB\";\n"
"color: #0f111e;\n"
"background-color: #aba8a7;")
        self.label_18 = QLabel(self.v2square_font)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 80, 151, 31))
        font1 = QFont()
        font1.setFamily(u"Agency FB")
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"color: rgb(43, 43, 43);\n"
"font: 8pt \"Agency FB\";\n"
"font-size: 15px;")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.pushButton_21 = QPushButton(self.v2square_font)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(20, 120, 111, 23))
        self.pushButton_21.setStyleSheet(u"border-radius:10px;\n"
"font: 8pt \"Nasalization Rg\";\n"
"color: #0f111e;;")
        self.element_font = QFrame(self.font_window)
        self.element_font.setObjectName(u"element_font")
        self.element_font.setGeometry(QRect(350, 5, 150, 150))
        self.element_font.setMinimumSize(QSize(150, 150))
        self.element_font.setMaximumSize(QSize(150, 150))
        self.element_font.setStyleSheet(u"QFrame{\n"
"	background-color: #00dc82;\n"
"	border-radius: 10px;	\n"
"}\n"
"QFrame:hover{\n"
"	\n"
"}")
        self.element_font.setFrameShape(QFrame.StyledPanel)
        self.element_font.setFrameShadow(QFrame.Raised)
        self.frame_39 = QFrame(self.element_font)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setGeometry(QRect(10, 9, 131, 61))
        self.frame_39.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.pushButton_22 = QPushButton(self.frame_39)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(0, 0, 131, 61))
        self.pushButton_22.setStyleSheet(u"border-radius:10px;\n"
"font: 75 15pt \"Baloo 2\";\n"
"color: #0f111e;\n"
"background-color: #aba8a7;")
        self.label_19 = QLabel(self.element_font)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(0, 80, 151, 31))
        font2 = QFont()
        font2.setFamily(u"Baloo 2")
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(9)
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"color: rgb(43, 43, 43);\n"
"font: 75 15pt \"Baloo 2\";\n"
"font-size: 15px;")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.pushButton_23 = QPushButton(self.element_font)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(20, 120, 111, 23))
        self.pushButton_23.setStyleSheet(u"border-radius:10px;\n"
"font: 8pt \"Nasalization Rg\";\n"
"color:#0f111e;")
        self.coming_soon_font = QFrame(self.font_window)
        self.coming_soon_font.setObjectName(u"coming_soon_font")
        self.coming_soon_font.setGeometry(QRect(530, 20, 371, 121))
        self.coming_soon_font.setStyleSheet(u"border-radius: 20px;\n"
"background-color: #00dc82;")
        self.coming_soon_font.setFrameShape(QFrame.StyledPanel)
        self.coming_soon_font.setFrameShadow(QFrame.Raised)
        self.label_21 = QLabel(self.coming_soon_font)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(80, 40, 241, 41))
        self.label_21.setStyleSheet(u"color: #0f111e;\n"
"font-size: 25px;\n"
"font: 10pt \"Nasalization Rg\";")
        self.pages.addWidget(self.theme)
        self.settings_2 = QWidget()
        self.settings_2.setObjectName(u"settings_2")
        self.frame_4 = QFrame(self.settings_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 951, 461))
        self.frame_4.setStyleSheet(u"background-color:#0f111e;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 201, 51))
        self.label_5.setStyleSheet(u"font: 8pt \"Nasalization\";\n"
"color: #00dc82;\n"
"background-color: #2E3440;\n"
"font-size: 25px;\n"
"border-radius: 25px;\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 80, 201, 151))
        self.frame_5.setStyleSheet(u"background-color: #2E3440;\n"
"border-radius: 15px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.Notification = QCheckBox(self.frame_5)
        self.Notification.setObjectName(u"Notification")
        self.Notification.setGeometry(QRect(10, 20, 181, 31))
        self.Notification.setStyleSheet(u"font: 12pt \"Nasalization\";\n"
"color: #0f111e;\n"
"spacing: 5px;\n"
"border-radius:15px;\n"
"background-color: #00dc82;\n"
"padding: 10px;")
        self.Notification_2 = QCheckBox(self.frame_5)
        self.Notification_2.setObjectName(u"Notification_2")
        self.Notification_2.setGeometry(QRect(10, 60, 181, 31))
        self.Notification_2.setStyleSheet(u"font: 12pt \"Nasalization\";\n"
"color: #0f111e;\n"
"spacing: 5px;\n"
"border-radius:15px;\n"
"background-color:#00dc82;\n"
"padding: 10px;")
        self.Notification_3 = QCheckBox(self.frame_5)
        self.Notification_3.setObjectName(u"Notification_3")
        self.Notification_3.setGeometry(QRect(10, 100, 181, 31))
        self.Notification_3.setStyleSheet(u"font: 12pt \"Nasalization\";\n"
"color:#0f111e;\n"
"spacing: 5px;\n"
"border-radius:15px;\n"
"background-color:#00dc82;\n"
"padding: 10px;")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(220, 290, 211, 161))
        self.frame_6.setStyleSheet(u"background-color: #2E3440;\n"
"border-radius: 15px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.commandLinkButton_3 = QCommandLinkButton(self.frame_6)
        self.commandLinkButton_3.setObjectName(u"commandLinkButton_3")
        self.commandLinkButton_3.setGeometry(QRect(10, 10, 191, 41))
        self.commandLinkButton_3.setStyleSheet(u"font: 12pt \"Nasalization\";\n"
"color:#0f111e;\n"
"background-color: #00dc82;\n"
"border-radius: 20px;")
        icon5 = QIcon()
        icon5.addFile(u"../V2 Desk Icons/lock_24px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_3.setIcon(icon5)
        self.commandLinkButton_3.setIconSize(QSize(30, 30))
        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 60, 191, 91))
        self.label_16.setStyleSheet(u"font: 10pt \"Nasalization\";\n"
"color: #0f111e;\n"
"background-color: #00dc82;\n"
"border-radius: 20px;")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(10, 240, 201, 211))
        self.frame_9.setStyleSheet(u"background-color: #2E3440;\n"
"border-radius: 15px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 141, 31))
        self.label_6.setStyleSheet(u"font: 8pt \"Nasalization\";\n"
"color: #0f111e;\n"
"background-color: #00dc82;\n"
"font-size: 25px;\n"
"border-radius: 15px;\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.radioButton_12 = QRadioButton(self.frame_9)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setGeometry(QRect(10, 60, 181, 31))
        self.radioButton_12.setStyleSheet(u"font: 12pt \"Nasalization\";\n"
"color: #0f111e;\n"
"spacing: 5px;\n"
"border-radius:15px;\n"
"background-color: #00dc82;\n"
"padding: 10px;")
        self.radioButton_13 = QRadioButton(self.frame_9)
        self.radioButton_13.setObjectName(u"radioButton_13")
        self.radioButton_13.setGeometry(QRect(10, 140, 181, 31))
        self.radioButton_13.setStyleSheet(u"font: 12pt \"Nasalization\";\n"
"color: #0f111e;\n"
"spacing: 5px;\n"
"border-radius:15px;\n"
"background-color: #00dc82;\n"
"padding: 10px;")
        self.radioButton_14 = QRadioButton(self.frame_9)
        self.radioButton_14.setObjectName(u"radioButton_14")
        self.radioButton_14.setGeometry(QRect(10, 100, 181, 31))
        self.radioButton_14.setStyleSheet(u"font: 12pt \"Nasalization\";\n"
"color: #0f111e;\n"
"spacing: 5px;\n"
"border-radius:15px;\n"
"background-color:#00dc82;\n"
"padding: 10px;")
        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(440, 290, 421, 161))
        self.frame_8.setStyleSheet(u"background-color: #2E3440;\n"
"border-radius: 15px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.commandLinkButton = QCommandLinkButton(self.frame_8)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(20, 90, 371, 41))
        self.commandLinkButton.setStyleSheet(u"font: 12pt \"Nasalization\";\n"
"color: #0f111e;\n"
"background-color:#00dc82;\n"
"border-radius: 20px;")
        icon6 = QIcon()
        icon6.addFile(u"V2 Icons/login_px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon6)
        self.commandLinkButton.setIconSize(QSize(30, 30))
        self.commandLinkButton_2 = QCommandLinkButton(self.frame_8)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")
        self.commandLinkButton_2.setGeometry(QRect(20, 30, 371, 41))
        self.commandLinkButton_2.setStyleSheet(u"font: 12pt \"Nasalization\";\n"
"color:#0f111e;\n"
"background-color:#00dc82;;\n"
"border-radius: 20px;")
        icon7 = QIcon()
        icon7.addFile(u"V2 Icons/power_off_buttn_24px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_2.setIcon(icon7)
        self.commandLinkButton_2.setIconSize(QSize(30, 30))
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(220, 80, 641, 201))
        self.frame_7.setStyleSheet(u"background-color: #2E3440;\n"
"border-radius: 15px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.tabWidget = QTabWidget(self.frame_7)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 621, 181))
        self.tabWidget.setStyleSheet(u"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"\n"
"}\n"
"QTabWidget::tab-bar {\n"
"left: 5px; /* move to the right by 5px */\n"
"}\n"
"/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"background:#00dc82;\n"
"width: 80%;\n"
"font: 8pt \"Nasalization\";\n"
"color: #0f111e;\n"
"border-radius: 8px;\n"
"min-width: 8ex;\n"
"padding: 2px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background:#00dc82;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frame_10 = QFrame(self.tab)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(-1, -1, 631, 171))
        self.frame_10.setStyleSheet(u"border-radius: 0px")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.Notification_4 = QCheckBox(self.frame_10)
        self.Notification_4.setObjectName(u"Notification_4")
        self.Notification_4.setGeometry(QRect(10, 40, 181, 31))
        self.Notification_4.setStyleSheet(u"font: 12pt \"Nasalization\";\n"
"color:#0f111e;;\n"
"spacing: 5px;\n"
"border-radius:15px;\n"
"background-color:#00dc82;\n"
"padding: 10px;")
        self.Notification_5 = QCheckBox(self.frame_10)
        self.Notification_5.setObjectName(u"Notification_5")
        self.Notification_5.setGeometry(QRect(10, 80, 181, 31))
        self.Notification_5.setStyleSheet(u"font: 12pt \"Nasalization\";\n"
"color: #0f111e;\n"
"spacing: 5px;\n"
"border-radius:15px;\n"
"background-color: #00dc82;\n"
"padding: 10px;")
        self.Notification_6 = QCheckBox(self.frame_10)
        self.Notification_6.setObjectName(u"Notification_6")
        self.Notification_6.setGeometry(QRect(200, 80, 201, 31))
        self.Notification_6.setStyleSheet(u"font: 12pt \"Nasalization\";\n"
"color: #0f111e;\n"
"spacing: 5px;\n"
"border-radius:15px;\n"
"background-color: #00dc82;\n"
"padding: 10px;")
        self.Notification_7 = QCheckBox(self.frame_10)
        self.Notification_7.setObjectName(u"Notification_7")
        self.Notification_7.setGeometry(QRect(200, 40, 201, 31))
        self.Notification_7.setStyleSheet(u"font: 12pt \"Nasalization\";\n"
"color:r#0f111e;\n"
"spacing: 5px;\n"
"border-radius:15px;\n"
"background-color: #00dc82;\n"
"padding: 10px;")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_11 = QFrame(self.tab_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(0, 0, 621, 171))
        self.frame_11.setStyleSheet(u"border-radius: 0px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.Notification_8 = QCheckBox(self.frame_11)
        self.Notification_8.setObjectName(u"Notification_8")
        self.Notification_8.setGeometry(QRect(10, 30, 201, 31))
        self.Notification_8.setStyleSheet(u"font: 12pt \"Nasalization\";\n"
"color: #0f111e;;\n"
"spacing: 5px;\n"
"border-radius:15px;\n"
"background-color: #00dc82;\n"
"padding: 10px;")
        self.Notification_9 = QCheckBox(self.frame_11)
        self.Notification_9.setObjectName(u"Notification_9")
        self.Notification_9.setGeometry(QRect(220, 30, 191, 31))
        self.Notification_9.setStyleSheet(u"font: 12pt \"Nasalization\";\n"
"color: #0f111e;\n"
"spacing: 5px;\n"
"border-radius:15px;\n"
"background-color:#00dc82;\n"
"padding: 10px;")
        self.Notification_10 = QCheckBox(self.frame_11)
        self.Notification_10.setObjectName(u"Notification_10")
        self.Notification_10.setGeometry(QRect(10, 70, 201, 31))
        self.Notification_10.setStyleSheet(u"font: 12pt \"Nasalization\";\n"
"color: #0f111e;\n"
"spacing: 5px;\n"
"border-radius:15px;\n"
"background-color: #00dc82;\n"
"padding: 10px;")
        self.Notification_11 = QCheckBox(self.frame_11)
        self.Notification_11.setObjectName(u"Notification_11")
        self.Notification_11.setGeometry(QRect(220, 70, 191, 31))
        self.Notification_11.setStyleSheet(u"font: 12pt \"Nasalization\";\n"
"color:#0f111e;\n"
"spacing: 5px;\n"
"border-radius:15px;\n"
"background-color: #00dc82;\n"
"padding: 10px;")
        self.tabWidget.addTab(self.tab_2, "")
        self.pages.addWidget(self.settings_2)
        self.Profile = QWidget()
        self.Profile.setObjectName(u"Profile")
        self.frame_12 = QFrame(self.Profile)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(0, 0, 951, 461))
        self.frame_12.setStyleSheet(u"background-color: #0f111e;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(300, 80, 331, 361))
        self.frame_13.setStyleSheet(u"background-color:#2E3440;\n"
"border-radius: 20px")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.label_22 = QLabel(self.frame_13)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 110, 311, 31))
        self.label_22.setStyleSheet(u"background-color:#aba8a7;\n"
"border-radius: 10px;\n"
"font: 8pt \"Nasalization\";\n"
"color:#0f111e;\n"
"padding: 5px;")
        self.label_23 = QLabel(self.frame_13)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 190, 311, 31))
        self.label_23.setStyleSheet(u"background-color: #aba8a7;\n"
"border-radius: 10px;\n"
"font: 8pt \"Nasalization\";\n"
"color: #0f111e;\n"
"padding: 10px;")
        self.label_24 = QLabel(self.frame_13)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(0, 70, 331, 31))
        self.label_24.setStyleSheet(u"\n"
"border-radius: 10px;\n"
"font: 8pt \"Nasalization\";\n"
"color: #0f111e;\n"
"padding: 10px;")
        self.label_26 = QLabel(self.frame_13)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(0, 150, 331, 31))
        self.label_26.setStyleSheet(u"\n"
"border-radius: 10px;\n"
"font: 8pt \"Nasalization\";\n"
"color: #0f111e;\n"
"padding: 10px;")
        self.pushButton_4 = QPushButton(self.frame_12)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(410, 20, 111, 111))
        self.pushButton_4.setStyleSheet(u"border-radius: 55%;\n"
"background-color: #111;")
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(80, 80))
        self.pages.addWidget(self.Profile)
        self.Console = QWidget()
        self.Console.setObjectName(u"Console")
        self.frame_34 = QFrame(self.Console)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setGeometry(QRect(0, 0, 951, 461))
        self.frame_34.setStyleSheet(u"background-color: rgb(17, 17, 17);")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_34)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"background-color: rgb(15, 17, 30);")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.textEdit = QTextEdit(self.frame_35)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 400, 901, 31))
        self.textEdit.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.textEdit.setStyleSheet(u"background-color: #2E3440;\n"
"border-radius: 15px;\n"
"font: 11pt \"Nasalization\";\n"
"color:#00dc82;")
        self.label_3 = QLabel(self.frame_35)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 201, 51))
        self.label_3.setStyleSheet(u"font: 8pt \"Nasalization\";\n"
"color: #00dc82;\n"
"background-color: #2E3440;\n"
"font-size: 25px;\n"
"border-radius: 25px;\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frame_35)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 80, 901, 311))
        self.label_4.setStyleSheet(u"font: 8pt \"Nasalization\";\n"
"color: #00dc82;\n"
"background-color: #2E3440;\n"
"font-size: 25px;\n"
"border-radius: 15px;\n"
"")
        self.label_4.setFrameShape(QFrame.Panel)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.frame_35)

        self.pages.addWidget(self.Console)
        self.Desktop_2 = QWidget()
        self.Desktop_2.setObjectName(u"Desktop_2")
        self.Desktop_2.setStyleSheet(u"background-color: rgb(17, 17, 17);\n"
"border-bottom-right-radius: 13px;")
        self.frame_2 = QFrame(self.Desktop_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 951, 511))
        self.frame_2.setStyleSheet(u"border-bottom-right-radius: 13px;\n"
"background-color: rgb(15, 17, 30);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.calc = QPushButton(self.frame_2)
        self.calc.setObjectName(u"calc")
        self.calc.setGeometry(QRect(890, 70, 40, 40))
        self.calc.setMinimumSize(QSize(40, 40))
        self.calc.setMaximumSize(QSize(40, 40))
        self.calc.setCursor(QCursor(Qt.PointingHandCursor))
        self.calc.setStyleSheet(u"background-color:#2E3440;\n"
"border: none;\n"
"border-radius: 8px;")
        icon8 = QIcon()
        icon8.addFile(u"V2 Icons/calculator4px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calc.setIcon(icon8)
        self.calc.setIconSize(QSize(30, 30))
        self.calc_2 = QPushButton(self.frame_2)
        self.calc_2.setObjectName(u"calc_2")
        self.calc_2.setGeometry(QRect(890, 170, 40, 40))
        self.calc_2.setMinimumSize(QSize(40, 40))
        self.calc_2.setMaximumSize(QSize(40, 40))
        self.calc_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.calc_2.setStyleSheet(u"background-color: #2E3440;\n"
"border: none;\n"
"border-radius: 8px;")
        icon9 = QIcon()
        icon9.addFile(u"V2 Icons/private_folderpx.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calc_2.setIcon(icon9)
        self.calc_2.setIconSize(QSize(30, 30))
        self.calc_3 = QPushButton(self.frame_2)
        self.calc_3.setObjectName(u"calc_3")
        self.calc_3.setGeometry(QRect(890, 120, 40, 40))
        self.calc_3.setMinimumSize(QSize(40, 40))
        self.calc_3.setMaximumSize(QSize(40, 40))
        self.calc_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.calc_3.setStyleSheet(u"background-color: #2E3440;\n"
"border: none;\n"
"border-radius: 8px;")
        icon10 = QIcon()
        icon10.addFile(u"V2 Icons/music_video_0px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calc_3.setIcon(icon10)
        self.calc_3.setIconSize(QSize(20, 20))
        self.calc_4 = QPushButton(self.frame_2)
        self.calc_4.setObjectName(u"calc_4")
        self.calc_4.setGeometry(QRect(890, 20, 40, 40))
        self.calc_4.setMinimumSize(QSize(40, 40))
        self.calc_4.setMaximumSize(QSize(40, 40))
        self.calc_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.calc_4.setStyleSheet(u"background-color: #2E3440;\n"
"border: none;\n"
"border-radius: 8px;")
        icon11 = QIcon()
        icon11.addFile(u"V2 Icons/record_px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calc_4.setIcon(icon11)
        self.calc_4.setIconSize(QSize(30, 30))
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(370, 390, 211, 41))
        self.frame_3.setStyleSheet(u"background-color: #2E3440;\n"
"border-radius:20px;\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.calc_9 = QPushButton(self.frame_3)
        self.calc_9.setObjectName(u"calc_9")
        self.calc_9.setGeometry(QRect(0, 0, 40, 40))
        self.calc_9.setMinimumSize(QSize(40, 40))
        self.calc_9.setMaximumSize(QSize(40, 40))
        self.calc_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.calc_9.setStyleSheet(u"background-color: #2E3440;\n"
"border: none;\n"
"border-top-left-radius:19px;\n"
"border-bottom-left-radius:19px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;")
        self.calc_9.setIcon(icon1)
        self.calc_9.setIconSize(QSize(40, 40))
        self.calc_11 = QPushButton(self.frame_3)
        self.calc_11.setObjectName(u"calc_11")
        self.calc_11.setGeometry(QRect(40, 0, 40, 40))
        self.calc_11.setMinimumSize(QSize(40, 40))
        self.calc_11.setMaximumSize(QSize(40, 40))
        self.calc_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.calc_11.setStyleSheet(u"background-color:#2E3440;;\n"
"border: none;\n"
"border-radius: 0px;")
        icon12 = QIcon()
        icon12.addFile(u"V2 Icons/shopping_bag_px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calc_11.setIcon(icon12)
        self.calc_11.setIconSize(QSize(30, 30))
        self.calc_12 = QPushButton(self.frame_3)
        self.calc_12.setObjectName(u"calc_12")
        self.calc_12.setGeometry(QRect(80, 0, 40, 40))
        self.calc_12.setMinimumSize(QSize(40, 40))
        self.calc_12.setMaximumSize(QSize(40, 40))
        self.calc_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.calc_12.setStyleSheet(u"background-color: #2E3440;\n"
"border: none;\n"
"border-radius: 0px;")
        icon13 = QIcon()
        icon13.addFile(u"V2 Icons/opened_folder_5x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calc_12.setIcon(icon13)
        self.calc_12.setIconSize(QSize(24, 24))
        self.calc_13 = QPushButton(self.frame_3)
        self.calc_13.setObjectName(u"calc_13")
        self.calc_13.setGeometry(QRect(120, 0, 40, 40))
        self.calc_13.setMinimumSize(QSize(40, 40))
        self.calc_13.setMaximumSize(QSize(40, 40))
        self.calc_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.calc_13.setStyleSheet(u"background-color: #2E3440;\n"
"border: none;\n"
"border-radius: 0px;")
        icon14 = QIcon()
        icon14.addFile(u"V2 Icons/cloudpx.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calc_13.setIcon(icon14)
        self.calc_13.setIconSize(QSize(30, 30))
        self.calc_14 = QPushButton(self.frame_3)
        self.calc_14.setObjectName(u"calc_14")
        self.calc_14.setGeometry(QRect(160, 0, 40, 40))
        self.calc_14.setMinimumSize(QSize(40, 40))
        self.calc_14.setMaximumSize(QSize(40, 40))
        self.calc_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.calc_14.setStyleSheet(u"background-color: #2E3440;\n"
"border: none;\n"
"border-radius: 8px;")
        icon15 = QIcon()
        icon15.addFile(u"V2 Icons/update_px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calc_14.setIcon(icon15)
        self.calc_14.setIconSize(QSize(30, 30))
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 0, 951, 461))
        icon16 = QIcon()
        icon16.addFile(u"V2 Icons/jakob-owens-EwRM05V0VSI-unsplash.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon16)
        self.pushButton.setIconSize(QSize(1000, 1000))
        self.pushButton.raise_()
        self.frame_3.raise_()
        self.calc.raise_()
        self.calc_4.raise_()
        self.calc_3.raise_()
        self.calc_2.raise_()
        self.pages.addWidget(self.Desktop_2)

        self.verticalLayout_5.addWidget(self.pages)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.drop_shadow_layout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.drop_shadow_frame)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"v2", None))
        self.menu_butt.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize_2.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize_2.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.V2.setText(QCoreApplication.translate("MainWindow", u"Mars", None))
        self.Desktop.setText(QCoreApplication.translate("MainWindow", u"    Mars Desktop", None))
        self.profile.setText(QCoreApplication.translate("MainWindow", u"    Profile", None))
        self.v2logo.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Google", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Open AppName", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Send Whatapp Msg", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"YouTube", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"When is My Bday", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"What's The Time", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"My Current Location", None))
        self.mic.setText("")
        self.themes_label.setText(QCoreApplication.translate("MainWindow", u"Themes", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"MARS Light", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Select ", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Element Styled", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Select ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MARS Default", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Select ", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Custom Theme Comming soon...", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Abcd Xyz", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"M Default Font", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Select ", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Abcd Xyz", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"MARS Square", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Select ", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Abcd Xyz", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Element Styled", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Select ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Custom Font Comming soon...", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.Notification.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.Notification_2.setText(QCoreApplication.translate("MainWindow", u"Audio Spectrum", None))
        self.Notification_3.setText(QCoreApplication.translate("MainWindow", u"Noise Supresion", None))
        self.commandLinkButton_3.setText(QCoreApplication.translate("MainWindow", u"Privacy", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Your Data Is Protected", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Graphics", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"Ultra", None))
        self.radioButton_13.setText(QCoreApplication.translate("MainWindow", u"Low", None))
        self.radioButton_14.setText(QCoreApplication.translate("MainWindow", u"HiGh", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.commandLinkButton_2.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.Notification_4.setText(QCoreApplication.translate("MainWindow", u"Ai Assist", None))
        self.Notification_5.setText(QCoreApplication.translate("MainWindow", u"Post ProcessinG", None))
        self.Notification_6.setText(QCoreApplication.translate("MainWindow", u"Boot Accelertion", None))
        self.Notification_7.setText(QCoreApplication.translate("MainWindow", u"AI acceleration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Mars", None))
        self.Notification_8.setText(QCoreApplication.translate("MainWindow", u"v2 APP Boost", None))
        self.Notification_9.setText(QCoreApplication.translate("MainWindow", u"Smooth transition", None))
        self.Notification_10.setText(QCoreApplication.translate("MainWindow", u"Cloud acceleration", None))
        self.Notification_11.setText(QCoreApplication.translate("MainWindow", u"Ai Presence", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Desktop", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"_sh\u039bdoww", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"UserName", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"PassWord", None))
        self.pushButton_4.setText("")
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  type your Command...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Console", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"    M.A.R.S:Welcome to console type your commands", None))
        self.calc.setText("")
        self.calc_2.setText("")
        self.calc_3.setText("")
        self.calc_4.setText("")
        self.calc_9.setText("")
        self.calc_11.setText("")
        self.calc_12.setText("")
        self.calc_13.setText("")
        self.calc_14.setText("")
        self.pushButton.setText("")
    # retranslateUi

