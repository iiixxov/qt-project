# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profileITkFOY.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(336, 713)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btn_profile_logo = QPushButton(Form)
        self.btn_profile_logo.setObjectName(u"btn_profile_logo")
        icon = QIcon()
        icon.addFile(u"data/icons/user-b.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_profile_logo.setIcon(icon)
        self.btn_profile_logo.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_profile_logo)

        self.lbl_username = QLabel(Form)
        self.lbl_username.setObjectName(u"lbl_username")
        self.lbl_username.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_username)

        self.btn_change_password = QPushButton(Form)
        self.btn_change_password.setObjectName(u"btn_change_password")

        self.verticalLayout.addWidget(self.btn_change_password)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_profile_logo.setText("")
        self.lbl_username.setText(QCoreApplication.translate("Form", u"\u0418\u041c\u042f \u041f\u041e\u041b\u042c\u0417\u041e\u0412\u0410\u0422\u0415\u041b\u042f", None))
        self.btn_change_password.setText(QCoreApplication.translate("Form", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
    # retranslateUi

