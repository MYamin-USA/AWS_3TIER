import os
import pymysql
from pymysql.cursors import DictCursor
from dotenv import load_dotenv

# ==========================================
# 1. ENVIRONMENT & SECRETS CONFIGURATION
# ==========================================
load_dotenv()

# Secondary local fallback path check for cross-platform compatibility
local_env_paths = [
    os.path.join(os.path.dirname(__file__), ".env"),
    r"C:\Users\yamin\pythonprojects\secrets\portal\.env",
]
for env_path in local_env_paths:
    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path, override=False)

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT", 3306))

# ==========================================
# 2. DATABASE CONNECTION FACTORY
# ==========================================
def get_connection():
    """
    Establishes and returns a secure MySQL connection to Amazon RDS.
    Uses DictCursor so query outputs map directly to pandas DataFrames.
    """
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT,
            cursorclass=DictCursor,
            connect_timeout=5,
            autocommit=True
        )
        return connection
    except Exception as e:
        print(f"❌ Amazon RDS Connection Exception: {e}")
        return None

# ==========================================
# 3. AUTOMATIC SCHEMA INITIALIZATION
# ==========================================
def init_db():
    """
    Verifies that the essential RDS tables exist.
    Creates 'products' and 'contact_messages' if missing.
    """
    conn = get_connection()
    if not conn:
        print("⚠️ Could not connect to Amazon RDS to verify/initialize schema.")
        return False

    try:
        with conn.cursor() as cursor:
            # Table 1: E-Commerce Inventory
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    sku VARCHAR(100) UNIQUE NOT NULL,
                    name VARCHAR(255) NOT NULL,
                    category VARCHAR(100) NOT NULL,
                    price DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
                    stock INT NOT NULL DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            # Table 2: Contact Form Submissions
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS contact_messages (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    subject VARCHAR(255),
                    message TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            # Check if products table is empty; if so, populate initial seed data
            cursor.execute("SELECT COUNT(*) as count FROM products;")
            result = cursor.fetchone()
            if result and result['count'] == 0:
                print("🌱 Empty products table detected. Seeding initial RDS inventory...")
                seed_query = """
                    INSERT INTO products (sku, name, category, price, stock)
                    VALUES 
                        (%s, %s, %s, %s, %s),
                        (%s, %s, %s, %s, %s),
                        (%s, %s, %s, %s, %s);
                """
                seed_data = (
                    "TEL-CSCO-8841", "Cisco IP Phone 8841", "Telecom", 185.00, 45,
                    "NET-UBNT-UDM", "Ubiquiti Dream Machine Pro", "Hardware", 379.99, 12,
                    "SRV-AWS-EC2T3", "Reserved EC2 t3.micro Voucher", "Electronics", 75.50, 100
                )
                cursor.execute(seed_query, seed_data)

        print("✅ Amazon RDS Schema initialized successfully.")
        return True
    except Exception as e:
        print(f"❌ RDS Table Initialization Error: {e}")
        return False
    finally:
        conn.close()

# ==========================================
# 4. E-COMMERCE PRODUCTS CRUD OPERATIONS
# ==========================================
def get_all_products():
    """
    Fetches all inventory assets from Amazon RDS ordered by latest additions.
    Returns a list of dicts suitable for Streamlit DataFrames.
    """
    conn = get_connection()
    if not conn:
        return []

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, sku, name, category, price, stock, created_at FROM products ORDER BY id DESC;")
            records = cursor.fetchall()
            return records
    except Exception as e:
        print(f"❌ RDS Fetch Inventory Error: {e}")
        return []
    finally:
        conn.close()

def add_product(sku: str, name: str, category: str, price: float, stock: int):
    """
    Inserts a new product into RDS or updates the existing entry on SKU collision.
    """
    conn = get_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            query = """
                INSERT INTO products (sku, name, category, price, stock)
                VALUES (%s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    name = VALUES(name),
                    category = VALUES(category),
                    price = VALUES(price),
                    stock = VALUES(stock);
            """
            cursor.execute(query, (sku, name, category, price, stock))
            return True
    except Exception as e:
        print(f"❌ RDS Add Product Error: {e}")
        return False
    finally:
        conn.close()

# ==========================================
# 5. CONTACT FORM MESSAGES CRUD OPERATIONS
# ==========================================
def save_contact_message(name: str, email: str, subject: str, message: str):
    """
    Persists incoming client contact form inquiries directly to Amazon RDS.
    """
    conn = get_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            query = """
                INSERT INTO contact_messages (name, email, subject, message)
                VALUES (%s, %s, %s, %s);
            """
            cursor.execute(query, (name, email, subject, message))
            return True
    except Exception as e:
        print(f"❌ RDS Save Contact Message Error: {e}")
        return False
    finally:
        conn.close()

# Run initialization upon script import
init_db()
