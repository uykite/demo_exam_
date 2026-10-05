from database import get_connection
from psycopg2.extras import RealDictCursor

def get_products(search="", category=None, supplier=None ,sort="Без сортировки"):
    connection = get_connection()
    if sort == "Название":
        order = "products.name"
        direction = "ASC"

    elif sort == "Цена":
        order = "products.price"
        direction = "ASC"

    elif sort == "Остаток(по возрастанию)":
        order = "products.stock_quantity"
        direction = "ASC"

    elif sort == "Остаток(по убыванию)":
        order = "products.stock_quantity"
        direction = "DESC"

    elif sort == "Скидка":
        order = "products.discount"
        direction = "ASC"

    else:
        order = "products.id"
        direction = "ASC"
    

    try:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                f"""
                SELECT
                    products.id,
                    products.name,
                    categories.name AS category_name,
                    products.description,
                    manufacturers.name AS manufacturer_name,
                    suppliers.name AS supplier_name,
                    products.price,
                    products.unit,
                    products.stock_quantity,
                    products.discount,
                    products.image_path
                FROM products
                JOIN categories
                    ON products.category_id = categories.id
                JOIN manufacturers
                    ON products.manufacturer_id = manufacturers.id
                JOIN suppliers
                    ON products.supplier_id = suppliers.id
                WHERE
                (
                    products.name ILIKE %s
                    OR categories.name ILIKE %s
                    OR products.description ILIKE %s
                    OR manufacturers.name ILIKE %s
                    OR suppliers.name ILIKE %s
                    OR products.unit ILIKE %s
                )
                AND (%s IS NULL OR categories.id = %s)
                AND (%s IS NULL OR suppliers.id = %s)
                ORDER BY {order} {direction}
                """,
                (
                    f"%{search}%",
                    f"%{search}%",
                    f"%{search}%",
                    f"%{search}%",
                    f"%{search}%",
                    f"%{search}%",
                    category,
                    category,
                    supplier,
                    supplier
                )
            )

            return cursor.fetchall()
    finally:
        connection.close()
        
        
def update_product(
    product_id,
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
):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE products
                SET
                    name = %s,
                    category_id = %s,
                    description = %s,
                    manufacturer_id = %s,
                    supplier_id = %s,
                    price = %s,
                    unit = %s,
                    stock_quantity = %s,
                    discount = %s,
                    image_path = %s
                WHERE id = %s
                """,
                (
                    name,
                    category_id,
                    description,
                    manufacturer_id,
                    supplier_id,
                    price,
                    unit,
                    stock_quantity,
                    discount,
                    image_path,
                    product_id
                )
            )
            connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()
        
        
def get_product(product_id):
    connection = get_connection()
    
    try:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT
                    products.id,
                    products.name,
                    products.category_id,
                    categories.name AS category_name,
                    products.description,
                    products.manufacturer_id,
                    manufacturers.name AS manufacturer_name,
                    products.supplier_id,
                    suppliers.name AS supplier_name,
                    products.price,
                    products.unit,
                    products.stock_quantity,
                    products.discount,
                    products.image_path
                FROM products
                JOIN categories
                    ON products.category_id = categories.id
                JOIN manufacturers
                    ON products.manufacturer_id = manufacturers.id
                JOIN suppliers
                    ON products.supplier_id = suppliers.id
                WHERE products.id = %s
                """,
                (product_id,)
                
            )
            
            return cursor.fetchone()
    finally:
        connection.close()
                   

        

        
def get_categories():
    connection=get_connection()
    
    try:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT id,name
                FROM categories
                ORDER BY name
                """
            )
            return cursor.fetchall()
        
    finally:
        connection.close()
        
def get_manufactures():
    connection = get_connection()
    
    try:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT id,name
                FROM manufacturers
                ORDER BY name
                """                
            )
            return cursor.fetchall()
    finally:
        connection.close()
        

def get_suppliers():
    connection = get_connection()
    try:
        with connection.cursor(cursor_factory = RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT id,name
                FROM suppliers
                ORDER BY name
                """
            )
            return cursor.fetchall()
    finally:
        connection.close()            
        
def add_product(
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
):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO products (
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
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
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
            )

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()