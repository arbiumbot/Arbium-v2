import sqlite3

DB_NAME = "arbium.db"

# Ініціалізація бази
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            language TEXT,
            is_admin INTEGER DEFAULT 0
        )
        """)
        conn.commit()

# Додавання користувача
def add_user(user_id, username, language, is_admin=0):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("INSERT OR IGNORE INTO users (id, username, language, is_admin) VALUES (?, ?, ?, ?)",
                  (user_id, username, language, is_admin))
        conn.commit()

# Отримання всіх користувачів
def get_users():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT id FROM users")
        return [row[0] for row in c.fetchall()]