import sqlite3

class DBManager:
    def __init__(self, db_name="test_database.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.setup_tables()

    def setup_tables(self):
        """Creates a dummy users table and seeds it with data."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                email TEXT NOT NULL,
                first_name TEXT,
                last_name TEXT
            )
        ''')
        # Seed it with the data we expect from ReqRes (mocking the backend)
        users = [
            (1, "george.bluth@reqres.in", "George", "Bluth"),
            (2, "janet.weaver@reqres.in", "Janet", "Weaver"),
            (3, "emma.wong@reqres.in", "Emma", "Wong")
        ]
        self.cursor.executemany('INSERT OR IGNORE INTO users VALUES (?,?,?,?)', users)
        self.conn.commit()

    def get_user_by_id(self, user_id):
        """Simulates querying the backend to verify data."""
        self.cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()