# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModality.WindowModal)
        Dialog.resize(385, 292)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setFrameShape(QFrame.Shape.Box)
        self.label.setLineWidth(4)
        self.label.setMidLineWidth(4)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.guest_button = QPushButton(Dialog)
        self.guest_button.setObjectName(u"guest_button")

        self.gridLayout.addWidget(self.guest_button, 4, 0, 1, 1)

        self.password_input = QLineEdit(Dialog)
        self.password_input.setObjectName(u"password_input")
        font1 = QFont()
        font1.setPointSize(14)
        self.password_input.setFont(font1)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.password_input, 2, 0, 1, 1)

        self.login_button = QPushButton(Dialog)
        self.login_button.setObjectName(u"login_button")

        self.gridLayout.addWidget(self.login_button, 3, 0, 1, 1)

        self.username_input = QLineEdit(Dialog)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setFont(font1)

        self.gridLayout.addWidget(self.username_input, 1, 0, 1, 1)

        self.error_label = QLabel(Dialog)
        self.error_label.setObjectName(u"error_label")

        self.gridLayout.addWidget(self.error_label, 5, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.guest_button.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u0439\u0442\u0438 \u043a\u0430\u043a \u0433\u043e\u0441\u0442\u044c", None))
        self.password_input.setText("")
        self.password_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"password...", None))
        self.login_button.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.username_input.setText("")
        self.username_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"login...", None))
        self.error_label.setText("")
    # retranslateUi

