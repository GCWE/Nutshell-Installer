# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view_info.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
import Icons_rc

class Ui_w_info(object):
    def setupUi(self, w_info):
        if not w_info.objectName():
            w_info.setObjectName(u"w_info")
        w_info.setWindowModality(Qt.ApplicationModal)
        w_info.resize(335, 144)
        icon = QIcon()
        icon.addFile(u":/Logo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        w_info.setWindowIcon(icon)
        self.gridLayout = QGridLayout(w_info)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gb_info = QGroupBox(w_info)
        self.gb_info.setObjectName(u"gb_info")
        font = QFont()
        font.setPointSize(12)
        self.gb_info.setFont(font)
        self.gb_info.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.gb_info)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 2)

        self.label = QLabel(self.gb_info)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lb_regDate = QLabel(self.gb_info)
        self.lb_regDate.setObjectName(u"lb_regDate")

        self.gridLayout_2.addWidget(self.lb_regDate, 0, 1, 1, 1)

        self.pb_close = QPushButton(self.gb_info)
        self.pb_close.setObjectName(u"pb_close")
        font2 = QFont()
        font2.setPointSize(10)
        self.pb_close.setFont(font2)

        self.gridLayout_2.addWidget(self.pb_close, 2, 2, 1, 1)

        self.pb_delete = QPushButton(self.gb_info)
        self.pb_delete.setObjectName(u"pb_delete")
        self.pb_delete.setFont(font2)

        self.gridLayout_2.addWidget(self.pb_delete, 2, 0, 1, 2)


        self.gridLayout.addWidget(self.gb_info, 0, 0, 1, 1)


        self.retranslateUi(w_info)

        QMetaObject.connectSlotsByName(w_info)
    # setupUi

    def retranslateUi(self, w_info):
        w_info.setWindowTitle(QCoreApplication.translate("w_info", u"Nutshell | View Info", None))
        self.gb_info.setTitle(QCoreApplication.translate("w_info", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("w_info", u"Build Date:", None))
        self.lb_regDate.setText(QCoreApplication.translate("w_info", u"TextLabel", None))
        self.pb_close.setText(QCoreApplication.translate("w_info", u"Close", None))
        self.pb_delete.setText(QCoreApplication.translate("w_info", u"Delete Program", None))
    # retranslateUi

