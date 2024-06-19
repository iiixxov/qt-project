# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowxjPqQG.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QHBoxLayout,
    QLabel, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(887, 612)
        MainWindow.setStyleSheet(u"* {\n"
"	background-color: rgb(239, 243, 246);\n"
"border: 1px solid red;\n"
"color: black;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.corner_block = QWidget(self.centralwidget)
        self.corner_block.setObjectName(u"corner_block")
        self.horizontalLayout = QHBoxLayout(self.corner_block)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_system_name = QLabel(self.corner_block)
        self.lbl_system_name.setObjectName(u"lbl_system_name")
        self.lbl_system_name.setScaledContents(False)
        self.lbl_system_name.setAlignment(Qt.AlignCenter)
        self.lbl_system_name.setOpenExternalLinks(False)

        self.horizontalLayout.addWidget(self.lbl_system_name)


        self.gridLayout.addWidget(self.corner_block, 0, 0, 1, 1)

        self.central_block = QTabWidget(self.centralwidget)
        self.central_block.setObjectName(u"central_block")
        self.central_block.setTabPosition(QTabWidget.North)
        self.central_block.setTabShape(QTabWidget.Rounded)
        self.central_block.setElideMode(Qt.ElideLeft)
        self.central_block.setUsesScrollButtons(True)
        self.central_block.setDocumentMode(True)
        self.central_block.setTabsClosable(False)
        self.central_block.setMovable(False)
        self.central_block.setTabBarAutoHide(False)

        self.gridLayout.addWidget(self.central_block, 1, 1, 1, 1)

        self.t_block = QWidget(self.centralwidget)
        self.t_block.setObjectName(u"t_block")
        self.horizontalLayout_2 = QHBoxLayout(self.t_block)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(241, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.t_block, 0, 1, 1, 3)

        self.l_block = QWidget(self.centralwidget)
        self.l_block.setObjectName(u"l_block")
        self.verticalLayout = QVBoxLayout(self.l_block)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 25, 0, 25)
        self.lw_tabs = QListWidget(self.l_block)
        self.lw_tabs.setObjectName(u"lw_tabs")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lw_tabs.sizePolicy().hasHeightForWidth())
        self.lw_tabs.setSizePolicy(sizePolicy)
        self.lw_tabs.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lw_tabs.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.lw_tabs.setFlow(QListView.TopToBottom)
        self.lw_tabs.setProperty("isWrapping", False)
        self.lw_tabs.setResizeMode(QListView.Fixed)
        self.lw_tabs.setLayoutMode(QListView.SinglePass)
        self.lw_tabs.setViewMode(QListView.ListMode)
        self.lw_tabs.setModelColumn(0)
        self.lw_tabs.setSelectionRectVisible(False)

        self.verticalLayout.addWidget(self.lw_tabs)


        self.gridLayout.addWidget(self.l_block, 1, 0, 1, 1)

        self.r_block = QTabWidget(self.centralwidget)
        self.r_block.setObjectName(u"r_block")
        self.r_block.setTabPosition(QTabWidget.North)
        self.r_block.setTabShape(QTabWidget.Rounded)
        self.r_block.setElideMode(Qt.ElideLeft)
        self.r_block.setUsesScrollButtons(True)
        self.r_block.setDocumentMode(True)
        self.r_block.setTabsClosable(False)
        self.r_block.setMovable(False)
        self.r_block.setTabBarAutoHide(False)

        self.gridLayout.addWidget(self.r_block, 1, 2, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.central_block.setCurrentIndex(-1)
        self.r_block.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_system_name.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430", None))
    # retranslateUi

