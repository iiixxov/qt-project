# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataKDvVFx.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QListView, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(906, 630)
        Form.setStyleSheet(u"* {\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(255, 0, 0);\n"
"\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(30, 30, 30, 30)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.layoutWidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_module = QLabel(self.widget_2)
        self.lbl_module.setObjectName(u"lbl_module")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_module.sizePolicy().hasHeightForWidth())
        self.lbl_module.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.lbl_module)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.trw_modules = QTreeWidget(self.layoutWidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.trw_modules.setHeaderItem(__qtreewidgetitem)
        self.trw_modules.setObjectName(u"trw_modules")
        self.trw_modules.setContextMenuPolicy(Qt.CustomContextMenu)
        self.trw_modules.header().setVisible(False)
        self.trw_modules.header().setDefaultSectionSize(100)

        self.verticalLayout_2.addWidget(self.trw_modules)

        self.splitter.addWidget(self.layoutWidget)
        self.wgt_table = QWidget(self.splitter)
        self.wgt_table.setObjectName(u"wgt_table")
        self.verticalLayout_3 = QVBoxLayout(self.wgt_table)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.wgt_table_tools = QWidget(self.wgt_table)
        self.wgt_table_tools.setObjectName(u"wgt_table_tools")
        self.horizontalLayout_6 = QHBoxLayout(self.wgt_table_tools)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.wgt_filters = QWidget(self.wgt_table_tools)
        self.wgt_filters.setObjectName(u"wgt_filters")
        self.horizontalLayout_4 = QHBoxLayout(self.wgt_filters)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_filter = QPushButton(self.wgt_filters)
        self.btn_filter.setObjectName(u"btn_filter")
        icon = QIcon()
        icon.addFile(u"data/icons/Filter-b.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_filter.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.btn_filter)

        self.lst_filter = QListWidget(self.wgt_filters)
        self.lst_filter.setObjectName(u"lst_filter")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lst_filter.sizePolicy().hasHeightForWidth())
        self.lst_filter.setSizePolicy(sizePolicy2)
        self.lst_filter.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lst_filter.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lst_filter.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.lst_filter.setFlow(QListView.LeftToRight)

        self.horizontalLayout_4.addWidget(self.lst_filter)


        self.horizontalLayout_6.addWidget(self.wgt_filters)

        self.wgt_cmd_bg = QWidget(self.wgt_table_tools)
        self.wgt_cmd_bg.setObjectName(u"wgt_cmd_bg")
        self.horizontalLayout_8 = QHBoxLayout(self.wgt_cmd_bg)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_6.addWidget(self.wgt_cmd_bg)

        self.btn_refresh = QPushButton(self.wgt_table_tools)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setFlat(True)

        self.horizontalLayout_6.addWidget(self.btn_refresh)


        self.verticalLayout_3.addWidget(self.wgt_table_tools)

        self.tbl_table = QTableWidget(self.wgt_table)
        self.tbl_table.setObjectName(u"tbl_table")
        self.tbl_table.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self.tbl_table)

        self.wgt_bot_table = QWidget(self.wgt_table)
        self.wgt_bot_table.setObjectName(u"wgt_bot_table")
        self.horizontalLayout_9 = QHBoxLayout(self.wgt_bot_table)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.btn_left_left = QPushButton(self.wgt_bot_table)
        self.btn_left_left.setObjectName(u"btn_left_left")

        self.horizontalLayout_9.addWidget(self.btn_left_left)

        self.btn_left = QPushButton(self.wgt_bot_table)
        self.btn_left.setObjectName(u"btn_left")

        self.horizontalLayout_9.addWidget(self.btn_left)

        self.wdt_lbl_rows_bg_2 = QWidget(self.wgt_bot_table)
        self.wdt_lbl_rows_bg_2.setObjectName(u"wdt_lbl_rows_bg_2")
        self.horizontalLayout_10 = QHBoxLayout(self.wdt_lbl_rows_bg_2)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lbl_rows = QLabel(self.wdt_lbl_rows_bg_2)
        self.lbl_rows.setObjectName(u"lbl_rows")

        self.horizontalLayout_10.addWidget(self.lbl_rows)


        self.horizontalLayout_9.addWidget(self.wdt_lbl_rows_bg_2)

        self.btn_right = QPushButton(self.wgt_bot_table)
        self.btn_right.setObjectName(u"btn_right")

        self.horizontalLayout_9.addWidget(self.btn_right)

        self.btn_right_right = QPushButton(self.wgt_bot_table)
        self.btn_right_right.setObjectName(u"btn_right_right")

        self.horizontalLayout_9.addWidget(self.btn_right_right)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addWidget(self.wgt_bot_table)

        self.splitter.addWidget(self.wgt_table)

        self.horizontalLayout.addWidget(self.splitter)


        self.horizontalLayout_5.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_module.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
        self.btn_filter.setText("")
        self.btn_refresh.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.btn_left_left.setText(QCoreApplication.translate("Form", u"<<", None))
        self.btn_left.setText(QCoreApplication.translate("Form", u"<", None))
        self.lbl_rows.setText(QCoreApplication.translate("Form", u"0-0", None))
        self.btn_right.setText(QCoreApplication.translate("Form", u">", None))
        self.btn_right_right.setText(QCoreApplication.translate("Form", u">>", None))
    # retranslateUi

