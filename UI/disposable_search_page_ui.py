# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'disposable_search_page.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QPushButton,
    QScrollArea, QSizePolicy, QWidget)
import Icons_rc

class Ui_w_addDisposableApps(object):
    def setupUi(self, w_addDisposableApps):
        if not w_addDisposableApps.objectName():
            w_addDisposableApps.setObjectName(u"w_addDisposableApps")
        w_addDisposableApps.setWindowModality(Qt.ApplicationModal)
        w_addDisposableApps.setEnabled(True)
        w_addDisposableApps.resize(525, 377)
        icon = QIcon()
        icon.addFile(u":/Logo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        w_addDisposableApps.setWindowIcon(icon)
        w_addDisposableApps.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(w_addDisposableApps)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gb_main = QGroupBox(w_addDisposableApps)
        self.gb_main.setObjectName(u"gb_main")
        font = QFont()
        font.setPointSize(20)
        self.gb_main.setFont(font)
        self.gb_main.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.gb_main)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(self.gb_main)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -146, 468, 447))
        self.gridLayout_13 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gb_firefox = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gb_firefox.setObjectName(u"gb_firefox")
        font1 = QFont()
        font1.setPointSize(12)
        self.gb_firefox.setFont(font1)
        self.gb_firefox.setAutoFillBackground(False)
        self.gb_firefox.setAlignment(Qt.AlignCenter)
        self.gridLayout_3 = QGridLayout(self.gb_firefox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pb_firefox = QPushButton(self.gb_firefox)
        self.pb_firefox.setObjectName(u"pb_firefox")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/browser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_firefox.setIcon(icon1)
        self.pb_firefox.setIconSize(QSize(90, 90))

        self.gridLayout_3.addWidget(self.pb_firefox, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.gb_firefox, 0, 0, 1, 1)

        self.gb_fedora = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gb_fedora.setObjectName(u"gb_fedora")
        self.gb_fedora.setFont(font1)
        self.gb_fedora.setAlignment(Qt.AlignCenter)
        self.gridLayout_8 = QGridLayout(self.gb_fedora)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pb_fedora = QPushButton(self.gb_fedora)
        self.pb_fedora.setObjectName(u"pb_fedora")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/desktop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_fedora.setIcon(icon2)
        self.pb_fedora.setIconSize(QSize(90, 90))

        self.gridLayout_8.addWidget(self.pb_fedora, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.gb_fedora, 2, 1, 1, 1)

        self.gb_chromium = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gb_chromium.setObjectName(u"gb_chromium")
        self.gb_chromium.setFont(font1)
        self.gb_chromium.setAlignment(Qt.AlignCenter)
        self.gridLayout_5 = QGridLayout(self.gb_chromium)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pb_chromium = QPushButton(self.gb_chromium)
        self.pb_chromium.setObjectName(u"pb_chromium")
        self.pb_chromium.setIcon(icon1)
        self.pb_chromium.setIconSize(QSize(90, 90))

        self.gridLayout_5.addWidget(self.pb_chromium, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.gb_chromium, 0, 1, 1, 1)

        self.gb_arch = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gb_arch.setObjectName(u"gb_arch")
        self.gb_arch.setFont(font1)
        self.gb_arch.setAlignment(Qt.AlignCenter)
        self.gridLayout_9 = QGridLayout(self.gb_arch)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pb_arch = QPushButton(self.gb_arch)
        self.pb_arch.setObjectName(u"pb_arch")
        self.pb_arch.setIcon(icon2)
        self.pb_arch.setIconSize(QSize(90, 90))

        self.gridLayout_9.addWidget(self.pb_arch, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.gb_arch, 2, 2, 1, 1)

        self.gb_ubuntu = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gb_ubuntu.setObjectName(u"gb_ubuntu")
        self.gb_ubuntu.setFont(font1)
        self.gb_ubuntu.setAlignment(Qt.AlignCenter)
        self.gridLayout_7 = QGridLayout(self.gb_ubuntu)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pb_ubuntu = QPushButton(self.gb_ubuntu)
        self.pb_ubuntu.setObjectName(u"pb_ubuntu")
        self.pb_ubuntu.setIcon(icon2)
        self.pb_ubuntu.setIconSize(QSize(90, 90))

        self.gridLayout_7.addWidget(self.pb_ubuntu, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.gb_ubuntu, 2, 0, 1, 1)

        self.gb_opera = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gb_opera.setObjectName(u"gb_opera")
        self.gb_opera.setFont(font1)
        self.gb_opera.setAlignment(Qt.AlignCenter)
        self.gridLayout_6 = QGridLayout(self.gb_opera)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pb_opera = QPushButton(self.gb_opera)
        self.pb_opera.setObjectName(u"pb_opera")
        self.pb_opera.setIcon(icon1)
        self.pb_opera.setIconSize(QSize(90, 90))

        self.gridLayout_6.addWidget(self.pb_opera, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.gb_opera, 0, 2, 1, 1)

        self.gb_debian = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gb_debian.setObjectName(u"gb_debian")
        self.gb_debian.setFont(font1)
        self.gb_debian.setAlignment(Qt.AlignCenter)
        self.gridLayout_10 = QGridLayout(self.gb_debian)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.pb_debian = QPushButton(self.gb_debian)
        self.pb_debian.setObjectName(u"pb_debian")
        self.pb_debian.setIcon(icon2)
        self.pb_debian.setIconSize(QSize(90, 90))

        self.gridLayout_10.addWidget(self.pb_debian, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.gb_debian, 3, 0, 1, 1)

        self.gb_alpine = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gb_alpine.setObjectName(u"gb_alpine")
        self.gb_alpine.setFont(font1)
        self.gb_alpine.setAlignment(Qt.AlignCenter)
        self.gridLayout_11 = QGridLayout(self.gb_alpine)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pb_alpine = QPushButton(self.gb_alpine)
        self.pb_alpine.setObjectName(u"pb_alpine")
        self.pb_alpine.setIcon(icon2)
        self.pb_alpine.setIconSize(QSize(90, 90))

        self.gridLayout_11.addWidget(self.pb_alpine, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.gb_alpine, 3, 1, 1, 1)

        self.gb_libreoffice = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gb_libreoffice.setObjectName(u"gb_libreoffice")
        self.gb_libreoffice.setFont(font1)
        self.gb_libreoffice.setAlignment(Qt.AlignCenter)
        self.gridLayout_12 = QGridLayout(self.gb_libreoffice)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.pb_libreoffice = QPushButton(self.gb_libreoffice)
        self.pb_libreoffice.setObjectName(u"pb_libreoffice")
        self.pb_libreoffice.setIcon(icon2)
        self.pb_libreoffice.setIconSize(QSize(90, 90))

        self.gridLayout_12.addWidget(self.pb_libreoffice, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.gb_libreoffice, 3, 2, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 3)


        self.gridLayout.addWidget(self.gb_main, 0, 0, 1, 1)


        self.retranslateUi(w_addDisposableApps)

        QMetaObject.connectSlotsByName(w_addDisposableApps)
    # setupUi

    def retranslateUi(self, w_addDisposableApps):
        w_addDisposableApps.setWindowTitle(QCoreApplication.translate("w_addDisposableApps", u"Nutshell | Disposable Application Search", None))
        self.gb_main.setTitle(QCoreApplication.translate("w_addDisposableApps", u"Application Search (Disposable)", None))
        self.gb_firefox.setTitle(QCoreApplication.translate("w_addDisposableApps", u"Firefox", None))
        self.pb_firefox.setText("")
        self.gb_fedora.setTitle(QCoreApplication.translate("w_addDisposableApps", u"Fedora", None))
        self.pb_fedora.setText("")
        self.gb_chromium.setTitle(QCoreApplication.translate("w_addDisposableApps", u"Chromium", None))
        self.pb_chromium.setText("")
        self.gb_arch.setTitle(QCoreApplication.translate("w_addDisposableApps", u"Arch", None))
        self.pb_arch.setText("")
        self.gb_ubuntu.setTitle(QCoreApplication.translate("w_addDisposableApps", u"Ubuntu", None))
        self.pb_ubuntu.setText("")
        self.gb_opera.setTitle(QCoreApplication.translate("w_addDisposableApps", u"Opera", None))
        self.pb_opera.setText("")
        self.gb_debian.setTitle(QCoreApplication.translate("w_addDisposableApps", u"Debian", None))
        self.pb_debian.setText("")
        self.gb_alpine.setTitle(QCoreApplication.translate("w_addDisposableApps", u"Alpine", None))
        self.pb_alpine.setText("")
        self.gb_libreoffice.setTitle(QCoreApplication.translate("w_addDisposableApps", u"LibreOffice", None))
        self.pb_libreoffice.setText("")
    # retranslateUi

