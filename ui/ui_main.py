# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainHpGsNM.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1420, 822)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"\n"
"background-color: qlineargradient(spread:pad, x1:0.670455, y1:0.812, x2:0, y2:0.471, stop:0 rgba(35, 134, 244, 244), stop:1 rgba(55, 193, 255, 255));\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.619, y1:0.875, x2:0.023, y2:0.0339545, stop:0 rgba(25, 118, 221, 255), stop:0.556818 rgba(3, 169, 244, 255));\n"
"\n"
"background-color :qlineargradient(spread:pad, x1:0.71, y1:0.982955, x2:0, y2:0.051, stop:0 rgba(25, 118, 221, 255), stop:0.6875 rgba(3, 169, 244, 255));")
        self.welcome = QWidget()
        self.welcome.setObjectName(u"welcome")
        self.welcome.setStyleSheet(u"border:none;")
        self.verticalLayout_2 = QVBoxLayout(self.welcome)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 145, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.welcome)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 100))
        self.frame_2.setStyleSheet(u"background-color:transparent;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(527, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(129, 0))
        self.label.setStyleSheet(u"background-color: rgba(217, 217, 217,.5);\n"
"color: rgb(183, 183, 183);")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(527, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.welcome)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setStyleSheet(u"background-color:transparent;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-family: Proxima Nova;\n"
"font-size: 28px;\n"
"font-weight: 700;\n"
"line-height: 34.1px;\n"
"text-align: center;\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(291, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(600, 0))
        self.label_3.setMaximumSize(QSize(600, 16777215))
        self.label_3.setStyleSheet(u"font-family: Proxima Nova;\n"
"font-size: 16px;\n"
"font-weight: 400;\n"
"line-height: 16px;\n"
"text-align: center;\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(290, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.welcome)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 70))
        self.frame_4.setStyleSheet(u"background-color:transparent;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(503, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.get_started = QPushButton(self.frame_4)
        self.get_started.setObjectName(u"get_started")
        self.get_started.setMinimumSize(QSize(177, 64))
        self.get_started.setCursor(QCursor(Qt.PointingHandCursor))
        self.get_started.setStyleSheet(u"font-family: Proxima Nova;\n"
"font-size: 16px;\n"
"font-weight: 700;\n"
"line-height: 16px;\n"
"text-align: center;\n"
"color: rgb(255, 255, 255);\n"
"background: #03A9F4;\n"
"border :none;\n"
"border-radius:4px;")

        self.horizontalLayout_3.addWidget(self.get_started)

        self.horizontalSpacer_6 = QSpacerItem(503, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.verticalSpacer_2 = QSpacerItem(20, 144, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.welcome)
        self.log = QWidget()
        self.log.setObjectName(u"log")
        self.gridLayout = QGridLayout(self.log)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(422, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.frame_6 = QFrame(self.log)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(360, 600))
        self.frame_6.setMaximumSize(QSize(360, 16777215))
        self.frame_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 144))
        self.frame_7.setMaximumSize(QSize(16777215, 144))
        self.frame_7.setStyleSheet(u"background-color: rgb(238, 238, 238);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 15)
        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_11)

        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setStyleSheet(u"font-family: Proxima Nova;\n"
"font-size: 22px;\n"
"font-weight: 400;\n"
"line-height: 22px;\n"
"text-align: left;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 50))
        self.frame_8.setMaximumSize(QSize(16777215, 50))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.logIn_tab = QRadioButton(self.frame_8)
        self.logIn_tab.setObjectName(u"logIn_tab")
        self.logIn_tab.setMinimumSize(QSize(100, 38))
        self.logIn_tab.setMaximumSize(QSize(14566, 50))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setBold(False)
        font.setItalic(False)
        self.logIn_tab.setFont(font)
        self.logIn_tab.setCursor(QCursor(Qt.PointingHandCursor))
        self.logIn_tab.setLayoutDirection(Qt.LeftToRight)
        self.logIn_tab.setStyleSheet(u"\n"
"QRadioButton{ \n"
"/*background-color :  transparent;*/\n"
"border : none ;\n"
"padding-left : 0px;\n"
"color : #242B2E;\n"
"font-family: 'Poppins';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
"text-align:center;\n"
"border-radius:0ox;\n"
"border-bottom:2px solid #eeeeee;\n"
" }\n"
"\n"
"QRadioButton:hover{\n"
"background: #eeeeee;\n"
"\n"
"}\n"
"QRadioButton:checked{\n"
"background-color : rgb(255, 255, 255) ;\n"
"color: rgb(0, 0, 0);\n"
"border-bottom:2px solid black;\n"
"}\n"
"QRadioButton::indicator {\n"
"width: 0px;\n"
"height: 0px;\n"
"border-radius: 0px;\n"
" }")
        self.logIn_tab.setIconSize(QSize(30, 30))
        self.logIn_tab.setChecked(True)
        self.logIn_tab.setAutoRepeat(False)

        self.horizontalLayout_8.addWidget(self.logIn_tab)

        self.signUp_tab = QRadioButton(self.frame_8)
        self.signUp_tab.setObjectName(u"signUp_tab")
        self.signUp_tab.setMinimumSize(QSize(100, 38))
        self.signUp_tab.setMaximumSize(QSize(14566, 50))
        self.signUp_tab.setFont(font)
        self.signUp_tab.setCursor(QCursor(Qt.PointingHandCursor))
        self.signUp_tab.setLayoutDirection(Qt.LeftToRight)
        self.signUp_tab.setStyleSheet(u"\n"
"QRadioButton{ \n"
"background-color :  transparent;\n"
"border : none ;\n"
"padding-left : 0px;\n"
"color : #242B2E;\n"
"font-family: 'Poppins';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
"text-align:center;\n"
"border-radius:0ox;\n"
"border-bottom:2px solid #eeeeee;\n"
" }\n"
"\n"
"QRadioButton:hover{\n"
"background: #eeeeee;\n"
"\n"
"}\n"
"QRadioButton:checked{\n"
"background-color : rgb(255, 255, 255) ;\n"
"color: rgb(0, 0, 0);\n"
"border-bottom:2px solid black;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 0px;\n"
"height: 0px;\n"
"border-radius: 0px;\n"
" }")
        self.signUp_tab.setIconSize(QSize(0, 0))
        self.signUp_tab.setChecked(False)

        self.horizontalLayout_8.addWidget(self.signUp_tab)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.stackedWidget_2 = QStackedWidget(self.frame_6)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"background-color: transparent;")
        self.gridLayout_2 = QGridLayout(self.login)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.login)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 83))
        self.frame_10.setMaximumSize(QSize(16777215, 83))
        self.frame_10.setStyleSheet(u"background-color: rgb(3, 169, 244);\n"
"border-bottom-left-radius : 10px;\n"
"border-bottom-right-radius : 10px;\n"
"border-top-left-radius : 0px;\n"
"border-top-right-radius : 0px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logIn_btn = QPushButton(self.frame_10)
        self.logIn_btn.setObjectName(u"logIn_btn")
        self.logIn_btn.setMinimumSize(QSize(147, 72))
        self.logIn_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.logIn_btn.setStyleSheet(u"font-family: Proxima Nova;\n"
"font-size: 18px;\n"
"font-weight: 400;\n"
"line-height: 18px;\n"
"text-align: left;\n"
"color: rgb(255, 255, 255);\n"
"text-align:center;")

        self.horizontalLayout_4.addWidget(self.logIn_btn)


        self.gridLayout_2.addWidget(self.frame_10, 2, 0, 1, 1)

        self.frame_9 = QFrame(self.login)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setSpacing(11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(22, 22, 22, 22)
        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.log_google = QPushButton(self.frame_12)
        self.log_google.setObjectName(u"log_google")
        self.log_google.setMinimumSize(QSize(55, 53))
        self.log_google.setStyleSheet(u"font-family: Proxima Nova;\n"
"color: rgb(0, 0, 0);\n"
"font-size: 15px;\n"
"font-weight: 400;\n"
"line-height: 15px;\n"
"text-align: left;\n"
"border:1px solid #F1F1F1;\n"
"padding-left :15px\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/google.png", QSize(), QIcon.Normal, QIcon.Off)
        self.log_google.setIcon(icon)
        self.log_google.setIconSize(QSize(26, 26))

        self.horizontalLayout_9.addWidget(self.log_google)


        self.verticalLayout_6.addWidget(self.frame_12)

        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))
        self.label_5.setStyleSheet(u"font-family: Proxima Nova;\n"
"color: rgb(0, 0, 0);\n"
"font-size: 15px;\n"
"font-weight: 400;\n"
"line-height: 15px;\n"
"text-align: left;\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.frame_13)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(200, 50))
        self.frame_42.setMaximumSize(QSize(560, 60))
        self.frame_42.setStyleSheet(u"border: 1px solid #F1F1F1")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_33.setSpacing(13)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_42)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(50, 50))
        self.frame_15.setStyleSheet(u"background: #F1F1F1;\n"
"border:none;\n"
"  border-bottom-right-radius:0px;\n"
"  border-top-right-radius:0px;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_15)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_6 = QLabel(self.frame_15)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/icons/assets/icons/credit-card-02.png"))

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)


        self.horizontalLayout_33.addWidget(self.frame_15)

        self.email_log = QLineEdit(self.frame_42)
        self.email_log.setObjectName(u"email_log")
        self.email_log.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setFamilies([u"Proxima Nova"])
        font1.setBold(False)
        self.email_log.setFont(font1)
        self.email_log.setLayoutDirection(Qt.RightToLeft)
        self.email_log.setStyleSheet(u"font-family: Proxima Nova;\n"
"color: rgb(71, 71, 71);\n"
"font-size: 15px;\n"
"font-weight: 400;\n"
"line-height: 15px;\n"
"text-align: left;\n"
"border:none")
        self.email_log.setMaxLength(32757)

        self.horizontalLayout_33.addWidget(self.email_log)

        self.frame_18 = QFrame(self.frame_42)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(50, 0))
        self.frame_18.setStyleSheet(u"border:none")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_33.addWidget(self.frame_18)


        self.horizontalLayout_10.addWidget(self.frame_42)


        self.verticalLayout_6.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.frame_14)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(200, 50))
        self.frame_43.setMaximumSize(QSize(560, 60))
        self.frame_43.setStyleSheet(u"border: 1px solid #F1F1F1")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_34.setSpacing(13)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 18, 0)
        self.frame_17 = QFrame(self.frame_43)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(50, 50))
        self.frame_17.setStyleSheet(u"background: #F1F1F1;\n"
"border:none;\n"
"  border-bottom-right-radius:0px;\n"
"  border-top-right-radius:0px;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_17)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_7 = QLabel(self.frame_17)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u":/icons/assets/icons/lock-01.png"))

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)


        self.horizontalLayout_34.addWidget(self.frame_17)

        self.pass_log = QLineEdit(self.frame_43)
        self.pass_log.setObjectName(u"pass_log")
        self.pass_log.setMinimumSize(QSize(0, 50))
        self.pass_log.setLayoutDirection(Qt.RightToLeft)
        self.pass_log.setStyleSheet(u"font-family: Proxima Nova;\n"
"color: rgb(102, 102, 102);\n"
"font-size: 15px;\n"
"font-weight: 400;\n"
"line-height: 15px;\n"
"text-align: left;\n"
"border:none")

        self.horizontalLayout_34.addWidget(self.pass_log)


        self.horizontalLayout_11.addWidget(self.frame_43)


        self.verticalLayout_6.addWidget(self.frame_14)

        self.frame_16 = QFrame(self.frame_9)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_16)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_4 = QPushButton(self.frame_16)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"font-family: Proxima Nova;\n"
"color: rgb(0, 0, 0);\n"
"font-size: 15px;\n"
"font-weight: 400;\n"
"line-height: 15px;\n"
"text-align: center;\n"
"")

        self.gridLayout_5.addWidget(self.pushButton_4, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_16)


        self.gridLayout_2.addWidget(self.frame_9, 1, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.login)
        self.signup = QWidget()
        self.signup.setObjectName(u"signup")
        self.signup.setStyleSheet(u"background-color: transparent;")
        self.verticalLayout_12 = QVBoxLayout(self.signup)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.signup)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_40)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_45 = QFrame(self.frame_40)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(200, 50))
        self.frame_45.setMaximumSize(QSize(560, 60))
        self.frame_45.setStyleSheet(u"border: 1px solid #F1F1F1")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_39.setSpacing(13)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.frame_45)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(50, 50))
        self.frame_37.setStyleSheet(u"background: #F1F1F1;\n"
"border:none;\n"
"  border-bottom-right-radius:0px;\n"
"  border-top-right-radius:0px;")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_37)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_20 = QLabel(self.frame_37)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setPixmap(QPixmap(u":/icons/assets/icons/credit-card-02.png"))

        self.gridLayout_12.addWidget(self.label_20, 0, 0, 1, 1)


        self.horizontalLayout_39.addWidget(self.frame_37)

        self.email_sign = QLineEdit(self.frame_45)
        self.email_sign.setObjectName(u"email_sign")
        self.email_sign.setMinimumSize(QSize(0, 50))
        self.email_sign.setFont(font1)
        self.email_sign.setLayoutDirection(Qt.RightToLeft)
        self.email_sign.setStyleSheet(u"font-family: Proxima Nova;\n"
"color: rgb(71, 71, 71);\n"
"font-size: 15px;\n"
"font-weight: 400;\n"
"line-height: 15px;\n"
"text-align: left;\n"
"border:none")
        self.email_sign.setMaxLength(32757)

        self.horizontalLayout_39.addWidget(self.email_sign)

        self.frame_38 = QFrame(self.frame_45)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(50, 0))
        self.frame_38.setStyleSheet(u"border:none")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_39.addWidget(self.frame_38)


        self.verticalLayout_11.addWidget(self.frame_45)

        self.frame_44 = QFrame(self.frame_40)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(200, 50))
        self.frame_44.setMaximumSize(QSize(560, 60))
        self.frame_44.setStyleSheet(u"border: 1px solid #F1F1F1")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_36.setSpacing(13)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 18, 0)
        self.frame_33 = QFrame(self.frame_44)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(50, 50))
        self.frame_33.setStyleSheet(u"background: #F1F1F1;\n"
"border:none;\n"
"  border-bottom-right-radius:0px;\n"
"  border-top-right-radius:0px;")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_33)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_17 = QLabel(self.frame_33)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setPixmap(QPixmap(u":/icons/assets/icons/lock-01.png"))

        self.gridLayout_9.addWidget(self.label_17, 0, 0, 1, 1)


        self.horizontalLayout_36.addWidget(self.frame_33)

        self.pass_sign = QLineEdit(self.frame_44)
        self.pass_sign.setObjectName(u"pass_sign")
        self.pass_sign.setMinimumSize(QSize(0, 50))
        self.pass_sign.setLayoutDirection(Qt.RightToLeft)
        self.pass_sign.setStyleSheet(u"font-family: Proxima Nova;\n"
"color: rgb(102, 102, 102);\n"
"font-size: 15px;\n"
"font-weight: 400;\n"
"line-height: 15px;\n"
"text-align: left;\n"
"border:none")

        self.horizontalLayout_36.addWidget(self.pass_sign)


        self.verticalLayout_11.addWidget(self.frame_44)

        self.frame_46 = QFrame(self.frame_40)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(200, 50))
        self.frame_46.setMaximumSize(QSize(560, 60))
        self.frame_46.setStyleSheet(u"border: 1px solid #F1F1F1")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_40.setSpacing(13)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 18, 0)
        self.frame_39 = QFrame(self.frame_46)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(50, 50))
        self.frame_39.setStyleSheet(u"background: #F1F1F1;\n"
"border:none;\n"
"  border-bottom-right-radius:0px;\n"
"  border-top-right-radius:0px;")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_39)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_21 = QLabel(self.frame_39)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setPixmap(QPixmap(u":/icons/assets/icons/lock-01.png"))

        self.gridLayout_14.addWidget(self.label_21, 0, 0, 1, 1)


        self.horizontalLayout_40.addWidget(self.frame_39)

        self.repass_sign = QLineEdit(self.frame_46)
        self.repass_sign.setObjectName(u"repass_sign")
        self.repass_sign.setMinimumSize(QSize(0, 50))
        self.repass_sign.setLayoutDirection(Qt.RightToLeft)
        self.repass_sign.setStyleSheet(u"font-family: Proxima Nova;\n"
"color: rgb(102, 102, 102);\n"
"font-size: 15px;\n"
"font-weight: 400;\n"
"line-height: 15px;\n"
"text-align: left;\n"
"border:none")

        self.horizontalLayout_40.addWidget(self.repass_sign)


        self.verticalLayout_11.addWidget(self.frame_46)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)


        self.verticalLayout_12.addWidget(self.frame_40)

        self.frame_36 = QFrame(self.signup)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(0, 83))
        self.frame_36.setMaximumSize(QSize(16777215, 83))
        self.frame_36.setStyleSheet(u"background-color: rgb(3, 169, 244);\n"
"border-bottom-left-radius : 10px;\n"
"border-bottom-right-radius : 10px;\n"
"border-top-left-radius : 0px;\n"
"border-top-right-radius : 0px;")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.logIn_btn_2 = QPushButton(self.frame_36)
        self.logIn_btn_2.setObjectName(u"logIn_btn_2")
        self.logIn_btn_2.setMinimumSize(QSize(147, 72))
        self.logIn_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.logIn_btn_2.setStyleSheet(u"font-family: Proxima Nova;\n"
"font-size: 18px;\n"
"font-weight: 400;\n"
"line-height: 18px;\n"
"text-align: left;\n"
"color: rgb(255, 255, 255);\n"
"text-align:center;")

        self.horizontalLayout_5.addWidget(self.logIn_btn_2)


        self.verticalLayout_12.addWidget(self.frame_36)

        self.stackedWidget_2.addWidget(self.signup)

        self.verticalLayout_4.addWidget(self.stackedWidget_2)


        self.gridLayout.addWidget(self.frame_6, 1, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.log)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_7 = QVBoxLayout(self.home)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.home)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_21)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 30)
        self.frame_19 = QFrame(self.frame_21)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 0))
        self.frame_19.setMaximumSize(QSize(16777215, 67))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(50, 0, 0, 0)
        self.label_8 = QLabel(self.frame_19)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(67, 67))
        self.label_8.setStyleSheet(u"background: rgba(217, 217, 217,.5);\n"
"border-radius: 6px 0px 0px 0px;\n"
"\n"
"")

        self.horizontalLayout_12.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_19)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font-family: Proxima Nova;\n"
"color: rgb(0, 0, 0);\n"
"font-size: 20px;\n"
"font-weight: 400;\n"
"line-height: 20px;\n"
"text-align: center;\n"
"")

        self.horizontalLayout_12.addWidget(self.label_9)

        self.horizontalSpacer_9 = QSpacerItem(948, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)


        self.verticalLayout_8.addWidget(self.frame_19)

        self.label_10 = QLabel(self.frame_21)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 70))
        self.label_10.setMaximumSize(QSize(16777215, 65))
        self.label_10.setStyleSheet(u"font-family: Proxima Nova;\n"
"font-size: 28px;\n"
"font-weight: 700;\n"
"line-height: 28px;\n"
"text-align: center;\n"
"color: #03A9F4;\n"
"")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_10)

        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_10 = QSpacerItem(263, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)

        self.drag_frame = QFrame(self.frame_22)
        self.drag_frame.setObjectName(u"drag_frame")
        self.drag_frame.setMinimumSize(QSize(572, 178))
        self.drag_frame.setMaximumSize(QSize(16777215, 180))
        self.drag_frame.setStyleSheet(u"background: rgba(3, 169, 244, 0.05);\n"
"\n"
"\n"
"border: 2px dashed #03A9F4;")
        self.drag_frame.setFrameShape(QFrame.StyledPanel)
        self.drag_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.drag_frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.drag_frame)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"border:none;\n"
"background-color:transparent;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 15, 0, 10)
        self.horizontalSpacer_12 = QSpacerItem(297, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_12)

        self.label_11 = QLabel(self.frame_25)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setPixmap(QPixmap(u":/icons/assets/icons/upload-cloud-02.png"))

        self.horizontalLayout_14.addWidget(self.label_11)

        self.horizontalSpacer_13 = QSpacerItem(297, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_13)


        self.verticalLayout_9.addWidget(self.frame_25)

        self.label_12 = QLabel(self.drag_frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 20))
        self.label_12.setStyleSheet(u"font-family: Proxima Nova;\n"
"font-size: 16px;\n"
"font-weight: 400;\n"
"line-height: 16px;\n"
"text-align: center;\n"
"color: rgba(36, 43, 46, 1);\n"
"border:none;\n"
"background-color:transparent;")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_12)

        self.label_13 = QLabel(self.drag_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 30))
        self.label_13.setStyleSheet(u"border:none;\n"
"font-family: Proxima Nova;\n"
"font-size: 16px;\n"
"font-weight: 400;\n"
"line-height: 16px;\n"
"text-align: center;\n"
"color: rgb(0, 0, 0);\n"
"background-color:transparent;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_13)

        self.frame_24 = QFrame(self.drag_frame)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"border:none;\n"
"background-color:transparent;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(255, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_14)

        self.browse_file = QPushButton(self.frame_24)
        self.browse_file.setObjectName(u"browse_file")
        self.browse_file.setMinimumSize(QSize(136, 40))
        self.browse_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.browse_file.setStyleSheet(u"\n"
"font-family: Proxima Nova;\n"
"font-size: 16px;\n"
"font-weight: 700;\n"
"line-height: 16px;\n"
"text-align: center;\n"
"background: rgba(3, 169, 244, 1);\n"
"color : white;\n"
"border-radius: 4px;\n"
"\n"
"")

        self.horizontalLayout_15.addWidget(self.browse_file)

        self.horizontalSpacer_15 = QSpacerItem(255, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_15)


        self.verticalLayout_9.addWidget(self.frame_24)


        self.horizontalLayout_13.addWidget(self.drag_frame)

        self.horizontalSpacer_11 = QSpacerItem(262, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)


        self.verticalLayout_8.addWidget(self.frame_22)


        self.verticalLayout_7.addWidget(self.frame_21)

        self.frame_26 = QFrame(self.home)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 3))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_26)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(200, 0))
        self.frame_29.setMaximumSize(QSize(200, 16777215))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_29)

        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(1018, 0))
        self.frame_27.setStyleSheet(u"border-top:1px solid rgb(194, 194, 194);\n"
"")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(200, 0))
        self.frame_28.setMaximumSize(QSize(200, 16777215))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_28)


        self.verticalLayout_7.addWidget(self.frame_26)

        self.frame_20 = QFrame(self.home)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 30, 0, 50)
        self.label_14 = QLabel(self.frame_20)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 20))
        self.label_14.setMaximumSize(QSize(16777215, 30))
        self.label_14.setStyleSheet(u"font-family: Proxima Nova;\n"
"font-size: 28px;\n"
"font-weight: 700;\n"
"line-height: 28px;\n"
"text-align: center;\n"
"color: rgba(3, 169, 244, 1);\n"
"")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_20)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 20))
        self.label_15.setMaximumSize(QSize(16777215, 35))
        self.label_15.setStyleSheet(u"font-family: Proxima Nova;\n"
"font-size: 16px;\n"
"font-weight: 400;\n"
"line-height: 16px;\n"
"text-align: center;\n"
"color: rgba(36, 43, 46, 1);\n"
"")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_15)

        self.frame_30 = QFrame(self.frame_20)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_16 = QSpacerItem(283, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_16)

        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(633, 48))
        self.frame_31.setMaximumSize(QSize(16777215, 48))
        self.frame_31.setStyleSheet(u"border: 1px solid rgba(223, 225, 227, 1);\n"
"border-radius:5px;")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_18.setSpacing(11)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(10, 4, 4, 4)
        self.label_16 = QLabel(self.frame_31)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"border:none\n"
"")
        self.label_16.setPixmap(QPixmap(u":/icons/assets/icons/youtube.png"))

        self.horizontalLayout_18.addWidget(self.label_16)

        self.youtube_url = QLineEdit(self.frame_31)
        self.youtube_url.setObjectName(u"youtube_url")
        self.youtube_url.setMinimumSize(QSize(0, 34))
        self.youtube_url.setFont(font1)
        self.youtube_url.setLayoutDirection(Qt.RightToLeft)
        self.youtube_url.setStyleSheet(u"font-family: Proxima Nova;\n"
"font-size: 15px;\n"
"font-weight: 400;\n"
"line-height: 15px;\n"
"text-align: left;\n"
"border:none")
        self.youtube_url.setMaxLength(32757)

        self.horizontalLayout_18.addWidget(self.youtube_url)

        self.play_youtube = QPushButton(self.frame_31)
        self.play_youtube.setObjectName(u"play_youtube")
        self.play_youtube.setMinimumSize(QSize(136, 40))
        self.play_youtube.setCursor(QCursor(Qt.PointingHandCursor))
        self.play_youtube.setStyleSheet(u"background: rgba(3, 169, 244, 0.51);\n"
"font-family: Proxima Nova;\n"
"font-size: 16px;\n"
"font-weight: 700;\n"
"line-height: 16px;\n"
"text-align: center;\n"
"color: rgba(255, 255, 255,.55);\n"
"")

        self.horizontalLayout_18.addWidget(self.play_youtube)


        self.horizontalLayout_17.addWidget(self.frame_31)

        self.horizontalSpacer_17 = QSpacerItem(283, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_17)


        self.verticalLayout_10.addWidget(self.frame_30)


        self.verticalLayout_7.addWidget(self.frame_20)

        self.stackedWidget.addWidget(self.home)
        self.video_player = QWidget()
        self.video_player.setObjectName(u"video_player")
        self.video_player.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.gridLayout_6 = QGridLayout(self.video_player)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.video_player)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_23)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_23)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(1415, 555))
        self.frame_41.setMaximumSize(QSize(1677215, 16777215))
        self.frame_41.setToolTipDuration(5)
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_41)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_8.addWidget(self.frame_41, 0, 0, 1, 1)

        self.sub_floating = QFrame(self.frame_23)
        self.sub_floating.setObjectName(u"sub_floating")
        self.sub_floating.setMinimumSize(QSize(0, 45))
        self.sub_floating.setMaximumSize(QSize(0, 0))
        self.sub_floating.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 4px ;\n"
"padding:10px;\n"
"")
        self.sub_floating.setFrameShape(QFrame.StyledPanel)
        self.sub_floating.setFrameShadow(QFrame.Raised)

        self.gridLayout_8.addWidget(self.sub_floating, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_23, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.video_player)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"               LOGO    ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Welcome to TechSpecs Ray", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"em ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim v", None))
        self.get_started.setText(QCoreApplication.translate("MainWindow", u"Let\u2019s get started", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Techspecs Ray", None))
        self.logIn_tab.setText(QCoreApplication.translate("MainWindow", u"           Log In", None))
        self.signUp_tab.setText(QCoreApplication.translate("MainWindow", u"        Sign Up", None))
        self.logIn_btn.setText(QCoreApplication.translate("MainWindow", u"LOG IN", None))
        self.log_google.setText(QCoreApplication.translate("MainWindow", u"       Sign in with Google", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"OR", None))
        self.label_6.setText("")
        self.email_log.setText("")
        self.email_log.setPlaceholderText(QCoreApplication.translate("MainWindow", u"yours@example.com", None))
        self.label_7.setText("")
        self.pass_log.setText("")
        self.pass_log.setPlaceholderText(QCoreApplication.translate("MainWindow", u"your password", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Don\u2019t remember your password?", None))
        self.label_20.setText("")
        self.email_sign.setText("")
        self.email_sign.setPlaceholderText(QCoreApplication.translate("MainWindow", u"yours@example.com", None))
        self.label_17.setText("")
        self.pass_sign.setText("")
        self.pass_sign.setPlaceholderText(QCoreApplication.translate("MainWindow", u"your password", None))
        self.label_21.setText("")
        self.repass_sign.setText("")
        self.repass_sign.setPlaceholderText(QCoreApplication.translate("MainWindow", u"rewrite your password", None))
        self.logIn_btn_2.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TechSpecs Ray", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Play video from file", None))
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Drag & drop video and audio files here", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"OR", None))
        self.browse_file.setText(QCoreApplication.translate("MainWindow", u"Browse Files", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Play direct from Youtube", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Insert your Youtube video link below to play directly from youtube", None))
        self.label_16.setText("")
        self.youtube_url.setText("")
        self.youtube_url.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insert your Youtube video link here", None))
        self.play_youtube.setText(QCoreApplication.translate("MainWindow", u"Play Video", None))
    # retranslateUi

