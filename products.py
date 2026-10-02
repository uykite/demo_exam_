from database import get_connection
from psycopg2.extras import RealDictCursor

def get_products(search=""):
    connection = get_connection()

    try:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
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
                    products.name ILIKE %s
                    OR categories.name ILIKE %s
                    OR products.description ILIKE %s
                    OR manufacturers.name ILIKE %s
                    OR suppliers.name ILIKE %s
                    OR products.unit ILIKE %s
                ORDER BY products.id
                """,
                (
                    f"%{search}%",
                    f"%{search}%",
                    f"%{search}%",
                    f"%{search}%",
                    f"%{search}%",
                    f"%{search}%"
                )
            )

            return cursor.fetchall()
    finally:
        connection.close()