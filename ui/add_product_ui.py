# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_product.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_AddProductDialog(object):
    def setupUi(self, AddProductDialog):
        if not AddProductDialog.objectName():
            AddProductDialog.setObjectName(u"AddProductDialog")
        AddProductDialog.resize(798, 880)
        self.verticalLayout = QVBoxLayout(AddProductDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_label = QLabel(AddProductDialog)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.name_label = QLabel(AddProductDialog)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.name_label)

        self.name_input = QLineEdit(AddProductDialog)
        self.name_input.setObjectName(u"name_input")

        self.verticalLayout.addWidget(self.name_input)

        self.category_label = QLabel(AddProductDialog)
        self.category_label.setObjectName(u"category_label")
        self.category_label.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.category_label)

        self.category_combo = QComboBox(AddProductDialog)
        self.category_combo.setObjectName(u"category_combo")

        self.verticalLayout.addWidget(self.category_combo)

        self.description_label = QLabel(AddProductDialog)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.description_label)

        self.description_input = QTextEdit(AddProductDialog)
        self.description_input.setObjectName(u"description_input")
        self.description_input.setMaximumSize(QSize(16777215, 70))

        self.verticalLayout.addWidget(self.description_input)

        self.manufacturer_label = QLabel(AddProductDialog)
        self.manufacturer_label.setObjectName(u"manufacturer_label")
        self.manufacturer_label.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.manufacturer_label)

        self.manufacturer_combo = QComboBox(AddProductDialog)
        self.manufacturer_combo.setObjectName(u"manufacturer_combo")

        self.verticalLayout.addWidget(self.manufacturer_combo)

        self.supplier_label = QLabel(AddProductDialog)
        self.supplier_label.setObjectName(u"supplier_label")

        self.verticalLayout.addWidget(self.supplier_label)

        self.supplier_combo = QComboBox(AddProductDialog)
        self.supplier_combo.setObjectName(u"supplier_combo")

        self.verticalLayout.addWidget(self.supplier_combo)

        self.price_label = QLabel(AddProductDialog)
        self.price_label.setObjectName(u"price_label")

        self.verticalLayout.addWidget(self.price_label)

        self.price_input = QLineEdit(AddProductDialog)
        self.price_input.setObjectName(u"price_input")

        self.verticalLayout.addWidget(self.price_input)

        self.unit_label = QLabel(AddProductDialog)
        self.unit_label.setObjectName(u"unit_label")

        self.verticalLayout.addWidget(self.unit_label)

        self.unit_input = QLineEdit(AddProductDialog)
        self.unit_input.setObjectName(u"unit_input")

        self.verticalLayout.addWidget(self.unit_input)

        self.stock_label = QLabel(AddProductDialog)
        self.stock_label.setObjectName(u"stock_label")

        self.verticalLayout.addWidget(self.stock_label)

        self.stock_input = QLineEdit(AddProductDialog)
        self.stock_input.setObjectName(u"stock_input")

        self.verticalLayout.addWidget(self.stock_input)

        self.discount_label = QLabel(AddProductDialog)
        self.discount_label.setObjectName(u"discount_label")

        self.verticalLayout.addWidget(self.discount_label)

        self.discount_input = QLineEdit(AddProductDialog)
        self.discount_input.setObjectName(u"discount_input")

        self.verticalLayout.addWidget(self.discount_input)

        self.image_label_title = QLabel(AddProductDialog)
        self.image_label_title.setObjectName(u"image_label_title")

        self.verticalLayout.addWidget(self.image_label_title)

        self.image_label = QLabel(AddProductDialog)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setMinimumSize(QSize(300, 200))
        self.image_label.setMaximumSize(QSize(16777215, 16777215))
        self.image_label.setFrameShape(QFrame.Shape.Box)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.image_label)

        self.image_button = QPushButton(AddProductDialog)
        self.image_button.setObjectName(u"image_button")

        self.verticalLayout.addWidget(self.image_button)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.save_button = QPushButton(AddProductDialog)
        self.save_button.setObjectName(u"save_button")

        self.buttons_layout.addWidget(self.save_button)

        self.cancel_button = QPushButton(AddProductDialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.buttons_layout.addWidget(self.cancel_button)


        self.verticalLayout.addLayout(self.buttons_layout)


        self.retranslateUi(AddProductDialog)

        QMetaObject.connectSlotsByName(AddProductDialog)
    # setupUi

    def retranslateUi(self, AddProductDialog):
        AddProductDialog.setWindowTitle(QCoreApplication.translate("AddProductDialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.title_label.setText(QCoreApplication.translate("AddProductDialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.name_label.setText(QCoreApplication.translate("AddProductDialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.category_label.setText(QCoreApplication.translate("AddProductDialog", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.description_label.setText(QCoreApplication.translate("AddProductDialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.manufacturer_label.setText(QCoreApplication.translate("AddProductDialog", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c:", None))
        self.supplier_label.setText(QCoreApplication.translate("AddProductDialog", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a:", None))
        self.price_label.setText(QCoreApplication.translate("AddProductDialog", u"\u0426\u0435\u043d\u0430:", None))
        self.price_input.setPlaceholderText(QCoreApplication.translate("AddProductDialog", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: 1299.99", None))
        self.unit_label.setText(QCoreApplication.translate("AddProductDialog", u"\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f:", None))
        self.stock_label.setText(QCoreApplication.translate("AddProductDialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.stock_input.setPlaceholderText(QCoreApplication.translate("AddProductDialog", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: 10", None))
        self.discount_label.setText(QCoreApplication.translate("AddProductDialog", u"\u0421\u043a\u0438\u0434\u043a\u0430:", None))
        self.discount_input.setPlaceholderText(QCoreApplication.translate("AddProductDialog", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: 15", None))
        self.image_label_title.setText(QCoreApplication.translate("AddProductDialog", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435:", None))
        self.image_label.setText(QCoreApplication.translate("AddProductDialog", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043e", None))
        self.image_button.setText(QCoreApplication.translate("AddProductDialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.save_button.setText(QCoreApplication.translate("AddProductDialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancel_button.setText(QCoreApplication.translate("AddProductDialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

