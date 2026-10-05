# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orders.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_OrdersWindow(object):
    def setupUi(self, OrdersWindow):
        if not OrdersWindow.objectName():
            OrdersWindow.setObjectName(u"OrdersWindow")
        OrdersWindow.resize(540, 333)
        self.verticalLayout = QVBoxLayout(OrdersWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_label = QLabel(OrdersWindow)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.orders_table = QTableWidget(OrdersWindow)
        if (self.orders_table.columnCount() < 5):
            self.orders_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.orders_table.setObjectName(u"orders_table")
        self.orders_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.orders_table.setAlternatingRowColors(True)
        self.orders_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.orders_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.orders_table.horizontalHeader().setStretchLastSection(True)
        self.orders_table.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.orders_table)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.back_button = QPushButton(OrdersWindow)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setMaximumSize(QSize(50, 16777215))

        self.buttons_layout.addWidget(self.back_button)

        self.add_order_button = QPushButton(OrdersWindow)
        self.add_order_button.setObjectName(u"add_order_button")

        self.buttons_layout.addWidget(self.add_order_button)

        self.edit_order_button = QPushButton(OrdersWindow)
        self.edit_order_button.setObjectName(u"edit_order_button")

        self.buttons_layout.addWidget(self.edit_order_button)

        self.delete_order_button = QPushButton(OrdersWindow)
        self.delete_order_button.setObjectName(u"delete_order_button")

        self.buttons_layout.addWidget(self.delete_order_button)


        self.verticalLayout.addLayout(self.buttons_layout)


        self.retranslateUi(OrdersWindow)

        QMetaObject.connectSlotsByName(OrdersWindow)
    # setupUi

    def retranslateUi(self, OrdersWindow):
        OrdersWindow.setWindowTitle(QCoreApplication.translate("OrdersWindow", u"\u0417\u0430\u043a\u0430\u0437\u044b", None))
        self.title_label.setText(QCoreApplication.translate("OrdersWindow", u"\u0417\u0430\u043a\u0430\u0437\u044b", None))
        ___qtablewidgetitem = self.orders_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("OrdersWindow", u"\u0422\u043e\u0432\u0430\u0440", None))
        ___qtablewidgetitem1 = self.orders_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("OrdersWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        ___qtablewidgetitem2 = self.orders_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("OrdersWindow", u"\u041f\u0443\u043d\u043a\u0442 \u0432\u044b\u0434\u0430\u0447\u0438", None))
        ___qtablewidgetitem3 = self.orders_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("OrdersWindow", u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        ___qtablewidgetitem4 = self.orders_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("OrdersWindow", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438", None))
        self.back_button.setText(QCoreApplication.translate("OrdersWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.add_order_button.setText(QCoreApplication.translate("OrdersWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.edit_order_button.setText(QCoreApplication.translate("OrdersWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.delete_order_button.setText(QCoreApplication.translate("OrdersWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

