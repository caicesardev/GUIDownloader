# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowQPWODn.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QToolButton, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 480)
        MainWindow.setMinimumSize(QSize(440, 335))
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
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 2, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 2, 1)

        self.centralframe = QFrame(self.centralwidget)
        self.centralframe.setObjectName(u"centralframe")
        self.centralframe.setMinimumSize(QSize(410, 300))
        self.gridLayout_2 = QGridLayout(self.centralframe)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.verticalSpacer_3 = QSpacerItem(20, 9, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 7, 0, 1, 2)

        self.spd_label_frame = QFrame(self.centralframe)
        self.spd_label_frame.setObjectName(u"spd_label_frame")
        self.spd_label_frame.setMaximumSize(QSize(16777215, 65))
        self.horizontalLayout_2 = QHBoxLayout(self.spd_label_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 0, 0, 0)
        self.groupBox = QGroupBox(self.spd_label_frame)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.mp4_radio_btn = QRadioButton(self.groupBox)
        self.mp4_radio_btn.setObjectName(u"mp4_radio_btn")
        self.mp4_radio_btn.setChecked(True)

        self.horizontalLayout_3.addWidget(self.mp4_radio_btn)

        self.mp3_radio_btn = QRadioButton(self.groupBox)
        self.mp3_radio_btn.setObjectName(u"mp3_radio_btn")

        self.horizontalLayout_3.addWidget(self.mp3_radio_btn)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.speed_label = QLabel(self.spd_label_frame)
        self.speed_label.setObjectName(u"speed_label")
        self.speed_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.speed_label)


        self.gridLayout_2.addWidget(self.spd_label_frame, 11, 0, 1, 2)

        self.cancel_button = QToolButton(self.centralframe)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setEnabled(False)
        self.cancel_button.setMinimumSize(QSize(32, 26))
        self.cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_button.setIconSize(QSize(12, 12))

        self.gridLayout_2.addWidget(self.cancel_button, 9, 1, 1, 1)

        self.input = QLineEdit(self.centralframe)
        self.input.setObjectName(u"input")
        self.input.setMinimumSize(QSize(0, 25))
        self.input.setFont(font)
        self.input.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.input, 6, 0, 1, 2)

        self.buttons_frame = QFrame(self.centralframe)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setMaximumSize(QSize(16777215, 40))
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttons_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.download_button = QPushButton(self.buttons_frame)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setMinimumSize(QSize(0, 30))
        self.download_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.download_button)


        self.gridLayout_2.addWidget(self.buttons_frame, 10, 0, 1, 2)

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

        self.gridLayout_2.addWidget(self.progress_bar, 9, 0, 1, 1)


        self.gridLayout.addWidget(self.centralframe, 1, 1, 2, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 700, 21))
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
        self.input.returnPressed.connect(self.download_button.animateClick)

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
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Formato", None))
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
        self.cancel_button.setToolTip(QCoreApplication.translate("MainWindow", u"Cancelar descarga", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.input.setToolTip(QCoreApplication.translate("MainWindow", u"Enlace del v\u00eddeo", None))
#endif // QT_CONFIG(tooltip)
        self.input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escribe el enlace del v\u00eddeo", None))
#if QT_CONFIG(tooltip)
        self.download_button.setToolTip(QCoreApplication.translate("MainWindow", u"Descargar v\u00eddeo", None))
#endif // QT_CONFIG(tooltip)
        self.download_button.setText(QCoreApplication.translate("MainWindow", u"Descargar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Descargador de YouTube", None))
#if QT_CONFIG(tooltip)
        self.progress_bar.setToolTip(QCoreApplication.translate("MainWindow", u"Progreso", None))
#endif // QT_CONFIG(tooltip)
        self.menuAplicaci_n.setTitle(QCoreApplication.translate("MainWindow", u"Aplicaci\u00f3n", None))
        self.menuLenguaje.setTitle(QCoreApplication.translate("MainWindow", u"Lenguaje", None))
    # retranslateUi

