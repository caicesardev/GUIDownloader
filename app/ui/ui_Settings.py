# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsoYAlCp.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)
import images_rc

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(500, 180)
        Settings.setMinimumSize(QSize(500, 180))
        Settings.setMaximumSize(QSize(500, 180))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(11)
        Settings.setFont(font)
        icon = QIcon()
        icon.addFile(u":/res/images/downloading.png", QSize(), QIcon.Normal, QIcon.Off)
        Settings.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Settings)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(Settings)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMaximumSize(QSize(16777215, 80))
        font1 = QFont()
        font1.setFamilies([u"Roboto Mono"])
        font1.setPointSize(10)
        self.header_frame.setFont(font1)
        self.header_frame.setStyleSheet(u"QFrame#header_frame{background: #006064;}")
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(18, -1, -1, -1)
        self.label = QLabel(self.header_frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(32, 32))
        self.label.setPixmap(QPixmap(u":/res/images/downloading.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.title = QLabel(self.header_frame)
        self.title.setObjectName(u"title")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        self.title.setFont(font2)

        self.horizontalLayout.addWidget(self.title)


        self.verticalLayout.addWidget(self.header_frame)

        self.central_frame = QFrame(Settings)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setStyleSheet(u"QFrame#central_frame \n"
"{\n"
"	background: white;\n"
"}")
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.central_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.central_frame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.path_edit = QLineEdit(self.groupBox)
        self.path_edit.setObjectName(u"path_edit")
        self.path_edit.setReadOnly(True)

        self.gridLayout.addWidget(self.path_edit, 0, 1, 1, 1)

        self.open_btn = QToolButton(self.groupBox)
        self.open_btn.setObjectName(u"open_btn")

        self.gridLayout.addWidget(self.open_btn, 0, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Configuraci\u00f3n", None))
        self.title.setText(QCoreApplication.translate("Settings", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Configuraci\u00f3n</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("Settings", u"Ruta de descarga", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"Ruta:", None))
        self.path_edit.setPlaceholderText(QCoreApplication.translate("Settings", u"Ruta de descarga", None))
#if QT_CONFIG(tooltip)
        self.open_btn.setToolTip(QCoreApplication.translate("Settings", u"Seleccionar carpeta", None))
#endif // QT_CONFIG(tooltip)
        self.open_btn.setText(QCoreApplication.translate("Settings", u"...", None))
    # retranslateUi

