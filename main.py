import sys
import shutil

from pathlib import Path

from PySide6.QtWidgets import QFileDialog
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
    QComboBox,
    QTextEdit
)


from products import get_products, get_categories, get_manufactures, get_suppliers, add_product, get_product, update_product
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
        add_product_path = project_path/ "ui" / "add_product.ui"
        self.selected_image_path = None
        self.editing_product_image_path = None
        self.editing_product_id = None
        self.login_window = load_ui(login_path)
        self.products_window = load_ui(products_path)
        self.add_product_window = load_ui(add_product_path)
        
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
        self.sort_combo = self.products_window.findChild(
            QComboBox,
            "sort_combo"
        )
        self.add_product_button = self.products_window.findChild(
            QPushButton,
            "add_product_button"
        )
        
        self.product_category_combo = self.add_product_window.findChild(
            QComboBox,
            "category_combo"
        )
        
        self.product_manufacturer_combo = self.add_product_window.findChild(
            QComboBox,
            "manufacturer_combo"
        )
        
        self.product_supplier_combo = self.add_product_window.findChild(
            QComboBox,
            "supplier_combo"
        )
        
        self.product_name_input = self.add_product_window.findChild(
            QLineEdit,
            "name_input"
        )

        self.product_description_input = self.add_product_window.findChild(
            QTextEdit,
            "description_input"
        )

        self.product_price_input = self.add_product_window.findChild(
            QLineEdit,
            "price_input"
        )

        self.product_unit_input = self.add_product_window.findChild(
            QLineEdit,
            "unit_input"
        )

        self.product_stock_input = self.add_product_window.findChild(
            QLineEdit,
            "stock_input"
        )

        self.product_discount_input = self.add_product_window.findChild(
            QLineEdit,
            "discount_input"
        )

        self.product_save_button = self.add_product_window.findChild(
            QPushButton,
            "save_button"
        )

        self.product_cancel_button = self.add_product_window.findChild(
            QPushButton,
            "cancel_button"
        )     
        
        self.product_image_button= self.add_product_window.findChild(
            QPushButton,
            "image_button"
        )
        
        self.product_image_label = self.add_product_window.findChild(
            QLabel,
            "image_label"
        )
        
        self.user_label = self.products_window.findChild(
            QLabel,
            "user_label"
        )
        
        self.logout_button = self.products_window.findChild(
            QPushButton,
            "logout_button"
        )
        
        self.edit_product_button = self.products_window.findChild(
            QPushButton,
            "edit_product_button"
        )           
        
        self.delete_product_button = self.products_window.findChild(
            QPushButton,
            "delete_product_button"
        )
        
        self.supplier_filter = self.products_window.findChild(
            QComboBox,
            "supplier_filter"
        )
        

        self.stack.addWidget(self.login_window)
        self.stack.addWidget(self.products_window)

        self.stack.setCurrentWidget(self.login_window)

        self.login_button.clicked.connect(self.login)
        self.guest_button.clicked.connect(self.login_as_guest)
        self.load_categories()
        self.load_supplier()
        self.search_input.textChanged.connect(self.load_products)
        self.category_filter.currentIndexChanged.connect(self.load_products)
        self.sort_combo.currentIndexChanged.connect(self.load_products)
        self.add_product_button.clicked.connect(self.open_add_product)
        self.product_save_button.clicked.connect(self.save_product)
        self.product_cancel_button.clicked.connect(self.add_product_window.close)
        self.product_image_button.clicked.connect(self.select_image)
        self.logout_button.clicked.connect(self.logout)
        self.supplier_filter.currentIndexChanged.connect(self.load_products)
        self.edit_product_button.clicked.connect(self.open_edit_product)

    def logout(self):
        self.current_user = None
        
        self.username_input.clear()
        self.password_input.clear()
        self.error_label.setText("")
        
        self.stack.setCurrentWidget(self.login_window)
    
    def select_image(self):
        fille_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите изображение",
            "",
            "Изображения (*.png *.jpg *.jpeg)"
        )
        if not fille_path:
            return
        
        self.selected_image_path = fille_path
        
        pixmap = QPixmap(fille_path)
        
        if pixmap.isNull():
            self.selected_image_path = None
            return
        
        pixmap = pixmap.scaled(
            300,
            200,
            Qt.KeepAspectRatio
        )
        
        self.product_image_label.setPixmap(pixmap)
        self.product_image_label.setText("")



    def save_product(self):
        name = self.product_name_input.text().strip()
        description = self.product_description_input.toPlainText().strip()
        
        category_id = self.product_category_combo.currentData()
        manufacturer_id = self.product_manufacturer_combo.currentData()
        supplier_id = self.product_supplier_combo.currentData()
        
        price_text = self.product_price_input.text().strip()
        unit = self.product_unit_input.text().strip()
        stock_text = self.product_stock_input.text().strip()
        discount_text = self.product_discount_input.text().strip()

        if not name:
            print("Ошибка: не указано название товара")
            return

        if category_id is None:
            print("Ошибка: не выбрана категория")
            return

        if manufacturer_id is None:
            print("Ошибка: не выбран производитель")
            return

        if supplier_id is None:
            print("Ошибка: не выбран поставщик")
            return

        if not unit:
            print("Ошибка: не указана единица измерения")
            return

        # Проверяем цену
        try:
            price = float(price_text)
        except ValueError:
            print("Ошибка: цена должна быть числом")
            return

        if price < 0:
            print("Ошибка: цена не может быть отрицательной")
            return

        # Проверяем количество
        try:
            stock_quantity = int(stock_text)
        except ValueError:
            print("Ошибка: количество должно быть целым числом")
            return

        if stock_quantity < 0:
            print("Ошибка: количество не может быть отрицательным")
            return

        # Проверяем скидку
        try:
            discount = float(discount_text)
        except ValueError:
            print("Ошибка: скидка должна быть числом")
            return

        if discount < 0 or discount > 100:
            print("Ошибка: скидка должна быть от 0 до 100")
            return


        image_path = self.editing_product_image_path

        if self.selected_image_path:
            images_folder = Path(__file__).parent / "images"
            images_folder.mkdir(exist_ok=True)

            source_path = Path(self.selected_image_path)
            image_name = source_path.name

            destination_path = images_folder / image_name
            shutil.copy2(source_path, destination_path)

            image_path = f"images/{image_name}"
        try:
            if self.editing_product_id is None:
                add_product(
                    name,
                    category_id,
                    description,
                    manufacturer_id,
                    supplier_id,
                    price,
                    unit,
                    stock_quantity,
                    discount,
                    image_path
                )
                print("Успешно добавлено")
            else:
                update_product(
                    self.editing_product_id,
                    name,
                    category_id,
                    description,
                    manufacturer_id,
                    supplier_id,
                    price,
                    unit,
                    stock_quantity,
                    discount,
                    image_path
                )
                print("Товар успешно изменен")
                if self.selected_image_path and self.editing_product_image_path:
                    old_image = Path(__file__).parent / self.editing_product_image_path
                    
                    if old_image.exists() and old_image != Path(__file__).parent/image_path:
                        old_image.unlink()
                        
                        
            self.add_product_window.close()
            self.load_products()
    
        except Exception as e:
            import traceback
            print("Ошибка при сохранении товара:", e)
            traceback.print_exc() 
        

    def open_add_product(self):
        self.editing_product_id = None
        self.selected_image_path = None

        self.add_product_window.setWindowTitle("Добавление товара")
        self.product_image_label.clear()
        self.product_image_label.setText("Изображение не выбрано")

        self.product_name_input.clear()
        self.product_description_input.clear()
        self.product_price_input.clear()
        self.product_unit_input.clear()
        self.product_stock_input.clear()
        self.product_discount_input.clear()

        self.load_product_form_data()

        self.add_product_window.show()

    def load_product_form_data(self):
        try:
            categories = get_categories()
            manufacturers = get_manufactures()
            suppliers = get_suppliers()
            
            self.product_category_combo.clear()
            self.product_manufacturer_combo.clear()
            self.product_supplier_combo.clear()
            
            for category in categories:
                self.product_category_combo.addItem(
                    category["name"],
                    category["id"]
                )
                
            for manufacturer in manufacturers:
                self.product_manufacturer_combo.addItem(
                    manufacturer["name"],
                    manufacturer["id"]
                )
            
            for supplier in suppliers:
                self.product_supplier_combo.addItem(
                    supplier["name"],
                    supplier["id"]
                )
        except Exception as e:
            print("Error",e)
    
    
    def load_supplier(self):
        self.supplier_filter.clear()
        self.supplier_filter.addItem("Все поставщики",None)

        suppliers = get_suppliers()
        
        for supplier in suppliers:
            self.supplier_filter.addItem(
                supplier["name"],
                supplier["id"]
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
            self.user_label.setText(user["full_name"])
            self.apply_role_permissions()
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
        self.user_label.setText("Гость")
        self.apply_role_permissions()
        self.load_products()
        self.error_label.setText("")

        self.stack.setCurrentWidget(
            self.products_window
        )
        
    def apply_role_permissions(self):
        role = self.current_user["role_name"]

        is_admin = role == "Администратор"
        is_manager = role == "Менеджер"

        self.search_input.setEnabled(is_admin or is_manager)
        self.category_filter.setEnabled(is_admin or is_manager)
        self.sort_combo.setEnabled(is_admin or is_manager)
        self.supplier_filter.setEnabled(is_admin or is_manager)

        self.add_product_button.setVisible(is_admin)
        self.edit_product_button.setVisible(is_admin)
        self.delete_product_button.setVisible(is_admin)
        
    def load_products(self):
        try:
            search = self.search_input.text().strip()
            category = self.category_filter.currentData()   
            supplier = self.supplier_filter.currentData()       
            sort = self.sort_combo.currentText()
            products = get_products(
                search,
                category,
                supplier,
                sort
            )
            
            self.products_table.setRowCount(0)
        
            
            for product in products:
                row = self.products_table.rowCount()
                self.products_table.insertRow(row)
                
                #ПОЯСНИТЬ ЧАТОМ ГПТ
                item = QTableWidgetItem()
                item.setData(Qt.UserRole,product["id"])

                image_path = None

                if product["image_path"]:
                    image_path = Path(__file__).parent / product["image_path"]

                # Если изображения нет или оно не найдено,
                # используем изображение-заглушку
                if image_path is None or not image_path.exists():
                    image_path = Path(__file__).parent / "images" / "not_found.jpg"

                pixmap = QPixmap(str(image_path))

                if not pixmap.isNull():
                    pixmap = pixmap.scaled(
                        100,
                        70,
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )

                    item.setData(Qt.DecorationRole, pixmap)

                self.products_table.setItem(row, 0, item)
                #ПОЯСНИТЬ ЧАТОМ ГПТ
                
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
                
                price = float(product["price"])
                discount = float(product["discount"])

                if discount > 0:
                    discounted_price = price * (1 - discount / 100)

                    price_label = QLabel()
                    price_label.setText(
                        f"""
                        <span style="color:red; text-decoration:line-through;">
                            {price:.2f}
                        </span>
                        <br>
                        <span style="color:black;">
                            {discounted_price:.2f}
                        </span>
                        """
                    )

                    self.products_table.setCellWidget(row, 6, price_label)

                else:
                    self.products_table.setItem(
                        row,
                        6,
                        QTableWidgetItem(f"{price:.2f}")
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
                        item = self.products_table.item(row, column)

                        if item is not None:
                            item.setBackground(QColor("#87CEEB"))

                    price_widget = self.products_table.cellWidget(row, 6)

                    if price_widget is not None:
                        price_widget.setStyleSheet(
                            "background-color: #87CEEB;"
                        )

                elif product["discount"] > 15:
                    for column in range(10):
                        item = self.products_table.item(row, column)

                        if item is not None:
                            item.setBackground(QColor("#2E8B57"))

                    price_widget = self.products_table.cellWidget(row, 6)

                    if price_widget is not None:
                        price_widget.setStyleSheet(
                            "background-color: #2E8B57;"
                        )
                
        except Exception as e:
            print("Error: ", e)
            
    def open_edit_product(self):
        row = self.products_table.currentRow()
        
        if row < 0 :
            print("Ошибка: товар не найден")
            return
        
        item = self.products_table.item(row,0)
        
        if item is None:
            print("Ошибка не удалосьб определить товар")
            return
        
        product_id = item.data(Qt.UserRole)
        
        try:
            product = get_product(product_id)
            if product is None:
                print("Товар не найден")
                return
            
            self.editing_product_id = product_id
            self.selected_image_path = None
            self.editing_product_image_path = product["image_path"]
            
            self.add_product_window.setWindowTitle("Редактирование товара")
            self.product_image_label.setText("Изображение не выбрано")
            self.product_image_label.clear()
            
            self.load_product_form_data()
            
            self.product_name_input.setText(product["name"])
            self.product_description_input.setPlainText(str(product["description"]))
            
            self.product_price_input.setText(str(product["price"]))
            self.product_unit_input.setText(product["unit"])
            self.product_stock_input.setText(str(product["stock_quantity"]))
            
            self.product_discount_input.setText(str(product["discount"]))
            self.product_category_combo.setCurrentIndex(
                self.product_category_combo.findData(
                    product["category_id"]
                )
            )
            self.product_manufacturer_combo.setCurrentIndex(
                self.product_manufacturer_combo.findData(
                    product["manufacturer_id"]
                )
            )
            self.product_supplier_combo.setCurrentIndex(
                self.product_supplier_combo.findData(
                    product["supplier_id"]
                )
            )
            
            if product["image_path"]:
                image_path = Path(__file__).parent / product["image_path"]

                if image_path.exists():
                    pixmap = QPixmap(str(image_path))
                    pixmap = pixmap.scaled(
                        300,
                        200,
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )

                    self.product_image_label.setPixmap(pixmap)
                    self.product_image_label.setText("")

            self.add_product_window.show()
            
        except Exception as e:
            print("Ошибка при открытии товара",e)

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()