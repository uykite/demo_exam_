from database import get_connection
import bcrypt

def get_user(username):
    connection = get_connection()
    
    try: 
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT users.id,
                users.username,
                users.password,
                users.full_name,
                roles.name AS role_name
                FROM users
                JOIN roles ON users.role_id = roles.id
                WHERE users.username = %s
                """,
                (username,)
            
            )
        
            return cursor.fetchone()
    finally:
        connection.close()

def check_password(password, password_hash):
    return bcrypt.checkpw(
        password.encode(),
        password_hash.encode()
    )