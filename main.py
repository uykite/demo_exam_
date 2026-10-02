import sys
from pathlib import Path


from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import Qt
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QLineEdit,
    QPushButton,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QComboBox
)


from products import get_products, get_categories
from auth import get_user, check_password


def load_ui(ui_file_path):
    ui_file = QFile(str(ui_file_path))
    ui_file.open(QFile.ReadOnly)

    loader = QUiLoader()
    window = loader.load(ui_file)

    ui_file.close()

    return window


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        project_path = Path(__file__).parent

        login_path = project_path / "ui" / "login.ui"
        products_path = project_path / "ui" / "products.ui"

        self.login_window = load_ui(login_path)
        self.products_window = load_ui(products_path)

        self.username_input = self.login_window.findChild(
            QLineEdit,
            "username_input"
        )

        self.password_input = self.login_window.findChild(
            QLineEdit,
            "password_input"
        )

        self.login_button = self.login_window.findChild(
            QPushButton,
            "login_button"
        )

        self.guest_button = self.login_window.findChild(
            QPushButton,
            "guest_button"
        )

        self.error_label = self.login_window.findChild(
            QLabel,
            "error_label"
        )
        
        self.products_table = self.products_window.findChild(
            QTableWidget,
            "products_table"
        )
        
        self.search_input = self.products_window.findChild(
            QLineEdit,
            "search_input"
        )
        
        self.category_filter = self.products_window.findChild(
            QComboBox,
            "category_filter"
        )

        self.stack.addWidget(self.login_window)
        self.stack.addWidget(self.products_window)

        self.stack.setCurrentWidget(self.login_window)

        self.login_button.clicked.connect(
            self.login
        )

        self.guest_button.clicked.connect(
            self.login_as_guest
        )
        self.load_categories()
        self.search_input.textChanged.connect(self.load_products)
        self.category_filter.currentIndexChanged.connect(
            self.load_products
        )


    def load_categories(self):
        try:
            categories = get_categories()
            
            self.category_filter.clear()
            self.category_filter.addItem("Все категории", None)
            
            for category in categories:
                self.category_filter.addItem(
                    category["name"],
                    category['id']
                )
        except Exception as e:
            print("Ощибка загрузик категорий",e)
            
    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text()

        if not username or not password:
            self.error_label.setText(
                "Введите логин и пароль."
            )
            return

        try:
            user = get_user(username)

            if user is None:
                self.error_label.setText(
                    "Пользователь не найден."
                )
                return

            if not check_password(
                password,
                user["password"]
            ):
                self.error_label.setText(
                    "Неверный пароль."
                )
                return

            self.current_user = user
            
            self.load_products()

            self.error_label.setText("")

            self.stack.setCurrentWidget(
                self.products_window
            )

            print("Успешный вход:")
            print("Пользователь:", user["username"])
            print("Имя:", user["full_name"])
            print("Роль:", user["role_name"])

        except Exception as error:
            self.error_label.setText(
                "Ошибка при входе в систему."
            )

            print("Ошибка авторизации:", error)

    def login_as_guest(self):
        self.current_user = {
            "id": None,
            "username": None,
            "password": None,
            "full_name": "Гость",
            "role_name": "Гость"
        }

        self.load_products()
        self.error_label.setText("")

        self.stack.setCurrentWidget(
            self.products_window
        )
    def load_products(self):
        try:
            search = self.search_input.text().strip()
            category = self.category_filter.currentData()
            
            print("Поиск:", search)
            print("Категория:", category)
            
            products = get_products(search, category)
            
            self.products_table.setRowCount(0)
        
            
            for product in products:
                row = self.products_table.rowCount()
                self.products_table.insertRow(row)
                
                image_path = Path(__file__).parent / product["image_path"]
                
                pixmap = QPixmap(str(image_path))
                pixmap = pixmap.scaled(
                    100,70,Qt.KeepAspectRatio
                )
                
                item = QTableWidgetItem()
                item.setData(
                    Qt.DecorationRole,
                    pixmap
                )
                self.products_table.setItem(
                    row,
                    0,
                    item
                )
                
                
                self.products_table.setItem(
                    row,1,
                    QTableWidgetItem(
                        product["name"]
                    )
                )
                
                self.products_table.setItem(
                    row,2,
                    QTableWidgetItem(
                        product["category_name"]
                    )
                )
                
                self.products_table.setItem(
                    row,3,
                    QTableWidgetItem(
                        product["description"] or ""
                    )
                )
                
                self.products_table.setItem(
                    row,4,
                    QTableWidgetItem(
                        product["manufacturer_name"]
                    )
                )
                
                self.products_table.setItem(
                    row,5,
                    QTableWidgetItem(
                        product["supplier_name"]
                    )
                )
                
                self.products_table.setItem(
                    row,6,
                    QTableWidgetItem(
                        str(product["price"])
                    )
                )
                
                self.products_table.setItem(
                    row,7,
                    QTableWidgetItem(
                        product["unit"]
                    )
                )
                
                self.products_table.setItem(
                    row,8,
                    QTableWidgetItem(
                        str(product["stock_quantity"])
                    )
                )
                
                self.products_table.setItem(
                    row,9,
                    QTableWidgetItem(
                        str(product["discount"])
                    )
                )
                
                if product["stock_quantity"] == 0:
                    for column in range(10):
                        self.products_table.item(row,column).setBackground(
                            QColor("#87CEEB")
                        )
                elif product["discount"] > 15:
                    for column in range(10):
                        self.products_table.item(row,column).setBackground(
                            QColor("#2E8B57")
                        )
                
                
        except Exception as e:
            print("Error: ", e)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()