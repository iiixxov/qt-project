# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notification_widgetaJcrVj.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_NotificationWidget(object):
    def setupUi(self, NotificationWidget):
        if not NotificationWidget.objectName():
            NotificationWidget.setObjectName(u"NotificationWidget")
        NotificationWidget.resize(175, 94)
        NotificationWidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(NotificationWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.notification_widget_bg = QWidget(NotificationWidget)
        self.notification_widget_bg.setObjectName(u"notification_widget_bg")
        self.gridLayout = QGridLayout(self.notification_widget_bg)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 25, 9, -1)
        self.btn_icon = QPushButton(self.notification_widget_bg)
        self.btn_icon.setObjectName(u"btn_icon")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_icon.sizePolicy().hasHeightForWidth())
        self.btn_icon.setSizePolicy(sizePolicy)
        self.btn_icon.setMinimumSize(QSize(0, 0))
        self.btn_icon.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"data/icons/Notification-b.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_icon.setIcon(icon)
        self.btn_icon.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.btn_icon, 0, 0, 2, 1)

        self.lbl_header = QLabel(self.notification_widget_bg)
        self.lbl_header.setObjectName(u"lbl_header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_header.sizePolicy().hasHeightForWidth())
        self.lbl_header.setSizePolicy(sizePolicy1)
        self.lbl_header.setWordWrap(True)

        self.gridLayout.addWidget(self.lbl_header, 0, 1, 1, 1)

        self.lbl_body = QLabel(self.notification_widget_bg)
        self.lbl_body.setObjectName(u"lbl_body")
        sizePolicy.setHeightForWidth(self.lbl_body.sizePolicy().hasHeightForWidth())
        self.lbl_body.setSizePolicy(sizePolicy)
        self.lbl_body.setWordWrap(True)

        self.gridLayout.addWidget(self.lbl_body, 1, 1, 1, 1)

        self.lbl_time = QLabel(self.notification_widget_bg)
        self.lbl_time.setObjectName(u"lbl_time")
        self.lbl_time.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_time.setWordWrap(True)

        self.gridLayout.addWidget(self.lbl_time, 2, 0, 1, 2)


        self.horizontalLayout.addWidget(self.notification_widget_bg)


        self.retranslateUi(NotificationWidget)

        QMetaObject.connectSlotsByName(NotificationWidget)
    # setupUi

    def retranslateUi(self, NotificationWidget):
        NotificationWidget.setWindowTitle(QCoreApplication.translate("NotificationWidget", u"Form", None))
        self.btn_icon.setText("")
        self.lbl_header.setText(QCoreApplication.translate("NotificationWidget", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a", None))
        self.lbl_body.setText(QCoreApplication.translate("NotificationWidget", u"\u0422\u0435\u043b\u043e\u0422\u0435\u043b\u043e\u0422\u0435\u043b\u043e\u0422\u0435\u043b\u043e\u0422\u0435\u043b", None))
        self.lbl_time.setText(QCoreApplication.translate("NotificationWidget", u"\u0412\u0440\u0435\u043c\u044f", None))
    # retranslateUi

