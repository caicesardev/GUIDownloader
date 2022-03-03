# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'MainWindowcfqsaq.ui'
##
# Created by: Qt User Interface Compiler version 6.2.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QSizePolicy,
                               QSpacerItem, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 600)
        MainWindow.setMinimumSize(QSize(880, 600))
        MainWindow.setMaximumSize(QSize(880, 600))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"../res/images/downloading.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(200, 200, 200, 200)
        self.centralframe = QFrame(self.centralwidget)
        self.centralframe.setObjectName(u"centralframe")
        self.centralframe.setFrameShape(QFrame.StyledPanel)
        self.centralframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.centralframe)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 8, 0, 1, 1)

        self.select_strm_button = QPushButton(self.centralframe)
        self.select_strm_button.setObjectName(u"select_strm_button")
        self.select_strm_button.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.select_strm_button, 7, 1, 1, 1)

        self.download_button = QPushButton(self.centralframe)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.download_button, 7, 0, 1, 1)

        self.label = QLabel(self.centralframe)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        self.label.setFont(font1)

        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 2)

        self.input = QLineEdit(self.centralframe)
        self.input.setObjectName(u"input")
        self.input.setMinimumSize(QSize(0, 25))
        self.input.setFont(font)
        self.input.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.input, 6, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.gridLayout.addWidget(self.centralframe, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"GUIDownloader", None))
        self.select_strm_button.setText(QCoreApplication.translate(
            "MainWindow", u"Seleccionar Stream", None))
        self.download_button.setText(
            QCoreApplication.translate("MainWindow", u"Descargar", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Descargador de YouTube", None))
# if QT_CONFIG(tooltip)
        self.input.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Enlace del v\u00eddeo (Enter para actualizar streams)", None))
#endif // QT_CONFIG(tooltip)
        self.input.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Escribe el enlace del v\u00eddeo", None))
    # retranslateUi
