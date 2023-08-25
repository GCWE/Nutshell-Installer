# Imports the modules required for GUI development
import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.program_type_ui import Ui_w_programType

class ProgramTypePage(qtw.QWidget, Ui_w_programType):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Custom buttons
        self.pb_persistent.clicked.connect(self.open_persistent_search)
        self.pb_disposable.clicked.connect(self.open_disposable_search)

    @qtc.Slot()
    def open_persistent_search(self):
        """Opens the persistent search page"""
        
        # Tells the download page a permanent program is selected
        global persistent
        persistent = True

        # Opens the persistent search page
        from persistent_search import PersistentSearchPage

        self.form = PersistentSearchPage()
        self.form.show()

        # Closes itself
        self.close()

    @qtc.Slot()
    def open_disposable_search(self):
        """Opens the disposable search page"""
        
        # Tells the download page a disposable program is selected
        global persistent
        persistent = False

        # Opens the disposable search page
        from disposable_search import DisposableSearchPage

        self.form = DisposableSearchPage()
        self.form.show()

        # Closes itself
        self.close()

# Runs the "Program Type" window
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = ProgramTypePage()
    window.show()

    sys.exit(app.exec())
