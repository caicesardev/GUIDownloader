
import sys
from ui.ui_About import Ui_Dialog

from PySide6.QtWidgets import (
    QApplication,
    QDialog
)


class AboutWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(AboutWindow, self).__init__(parent)

        self.setupUi(self)

        self.btn_box.accepted.connect(self.accept)

        self.exec_()


def main():
    app = QApplication(sys.argv)
    gui = AboutWindow()
    gui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
