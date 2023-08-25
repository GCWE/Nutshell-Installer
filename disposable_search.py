# Imports modules necessary for GUI development
import os
import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.disposable_search_page_ui import Ui_w_addDisposableApps

# List of available programs
programs = ["Firefox", "Chromium", "Opera", "Ubuntu", "Fedora", "Arch", "Debian", "Alpine", "LibreOffice"]

class DisposableSearchPage(qtw.QWidget, Ui_w_addDisposableApps):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Current working directory
        directory = os.getcwd()

        for program in programs:
            disposable_webtop = f"{directory}/Disposable_{program}_Webtop"

            # Creates custom button
            btn_connection = f"self.pb_{program.lower()}.clicked.connect(lambda: self.open_download('{program}'))"
            exec(btn_connection, locals())

            # Disables button if already installed
            if os.path.isdir(disposable_webtop):
                exec(f"self.pb_{program.lower()}.setDisabled(True)")

    @qtc.Slot()
    def open_download(self, choice):
        """Opens download page for specific program"""
        
        # Accessible by download page
        global program_name
        program_name = choice

        # Opens download page
        from download import DownloadPage

        self.form = DownloadPage()
        
        # Specific window appearance for specific program
        self.form.setWindowTitle(f"Download {choice} (Disposable)")
        self.form.groupBox.setTitle(f"Download {choice} (Disposable)")
        self.form.lb_downloadDescription.setText(f"""Install {choice} (Disposable) on Nutshell.
                                                 
Note: This will install a disposable version of the application - once the {choice} window is closed, Nutshell will destroy the instance's data to protect your privacy.

Are you sure you want to install {choice} (Disposable)?""")
        self.form.lb_downloadDescription.setWordWrap(True)
        self.form.exec()

# Runs the "Disposable Search" page
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = DisposableSearchPage()
    window.show()

    sys.exit(app.exec())
