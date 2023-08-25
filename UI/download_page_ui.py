# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'download_page.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import Icons_rc

class Ui_d_download(object):
    def setupUi(self, d_download):
        if not d_download.objectName():
            d_download.setObjectName(u"d_download")
        d_download.resize(400, 233)
        icon = QIcon()
        icon.addFile(u":/Logo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        d_download.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(d_download)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(d_download)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 2)

        self.pb_cancel = QPushButton(self.groupBox)
        self.pb_cancel.setObjectName(u"pb_cancel")
        font1 = QFont()
        font1.setPointSize(8)
        self.pb_cancel.setFont(font1)

        self.gridLayout.addWidget(self.pb_cancel, 2, 2, 1, 1)

        self.pb_download = QPushButton(self.groupBox)
        self.pb_download.setObjectName(u"pb_download")
        self.pb_download.setFont(font1)

        self.gridLayout.addWidget(self.pb_download, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.lb_downloadDescription = QLabel(self.groupBox)
        self.lb_downloadDescription.setObjectName(u"lb_downloadDescription")
        font2 = QFont()
        font2.setPointSize(12)
        self.lb_downloadDescription.setFont(font2)
        self.lb_downloadDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lb_downloadDescription.setMargin(5)

        self.gridLayout.addWidget(self.lb_downloadDescription, 0, 0, 1, 3)


        self.verticalLayout.addWidget(self.groupBox)

        QWidget.setTabOrder(self.pb_download, self.pb_cancel)

        self.retranslateUi(d_download)

        QMetaObject.connectSlotsByName(d_download)
    # setupUi

    def retranslateUi(self, d_download):
        d_download.setWindowTitle(QCoreApplication.translate("d_download", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("d_download", u"GroupBox", None))
        self.pb_cancel.setText(QCoreApplication.translate("d_download", u"Cancel", None))
        self.pb_download.setText(QCoreApplication.translate("d_download", u"Download", None))
        self.lb_downloadDescription.setText(QCoreApplication.translate("d_download", u"TextLabel", None))
    # retranslateUi

