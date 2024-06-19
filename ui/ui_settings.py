# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsTfhYfr.ui'
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
    QHeaderView, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(833, 536)
        Form.setStyleSheet(u"* {\n"
"	background-color: rgb(239, 243, 246);\n"
"border: 1px solid red;\n"
"color: black;\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(30, 30, 30, 30)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.settings_layout = QWidget()
        self.settings_layout.setObjectName(u"settings_layout")
        self.settings_layout.setGeometry(QRect(0, 0, 669, 438))
        self.gridLayout = QGridLayout(self.settings_layout)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea.setWidget(self.settings_layout)

        self.gridLayout_2.addWidget(self.scrollArea, 2, 1, 1, 1)

        self.settings_tree = QTreeWidget(self.widget)
        __qtreewidgetitem = QTreeWidgetItem(self.settings_tree)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(self.settings_tree)
        self.settings_tree.setObjectName(u"settings_tree")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_tree.sizePolicy().hasHeightForWidth())
        self.settings_tree.setSizePolicy(sizePolicy)
        self.settings_tree.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.settings_tree.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.settings_tree.setAutoScrollMargin(16)
        self.settings_tree.setAutoExpandDelay(-1)
        self.settings_tree.setIndentation(20)
        self.settings_tree.setRootIsDecorated(True)
        self.settings_tree.setUniformRowHeights(False)
        self.settings_tree.setItemsExpandable(True)
        self.settings_tree.setSortingEnabled(False)
        self.settings_tree.setAnimated(False)
        self.settings_tree.setAllColumnsShowFocus(False)
        self.settings_tree.setWordWrap(False)
        self.settings_tree.setHeaderHidden(True)
        self.settings_tree.setExpandsOnDoubleClick(True)
        self.settings_tree.setColumnCount(1)
        self.settings_tree.header().setVisible(False)
        self.settings_tree.header().setCascadingSectionResizes(False)
        self.settings_tree.header().setMinimumSectionSize(41)
        self.settings_tree.header().setDefaultSectionSize(100)
        self.settings_tree.header().setHighlightSections(False)
        self.settings_tree.header().setProperty("showSortIndicator", False)
        self.settings_tree.header().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.settings_tree, 2, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(611, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_save = QPushButton(self.widget_2)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_save)


        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 1, 2)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtreewidgetitem = self.settings_tree.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None));

        __sortingEnabled = self.settings_tree.isSortingEnabled()
        self.settings_tree.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.settings_tree.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Form", u"_database", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Form", u"host", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("Form", u"port", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("Form", u"db_name", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(3)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("Form", u"connect_args", None));
        ___qtreewidgetitem6 = self.settings_tree.topLevelItem(1)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        self.settings_tree.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

