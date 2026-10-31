# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'About.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QGridLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import images_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(700, 450)
        Dialog.setMinimumSize(QSize(700, 450))
        Dialog.setMaximumSize(QSize(880, 600))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(u":/res/images/downloading.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
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
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

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

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.logo = QLabel(self.top_frame)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(150, 140))
        self.logo.setPixmap(QPixmap(u":/res/images/downloading.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setMargin(0)

        self.gridLayout.addWidget(self.logo, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.top_frame)

        self.bottom_frame = QFrame(Dialog)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setFocusPolicy(Qt.ClickFocus)
        self.verticalLayout_3 = QVBoxLayout(self.bottom_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.lbl_version = QLabel(self.bottom_frame)
        self.lbl_version.setObjectName(u"lbl_version")
        self.lbl_version.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        self.lbl_version.setFont(font2)
        self.lbl_version.setAlignment(Qt.AlignCenter)
        self.lbl_version.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.lbl_version)

        self.lbl_description = QLabel(self.bottom_frame)
        self.lbl_description.setObjectName(u"lbl_description")
        self.lbl_description.setMaximumSize(QSize(16777215, 20))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(12)
        self.lbl_description.setFont(font3)
        self.lbl_description.setAlignment(Qt.AlignCenter)
        self.lbl_description.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.lbl_description)

        self.lbl_versions = QLabel(self.bottom_frame)
        self.lbl_versions.setObjectName(u"lbl_versions")
        self.lbl_versions.setMaximumSize(QSize(16777215, 20))
        self.lbl_versions.setFont(font2)
        self.lbl_versions.setAlignment(Qt.AlignCenter)
        self.lbl_versions.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.lbl_versions)

        self.lbl_repository = QLabel(self.bottom_frame)
        self.lbl_repository.setObjectName(u"lbl_repository")
        self.lbl_repository.setMaximumSize(QSize(16777215, 20))
        self.lbl_repository.setFont(font2)
        self.lbl_repository.setAlignment(Qt.AlignCenter)
        self.lbl_repository.setOpenExternalLinks(True)
        self.lbl_repository.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.lbl_repository)

        self.lbl_copyright = QLabel(self.bottom_frame)
        self.lbl_copyright.setObjectName(u"lbl_copyright")
        self.lbl_copyright.setMaximumSize(QSize(16777215, 20))
        self.lbl_copyright.setFont(font2)
        self.lbl_copyright.setAlignment(Qt.AlignCenter)
        self.lbl_copyright.setOpenExternalLinks(True)
        self.lbl_copyright.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.lbl_copyright)

        self.btn_box = QDialogButtonBox(self.bottom_frame)
        self.btn_box.setObjectName(u"btn_box")
        self.btn_box.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout_3.addWidget(self.btn_box)


        self.verticalLayout.addWidget(self.bottom_frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Acerca de GUIDownloader", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"GUIDownloader", None))
        self.lbl_version.setText(QCoreApplication.translate("Dialog", u"Versi\u00f3n", None))
        self.lbl_description.setText(QCoreApplication.translate("Dialog", u"Una aplicaci\u00f3n construida con Python, Qt (PySide6) y yt-dlp.", None))
        self.lbl_versions.setText(QCoreApplication.translate("Dialog", u"Python | PySide6 | yt-dlp", None))
        self.lbl_repository.setText(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Proyecto disponible en: <a href=\"https://www.github.com/caicesardev/GUIDownloader\">https://www.github.com/caicesardev/GUIDownloader</a></p></body></html>", None))
        self.lbl_copyright.setText(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00a9 2022 by <a href=\"https://caiogomes.herokuapp.com\">Caio Gomes</a></p></body></html>", None))
    # retranslateUi

