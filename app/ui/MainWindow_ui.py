# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
    QSizePolicy, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(616, 420)
        icon = QIcon()
        icon.addFile(u":/res/images/downloading.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_about_qt = QAction(MainWindow)
        self.action_about_qt.setObjectName(u"action_about_qt")
        self.action_settings = QAction(MainWindow)
        self.action_settings.setObjectName(u"action_settings")
        self.action_restart = QAction(MainWindow)
        self.action_restart.setObjectName(u"action_restart")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(11)
        font.setStyleStrategy(QFont.PreferAntialias)
        font.setHintingPreference(QFont.PreferFullHinting)
        self.centralwidget.setFont(font)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.central_frame = QFrame(self.centralwidget)
        self.central_frame.setObjectName(u"central_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_frame.sizePolicy().hasHeightForWidth())
        self.central_frame.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.central_frame)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.lbl_frame = QFrame(self.central_frame)
        self.lbl_frame.setObjectName(u"lbl_frame")
        sizePolicy.setHeightForWidth(self.lbl_frame.sizePolicy().hasHeightForWidth())
        self.lbl_frame.setSizePolicy(sizePolicy)
        self.lbl_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.lbl_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.lbl_app_name = QLabel(self.lbl_frame)
        self.lbl_app_name.setObjectName(u"lbl_app_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_app_name.sizePolicy().hasHeightForWidth())
        self.lbl_app_name.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(17)
        font1.setBold(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        font1.setHintingPreference(QFont.PreferFullHinting)
        self.lbl_app_name.setFont(font1)

        self.verticalLayout_2.addWidget(self.lbl_app_name)

        self.lbl_app_description = QLabel(self.lbl_frame)
        self.lbl_app_description.setObjectName(u"lbl_app_description")
        sizePolicy1.setHeightForWidth(self.lbl_app_description.sizePolicy().hasHeightForWidth())
        self.lbl_app_description.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.lbl_app_description)


        self.verticalLayout.addWidget(self.lbl_frame)

        self.inputs_frame = QFrame(self.central_frame)
        self.inputs_frame.setObjectName(u"inputs_frame")
        self.inputs_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.inputs_frame)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.url_input = QLineEdit(self.inputs_frame)
        self.url_input.setObjectName(u"url_input")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.url_input.sizePolicy().hasHeightForWidth())
        self.url_input.setSizePolicy(sizePolicy2)
        self.url_input.setMinimumSize(QSize(0, 35))
        self.url_input.setFont(font)

        self.verticalLayout_3.addWidget(self.url_input)

        self.progress_bar = QProgressBar(self.inputs_frame)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(0)

        self.verticalLayout_3.addWidget(self.progress_bar)

        self.tab_widget = QTabWidget(self.inputs_frame)
        self.tab_widget.setObjectName(u"tab_widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tab_widget.sizePolicy().hasHeightForWidth())
        self.tab_widget.setSizePolicy(sizePolicy3)
        self.tab_widget.setMinimumSize(QSize(0, 100))
        self.tab_widget.setFont(font)
        self.tab_widget.setMovable(True)
        self.video_tab = QWidget()
        self.video_tab.setObjectName(u"video_tab")
        self.horizontalLayout = QHBoxLayout(self.video_tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.combo_video_format = QComboBox(self.video_tab)
        self.combo_video_format.addItem("")
        self.combo_video_format.setObjectName(u"combo_video_format")
        self.combo_video_format.setEnabled(False)
        self.combo_video_format.setMinimumSize(QSize(0, 33))
        self.combo_video_format.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.combo_video_format)

        self.combo_video_quality = QComboBox(self.video_tab)
        self.combo_video_quality.addItem("")
        self.combo_video_quality.setObjectName(u"combo_video_quality")
        self.combo_video_quality.setEnabled(False)
        self.combo_video_quality.setMinimumSize(QSize(0, 33))
        self.combo_video_quality.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.combo_video_quality)

        self.tab_widget.addTab(self.video_tab, "")
        self.audio_tab = QWidget()
        self.audio_tab.setObjectName(u"audio_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.audio_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.combo_audio_format = QComboBox(self.audio_tab)
        self.combo_audio_format.addItem("")
        self.combo_audio_format.setObjectName(u"combo_audio_format")
        self.combo_audio_format.setEnabled(False)
        self.combo_audio_format.setMinimumSize(QSize(0, 33))
        self.combo_audio_format.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.combo_audio_format)

        self.combo_audio_quality = QComboBox(self.audio_tab)
        self.combo_audio_quality.addItem("")
        self.combo_audio_quality.setObjectName(u"combo_audio_quality")
        self.combo_audio_quality.setEnabled(False)
        self.combo_audio_quality.setMinimumSize(QSize(0, 33))
        self.combo_audio_quality.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.combo_audio_quality)

        self.tab_widget.addTab(self.audio_tab, "")

        self.verticalLayout_3.addWidget(self.tab_widget)

        self.download_button = QPushButton(self.inputs_frame)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setEnabled(False)
        self.download_button.setMinimumSize(QSize(0, 35))
        self.download_button.setFont(font)
        self.download_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.download_button)


        self.verticalLayout.addWidget(self.inputs_frame)


        self.gridLayout.addWidget(self.central_frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menu_bar = QMenuBar(MainWindow)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 616, 33))
        self.menu_help = QMenu(self.menu_bar)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_file = QMenu(self.menu_bar)
        self.menu_file.setObjectName(u"menu_file")
        MainWindow.setMenuBar(self.menu_bar)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setPointSize(11)
        self.status_bar.setFont(font2)
        MainWindow.setStatusBar(self.status_bar)

        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())
        self.menu_help.addAction(self.action_about)
        self.menu_help.addAction(self.action_about_qt)
        self.menu_file.addAction(self.action_settings)
        self.menu_file.addAction(self.action_restart)
        self.menu_file.addAction(self.action_exit)

        self.retranslateUi(MainWindow)

        self.tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GUIDownloader", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"Acerca de GUIDownloader", None))
        self.action_about_qt.setText(QCoreApplication.translate("MainWindow", u"Acerca de Qt", None))
        self.action_settings.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.action_restart.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
#if QT_CONFIG(shortcut)
        self.action_restart.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.lbl_app_name.setText(QCoreApplication.translate("MainWindow", u"GUIDownloader", None))
        self.lbl_app_description.setText(QCoreApplication.translate("MainWindow", u"Introduce una URL para empezar la descarga.", None))
#if QT_CONFIG(tooltip)
        self.url_input.setToolTip(QCoreApplication.translate("MainWindow", u"Introduce una URL de YouTube", None))
#endif // QT_CONFIG(tooltip)
        self.url_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduce una URL de YouTube...", None))
        self.combo_video_format.setItemText(0, QCoreApplication.translate("MainWindow", u"No hay formatos disponibles", None))

        self.combo_video_quality.setItemText(0, QCoreApplication.translate("MainWindow", u"No hay formatos disponibles", None))

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.video_tab), QCoreApplication.translate("MainWindow", u"Formato de v\u00eddeo", None))
        self.combo_audio_format.setItemText(0, QCoreApplication.translate("MainWindow", u"No hay formatos disponibles", None))

        self.combo_audio_quality.setItemText(0, QCoreApplication.translate("MainWindow", u"No hay formatos disponibles", None))

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.audio_tab), QCoreApplication.translate("MainWindow", u"Formato de audio", None))
#if QT_CONFIG(tooltip)
        self.download_button.setToolTip(QCoreApplication.translate("MainWindow", u"Descargar enlace de YouTube", None))
#endif // QT_CONFIG(tooltip)
        self.download_button.setText(QCoreApplication.translate("MainWindow", u"Descargar", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

