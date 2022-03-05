# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutRFGkoy.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout)
import images_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(880, 600)
        Dialog.setMinimumSize(QSize(880, 600))
        Dialog.setMaximumSize(QSize(880, 600))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(u":/res/images/downloading.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(Dialog)
        self.top_frame.setObjectName(u"top_frame")
        self.gridLayout = QGridLayout(self.top_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.line = QFrame(self.top_frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 3)

        self.title = QLabel(self.top_frame)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.title.setFont(font1)
        self.title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.title, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.logo = QLabel(self.top_frame)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(150, 140))
        self.logo.setPixmap(QPixmap(u":/res/images/downloading.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setMargin(0)

        self.gridLayout.addWidget(self.logo, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.top_frame)

        self.bottom_frame = QFrame(Dialog)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.verticalLayout_3 = QVBoxLayout(self.bottom_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.version = QLabel(self.bottom_frame)
        self.version.setObjectName(u"version")
        self.version.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        self.version.setFont(font2)
        self.version.setAlignment(Qt.AlignCenter)
        self.version.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.version)

        self.label = QLabel(self.bottom_frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(12)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.bottom_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.bottom_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.label_3)

        self.copyright = QLabel(self.bottom_frame)
        self.copyright.setObjectName(u"copyright")
        self.copyright.setMaximumSize(QSize(16777215, 20))
        self.copyright.setFont(font2)
        self.copyright.setAlignment(Qt.AlignCenter)
        self.copyright.setOpenExternalLinks(True)
        self.copyright.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.copyright)


        self.verticalLayout.addWidget(self.bottom_frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"GUIDownloader | About", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"GUIDownloader", None))
        self.version.setText(QCoreApplication.translate("Dialog", u"Versi\u00f3n 1.0.0 (Compilaci\u00f3n de 03/03/2022 )", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Una aplicaci\u00f3n construida con Python y  Qt (PySide6).", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Python 3.9 | | PySide6 6.2.3 | | PyTube 12.0.0", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Proyecto disponible en: <a href=\"https://www.github.com/caicesardev/GUIDownloader\">https://www.github.com/caicesardev/GUIDownloader</a></p></body></html>", None))
        self.copyright.setText(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00a9 2022 by <a href=\"https://caiogomes.herokuapp.com\">Caio Gomes</a></p></body></html>", None))
    # retranslateUi

