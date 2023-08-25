# Imports the modules necessary for the GUI development
import sys
from datetime import datetime
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.download_page_ui import Ui_d_download

# Modules required for writing files
import os
from pathlib import Path
import json

# Imports the "build date" dictionary into the program
path = Path("build_date.json")
contents = path.read_text()
build_date = json.loads(contents)

class DownloadPage(qtw.QDialog, Ui_d_download):
   def __init__(self):
      super().__init__()
      self.setupUi(self)

      # Custom buttons
      self.pb_cancel.clicked.connect(self.close)
      self.pb_download.clicked.connect(self.create_dockerfile)

   @qtc.Slot()
   def create_dockerfile(self):
      """Building the program"""
      
      from program_type import persistent

      # Determines whether the program to be built is persistent or not
      if persistent == True:
         from persistent_search import program_name
      else:
         from disposable_search import program_name

      # Current working directory
      directory = os.getcwd()

      # Replaces the \ with a / (to prevent unicode errors)
      directory = directory.replace("\\", "/")

      # Location for the new webtop
      if persistent == True:
         new_webtop = f"{directory}/{program_name}_Webtop"
      else:
         new_webtop = f"{directory}/Disposable_{program_name}_Webtop"

      # If the webtop folder does not already exist
      if os.path.isdir(new_webtop) == False:
         # Webtop folder created
         os.mkdir(new_webtop)

         # Establishing categories
         operating_system = ["Ubuntu", "Fedora", "Arch", "Debian"]
         other_tools = ["Firefox", "Chromium", "Opera", "LibreOffice"]
            
         # If the program is persistent
         if persistent == True:
            program_type = f"{program_name.lower()}_persistent"

            # Creates config file (to store volumes)
            os.mkdir(f"{new_webtop}/config")

            # Building file for specific operating systems
            if program_name in operating_system:
               with open(f"{new_webtop}/docker-compose.yml", "w") as docker_file:
                  docker_file.write(f"""---
version: "2.1"
services:
   webtop:
      image: ghcr.io/linuxserver/webtop:{program_name.lower()}-xfce
      container_name: {program_name.lower()}_webtop
      environment:
         - PUID=1000
         - PGID=1000
         - TZ=Etc/UTC
      volumes:
         - {new_webtop}/config:/config
      ports:
         - 300{operating_system.index(program_name)}:3000
      shm_size: "1gb"
      restart: unless-stopped""")
            
            # Building file for Alpine OS
            elif program_name == "Alpine":
               with open(f"{new_webtop}/docker-compose.yml", "w") as docker_file:
                  docker_file.write(f"""---
version: "2.1"
services:
   webtop:
      image: ghcr.io/linuxserver/webtop:latest
      container_name: alpine_webtop
      environment:
         - PUID=1000
         - PGID=1000
         - TZ=Etc/UTC
      volumes:
         - {new_webtop}/config:/config
      ports:
         - 3004:3000
      shm_size: "1gb"
      restart: unless-stopped""")
            
            # Building file for browsers/LibreOffice
            else:
               with open(f"{new_webtop}/docker-compose.yml", "w") as docker_file:
                  docker_file.write(f"""---
version: "2.1"
services:
  {program_name.lower()}:
    image: lscr.io/linuxserver/{program_name.lower()}:latest
    container_name: {program_name.lower()}
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
         - {new_webtop}/config:/config
    ports:
      - 300{other_tools.index(program_name) + 5}:3000
    shm_size: "1gb"
    restart: unless-stopped""")
            
         # If the desired program is disposable
         else:
            program_type = f"{program_name.lower()}_disposable"

            if program_name in operating_system:
               with open(f"{new_webtop}/docker-compose.yml", "w") as docker_file:
                  docker_file.write(f"""---
version: "2.1"
services:
   webtop:
      image: ghcr.io/linuxserver/webtop:{program_name.lower()}-xfce
      container_name: disposable_{program_name.lower()}_webtop
      environment:
         - PUID=1000
         - PGID=1000
         - TZ=Etc/UTC
      ports:
         - 300{operating_system.index(program_name) + 9}:3000
      shm_size: "1gb"
      restart: unless-stopped""")
            
            elif program_name == "Alpine":
               with open(f"{new_webtop}/docker-compose.yml", "w") as docker_file:
                  docker_file.write(f"""---
version: "2.1"
services:
   webtop:
      image: ghcr.io/linuxserver/webtop:latest
      container_name: disposable_alpine_webtop
      environment:
         - PUID=1000
         - PGID=1000
         - TZ=Etc/UTC
      ports:
         - 30013:3000
      shm_size: "1gb"
      restart: unless-stopped""")
            
            else:
               with open(f"{new_webtop}/docker-compose.yml", "w") as docker_file:
                  docker_file.write(f"""---
version: "2.1"
services:
  {program_name.lower()}:
    image: lscr.io/linuxserver/{program_name.lower()}:latest
    container_name: disposable_{program_name.lower()}
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    ports:
      - 300{other_tools.index(program_name) + 14}:3000
    shm_size: "1gb"
    restart: unless-stopped""")
                  
         if persistent == True:
            program = f"{program_name} (Persistent)"
         else:
            program = f"{program_name} (Disposable)"

         # Ascending order of the programs' display port
         port_order = ["Ubuntu (Persistent)",
                       "Fedora (Persistent)",
                       "Arch (Persistent)",
                       "Debian (Persistent)",
                       "Alpine (Persistent)",
                       "Firefox (Persistent)",
                       "Chromium (Persistent)",
                       "Opera (Persistent)",
                       "LibreOffice (Persistent)",
                       "Ubuntu (Disposable)",
                       "Fedora (Disposable)",
                       "Arch (Disposable)",
                       "Debian (Disposable)",
                       "Alpine (Disposable)",
                       "Firefox (Disposable)",
                       "Chromium (Disposable)",
                       "Opera (Disposable)",
                       "LibreOffice (Disposable)"]

         # File for running webtop
         with open(f"{new_webtop}/run_{program_type}.py", "w") as run_nutshell:
            run_nutshell.write(f"""#!/usr/bin/env python
# Imports the modules necessary for GUI development
import time
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# Provides access to the web - opens "localhost:300{port_order.index(program)}"
from PyQt5.QtWebEngineWidgets import *

class RunNutshell():
   def __init__(self):
      os.system("docker-compose -f {new_webtop}/docker-compose.yml up -d")
      
      # Prevents the program from crashing (from loading too early)
      time.sleep(3)

      # Builds the program window
      self.window = QWidget()

      # Sets the window title unique to the program's purpose
      self.window.setWindowTitle("{program}")

      # Widget that opens the web
      self.browser = QWebEngineView()

      # Places the widget in the window
      self.layout = QVBoxLayout()
      self.layout.addWidget(self.browser)

      # Sets the program route to the webtop
      self.browser.setUrl(QUrl("http://localhost:300{port_order.index(program)}/"))

      # Displays the program window
      self.window.setLayout(self.layout)
      self.window.show()

      app.aboutToQuit.connect(self.closeEvent)
      
   def closeEvent(self):
      os.system("docker-compose -f {new_webtop}/docker-compose.yml down")

# Runs the window
app = QApplication([])
window = RunNutshell()
app.exec()""")
		
      # Makes file executable
      os.system(f"chmod a+x {new_webtop}/run_{program_type}.py")

      desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
      
      # Creates a desktop shortcut to the executable
      with open(f"{desktop}/run_{program_type}.desktop", "w") as desktop_shortcut:
         desktop_shortcut.write(f"""[Desktop Entry]
Version=1.0
Type=Application
Name={program}
Exec={new_webtop}/run_{program_type}.py
Path={directory}
Terminal=false
StartupNotify=false
""")
         # Saves date to JSON file
         current_time = datetime.now()
         timestamp = datetime.fromtimestamp(current_time.timestamp())
         str_build_date = timestamp.strftime("%d %B, %Y")

         build_date[program] = str_build_date

         with open("build_date.json", "w") as outfile:
            json.dump(build_date, outfile)

         self.close()

         # Success message and instructions to proceed
         self.success_msg = qtw.QMessageBox()

         self.success_msg.setWindowTitle(f"Successfully installed {program}")
         self.success_msg.setText(f"{program} was successfully installed! You can now close Nutshell Installer.\n\nNote that the first boot of {program_name} may take a couple of minutes. Check Task Manager to see that the daemon is running.\n\nIf you're worried, open a terminal and execute:\n	cd {new_webtop}\n	./run_{program_type}.py\n\nAfter that, you're all set!")
         self.success_msg.exec()         

# Opens the "Download" page
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    download_dialog = DownloadPage()
    download_dialog.open()

    sys.exit(app.exec())
