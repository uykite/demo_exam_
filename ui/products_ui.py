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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.titile_label = QLabel(self.centralwidget)
        self.titile_label.setObjectName(u"titile_label")
        self.titile_label.setGeometry(QRect(260, 40, 301, 71))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.titile_label.setFont(font)
        self.titile_label.setAcceptDrops(False)
        self.titile_label.setFrameShape(QFrame.Shape.Box)
        self.titile_label.setLineWidth(3)
        self.titile_label.setMidLineWidth(2)
        self.titile_label.setTextFormat(Qt.TextFormat.AutoText)
        self.titile_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titile_label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0432\u0430\u0440\u044b", None))
    # retranslateUi

