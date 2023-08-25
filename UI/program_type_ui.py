# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'program_type.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import Icons_rc

class Ui_w_programType(object):
    def setupUi(self, w_programType):
        if not w_programType.objectName():
            w_programType.setObjectName(u"w_programType")
        w_programType.setWindowModality(Qt.ApplicationModal)
        w_programType.resize(404, 162)
        icon = QIcon()
        icon.addFile(u":/Logo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        w_programType.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(w_programType)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(w_programType)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_persistent = QPushButton(self.groupBox)
        self.pb_persistent.setObjectName(u"pb_persistent")

        self.gridLayout.addWidget(self.pb_persistent, 3, 0, 1, 1)

        self.pb_disposable = QPushButton(self.groupBox)
        self.pb_disposable.setObjectName(u"pb_disposable")

        self.gridLayout.addWidget(self.pb_disposable, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 0, 1, 2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(w_programType)

        QMetaObject.connectSlotsByName(w_programType)
    # setupUi

    def retranslateUi(self, w_programType):
        w_programType.setWindowTitle(QCoreApplication.translate("w_programType", u"Nutshell | Program Type", None))
        self.groupBox.setTitle("")
#if QT_CONFIG(tooltip)
        self.pb_persistent.setToolTip(QCoreApplication.translate("w_programType", u"Library for programs that save data in between sessions.", None))
#endif // QT_CONFIG(tooltip)
        self.pb_persistent.setText(QCoreApplication.translate("w_programType", u"Persistent", None))
#if QT_CONFIG(tooltip)
        self.pb_disposable.setToolTip(QCoreApplication.translate("w_programType", u"Library of programs which destroy data once session is exited (recommended).", None))
#endif // QT_CONFIG(tooltip)
        self.pb_disposable.setText(QCoreApplication.translate("w_programType", u"Disposable", None))
        self.label.setText(QCoreApplication.translate("w_programType", u"Program Type", None))
    # retranslateUi

