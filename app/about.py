
import sys
from ui.ui_About import Ui_Dialog

from PySide6.QtCore import (
    QLibraryInfo,
    QLocale,
    QTranslator,
)
from PySide6.QtWidgets import (
    QApplication,
    QDialog
)


# About.
class About(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)

        self.setupUi(self)

        self.btn_box.accepted.connect(self.accept)

        self.exec_()


def main():
    app = QApplication(sys.argv)

    translator = QTranslator()
    translator.load("qtbase_" + QLocale.system().name(),
                    QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    gui = About()
    gui.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
