# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_OrderFormDialog(object):
    def setupUi(self, OrderFormDialog):
        if not OrderFormDialog.objectName():
            OrderFormDialog.setObjectName(u"OrderFormDialog")
        OrderFormDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(OrderFormDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_label = QLabel(OrderFormDialog)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.product_label = QLabel(OrderFormDialog)
        self.product_label.setObjectName(u"product_label")

        self.verticalLayout.addWidget(self.product_label)

        self.product_combo = QComboBox(OrderFormDialog)
        self.product_combo.setObjectName(u"product_combo")

        self.verticalLayout.addWidget(self.product_combo)

        self.status_label = QLabel(OrderFormDialog)
        self.status_label.setObjectName(u"status_label")

        self.verticalLayout.addWidget(self.status_label)

        self.status_combo = QComboBox(OrderFormDialog)
        self.status_combo.setObjectName(u"status_combo")

        self.verticalLayout.addWidget(self.status_combo)

        self.pickup_point_label = QLabel(OrderFormDialog)
        self.pickup_point_label.setObjectName(u"pickup_point_label")

        self.verticalLayout.addWidget(self.pickup_point_label)

        self.pickup_point_combo = QComboBox(OrderFormDialog)
        self.pickup_point_combo.setObjectName(u"pickup_point_combo")

        self.verticalLayout.addWidget(self.pickup_point_combo)

        self.order_date_label = QLabel(OrderFormDialog)
        self.order_date_label.setObjectName(u"order_date_label")

        self.verticalLayout.addWidget(self.order_date_label)

        self.order_date_input = QDateEdit(OrderFormDialog)
        self.order_date_input.setObjectName(u"order_date_input")
        self.order_date_input.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.order_date_input)

        self.pickup_date_label = QLabel(OrderFormDialog)
        self.pickup_date_label.setObjectName(u"pickup_date_label")

        self.verticalLayout.addWidget(self.pickup_date_label)

        self.pickup_date_input = QDateEdit(OrderFormDialog)
        self.pickup_date_input.setObjectName(u"pickup_date_input")
        self.pickup_date_input.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.pickup_date_input)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.save_order_button = QPushButton(OrderFormDialog)
        self.save_order_button.setObjectName(u"save_order_button")

        self.buttons_layout.addWidget(self.save_order_button)

        self.cancel_order_button = QPushButton(OrderFormDialog)
        self.cancel_order_button.setObjectName(u"cancel_order_button")

        self.buttons_layout.addWidget(self.cancel_order_button)


        self.verticalLayout.addLayout(self.buttons_layout)


        self.retranslateUi(OrderFormDialog)

        QMetaObject.connectSlotsByName(OrderFormDialog)
    # setupUi

    def retranslateUi(self, OrderFormDialog):
        OrderFormDialog.setWindowTitle(QCoreApplication.translate("OrderFormDialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.title_label.setText(QCoreApplication.translate("OrderFormDialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.product_label.setText(QCoreApplication.translate("OrderFormDialog", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b:", None))
        self.status_label.setText(QCoreApplication.translate("OrderFormDialog", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u043a\u0430\u0437\u0430:", None))
        self.pickup_point_label.setText(QCoreApplication.translate("OrderFormDialog", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0443\u043d\u043a\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438:", None))
        self.order_date_label.setText(QCoreApplication.translate("OrderFormDialog", u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0430:", None))
        self.pickup_date_label.setText(QCoreApplication.translate("OrderFormDialog", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438:", None))
        self.save_order_button.setText(QCoreApplication.translate("OrderFormDialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancel_order_button.setText(QCoreApplication.translate("OrderFormDialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

