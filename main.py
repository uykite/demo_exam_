import sys
import shutil

from pathlib import Path

from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import Qt
from PySide6.QtCore import QFile, QDate
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
    QTextEdit,
    QMessageBox,
    QDateEdit
)


from products import get_products, get_categories, get_manufactures, get_suppliers, add_product, get_product, update_product, delete_product
from orders import (
    get_orders,
    get_order_products,
    get_order_statuses,
    get_pickup_points,
    add_order,
    get_order,
    update_order,
    delete_order
)
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
        order_path = project_path / "ui" / "orders.ui"
        order_form_path = project_path/ "ui" / "order_form.ui"
        
        self.selected_image_path = None
        self.editing_product_image_path = None
        self.editing_order_id = None
        self.editing_product_id = None
        self.login_window = load_ui(login_path)
        self.products_window = load_ui(products_path)
        self.add_product_window = load_ui(add_product_path)
        self.orders_window = load_ui(order_path)
        self.order_form_window = load_ui(order_form_path)
        
        
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
        
        self.orders_button = self.products_window.findChild(
            QPushButton,
            "orders_button"
        )
        
        self.orders_table = self.orders_window.findChild(
            QTableWidget,
            "orders_table"
        )

        self.add_order_button = self.orders_window.findChild(
            QPushButton,
            "add_order_button"
        )

        self.edit_order_button = self.orders_window.findChild(
            QPushButton,
            "edit_order_button"
        )

        self.delete_order_button = self.orders_window.findChild(
            QPushButton,
            "delete_order_button"
        )
        
        self.back_orders_button = self.orders_window.findChild(
            QPushButton,
            "back_button"
        )
        
        self.order_product_combo = self.order_form_window.findChild(
            QComboBox,
            "product_combo"
        )

        self.order_status_combo = self.order_form_window.findChild(
            QComboBox,
            "status_combo"
        )

        self.order_pickup_point_combo = self.order_form_window.findChild(
            QComboBox,
            "pickup_point_combo"
        )

        self.order_date_input = self.order_form_window.findChild(
            QDateEdit,
            "order_date_input"
        )

        self.order_pickup_date_input = self.order_form_window.findChild(
            QDateEdit,
            "pickup_date_input"
        )

        self.save_order_button = self.order_form_window.findChild(
            QPushButton,
            "save_order_button"
        )

        self.cancel_order_button = self.order_form_window.findChild(
            QPushButton,
            "cancel_order_button"
        )
        


        self.stack.addWidget(self.login_window)
        self.stack.addWidget(self.products_window)
        self.stack.addWidget(self.orders_window)
        self.stack.addWidget(self.order_form_window)

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
        self.delete_product_button.clicked.connect(self.delete_selected_product)
        self.orders_button.clicked.connect(self.open_orders)
        self.back_orders_button.clicked.connect(self.open_products)
        
        self.cancel_order_button.clicked.connect(self.open_orders)
        self.add_order_button.clicked.connect(self.open_add_order)
        self.save_order_button.clicked.connect(self.save_order)
        self.edit_order_button.clicked.connect(self.open_edit_order)
        self.delete_order_button.clicked.connect(self.delete_selected_order)
      
      
    def delete_selected_order(self):
        selected_row = self.orders_table.currentRow()

        if selected_row < 0:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Выберите заказ для удаления."
            )
            return

        item = self.orders_table.item(selected_row, 0)
        order_id = item.data(Qt.UserRole)

        reply = QMessageBox.question(
            self,
            "Удаление заказа",
            "Вы действительно хотите удалить выбранный заказ?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply != QMessageBox.Yes:
            return

        try:
            delete_order(order_id)

            QMessageBox.information(
                self,
                "Успешно",
                "Заказ успешно удалён."
            )

            self.load_orders()

        except Exception as e:
            QMessageBox.critical(
                self,
                "Ошибка",
                f"Не удалось удалить заказ:\n{e}"
            )
      
    def open_edit_order(self):
        selected_row = self.orders_table.currentRow()

        if selected_row < 0:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Выберите заказ для редактирования."
            )
            return

        item = self.orders_table.item(selected_row, 0)
        order_id = item.data(Qt.UserRole)

        order = get_order(order_id)

        if order is None:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Заказ не найден."
            )
            return

        self.editing_order_id = order_id

        self.load_order_form_data()

        self.order_product_combo.setCurrentIndex(
            self.order_product_combo.findData(order["product_id"])
        )

        self.order_status_combo.setCurrentIndex(
            self.order_status_combo.findData(order["status_id"])
        )

        self.order_pickup_point_combo.setCurrentIndex(
            self.order_pickup_point_combo.findData(order["pickup_point_id"])
        )

        order_date = order["order_date"]
        pickup_date = order["pickup_date"]

        self.order_date_input.setDate(
            QDate(
                order_date.year,
                order_date.month,
                order_date.day
            )
        )

        self.order_pickup_date_input.setDate(
            QDate(
                pickup_date.year,
                pickup_date.month,
                pickup_date.day
            )
        )

        self.order_form_window.findChild(
            QLabel,
            "title_label"
        ).setText("Редактирование заказа")

        self.stack.setCurrentWidget(self.order_form_window)
      
    def save_order(self):
        try:
            product_id = self.order_product_combo.currentData()
            status_id = self.order_status_combo.currentData()
            pickup_point_id = self.order_pickup_point_combo.currentData()

            order_date = self.order_date_input.date().toString("yyyy-MM-dd")
            pickup_date = self.order_pickup_date_input.date().toString("yyyy-MM-dd")

            if product_id is None:
                QMessageBox.warning(self, "Ошибка", "Выберите товар.")
                return

            if status_id is None:
                QMessageBox.warning(self, "Ошибка", "Выберите статус.")
                return

            if pickup_point_id is None:
                QMessageBox.warning(self, "Ошибка", "Выберите пункт выдачи.")
                return

            if self.editing_order_id is None:
                add_order(
                    product_id,
                    status_id,
                    pickup_point_id,
                    order_date,
                    pickup_date
                )

                message = "Заказ успешно добавлен."

            else:
                update_order(
                    self.editing_order_id,
                    product_id,
                    status_id,
                    pickup_point_id,
                    order_date,
                    pickup_date
                )

                message = "Заказ успешно изменён."

            QMessageBox.information(
                self,
                "Успешно",
                message
            )

            self.editing_order_id = None
            self.open_orders()

        except Exception as e:
            QMessageBox.critical(
                self,
                "Ошибка",
                f"Не удалось сохранить заказ:\n{e}"
            )
    
      
    def load_order_form_data(self):
        try:
            products = get_order_products()
            statuses = get_order_statuses()
            pickup_points = get_pickup_points()
                
            self.order_product_combo.clear()
            self.order_status_combo.clear()
            self.order_pickup_point_combo.clear()    
            
            for product in products:
                self.order_product_combo.addItem(
                    product["name"],
                    product["id"]
                )
            for status in statuses:
                self.order_status_combo.addItem(
                    status["name"],
                    status["id"]
                )

            for point in pickup_points:
                self.order_pickup_point_combo.addItem(
                    point["address"],
                    point["id"]
                )
        except Exception as e:
            print("Ошибка при загрузке формы заказов:",e)
                
      
    def open_add_order(self):
        self.editing_order_id = None

        self.load_order_form_data()

        self.order_form_window.findChild(
            QLabel,
            "title_label"
        ).setText("Добавление заказа")

        self.stack.setCurrentWidget(self.order_form_window)
      
    def open_products(self):
        self.stack.setCurrentWidget(self.products_window)

    def open_orders(self):
        self.load_orders()
        self.stack.setCurrentWidget(self.orders_window)
      
      
    def load_orders(self):
        try:
            orders = get_orders()
            
            self.orders_table.setRowCount(0)
            
            for order in orders:
                row = self.orders_table.rowCount()
                self.orders_table.insertRow(row)
                
                item = QTableWidgetItem(order["product_name"])
                item.setData(Qt.UserRole, order["id"])
                self.orders_table.setItem(row,0,item)
                
                self.orders_table.setItem(
                    row,
                    1,
                    QTableWidgetItem(order["status_name"])
                )     

                self.orders_table.setItem(
                    row,
                    2,
                    QTableWidgetItem(order["pickup_address"])
                )

                self.orders_table.setItem(
                    row,
                    3,
                    QTableWidgetItem(str(order["order_date"]))
                )

                self.orders_table.setItem(
                    row,
                    4,
                    QTableWidgetItem(str(order["pickup_date"]))
                )
        except Exception as e:
            print("Ошибки при загрузке заказов: ",e)
                
                
    def delete_selected_product(self):
        row = self.products_table.currentRow()
        
        if row < 0:
            QMessageBox.warning(
                self,
                "Удаление товара",
                "Сначала выберите товар"
            )
            return
        item = self.products_table.item(row,0)
        
        if item is None:
            QMessageBox.warning(
                self,
                "Удаление товара",
                "Не удалось определить выбранный товар"
            )
            return
        
        product_id = item.data(Qt.UserRole)
        product_name = self.products_table.item(row,1).text()
        
        answer = QMessageBox.question(
            self,
            "Удаление товара",
            f"Вы действительно хотите удалить товар: {product_name} ?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if answer != QMessageBox.Yes:
            return
        
        try:
            delete_product(product_id)
            
            QMessageBox.information(
                self,
                "Удаление товара",
                "Товар успешно удален"
            )
            self.load_products(
            )
        except Exception as e:
            print("Ошибка удаление товара: ", e)
            
            QMessageBox.warning(
                self,
                "Ошибка удаления",
                "Нельзя удалить этот товар.\n"
                "Возможно, он уже используется в заказе."
            )
    
    
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

            QMessageBox.warning(
                self,
                "Ошибка",
                "Введите название товара."
            )

            return

        if category_id is None:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Выберите категорию."
            )

            return

        if manufacturer_id is None:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Выберите производителя."
            )

            return

        if supplier_id is None:

            QMessageBox.warning(
                self,
                "Ошибка",
                "Выберите поставщика."
            )

            return

        if not unit:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Введите единицу измерения."
            )

            return

        # Проверяем цену
        try:
            price = float(price_text)
        except ValueError:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Цена должна быть числом."
            )

            return

        if price < 0:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Цена не может быть отрицательной."
            )
            return

        # Проверяем количество
        try:
            stock_quantity = int(stock_text)
        except ValueError:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Количество должно быть целым числом."
            )

            return

        if stock_quantity < 0:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Количество не может быть отрицательным."
            )
            return

        # Проверяем скидку
        try:
            discount = float(discount_text)
        except ValueError:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Скидка должна быть числом."
            )

            return

        if discount < 0 or discount > 100:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Скидка должна быть от 0 до 100%."
            )
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
        self.editing_product_image_path = None

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
        self.orders_button.setVisible(is_admin or is_manager)
        self.add_order_button.setVisible(is_admin)
        self.edit_order_button.setVisible(is_admin)
        self.delete_order_button.setVisible(is_admin)
        
        
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