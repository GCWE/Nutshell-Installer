# Imports the modules required for GUI development
import os
import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.persistent_search_page_ui import Ui_w_addPersistentApps

# List of available programs
programs = ["Firefox", "Chromium", "Opera", "Ubuntu", "Fedora", "Arch", "Debian", "Alpine", "LibreOffice"]

class PersistentSearchPage(qtw.QWidget, Ui_w_addPersistentApps):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Current working directory
        directory = os.getcwd()

        for program in programs:
            persistent_webtop = f"{directory}/{program}_Webtop"

            # Creates custom button
            btn_connection = f"self.pb_{program.lower()}.clicked.connect(lambda: self.open_download('{program}'))"
            exec(btn_connection, locals())

            # Disables button if program already exists
            if os.path.isdir(persistent_webtop):
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
        self.form.setWindowTitle(f"Download {choice} (Persistent)")
        self.form.groupBox.setTitle(f"Download {choice} (Persistent)")
        self.form.lb_downloadDescription.setText(f"""Install {choice} (Persistent) on Nutshell.
                                                 
Note: This will install a persistent version of the application, making the host machine more susceptible to cyber attacks.

Are you sure you want to install {choice} (Persistent)?""")
        self.form.lb_downloadDescription.setWordWrap(True)
        self.form.exec()

# Runs the "Permanent Search" Page
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = PersistentSearchPage()
    window.show()

    sys.exit(app.exec())
