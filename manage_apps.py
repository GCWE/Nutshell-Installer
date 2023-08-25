import os
import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.manage_apps_ui import Ui_w_manageApps
from view_info import InfoPage

programs = ["Firefox", "Chromium", "Opera", "Ubuntu", "Fedora", "Arch", "Debian", "Alpine", "LibreOffice"]

class ManagePage(qtw.QWidget, Ui_w_manageApps):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.gb_main.setFont(qtg.QFont("Segoe UI", 14))

        directory = os.getcwd()
        
        for program in programs:
            exec(f"self.pb_{program.lower()}Persistent.clicked.connect(lambda: self.open_info('{program}', ' (Persistent)'))", locals())
            exec(f"self.pb_{program.lower()}Disposable.clicked.connect(lambda: self.open_info('{program}', ' (Disposable)'))", locals())

            persistent_webtop = f"{directory}/{program}_Webtop"
            disposable_webtop = f"{directory}/Disposable_{program}_Webtop"

            if os.path.isdir(persistent_webtop) == False:
                exec(f"self.gb_{program.lower()}Persistent.setVisible(False)")
            
            if os.path.isdir(disposable_webtop) == False:
                exec(f"self.gb_{program.lower()}Disposable.setVisible(False)")

    @qtc.Slot()
    def open_info(self, program, state):
        global program_name
        global program_type

        program_name = program
        program_type = program + state

        self.form = InfoPage()
        self.form.show()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = ManagePage()
    window.show()

    sys.exit(app.exec())