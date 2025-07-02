import mysql.connector
from mysql.connector import Error

# Konfigurasi database
# Sesuaikan dengan konfigurasi MySQL di komputer Anda
DB_CONFIG = {
    'host': 'localhost',
    'database': 'db_pendaftaran_maba',
    'user': 'root',  # Ganti jika username berbeda
    'password': ''   # Isi jika MySQL Anda menggunakan password
}

def get_db_connection():
    """
    Membuat koneksi database MySQL
    """
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None

def close_connection(conn, cursor=None):
    """
    Menutup koneksi database
    """
    if cursor:
        cursor.close()
    if conn and conn.is_connected():
        conn.close()
