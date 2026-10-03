# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'products.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.WindowModal)
        MainWindow.resize(647, 299)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_widget = QWidget(self.widget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.header_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logout_button = QPushButton(self.header_widget)
        self.logout_button.setObjectName(u"logout_button")

        self.horizontalLayout.addWidget(self.logout_button)

        self.title_label = QLabel(self.header_widget)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.title_label.setFont(font)

        self.horizontalLayout.addWidget(self.title_label)

        self.horizontalSpacer = QSpacerItem(774, 19, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.user_label = QLabel(self.header_widget)
        self.user_label.setObjectName(u"user_label")

        self.horizontalLayout.addWidget(self.user_label)


        self.verticalLayout.addWidget(self.header_widget)

        self.filters_widget = QWidget(self.widget)
        self.filters_widget.setObjectName(u"filters_widget")
        self.filters_widget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.filters_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_input = QLineEdit(self.filters_widget)
        self.search_input.setObjectName(u"search_input")

        self.horizontalLayout_2.addWidget(self.search_input)

        self.category_filter = QComboBox(self.filters_widget)
        self.category_filter.addItem("")
        self.category_filter.setObjectName(u"category_filter")

        self.horizontalLayout_2.addWidget(self.category_filter)

        self.sort_combo = QComboBox(self.filters_widget)
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.setObjectName(u"sort_combo")

        self.horizontalLayout_2.addWidget(self.sort_combo)


        self.verticalLayout.addWidget(self.filters_widget)

        self.products_table = QTableWidget(self.widget)
        if (self.products_table.columnCount() < 10):
            self.products_table.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.products_table.setObjectName(u"products_table")
        self.products_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.products_table.setAlternatingRowColors(True)
        self.products_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout.addWidget(self.products_table)

        self.actions_widget = QWidget(self.widget)
        self.actions_widget.setObjectName(u"actions_widget")
        self.actions_widget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.actions_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.add_product_button = QPushButton(self.actions_widget)
        self.add_product_button.setObjectName(u"add_product_button")

        self.horizontalLayout_3.addWidget(self.add_product_button)

        self.edit_product_button = QPushButton(self.actions_widget)
        self.edit_product_button.setObjectName(u"edit_product_button")

        self.horizontalLayout_3.addWidget(self.edit_product_button)

        self.delete_product_button = QPushButton(self.actions_widget)
        self.delete_product_button.setObjectName(u"delete_product_button")

        self.horizontalLayout_3.addWidget(self.delete_product_button)


        self.verticalLayout.addWidget(self.actions_widget)


        self.verticalLayout_2.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logout_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0432\u0430\u0440\u044b", None))
        self.user_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0442\u043e\u0432\u0430\u0440\u043e\u0432...", None))
        self.category_filter.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))

        self.sort_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0437 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438", None))
        self.sort_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.sort_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430", None))
        self.sort_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u0442\u043e\u043a", None))
        self.sort_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0438\u0434\u043a\u0430", None))

        ___qtablewidgetitem = self.products_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        ___qtablewidgetitem1 = self.products_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        ___qtablewidgetitem2 = self.products_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        ___qtablewidgetitem3 = self.products_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        ___qtablewidgetitem4 = self.products_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        ___qtablewidgetitem5 = self.products_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a", None))
        ___qtablewidgetitem6 = self.products_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430", None))
        ___qtablewidgetitem7 = self.products_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0434\u0438\u043d\u0438\u0446\u0430", None))
        ___qtablewidgetitem8 = self.products_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u0442\u043e\u043a", None))
        ___qtablewidgetitem9 = self.products_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0438\u0434\u043a\u0430", None))
        self.add_product_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440", None))
        self.edit_product_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440", None))
        self.delete_product_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440", None))
    # retranslateUi

