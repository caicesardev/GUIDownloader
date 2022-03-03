# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowwiVbaw.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QWidget)
import images_rc

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
        icon.addFile(u":/res/images/downloading.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.about_menu_action = QAction(MainWindow)
        self.about_menu_action.setObjectName(u"about_menu_action")
        self.restart_menu_action = QAction(MainWindow)
        self.restart_menu_action.setObjectName(u"restart_menu_action")
        self.exit_menu_action = QAction(MainWindow)
        self.exit_menu_action.setObjectName(u"exit_menu_action")
        self.spanish_menu_action = QAction(MainWindow)
        self.spanish_menu_action.setObjectName(u"spanish_menu_action")
        self.catalan_menu_action = QAction(MainWindow)
        self.catalan_menu_action.setObjectName(u"catalan_menu_action")
        self.english_menu_action = QAction(MainWindow)
        self.english_menu_action.setObjectName(u"english_menu_action")
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
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 10, 0, 1, 1)

        self.select_strm_button = QPushButton(self.centralframe)
        self.select_strm_button.setObjectName(u"select_strm_button")
        self.select_strm_button.setMinimumSize(QSize(0, 30))
        self.select_strm_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.select_strm_button, 7, 1, 1, 1)

        self.input = QLineEdit(self.centralframe)
        self.input.setObjectName(u"input")
        self.input.setMinimumSize(QSize(0, 25))
        self.input.setFont(font)
        self.input.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.input, 6, 0, 1, 2)

        self.download_button = QPushButton(self.centralframe)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setMinimumSize(QSize(0, 30))
        self.download_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.download_button, 7, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.label = QLabel(self.centralframe)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        self.label.setFont(font1)

        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 2)

        self.progress_bar = QProgressBar(self.centralframe)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(0)

        self.gridLayout_2.addWidget(self.progress_bar, 8, 0, 1, 2)


        self.gridLayout.addWidget(self.centralframe, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 880, 22))
        self.menuAplicaci_n = QMenu(self.menuBar)
        self.menuAplicaci_n.setObjectName(u"menuAplicaci_n")
        self.menuLenguaje = QMenu(self.menuBar)
        self.menuLenguaje.setObjectName(u"menuLenguaje")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuAplicaci_n.menuAction())
        self.menuBar.addAction(self.menuLenguaje.menuAction())
        self.menuAplicaci_n.addAction(self.about_menu_action)
        self.menuAplicaci_n.addAction(self.restart_menu_action)
        self.menuAplicaci_n.addAction(self.exit_menu_action)
        self.menuLenguaje.addAction(self.spanish_menu_action)
        self.menuLenguaje.addAction(self.catalan_menu_action)
        self.menuLenguaje.addAction(self.english_menu_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GUIDownloader", None))
        self.about_menu_action.setText(QCoreApplication.translate("MainWindow", u"Acerca de", None))
        self.restart_menu_action.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
        self.exit_menu_action.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.spanish_menu_action.setText(QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.catalan_menu_action.setText(QCoreApplication.translate("MainWindow", u"Catal\u00e0", None))
        self.english_menu_action.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.select_strm_button.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Stream", None))
#if QT_CONFIG(tooltip)
        self.input.setToolTip(QCoreApplication.translate("MainWindow", u"Enlace del v\u00eddeo (Enter para actualizar streams)", None))
#endif // QT_CONFIG(tooltip)
        self.input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escribe el enlace del v\u00eddeo", None))
        self.download_button.setText(QCoreApplication.translate("MainWindow", u"Descargar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Descargador de YouTube", None))
        self.menuAplicaci_n.setTitle(QCoreApplication.translate("MainWindow", u"Aplicaci\u00f3n", None))
        self.menuLenguaje.setTitle(QCoreApplication.translate("MainWindow", u"Lenguaje", None))
    # retranslateUi

