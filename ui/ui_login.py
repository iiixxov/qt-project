# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginTZNKIv.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName(u"LoginDialog")
        LoginDialog.setWindowModality(Qt.WindowModal)
        LoginDialog.resize(530, 177)
        LoginDialog.setMinimumSize(QSize(0, 0))
        LoginDialog.setMaximumSize(QSize(9999, 9999))
        LoginDialog.setStyleSheet(u"#background {\n"
"background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"#logo {\n"
"background: transparent;\n"
"border: null;\n"
"}\n"
"\n"
".QLabel {\n"
"	color: rgb(86, 96, 113)\n"
"}\n"
"\n"
".QLineEdit, .QComboBox {\n"
"	border: null;\n"
"	color: black;\n"
"	font: 11pt \"Segoe UI\";\n"
"background-color: transparent;\n"
"padding: 5;\n"
"border-bottom: 1px solid black;\n"
"}\n"
"\n"
"#btn_login {\n"
"border: null;\n"
"	color: white;\n"
"	font: 11pt \"Segoe UI\";\n"
"background-color: rgb(86, 96, 113);\n"
"padding: 5;\n"
"}\n"
"#btn_login:hover, #ch_login_as_user:hover {\n"
"background-color: rgb(69, 75, 84);\n"
"}\n"
"\n"
"#error_text {\n"
"background: transparent;\n"
"border: null;\n"
"color: rgb(54, 71, 79);\n"
"}\n"
"\n"
".QCheckBox{\n"
"border: null;\n"
"background: transparent;\n"
"color: white;\n"
"padding: 3%;\n"
"text-align: center;\n"
"}\n"
".QCheckBox::indicator {\n"
"width: 0;\n"
"}")
        self.horizontalLayout = QHBoxLayout(LoginDialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.background = QWidget(LoginDialog)
        self.background.setObjectName(u"background")
        self.gridLayout = QGridLayout(self.background)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(25)
        self.gridLayout.setContentsMargins(25, -1, 25, -1)
        self.btn_login = QPushButton(self.background)
        self.btn_login.setObjectName(u"btn_login")

        self.gridLayout.addWidget(self.btn_login, 3, 1, 1, 1)

        self.error_text = QTextEdit(self.background)
        self.error_text.setObjectName(u"error_text")
        self.error_text.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_text.sizePolicy().hasHeightForWidth())
        self.error_text.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.error_text, 2, 0, 2, 1)

        self.inp_password = QLineEdit(self.background)
        self.inp_password.setObjectName(u"inp_password")
        self.inp_password.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.inp_password, 2, 1, 1, 1)

        self.inp_user = QLineEdit(self.background)
        self.inp_user.setObjectName(u"inp_user")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.inp_user.sizePolicy().hasHeightForWidth())
        self.inp_user.setSizePolicy(sizePolicy1)
        self.inp_user.setEchoMode(QLineEdit.Normal)

        self.gridLayout.addWidget(self.inp_user, 1, 1, 1, 1)

        self.system_name = QLabel(self.background)
        self.system_name.setObjectName(u"system_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.system_name.sizePolicy().hasHeightForWidth())
        self.system_name.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.system_name.setFont(font)
        self.system_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.system_name, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.background)


        self.retranslateUi(LoginDialog)

        QMetaObject.connectSlotsByName(LoginDialog)
    # setupUi

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QCoreApplication.translate("LoginDialog", u"\u0412\u0445\u043e\u0434", None))
        self.btn_login.setText(QCoreApplication.translate("LoginDialog", u"\u0412\u041e\u0419\u0422\u0418", None))
        self.error_text.setHtml(QCoreApplication.translate("LoginDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.inp_password.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.inp_user.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.system_name.setText(QCoreApplication.translate("LoginDialog", u"\u0412\u0425\u041e\u0414 \u0412 \u0421\u0418\u0421\u0422\u0415\u041c\u0423", None))
    # retranslateUi

