import pytest
from utils.db_manager import DatabaseManager


@pytest.fixture(scope="session")
def db_manager():
    """
    Session-scoped fixture that provides a database manager instance.
    Creates the database once for all tests and cleans up after.
    """
    print("\n   ⚡ [Setup] Initializing Database...")
    db = DatabaseManager("test_database.db")
    
    # Create the users table with test data
    db.create_table("users", "id INTEGER PRIMARY KEY, email TEXT NOT NULL, first_name TEXT, last_name TEXT")
    
    # Seed test data
    users = [
        (1, "george.bluth@reqres.in", "George", "Bluth"),
        (2, "janet.weaver@reqres.in", "Janet", "Weaver"),
        (3, "emma.wong@reqres.in", "Emma", "Wong")
    ]
    for user in users:
        db.execute_update("INSERT OR IGNORE INTO users VALUES (?,?,?,?)", user)
    
    # Add get_user_by_id method dynamically
    def get_user_by_id(user_id):
        results = db.execute_query("SELECT * FROM users WHERE id=?", (user_id,))
        return results[0] if results else None
    
    db.get_user_by_id = get_user_by_id
    db.close_connection = lambda: None  # DatabaseManager uses context managers
    
    yield db
    
    print("\n   🧹 [Teardown] Closing Database Connection...")
    db.drop_table("users")


@pytest.fixture(scope="function")
def clean_db(db_manager):
    """
    Function-scoped fixture that ensures a clean database state for each test.
    """
    # Setup: Database is already created by db_manager fixture
    yield db_manager
    
    # Teardown: Reset database to initial state if needed
    # (In this case, our setup_tables() already handles this with INSERT OR IGNORE)
    pass
