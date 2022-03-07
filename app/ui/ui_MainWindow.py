# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowyIvbym.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QToolButton,
    QWidget)
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
        self.aboutqt_menu_action = QAction(MainWindow)
        self.aboutqt_menu_action.setObjectName(u"aboutqt_menu_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(170, 170, 170, 170)
        self.centralframe = QFrame(self.centralwidget)
        self.centralframe.setObjectName(u"centralframe")
        self.gridLayout_2 = QGridLayout(self.centralframe)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 13, 0, 1, 1)

        self.cancel_button = QToolButton(self.centralframe)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setEnabled(False)
        self.cancel_button.setMinimumSize(QSize(32, 26))
        self.cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/res/images/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_button.setIcon(icon1)
        self.cancel_button.setIconSize(QSize(12, 12))

        self.gridLayout_2.addWidget(self.cancel_button, 9, 2, 1, 1)

        self.input = QLineEdit(self.centralframe)
        self.input.setObjectName(u"input")
        self.input.setMinimumSize(QSize(0, 25))
        self.input.setFont(font)
        self.input.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.input, 6, 0, 1, 3)

        self.spd_label_frame = QFrame(self.centralframe)
        self.spd_label_frame.setObjectName(u"spd_label_frame")
        self.spd_label_frame.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.spd_label_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, -1, 0, 0)
        self.mp4_radio_btn = QRadioButton(self.spd_label_frame)
        self.mp4_radio_btn.setObjectName(u"mp4_radio_btn")
        self.mp4_radio_btn.setChecked(True)

        self.horizontalLayout_2.addWidget(self.mp4_radio_btn)

        self.mp3_radio_btn = QRadioButton(self.spd_label_frame)
        self.mp3_radio_btn.setObjectName(u"mp3_radio_btn")

        self.horizontalLayout_2.addWidget(self.mp3_radio_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.speed_label = QLabel(self.spd_label_frame)
        self.speed_label.setObjectName(u"speed_label")
        self.speed_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.speed_label)


        self.gridLayout_2.addWidget(self.spd_label_frame, 11, 0, 1, 3)

        self.buttons_frame = QFrame(self.centralframe)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttons_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.download_button = QPushButton(self.buttons_frame)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setMinimumSize(QSize(0, 30))
        self.download_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.download_button)


        self.gridLayout_2.addWidget(self.buttons_frame, 10, 0, 1, 3)

        self.progress_bar = QProgressBar(self.centralframe)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(0)

        self.gridLayout_2.addWidget(self.progress_bar, 9, 0, 1, 1)

        self.label = QLabel(self.centralframe)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        self.label.setFont(font1)

        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.play_pause_button = QToolButton(self.centralframe)
        self.play_pause_button.setObjectName(u"play_pause_button")
        self.play_pause_button.setEnabled(False)
        self.play_pause_button.setMinimumSize(QSize(32, 26))
        self.play_pause_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/res/images/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/res/images/play.png", QSize(), QIcon.Active, QIcon.On)
        self.play_pause_button.setIcon(icon2)
        self.play_pause_button.setCheckable(True)

        self.gridLayout_2.addWidget(self.play_pause_button, 9, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 9, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 7, 0, 1, 1)


        self.gridLayout.addWidget(self.centralframe, 0, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 880, 22))
        self.menuBar.setStyleSheet(u"b")
        self.menuAplicaci_n = QMenu(self.menuBar)
        self.menuAplicaci_n.setObjectName(u"menuAplicaci_n")
        self.menuLenguaje = QMenu(self.menuBar)
        self.menuLenguaje.setObjectName(u"menuLenguaje")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuAplicaci_n.menuAction())
        self.menuBar.addAction(self.menuLenguaje.menuAction())
        self.menuAplicaci_n.addAction(self.about_menu_action)
        self.menuAplicaci_n.addAction(self.aboutqt_menu_action)
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
#if QT_CONFIG(shortcut)
        self.about_menu_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.restart_menu_action.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
#if QT_CONFIG(shortcut)
        self.restart_menu_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+R", None))
#endif // QT_CONFIG(shortcut)
        self.exit_menu_action.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(shortcut)
        self.exit_menu_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+W", None))
#endif // QT_CONFIG(shortcut)
        self.spanish_menu_action.setText(QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.catalan_menu_action.setText(QCoreApplication.translate("MainWindow", u"Catal\u00e0", None))
        self.english_menu_action.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.aboutqt_menu_action.setText(QCoreApplication.translate("MainWindow", u"Acerca de Qt", None))
#if QT_CONFIG(shortcut)
        self.aboutqt_menu_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+H", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.cancel_button.setToolTip(QCoreApplication.translate("MainWindow", u"Cancelar descarga", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.input.setToolTip(QCoreApplication.translate("MainWindow", u"Enlace del v\u00eddeo (Enter para actualizar streams)", None))
#endif // QT_CONFIG(tooltip)
        self.input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escribe el enlace del v\u00eddeo", None))
#if QT_CONFIG(tooltip)
        self.mp4_radio_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Descargar v\u00eddeos en formato MP4", None))
#endif // QT_CONFIG(tooltip)
        self.mp4_radio_btn.setText(QCoreApplication.translate("MainWindow", u"MP4", None))
#if QT_CONFIG(tooltip)
        self.mp3_radio_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Descargar v\u00eddeos en formato MP3", None))
#endif // QT_CONFIG(tooltip)
        self.mp3_radio_btn.setText(QCoreApplication.translate("MainWindow", u"MP3", None))
        self.speed_label.setText("")
#if QT_CONFIG(tooltip)
        self.download_button.setToolTip(QCoreApplication.translate("MainWindow", u"Descargar v\u00eddeo", None))
#endif // QT_CONFIG(tooltip)
        self.download_button.setText(QCoreApplication.translate("MainWindow", u"Descargar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Descargador de YouTube", None))
#if QT_CONFIG(tooltip)
        self.play_pause_button.setToolTip(QCoreApplication.translate("MainWindow", u"Reanudar/Pausar descarga", None))
#endif // QT_CONFIG(tooltip)
        self.play_pause_button.setText("")
        self.menuAplicaci_n.setTitle(QCoreApplication.translate("MainWindow", u"Aplicaci\u00f3n", None))
        self.menuLenguaje.setTitle(QCoreApplication.translate("MainWindow", u"Lenguaje", None))
    # retranslateUi

