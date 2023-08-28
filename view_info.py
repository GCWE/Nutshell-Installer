# Imports the modules necessary for GUI development
import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.view_info_ui import Ui_w_info

# Modules required for deleting program data
import os
from pathlib import Path
import json
import shutil
import subprocess

# Imports the "build date" dictionary into the program
path = Path("build_date.json")

# Current working directory
directory = os.getcwd()
directory = directory.replace("\\", "/")

class InfoPage(qtw.QWidget, Ui_w_info):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Reads the contents to ensure they've been updated accordingly
        contents = path.read_text()
        build_date = json.loads(contents)
		
        from manage_apps import program_type
		
		# Styles the window title
        self.gb_info.setTitle(program_type)
        self.gb_info.setFont(qtg.QFont("Segoe UI", 14))
        self.lb_regDate.setText(build_date[program_type])
		
		# Custom buttons
        self.pb_delete.clicked.connect(self.check_delete)
        self.pb_close.clicked.connect(self.close)

    @qtc.Slot()
    def check_delete(self):
        """If the user wishes to delete a given program"""

        # Rereads the contents to ensure they've been updated accordingly
        contents = path.read_text()
        build_date = json.loads(contents)

        from manage_apps import program_name, program_type
		
		# Messagebox appears, querying whether the user really wants to remove the program
        delete_msg = qtw.QMessageBox()
        delete_msg.setWindowTitle(f"Delete {program_type}?")
        delete_msg.setIcon(qtw.QMessageBox.Critical)
        delete_msg.setText(f"Are you sure you want to delete {program_type}?\n\nWARNING: This will remove all files associated with the program. The {program_type} container must stop running before this process is executed.")
        delete_msg.setStandardButtons(qtw.QMessageBox.Yes | qtw.QMessageBox.Cancel)
        delete_msg.setDefaultButton(qtw.QMessageBox.Cancel)
        user_choice = delete_msg.exec()

		# If the user does, the deletion process is initiated
        if user_choice == qtw.QMessageBox.Yes:
        	# Messageboxes close
            self.close()
            delete_msg.close()
			
			# Messagebox informs the user not to close the program
            processing_msg = qtw.QMessageBox()
            processing_msg.setWindowTitle(f"Deleting {program_type}")
            processing_msg.setText(f"Deleting {program_type}...\n\nExit out of this window, but DO NOT close Nutshell Installer.")
            processing_msg.exec()

            # Establishing locations
            persistent_webtop = f"{directory}/{program_name}_Webtop"
            disposable_webtop = f"{directory}/Disposable_{program_name}_Webtop"
            
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            
            # If the program is persistent
            if "(Persistent)" in program_type:
                os.system(f"docker-compose -f {persistent_webtop}/docker-compose.yml down")
                # Deletes the webtop folder, including all files within it
                shutil.rmtree(persistent_webtop)
                
                # Removes the desktop shortcut
                os.remove(f"{desktop}/run_{program_name.lower()}_persistent.desktop")
            #If the program is disposable
            else:
                os.system(f"docker-compose -f {disposable_webtop}/docker-compose.yml down")
                # Deletes the webtop folder, including all files within it
                shutil.rmtree(disposable_webtop)
                
                # Removes the desktop shortcut
                os.remove(f"{desktop}/run_{program_name.lower()}_disposable.desktop")

            # The "build date" info is removed from the JSON file
            del build_date[program_type]

            with open("build_date.json", "w") as outfile:
                json.dump(build_date, outfile)

            # Only deletes the image if there are no webtops using it
            if os.path.isdir(persistent_webtop) == False or os.path.isdir(disposable_webtop) == False:
                # Gets the image id for the specific program
                if program_name in ["Ubuntu", "Fedora", "Arch", "Debian"]:
                    image_id = subprocess.getoutput(f"docker images ghcr.io/linuxserver/webtop:{program_name.lower()}-xfce --format '\u007b\u007b.ID\u007d\u007d'")
                elif program_name == "Alpine":
                    image_id = subprocess.getoutput(f"docker images ghcr.io/linuxserver/webtop:latest --format '\u007b\u007b.ID\u007d\u007d'")
                else:
                    image_id = subprocess.getoutput(f"docker images lscr.io/linuxserver/{program_name.lower()}:latest --format '\u007b\u007b.ID\u007d\u007d'")
                
                # Removes apostrophes from id
                image_id = image_id.replace("'", "")
                
                # Only deletes the image if it exists
                if image_id != "":
                    # Removes the image with the image id
                    os.system(f"docker rmi {image_id}")

            # Outputs a success message
            processing_msg.setWindowTitle("Success!")
            processing_msg.setText(f"Successfully removed {program_type}!\n\nYou can now close Nutshell Installer.")
            processing_msg.exec()
    
# Runs the "View Info" page
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = InfoPage()
    window.show()

    sys.exit(app.exec())
