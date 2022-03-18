# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowtOIqSG.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QToolButton, QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 482)
        MainWindow.setMinimumSize(QSize(0, 440))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/res/images/downloading.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow#MainWindow{background: white;}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.central_frame = QFrame(self.centralwidget)
        self.central_frame.setObjectName(u"central_frame")
        self.verticalLayout = QVBoxLayout(self.central_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.central_frame)
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

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.about_menu_action = QPushButton(self.header_frame)
        self.about_menu_action.setObjectName(u"about_menu_action")
        self.about_menu_action.setMinimumSize(QSize(0, 40))
        self.about_menu_action.setMaximumSize(QSize(50, 16777215))
        self.about_menu_action.setIconSize(QSize(24, 24))
        self.about_menu_action.setFlat(True)

        self.horizontalLayout.addWidget(self.about_menu_action)

        self.aboutqt_menu_action = QPushButton(self.header_frame)
        self.aboutqt_menu_action.setObjectName(u"aboutqt_menu_action")
        self.aboutqt_menu_action.setMinimumSize(QSize(0, 40))
        self.aboutqt_menu_action.setMaximumSize(QSize(50, 16777215))
        self.aboutqt_menu_action.setIconSize(QSize(24, 24))
        self.aboutqt_menu_action.setFlat(True)

        self.horizontalLayout.addWidget(self.aboutqt_menu_action)

        self.restart_menu_action = QPushButton(self.header_frame)
        self.restart_menu_action.setObjectName(u"restart_menu_action")
        self.restart_menu_action.setMinimumSize(QSize(0, 40))
        self.restart_menu_action.setMaximumSize(QSize(50, 16777215))
        self.restart_menu_action.setIconSize(QSize(24, 24))
        self.restart_menu_action.setFlat(True)

        self.horizontalLayout.addWidget(self.restart_menu_action)

        self.exit_menu_action = QPushButton(self.header_frame)
        self.exit_menu_action.setObjectName(u"exit_menu_action")
        self.exit_menu_action.setMinimumSize(QSize(0, 40))
        self.exit_menu_action.setMaximumSize(QSize(50, 16777215))
        self.exit_menu_action.setIconSize(QSize(24, 24))
        self.exit_menu_action.setFlat(True)

        self.horizontalLayout.addWidget(self.exit_menu_action)


        self.verticalLayout.addWidget(self.header_frame)

        self.mid_frame = QFrame(self.central_frame)
        self.mid_frame.setObjectName(u"mid_frame")
        self.mid_frame.setFont(font)
        self.horizontalLayout_6 = QHBoxLayout(self.mid_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_6.setContentsMargins(50, 30, 50, 30)
        self.container_frame = QFrame(self.mid_frame)
        self.container_frame.setObjectName(u"container_frame")
        self.container_frame.setMinimumSize(QSize(440, 0))
        self.container_frame.setMaximumSize(QSize(960, 300))
        self.container_frame.setStyleSheet(u"QFrame#container_frame{background: whitesmoke; border: 1px solid #c2c2c2; border-radius: 10px;}")
        self.container_frame.setFrameShape(QFrame.StyledPanel)
        self.container_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.container_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 15, 20, 15)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.container_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(11)
        self.label_2.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_2)

        self.input = QLineEdit(self.container_frame)
        self.input.setObjectName(u"input")
        self.input.setMinimumSize(QSize(0, 25))
        self.input.setFont(font)
        self.input.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.input)

        self.progress_frame = QFrame(self.container_frame)
        self.progress_frame.setObjectName(u"progress_frame")
        self.progress_frame.setMaximumSize(QSize(16777215, 64))
        self.progress_frame.setFrameShape(QFrame.StyledPanel)
        self.progress_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.progress_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.progress_bar = QProgressBar(self.progress_frame)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(0)

        self.horizontalLayout_5.addWidget(self.progress_bar)

        self.cancel_button = QToolButton(self.progress_frame)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setEnabled(False)
        self.cancel_button.setMinimumSize(QSize(32, 26))
        self.cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_button.setIconSize(QSize(12, 12))

        self.horizontalLayout_5.addWidget(self.cancel_button)


        self.verticalLayout_3.addWidget(self.progress_frame)

        self.download_button = QPushButton(self.container_frame)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setMinimumSize(QSize(0, 30))
        self.download_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.download_button)

        self.tab_widget = QTabWidget(self.container_frame)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_widget.setMaximumSize(QSize(16777215, 93))
        self.video_tab = QWidget()
        self.video_tab.setObjectName(u"video_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.video_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.vf_combo_box = QComboBox(self.video_tab)
        self.vf_combo_box.addItem("")
        self.vf_combo_box.addItem("")
        self.vf_combo_box.addItem("")
        self.vf_combo_box.addItem("")
        self.vf_combo_box.setObjectName(u"vf_combo_box")

        self.horizontalLayout_3.addWidget(self.vf_combo_box)

        self.vq_combo_box = QComboBox(self.video_tab)
        self.vq_combo_box.addItem("")
        self.vq_combo_box.addItem("")
        self.vq_combo_box.addItem("")
        self.vq_combo_box.addItem("")
        self.vq_combo_box.addItem("")
        self.vq_combo_box.setObjectName(u"vq_combo_box")

        self.horizontalLayout_3.addWidget(self.vq_combo_box)

        self.tab_widget.addTab(self.video_tab, "")
        self.audio_tab = QWidget()
        self.audio_tab.setObjectName(u"audio_tab")
        self.horizontalLayout_4 = QHBoxLayout(self.audio_tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.af_combo_box = QComboBox(self.audio_tab)
        self.af_combo_box.addItem("")
        self.af_combo_box.addItem("")
        self.af_combo_box.addItem("")
        self.af_combo_box.addItem("")
        self.af_combo_box.setObjectName(u"af_combo_box")

        self.horizontalLayout_4.addWidget(self.af_combo_box)

        self.aq_combo_box = QComboBox(self.audio_tab)
        self.aq_combo_box.addItem("")
        self.aq_combo_box.addItem("")
        self.aq_combo_box.addItem("")
        self.aq_combo_box.addItem("")
        self.aq_combo_box.setObjectName(u"aq_combo_box")

        self.horizontalLayout_4.addWidget(self.aq_combo_box)

        self.tab_widget.addTab(self.audio_tab, "")

        self.verticalLayout_3.addWidget(self.tab_widget)

        self.options_frame = QFrame(self.container_frame)
        self.options_frame.setObjectName(u"options_frame")
        self.options_frame.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_2 = QHBoxLayout(self.options_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.vid_radio_btn = QRadioButton(self.options_frame)
        self.vid_radio_btn.setObjectName(u"vid_radio_btn")
        self.vid_radio_btn.setChecked(True)

        self.horizontalLayout_2.addWidget(self.vid_radio_btn)

        self.audio_radio_btn = QRadioButton(self.options_frame)
        self.audio_radio_btn.setObjectName(u"audio_radio_btn")

        self.horizontalLayout_2.addWidget(self.audio_radio_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.speed_label = QLabel(self.options_frame)
        self.speed_label.setObjectName(u"speed_label")
        self.speed_label.setFont(font)

        self.horizontalLayout_2.addWidget(self.speed_label)


        self.verticalLayout_3.addWidget(self.options_frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addWidget(self.container_frame)


        self.verticalLayout.addWidget(self.mid_frame)


        self.gridLayout.addWidget(self.central_frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setFont(font)
        self.status_bar.setStyleSheet(u"QStatusBar{background: whitesmoke;}")
        MainWindow.setStatusBar(self.status_bar)

        self.retranslateUi(MainWindow)

        self.tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GUIDownloader", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">GUIDownloader</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.about_menu_action.setStatusTip(QCoreApplication.translate("MainWindow", u"Acerca de ", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.aboutqt_menu_action.setStatusTip(QCoreApplication.translate("MainWindow", u"Acerca de Qt", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.restart_menu_action.setStatusTip(QCoreApplication.translate("MainWindow", u"Reiniciar aplicaci\u00f3n", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.exit_menu_action.setStatusTip(QCoreApplication.translate("MainWindow", u"Salir de la aplicaci\u00f3n", None))
#endif // QT_CONFIG(statustip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Descargador de YouTube", None))
#if QT_CONFIG(tooltip)
        self.input.setToolTip(QCoreApplication.translate("MainWindow", u"Enlace del v\u00eddeo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.input.setStatusTip(QCoreApplication.translate("MainWindow", u"Escribe el enlace del v\u00eddeo", None))
#endif // QT_CONFIG(statustip)
        self.input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escribe el enlace del v\u00eddeo", None))
#if QT_CONFIG(tooltip)
        self.progress_bar.setToolTip(QCoreApplication.translate("MainWindow", u"Progreso", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cancel_button.setToolTip(QCoreApplication.translate("MainWindow", u"Cancelar descarga", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.cancel_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Cancelar la descarga", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.download_button.setToolTip(QCoreApplication.translate("MainWindow", u"Descargar v\u00eddeo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.download_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Descargar v\u00eddeo", None))
#endif // QT_CONFIG(statustip)
        self.download_button.setText(QCoreApplication.translate("MainWindow", u"Descargar", None))
        self.vf_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"MP4", None))
        self.vf_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"MKV", None))
        self.vf_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"AVI", None))
        self.vf_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"WEBM", None))

        self.vq_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"1080p", None))
        self.vq_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"720p", None))
        self.vq_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"480p", None))
        self.vq_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"360p", None))
        self.vq_combo_box.setItemText(4, QCoreApplication.translate("MainWindow", u"144p", None))

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.video_tab), QCoreApplication.translate("MainWindow", u"Formato de v\u00eddeo", None))
        self.af_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"MP3", None))
        self.af_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"M4A", None))
        self.af_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"WAV", None))
        self.af_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"OGG", None))

        self.aq_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"360K", None))
        self.aq_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"192K", None))
        self.aq_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"144k", None))
        self.aq_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"96K", None))

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.audio_tab), QCoreApplication.translate("MainWindow", u"Formato de audio", None))
#if QT_CONFIG(tooltip)
        self.vid_radio_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Descargar v\u00eddeo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.vid_radio_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"Descargar en v\u00eddeo", None))
#endif // QT_CONFIG(statustip)
        self.vid_radio_btn.setText(QCoreApplication.translate("MainWindow", u"V\u00eddeo", None))
#if QT_CONFIG(tooltip)
        self.audio_radio_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Descargar solo audio", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.audio_radio_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"Descargar solo audio", None))
#endif // QT_CONFIG(statustip)
        self.audio_radio_btn.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
    # retranslateUi

