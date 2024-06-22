# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alabeluvXAoTM.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject,  QSize,  Qt)
from PySide6.QtGui import ( QCursor, QPixmap)
from PySide6.QtWidgets import (QSpacerItem, QFrame, QLabel, QPushButton, QSizePolicy,QHBoxLayout, QGridLayout, QVBoxLayout)
# from app import MainWindow as main
import resources_rc
class DragDrop(QFrame):
    def __init__(
        self,
        main
    ):
        super().__init__()

        self._main =  main
        self.file = '/'
        self.resize(800, 327)
        
        self.setAcceptDrops(True)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.drag_frame = QFrame(self)
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


        self.gridLayout.addWidget(self.drag_frame, 0, 0, 1, 1)


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"Drag & drop video and audio files here", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"OR", None))
        self.browse_file.setText(QCoreApplication.translate("Form", u"Browse Files", None))
    # retranslateUi

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            print(f'file_path {file_path}')
            self.file =  file_path
            self._main.start_media(file_path)
            event.accept()
        else:
            event.ignore()
