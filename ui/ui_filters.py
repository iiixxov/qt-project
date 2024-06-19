# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filterskyjRMd.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QDateEdit, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_FilterMenu(object):
    def setupUi(self, FilterMenu):
        if not FilterMenu.objectName():
            FilterMenu.setObjectName(u"FilterMenu")
        FilterMenu.resize(378, 562)
        FilterMenu.setStyleSheet(u"")
        self.gridLayout = QGridLayout(FilterMenu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.num = QWidget(FilterMenu)
        self.num.setObjectName(u"num")
        self.num.setEnabled(True)
        self.horizontalLayout_5 = QHBoxLayout(self.num)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.c_num = QComboBox(self.num)
        self.c_num.addItem("")
        self.c_num.addItem("")
        self.c_num.addItem("")
        self.c_num.addItem("")
        self.c_num.addItem("")
        self.c_num.addItem("")
        self.c_num.setObjectName(u"c_num")

        self.horizontalLayout_5.addWidget(self.c_num)

        self.i_num = QLineEdit(self.num)
        self.i_num.setObjectName(u"i_num")

        self.horizontalLayout_5.addWidget(self.i_num)


        self.gridLayout.addWidget(self.num, 3, 0, 1, 1)

        self.filter_list = QListWidget(FilterMenu)
        self.filter_list.setObjectName(u"filter_list")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter_list.sizePolicy().hasHeightForWidth())
        self.filter_list.setSizePolicy(sizePolicy)
        self.filter_list.setFrameShape(QFrame.NoFrame)
        self.filter_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.filter_list.setResizeMode(QListView.Fixed)

        self.gridLayout.addWidget(self.filter_list, 7, 0, 1, 1)

        self.str = QWidget(FilterMenu)
        self.str.setObjectName(u"str")
        self.str.setEnabled(True)
        self.horizontalLayout_3 = QHBoxLayout(self.str)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.c_str = QComboBox(self.str)
        self.c_str.addItem("")
        self.c_str.addItem("")
        self.c_str.setObjectName(u"c_str")

        self.horizontalLayout_3.addWidget(self.c_str)

        self.i_str = QLineEdit(self.str)
        self.i_str.setObjectName(u"i_str")

        self.horizontalLayout_3.addWidget(self.i_str)


        self.gridLayout.addWidget(self.str, 2, 0, 1, 1)

        self.wgt_filter_cmb_bg = QWidget(FilterMenu)
        self.wgt_filter_cmb_bg.setObjectName(u"wgt_filter_cmb_bg")
        self.horizontalLayout_2 = QHBoxLayout(self.wgt_filter_cmb_bg)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cmb_column = QComboBox(self.wgt_filter_cmb_bg)
        self.cmb_column.setObjectName(u"cmb_column")

        self.horizontalLayout_2.addWidget(self.cmb_column)


        self.gridLayout.addWidget(self.wgt_filter_cmb_bg, 1, 0, 1, 1)

        self.label = QLabel(FilterMenu)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.date = QWidget(FilterMenu)
        self.date.setObjectName(u"date")
        self.date.setEnabled(True)
        self.horizontalLayout_6 = QHBoxLayout(self.date)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.c_date = QComboBox(self.date)
        self.c_date.addItem("")
        self.c_date.addItem("")
        self.c_date.addItem("")
        self.c_date.addItem("")
        self.c_date.addItem("")
        self.c_date.addItem("")
        self.c_date.setObjectName(u"c_date")

        self.horizontalLayout_6.addWidget(self.c_date)

        self.i_date = QDateEdit(self.date)
        self.i_date.setObjectName(u"i_date")
        self.i_date.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.i_date.sizePolicy().hasHeightForWidth())
        self.i_date.setSizePolicy(sizePolicy1)
        self.i_date.setReadOnly(False)
        self.i_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.i_date.setAccelerated(False)
        self.i_date.setProperty("showGroupSeparator", False)
        self.i_date.setCalendarPopup(True)
        self.i_date.setCurrentSectionIndex(0)

        self.horizontalLayout_6.addWidget(self.i_date)


        self.gridLayout.addWidget(self.date, 4, 0, 1, 1)

        self.widget = QWidget(FilterMenu)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cmb_enum = QComboBox(self.widget)
        self.cmb_enum.setObjectName(u"cmb_enum")

        self.horizontalLayout_4.addWidget(self.cmb_enum)


        self.gridLayout.addWidget(self.widget, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_add = QPushButton(FilterMenu)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout.addWidget(self.btn_add)

        self.btn_accept = QPushButton(FilterMenu)
        self.btn_accept.setObjectName(u"btn_accept")
        self.btn_accept.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_accept)


        self.gridLayout.addLayout(self.horizontalLayout, 8, 0, 1, 1)


        self.retranslateUi(FilterMenu)

        QMetaObject.connectSlotsByName(FilterMenu)
    # setupUi

    def retranslateUi(self, FilterMenu):
        FilterMenu.setWindowTitle(QCoreApplication.translate("FilterMenu", u"Form", None))
        self.c_num.setItemText(0, QCoreApplication.translate("FilterMenu", u"\u0420\u0430\u0432\u043d\u043e", None))
        self.c_num.setItemText(1, QCoreApplication.translate("FilterMenu", u"\u041d\u0435 \u0440\u0430\u0432\u043d\u043e", None))
        self.c_num.setItemText(2, QCoreApplication.translate("FilterMenu", u"\u0411\u043e\u043b\u044c\u0448\u0435", None))
        self.c_num.setItemText(3, QCoreApplication.translate("FilterMenu", u"\u041c\u0435\u043d\u044c\u0448\u0435", None))
        self.c_num.setItemText(4, QCoreApplication.translate("FilterMenu", u"\u041d\u0435 \u0431\u043e\u043b\u044c\u0448\u0435", None))
        self.c_num.setItemText(5, QCoreApplication.translate("FilterMenu", u"\u041d\u0435 \u043c\u0435\u043d\u044c\u0448\u0435", None))

        self.c_str.setItemText(0, QCoreApplication.translate("FilterMenu", u"\u0421\u043e\u0434\u0435\u0440\u0436\u0438\u0442", None))
        self.c_str.setItemText(1, QCoreApplication.translate("FilterMenu", u"\u041d\u0435 \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442", None))

        self.label.setText(QCoreApplication.translate("FilterMenu", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0444\u0438\u043b\u044c\u0442\u0440\u0430", None))
        self.c_date.setItemText(0, QCoreApplication.translate("FilterMenu", u"\u0420\u0430\u0432\u043d\u043e", None))
        self.c_date.setItemText(1, QCoreApplication.translate("FilterMenu", u"\u041d\u0435 \u0440\u0430\u0432\u043d\u043e", None))
        self.c_date.setItemText(2, QCoreApplication.translate("FilterMenu", u"\u0411\u043e\u043b\u044c\u0448\u0435", None))
        self.c_date.setItemText(3, QCoreApplication.translate("FilterMenu", u"\u041c\u0435\u043d\u044c\u0448\u0435", None))
        self.c_date.setItemText(4, QCoreApplication.translate("FilterMenu", u"\u041d\u0435 \u0431\u043e\u043b\u044c\u0448\u0435", None))
        self.c_date.setItemText(5, QCoreApplication.translate("FilterMenu", u"\u041d\u0435 \u043c\u0435\u043d\u044c\u0448\u0435", None))

        self.i_date.setSpecialValueText("")
        self.btn_add.setText(QCoreApplication.translate("FilterMenu", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_accept.setText(QCoreApplication.translate("FilterMenu", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
    # retranslateUi

