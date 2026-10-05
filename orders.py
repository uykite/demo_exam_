from database import get_connection
from psycopg2.extras import RealDictCursor


def get_orders():
    connection = get_connection()

    try:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT
                    orders.id,
                    products.id AS product_id,
                    products.name AS product_name,
                    order_statuses.name AS status_name,
                    pickup_points.address AS pickup_address,
                    orders.order_date,
                    orders.pickup_date
                FROM orders
                JOIN products
                    ON orders.product_id = products.id
                JOIN order_statuses
                    ON orders.status_id = order_statuses.id
                JOIN pickup_points
                    ON orders.pickup_point_id = pickup_points.id
                ORDER BY orders.id
                """
            )

            return cursor.fetchall()

    finally:
        connection.close()
        
def get_order_products():
    connection = get_connection()

    try:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT id, name
                FROM products
                ORDER BY name
                """
            )

            return cursor.fetchall()

    finally:
        connection.close()


def get_order_statuses():
    connection = get_connection()

    try:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT id, name
                FROM order_statuses
                ORDER BY name
                """
            )

            return cursor.fetchall()

    finally:
        connection.close()


def get_pickup_points():
    connection = get_connection()

    try:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT id, address
                FROM pickup_points
                ORDER BY address
                """
            )

            return cursor.fetchall()

    finally:
        connection.close()
        
def add_order(product_id, status_id, pickup_point_id, order_date, pickup_date):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO orders (
                    product_id,
                    status_id,
                    pickup_point_id,
                    order_date,
                    pickup_date
                )
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    product_id,
                    status_id,
                    pickup_point_id,
                    order_date,
                    pickup_date
                )
            )

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()
        
def get_order(order_id):
    connection = get_connection()

    try:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT
                    orders.id,
                    orders.product_id,
                    orders.status_id,
                    orders.pickup_point_id,
                    orders.order_date,
                    orders.pickup_date
                FROM orders
                WHERE orders.id = %s
                """,
                (order_id,)
            )

            return cursor.fetchone()

    finally:
        connection.close()
        
def update_order(
    order_id,
    product_id,
    status_id,
    pickup_point_id,
    order_date,
    pickup_date
):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE orders
                SET
                    product_id = %s,
                    status_id = %s,
                    pickup_point_id = %s,
                    order_date = %s,
                    pickup_date = %s
                WHERE id = %s
                """,
                (
                    product_id,
                    status_id,
                    pickup_point_id,
                    order_date,
                    pickup_date,
                    order_id
                )
            )

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()
        
def delete_order(order_id):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM orders
                WHERE id = %s
                """,
                (order_id,)
            )

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()