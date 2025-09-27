# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Settings.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
    QGroupBox, QLabel, QLineEdit, QSizePolicy,
    QToolButton, QVBoxLayout, QWidget)
import images_rc

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(500, 213)
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(11)
        font.setStyleStrategy(QFont.PreferAntialias)
        font.setHintingPreference(QFont.PreferFullHinting)
        Settings.setFont(font)
        icon = QIcon()
        icon.addFile(u":/res/images/downloading.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Settings.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.central_frame = QFrame(Settings)
        self.central_frame.setObjectName(u"central_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_frame.sizePolicy().hasHeightForWidth())
        self.central_frame.setSizePolicy(sizePolicy)
        self.central_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.central_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.lbl_frame = QFrame(self.central_frame)
        self.lbl_frame.setObjectName(u"lbl_frame")
        self.lbl_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.lbl_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.lbl_settings = QLabel(self.lbl_frame)
        self.lbl_settings.setObjectName(u"lbl_settings")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_settings.sizePolicy().hasHeightForWidth())
        self.lbl_settings.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(17)
        font1.setBold(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        font1.setHintingPreference(QFont.PreferFullHinting)
        self.lbl_settings.setFont(font1)

        self.verticalLayout_4.addWidget(self.lbl_settings)

        self.lbl_settings_description = QLabel(self.lbl_frame)
        self.lbl_settings_description.setObjectName(u"lbl_settings_description")
        sizePolicy1.setHeightForWidth(self.lbl_settings_description.sizePolicy().hasHeightForWidth())
        self.lbl_settings_description.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.lbl_settings_description)


        self.verticalLayout_2.addWidget(self.lbl_frame)

        self.group_box_settings = QGroupBox(self.central_frame)
        self.group_box_settings.setObjectName(u"group_box_settings")
        sizePolicy.setHeightForWidth(self.group_box_settings.sizePolicy().hasHeightForWidth())
        self.group_box_settings.setSizePolicy(sizePolicy)
        self.group_box_settings.setFont(font)
        self.group_box_settings.setFlat(True)
        self.gridLayout = QGridLayout(self.group_box_settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.label_2 = QLabel(self.group_box_settings)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.path_edit = QLineEdit(self.group_box_settings)
        self.path_edit.setObjectName(u"path_edit")
        self.path_edit.setMinimumSize(QSize(0, 35))
        self.path_edit.setReadOnly(True)

        self.gridLayout.addWidget(self.path_edit, 0, 1, 1, 1)

        self.open_btn = QToolButton(self.group_box_settings)
        self.open_btn.setObjectName(u"open_btn")
        self.open_btn.setMinimumSize(QSize(35, 35))
        self.open_btn.setFont(font)
        self.open_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.open_btn, 0, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.group_box_settings)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Configuraci\u00f3n", None))
        self.lbl_settings.setText(QCoreApplication.translate("Settings", u"Configuraci\u00f3n", None))
        self.lbl_settings_description.setText(QCoreApplication.translate("Settings", u"Administra los par\u00e1metros de la aplicaci\u00f3n", None))
        self.group_box_settings.setTitle(QCoreApplication.translate("Settings", u"Descargas", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"Ruta:", None))
        self.path_edit.setPlaceholderText(QCoreApplication.translate("Settings", u"Ruta de descarga...", None))
#if QT_CONFIG(tooltip)
        self.open_btn.setToolTip(QCoreApplication.translate("Settings", u"Seleccionar carpeta", None))
#endif // QT_CONFIG(tooltip)
        self.open_btn.setText(QCoreApplication.translate("Settings", u"...", None))
    # retranslateUi

