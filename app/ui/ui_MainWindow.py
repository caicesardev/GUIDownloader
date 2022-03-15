# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowWmHCdE.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QToolButton, QWidget)
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

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 2, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.centralframe = QFrame(self.centralwidget)
        self.centralframe.setObjectName(u"centralframe")
        self.centralframe.setMinimumSize(QSize(410, 300))
        self.gridLayout_2 = QGridLayout(self.centralframe)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.buttons_frame = QFrame(self.centralframe)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setMaximumSize(QSize(16777215, 40))
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttons_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.download_button = QPushButton(self.buttons_frame)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setMinimumSize(QSize(0, 30))
        self.download_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.download_button)


        self.gridLayout_2.addWidget(self.buttons_frame, 9, 0, 1, 2)

        self.spd_label_frame = QFrame(self.centralframe)
        self.spd_label_frame.setObjectName(u"spd_label_frame")
        self.spd_label_frame.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_5 = QHBoxLayout(self.spd_label_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.speed_label = QLabel(self.spd_label_frame)
        self.speed_label.setObjectName(u"speed_label")
        self.speed_label.setMaximumSize(QSize(50, 20))
        self.speed_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.speed_label)


        self.gridLayout_2.addWidget(self.spd_label_frame, 13, 0, 1, 2)

        self.input = QLineEdit(self.centralframe)
        self.input.setObjectName(u"input")
        self.input.setMinimumSize(QSize(0, 25))
        self.input.setFont(font)
        self.input.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.input, 6, 0, 1, 2)

        self.label = QLabel(self.centralframe)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        self.label.setFont(font1)

        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 2)

        self.cancel_button = QToolButton(self.centralframe)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setEnabled(False)
        self.cancel_button.setMinimumSize(QSize(32, 26))
        self.cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_button.setIconSize(QSize(12, 12))

        self.gridLayout_2.addWidget(self.cancel_button, 8, 1, 1, 1)

        self.tab_widget = QTabWidget(self.centralframe)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_widget.setMaximumSize(QSize(16777215, 93))
        self.video_tab = QWidget()
        self.video_tab.setObjectName(u"video_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.video_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.f_combo_box_2 = QComboBox(self.video_tab)
        self.f_combo_box_2.addItem("")
        self.f_combo_box_2.addItem("")
        self.f_combo_box_2.addItem("")
        self.f_combo_box_2.addItem("")
        self.f_combo_box_2.setObjectName(u"f_combo_box_2")

        self.horizontalLayout_3.addWidget(self.f_combo_box_2)

        self.q_combo_box_2 = QComboBox(self.video_tab)
        self.q_combo_box_2.addItem("")
        self.q_combo_box_2.addItem("")
        self.q_combo_box_2.addItem("")
        self.q_combo_box_2.addItem("")
        self.q_combo_box_2.addItem("")
        self.q_combo_box_2.setObjectName(u"q_combo_box_2")

        self.horizontalLayout_3.addWidget(self.q_combo_box_2)

        self.tab_widget.addTab(self.video_tab, "")
        self.audio_tab = QWidget()
        self.audio_tab.setObjectName(u"audio_tab")
        self.horizontalLayout_4 = QHBoxLayout(self.audio_tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.f_combo_box_3 = QComboBox(self.audio_tab)
        self.f_combo_box_3.addItem("")
        self.f_combo_box_3.addItem("")
        self.f_combo_box_3.addItem("")
        self.f_combo_box_3.addItem("")
        self.f_combo_box_3.setObjectName(u"f_combo_box_3")

        self.horizontalLayout_4.addWidget(self.f_combo_box_3)

        self.q_combo_box_3 = QComboBox(self.audio_tab)
        self.q_combo_box_3.addItem("")
        self.q_combo_box_3.addItem("")
        self.q_combo_box_3.addItem("")
        self.q_combo_box_3.setObjectName(u"q_combo_box_3")

        self.horizontalLayout_4.addWidget(self.q_combo_box_3)

        self.tab_widget.addTab(self.audio_tab, "")

        self.gridLayout_2.addWidget(self.tab_widget, 11, 0, 1, 2)

        self.progress_bar = QProgressBar(self.centralframe)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(0)

        self.gridLayout_2.addWidget(self.progress_bar, 8, 0, 1, 1)

        self.options_frame = QFrame(self.centralframe)
        self.options_frame.setObjectName(u"options_frame")
        self.options_frame.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_2 = QHBoxLayout(self.options_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton = QRadioButton(self.options_frame)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.options_frame)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.gridLayout_2.addWidget(self.options_frame, 12, 0, 1, 2)


        self.gridLayout.addWidget(self.centralframe, 1, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 700, 22))
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

        self.tab_widget.setCurrentIndex(0)


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
        self.download_button.setToolTip(QCoreApplication.translate("MainWindow", u"Descargar v\u00eddeo", None))
#endif // QT_CONFIG(tooltip)
        self.download_button.setText(QCoreApplication.translate("MainWindow", u"Descargar", None))
        self.speed_label.setText("")
#if QT_CONFIG(tooltip)
        self.input.setToolTip(QCoreApplication.translate("MainWindow", u"Enlace del v\u00eddeo", None))
#endif // QT_CONFIG(tooltip)
        self.input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escribe el enlace del v\u00eddeo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Descargador de YouTube", None))
#if QT_CONFIG(tooltip)
        self.cancel_button.setToolTip(QCoreApplication.translate("MainWindow", u"Cancelar descarga", None))
#endif // QT_CONFIG(tooltip)
        self.f_combo_box_2.setItemText(0, QCoreApplication.translate("MainWindow", u"MP4", None))
        self.f_combo_box_2.setItemText(1, QCoreApplication.translate("MainWindow", u"MKV", None))
        self.f_combo_box_2.setItemText(2, QCoreApplication.translate("MainWindow", u"AVI", None))
        self.f_combo_box_2.setItemText(3, QCoreApplication.translate("MainWindow", u"WEBM", None))

        self.q_combo_box_2.setItemText(0, QCoreApplication.translate("MainWindow", u"1080p", None))
        self.q_combo_box_2.setItemText(1, QCoreApplication.translate("MainWindow", u"720p", None))
        self.q_combo_box_2.setItemText(2, QCoreApplication.translate("MainWindow", u"480p", None))
        self.q_combo_box_2.setItemText(3, QCoreApplication.translate("MainWindow", u"360p", None))
        self.q_combo_box_2.setItemText(4, QCoreApplication.translate("MainWindow", u"144p", None))

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.video_tab), QCoreApplication.translate("MainWindow", u"Formato de v\u00eddeo", None))
        self.f_combo_box_3.setItemText(0, QCoreApplication.translate("MainWindow", u"MP3", None))
        self.f_combo_box_3.setItemText(1, QCoreApplication.translate("MainWindow", u"M4A", None))
        self.f_combo_box_3.setItemText(2, QCoreApplication.translate("MainWindow", u"WAV", None))
        self.f_combo_box_3.setItemText(3, QCoreApplication.translate("MainWindow", u"OGG", None))

        self.q_combo_box_3.setItemText(0, QCoreApplication.translate("MainWindow", u"360K", None))
        self.q_combo_box_3.setItemText(1, QCoreApplication.translate("MainWindow", u"144k", None))
        self.q_combo_box_3.setItemText(2, QCoreApplication.translate("MainWindow", u"96K", None))

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.audio_tab), QCoreApplication.translate("MainWindow", u"Formato de audio", None))
#if QT_CONFIG(tooltip)
        self.progress_bar.setToolTip(QCoreApplication.translate("MainWindow", u"Progreso", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"Descargar v\u00eddeo", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"V\u00eddeo", None))
#if QT_CONFIG(tooltip)
        self.radioButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"Descargar solo audio", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.menuAplicaci_n.setTitle(QCoreApplication.translate("MainWindow", u"Aplicaci\u00f3n", None))
        self.menuLenguaje.setTitle(QCoreApplication.translate("MainWindow", u"Lenguaje", None))
    # retranslateUi

