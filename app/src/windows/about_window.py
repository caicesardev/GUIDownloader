import platform

import PySide6
from PySide6.QtWidgets import QDialog, QWidget
from yt_dlp.version import __version__ as yt_dlp_version

from constants import VERSION
from ui.About_ui import Ui_Dialog


class AboutWindow(QDialog, Ui_Dialog):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.lbl_version.setText(f"Versión {VERSION}")
        self.lbl_versions.setText(
            f"Python {platform.python_version()} | PySide6 {PySide6.__version__} | yt-dlp {yt_dlp_version}"
        )
        self.btn_box.accepted.connect(self.accept)
