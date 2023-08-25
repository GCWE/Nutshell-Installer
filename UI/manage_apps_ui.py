# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manage_apps.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)
import Icons_rc

class Ui_w_manageApps(object):
    def setupUi(self, w_manageApps):
        if not w_manageApps.objectName():
            w_manageApps.setObjectName(u"w_manageApps")
        w_manageApps.setWindowModality(Qt.ApplicationModal)
        w_manageApps.resize(563, 398)
        self.gridLayout = QGridLayout(w_manageApps)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gb_main = QGroupBox(w_manageApps)
        self.gb_main.setObjectName(u"gb_main")
        self.gb_main.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.gb_main)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(self.gb_main)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 506, 828))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gb_chromiumDisposable = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_chromiumDisposable.setObjectName(u"gb_chromiumDisposable")
        self.verticalLayout_11 = QVBoxLayout(self.gb_chromiumDisposable)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.gb_chromiumDisposable)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setPixmap(QPixmap(u":/Buttons/browser.png"))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_11)

        self.pb_chromiumDisposable = QPushButton(self.gb_chromiumDisposable)
        self.pb_chromiumDisposable.setObjectName(u"pb_chromiumDisposable")

        self.verticalLayout_11.addWidget(self.pb_chromiumDisposable)


        self.gridLayout_3.addWidget(self.gb_chromiumDisposable, 3, 1, 1, 1)

        self.gb_fedoraDisposable = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_fedoraDisposable.setObjectName(u"gb_fedoraDisposable")
        self.verticalLayout_14 = QVBoxLayout(self.gb_fedoraDisposable)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_10 = QLabel(self.gb_fedoraDisposable)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u":/Buttons/desktop.png"))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_10)

        self.pb_fedoraDisposable = QPushButton(self.gb_fedoraDisposable)
        self.pb_fedoraDisposable.setObjectName(u"pb_fedoraDisposable")

        self.verticalLayout_14.addWidget(self.pb_fedoraDisposable)


        self.gridLayout_3.addWidget(self.gb_fedoraDisposable, 4, 1, 1, 1)

        self.gb_debianPersistent = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_debianPersistent.setObjectName(u"gb_debianPersistent")
        self.verticalLayout_9 = QVBoxLayout(self.gb_debianPersistent)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.gb_debianPersistent)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/Buttons/desktop.png"))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5)

        self.pb_debianPersistent = QPushButton(self.gb_debianPersistent)
        self.pb_debianPersistent.setObjectName(u"pb_debianPersistent")

        self.verticalLayout_9.addWidget(self.pb_debianPersistent)


        self.gridLayout_3.addWidget(self.gb_debianPersistent, 2, 0, 1, 1)

        self.gb_ubuntuDisposable = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_ubuntuDisposable.setObjectName(u"gb_ubuntuDisposable")
        self.verticalLayout_15 = QVBoxLayout(self.gb_ubuntuDisposable)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_7 = QLabel(self.gb_ubuntuDisposable)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u":/Buttons/desktop.png"))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_7)

        self.pb_ubuntuDisposable = QPushButton(self.gb_ubuntuDisposable)
        self.pb_ubuntuDisposable.setObjectName(u"pb_ubuntuDisposable")

        self.verticalLayout_15.addWidget(self.pb_ubuntuDisposable)


        self.gridLayout_3.addWidget(self.gb_ubuntuDisposable, 4, 0, 1, 1)

        self.gb_operaPersistent = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_operaPersistent.setObjectName(u"gb_operaPersistent")
        self.verticalLayout = QVBoxLayout(self.gb_operaPersistent)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.gb_operaPersistent)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/Buttons/browser.png"))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.pb_operaPersistent = QPushButton(self.gb_operaPersistent)
        self.pb_operaPersistent.setObjectName(u"pb_operaPersistent")

        self.verticalLayout.addWidget(self.pb_operaPersistent)


        self.gridLayout_3.addWidget(self.gb_operaPersistent, 0, 2, 1, 1)

        self.gb_debianDisposable = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_debianDisposable.setObjectName(u"gb_debianDisposable")
        self.verticalLayout_18 = QVBoxLayout(self.gb_debianDisposable)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_8 = QLabel(self.gb_debianDisposable)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/Buttons/desktop.png"))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_8)

        self.pb_debianDisposable = QPushButton(self.gb_debianDisposable)
        self.pb_debianDisposable.setObjectName(u"pb_debianDisposable")

        self.verticalLayout_18.addWidget(self.pb_debianDisposable)


        self.gridLayout_3.addWidget(self.gb_debianDisposable, 5, 0, 1, 1)

        self.gb_archDisposable = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_archDisposable.setObjectName(u"gb_archDisposable")
        self.verticalLayout_13 = QVBoxLayout(self.gb_archDisposable)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_15 = QLabel(self.gb_archDisposable)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setPixmap(QPixmap(u":/Buttons/desktop.png"))
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_15)

        self.pb_archDisposable = QPushButton(self.gb_archDisposable)
        self.pb_archDisposable.setObjectName(u"pb_archDisposable")

        self.verticalLayout_13.addWidget(self.pb_archDisposable)


        self.gridLayout_3.addWidget(self.gb_archDisposable, 4, 2, 1, 1)

        self.gb_fedoraPersistent = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_fedoraPersistent.setObjectName(u"gb_fedoraPersistent")
        self.verticalLayout_5 = QVBoxLayout(self.gb_fedoraPersistent)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_13 = QLabel(self.gb_fedoraPersistent)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setPixmap(QPixmap(u":/Buttons/desktop.png"))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_13)

        self.pb_fedoraPersistent = QPushButton(self.gb_fedoraPersistent)
        self.pb_fedoraPersistent.setObjectName(u"pb_fedoraPersistent")

        self.verticalLayout_5.addWidget(self.pb_fedoraPersistent)


        self.gridLayout_3.addWidget(self.gb_fedoraPersistent, 1, 1, 1, 1)

        self.gb_operaDisposable = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_operaDisposable.setObjectName(u"gb_operaDisposable")
        self.verticalLayout_12 = QVBoxLayout(self.gb_operaDisposable)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_16 = QLabel(self.gb_operaDisposable)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setPixmap(QPixmap(u":/Buttons/browser.png"))
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_16)

        self.pb_operaDisposable = QPushButton(self.gb_operaDisposable)
        self.pb_operaDisposable.setObjectName(u"pb_operaDisposable")

        self.verticalLayout_12.addWidget(self.pb_operaDisposable)


        self.gridLayout_3.addWidget(self.gb_operaDisposable, 3, 2, 1, 1)

        self.gb_libreofficePersistent = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_libreofficePersistent.setObjectName(u"gb_libreofficePersistent")
        self.verticalLayout_7 = QVBoxLayout(self.gb_libreofficePersistent)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_17 = QLabel(self.gb_libreofficePersistent)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setPixmap(QPixmap(u":/Buttons/desktop.png"))
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_17)

        self.pb_libreofficePersistent = QPushButton(self.gb_libreofficePersistent)
        self.pb_libreofficePersistent.setObjectName(u"pb_libreofficePersistent")

        self.verticalLayout_7.addWidget(self.pb_libreofficePersistent)


        self.gridLayout_3.addWidget(self.gb_libreofficePersistent, 2, 2, 1, 1)

        self.gb_chromiumPersistent = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_chromiumPersistent.setObjectName(u"gb_chromiumPersistent")
        self.verticalLayout_3 = QVBoxLayout(self.gb_chromiumPersistent)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.gb_chromiumPersistent)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/Buttons/browser.png"))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.pb_chromiumPersistent = QPushButton(self.gb_chromiumPersistent)
        self.pb_chromiumPersistent.setObjectName(u"pb_chromiumPersistent")

        self.verticalLayout_3.addWidget(self.pb_chromiumPersistent)


        self.gridLayout_3.addWidget(self.gb_chromiumPersistent, 0, 1, 1, 1)

        self.gb_archPersistent = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_archPersistent.setObjectName(u"gb_archPersistent")
        self.verticalLayout_6 = QVBoxLayout(self.gb_archPersistent)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_18 = QLabel(self.gb_archPersistent)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setPixmap(QPixmap(u":/Buttons/desktop.png"))
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_18)

        self.pb_archPersistent = QPushButton(self.gb_archPersistent)
        self.pb_archPersistent.setObjectName(u"pb_archPersistent")

        self.verticalLayout_6.addWidget(self.pb_archPersistent)


        self.gridLayout_3.addWidget(self.gb_archPersistent, 1, 2, 1, 1)

        self.gb_firefoxPersistent = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_firefoxPersistent.setObjectName(u"gb_firefoxPersistent")
        self.verticalLayout_2 = QVBoxLayout(self.gb_firefoxPersistent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.gb_firefoxPersistent)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/Buttons/browser.png"))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.pb_firefoxPersistent = QPushButton(self.gb_firefoxPersistent)
        self.pb_firefoxPersistent.setObjectName(u"pb_firefoxPersistent")

        self.verticalLayout_2.addWidget(self.pb_firefoxPersistent)


        self.gridLayout_3.addWidget(self.gb_firefoxPersistent, 0, 0, 1, 1)

        self.gb_libreofficeDisposable = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_libreofficeDisposable.setObjectName(u"gb_libreofficeDisposable")
        self.verticalLayout_16 = QVBoxLayout(self.gb_libreofficeDisposable)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_14 = QLabel(self.gb_libreofficeDisposable)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u":/Buttons/desktop.png"))
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_14)

        self.pb_libreofficeDisposable = QPushButton(self.gb_libreofficeDisposable)
        self.pb_libreofficeDisposable.setObjectName(u"pb_libreofficeDisposable")

        self.verticalLayout_16.addWidget(self.pb_libreofficeDisposable)


        self.gridLayout_3.addWidget(self.gb_libreofficeDisposable, 5, 2, 1, 1)

        self.gb_ubuntuPersistent = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_ubuntuPersistent.setObjectName(u"gb_ubuntuPersistent")
        self.verticalLayout_4 = QVBoxLayout(self.gb_ubuntuPersistent)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.gb_ubuntuPersistent)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/Buttons/desktop.png"))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.pb_ubuntuPersistent = QPushButton(self.gb_ubuntuPersistent)
        self.pb_ubuntuPersistent.setObjectName(u"pb_ubuntuPersistent")

        self.verticalLayout_4.addWidget(self.pb_ubuntuPersistent)


        self.gridLayout_3.addWidget(self.gb_ubuntuPersistent, 1, 0, 1, 1)

        self.gb_alpineDisposable = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_alpineDisposable.setObjectName(u"gb_alpineDisposable")
        self.verticalLayout_17 = QVBoxLayout(self.gb_alpineDisposable)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_9 = QLabel(self.gb_alpineDisposable)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setPixmap(QPixmap(u":/Buttons/desktop.png"))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_9)

        self.pb_alpineDisposable = QPushButton(self.gb_alpineDisposable)
        self.pb_alpineDisposable.setObjectName(u"pb_alpineDisposable")

        self.verticalLayout_17.addWidget(self.pb_alpineDisposable)


        self.gridLayout_3.addWidget(self.gb_alpineDisposable, 5, 1, 1, 1)

        self.gb_alpinePersistent = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_alpinePersistent.setObjectName(u"gb_alpinePersistent")
        self.verticalLayout_8 = QVBoxLayout(self.gb_alpinePersistent)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_12 = QLabel(self.gb_alpinePersistent)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setPixmap(QPixmap(u":/Buttons/desktop.png"))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_12)

        self.pb_alpinePersistent = QPushButton(self.gb_alpinePersistent)
        self.pb_alpinePersistent.setObjectName(u"pb_alpinePersistent")

        self.verticalLayout_8.addWidget(self.pb_alpinePersistent)


        self.gridLayout_3.addWidget(self.gb_alpinePersistent, 2, 1, 1, 1)

        self.gb_firefoxDisposable = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_firefoxDisposable.setObjectName(u"gb_firefoxDisposable")
        self.verticalLayout_10 = QVBoxLayout(self.gb_firefoxDisposable)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.gb_firefoxDisposable)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/Buttons/browser.png"))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6)

        self.pb_firefoxDisposable = QPushButton(self.gb_firefoxDisposable)
        self.pb_firefoxDisposable.setObjectName(u"pb_firefoxDisposable")

        self.verticalLayout_10.addWidget(self.pb_firefoxDisposable)


        self.gridLayout_3.addWidget(self.gb_firefoxDisposable, 3, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.gb_main, 0, 0, 1, 1)


        self.retranslateUi(w_manageApps)

        QMetaObject.connectSlotsByName(w_manageApps)
    # setupUi

    def retranslateUi(self, w_manageApps):
        w_manageApps.setWindowTitle(QCoreApplication.translate("w_manageApps", u"Nutshell | Manage Apps", None))
        self.gb_main.setTitle(QCoreApplication.translate("w_manageApps", u"Manage Applications", None))
        self.gb_chromiumDisposable.setTitle(QCoreApplication.translate("w_manageApps", u"Chromium (Disposable)", None))
        self.label_11.setText("")
        self.pb_chromiumDisposable.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
        self.gb_fedoraDisposable.setTitle(QCoreApplication.translate("w_manageApps", u"Fedora (Disposable)", None))
        self.label_10.setText("")
        self.pb_fedoraDisposable.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
        self.gb_debianPersistent.setTitle(QCoreApplication.translate("w_manageApps", u"Debian (Persistent)", None))
        self.label_5.setText("")
        self.pb_debianPersistent.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
        self.gb_ubuntuDisposable.setTitle(QCoreApplication.translate("w_manageApps", u"Ubuntu (Disposable)", None))
        self.label_7.setText("")
        self.pb_ubuntuDisposable.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
        self.gb_operaPersistent.setTitle(QCoreApplication.translate("w_manageApps", u"Opera (Persistent)", None))
        self.label_3.setText("")
        self.pb_operaPersistent.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
        self.gb_debianDisposable.setTitle(QCoreApplication.translate("w_manageApps", u"Debian (Disposable)", None))
        self.label_8.setText("")
        self.pb_debianDisposable.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
        self.gb_archDisposable.setTitle(QCoreApplication.translate("w_manageApps", u"Arch (Disposable)", None))
        self.label_15.setText("")
        self.pb_archDisposable.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
        self.gb_fedoraPersistent.setTitle(QCoreApplication.translate("w_manageApps", u"Fedora (Persistent)", None))
        self.label_13.setText("")
        self.pb_fedoraPersistent.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
        self.gb_operaDisposable.setTitle(QCoreApplication.translate("w_manageApps", u"Opera (Disposable)", None))
        self.label_16.setText("")
        self.pb_operaDisposable.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
        self.gb_libreofficePersistent.setTitle(QCoreApplication.translate("w_manageApps", u"LibreOffice (Persistent)", None))
        self.label_17.setText("")
        self.pb_libreofficePersistent.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
        self.gb_chromiumPersistent.setTitle(QCoreApplication.translate("w_manageApps", u"Chromium (Persistent)", None))
        self.label_2.setText("")
        self.pb_chromiumPersistent.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
        self.gb_archPersistent.setTitle(QCoreApplication.translate("w_manageApps", u"Arch (Persistent)", None))
        self.label_18.setText("")
        self.pb_archPersistent.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
        self.gb_firefoxPersistent.setTitle(QCoreApplication.translate("w_manageApps", u"Firefox (Persistent)", None))
        self.label.setText("")
        self.pb_firefoxPersistent.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
        self.gb_libreofficeDisposable.setTitle(QCoreApplication.translate("w_manageApps", u"LibreOffice (Disposable)", None))
        self.label_14.setText("")
        self.pb_libreofficeDisposable.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
        self.gb_ubuntuPersistent.setTitle(QCoreApplication.translate("w_manageApps", u"Ubuntu (Persistent)", None))
        self.label_4.setText("")
        self.pb_ubuntuPersistent.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
        self.gb_alpineDisposable.setTitle(QCoreApplication.translate("w_manageApps", u"Alpine (Disposable)", None))
        self.label_9.setText("")
        self.pb_alpineDisposable.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
        self.gb_alpinePersistent.setTitle(QCoreApplication.translate("w_manageApps", u"Alpine (Persistent)", None))
        self.label_12.setText("")
        self.pb_alpinePersistent.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
        self.gb_firefoxDisposable.setTitle(QCoreApplication.translate("w_manageApps", u"Firefox (Disposable)", None))
        self.label_6.setText("")
        self.pb_firefoxDisposable.setText(QCoreApplication.translate("w_manageApps", u"Info", None))
    # retranslateUi

