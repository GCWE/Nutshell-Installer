# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)
import Icons_rc

class Ui_mw_Main(object):
    def setupUi(self, mw_Main):
        if not mw_Main.objectName():
            mw_Main.setObjectName(u"mw_Main")
        mw_Main.resize(576, 437)
        icon = QIcon()
        icon.addFile(u":/Logo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        mw_Main.setWindowIcon(icon)
        self.action_close = QAction(mw_Main)
        self.action_close.setObjectName(u"action_close")
        self.action_close.setCheckable(False)
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_close.setIcon(icon1)
        self.action_add = QAction(mw_Main)
        self.action_add.setObjectName(u"action_add")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_add.setIcon(icon2)
        self.action_manage = QAction(mw_Main)
        self.action_manage.setObjectName(u"action_manage")
        icon3 = QIcon()
        icon3.addFile(u":/Buttons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_manage.setIcon(icon3)
        self.centralwidget = QWidget(mw_Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(24)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pb_appSearch = QPushButton(self.groupBox)
        self.pb_appSearch.setObjectName(u"pb_appSearch")
        font1 = QFont()
        font1.setPointSize(14)
        self.pb_appSearch.setFont(font1)
        self.pb_appSearch.setIcon(icon2)

        self.verticalLayout.addWidget(self.pb_appSearch)

        self.pb_manageApps = QPushButton(self.groupBox)
        self.pb_manageApps.setObjectName(u"pb_manageApps")
        self.pb_manageApps.setFont(font1)
        self.pb_manageApps.setIcon(icon3)

        self.verticalLayout.addWidget(self.pb_manageApps)

        self.pb_cancel = QPushButton(self.groupBox)
        self.pb_cancel.setObjectName(u"pb_cancel")
        self.pb_cancel.setFont(font1)
        self.pb_cancel.setIcon(icon1)

        self.verticalLayout.addWidget(self.pb_cancel)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        mw_Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mw_Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 576, 22))
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menuApps = QMenu(self.menubar)
        self.menuApps.setObjectName(u"menuApps")
        mw_Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mw_Main)
        self.statusbar.setObjectName(u"statusbar")
        mw_Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuApps.menuAction())
        self.menuWindow.addAction(self.action_close)
        self.menuApps.addAction(self.action_add)
        self.menuApps.addAction(self.action_manage)

        self.retranslateUi(mw_Main)

        QMetaObject.connectSlotsByName(mw_Main)
    # setupUi

    def retranslateUi(self, mw_Main):
        mw_Main.setWindowTitle(QCoreApplication.translate("mw_Main", u"Nutshell App Installer", None))
        self.action_close.setText(QCoreApplication.translate("mw_Main", u"Close", None))
        self.action_add.setText(QCoreApplication.translate("mw_Main", u"Search...", None))
        self.action_manage.setText(QCoreApplication.translate("mw_Main", u"Manage...", None))
        self.groupBox.setTitle(QCoreApplication.translate("mw_Main", u"Nutshell App Installer", None))
        self.pb_appSearch.setText(QCoreApplication.translate("mw_Main", u"  Application Search", None))
        self.pb_manageApps.setText(QCoreApplication.translate("mw_Main", u"  Manage Applications", None))
        self.pb_cancel.setText(QCoreApplication.translate("mw_Main", u"  Cancel", None))
        self.menuWindow.setTitle(QCoreApplication.translate("mw_Main", u"Window", None))
        self.menuApps.setTitle(QCoreApplication.translate("mw_Main", u"Apps", None))
    # retranslateUi

