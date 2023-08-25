#!/usr/bin/env python

# Imports the modules necessary for GUI development
import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.main_window_ui import Ui_mw_Main
from program_type import ProgramTypePage
from manage_apps import ManagePage

class MainWindow(qtw.QMainWindow, Ui_mw_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Custom actions/buttons
        self.action_close.triggered.connect(self.close)
        self.pb_cancel.clicked.connect(self.close)

        self.action_manage.triggered.connect(self.open_manage)
        self.pb_manageApps.clicked.connect(self.open_manage)

        self.action_add.triggered.connect(self.open_search)
        self.pb_appSearch.clicked.connect(self.open_search)

    @qtc.Slot()
    def open_search(self):
        """Opens the 'Program Type" Page"""
        self.form = ProgramTypePage()
        self.form.show()

    @qtc.Slot()
    def open_manage(self):
        """Opens the 'Manage Apps' Page"""
        self.form = ManagePage()
        self.form.show()

# Runs the "Main" Page
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
