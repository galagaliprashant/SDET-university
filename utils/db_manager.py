"""
Database Manager Module
Handles database connections and operations for test automation.
"""

import sqlite3
from contextlib import contextmanager


class DatabaseManager:
    """
    A reusable database manager for SQLite operations.
    Provides connection management and common database operations.
    """
    
    def __init__(self, db_path):
        """
        Initialize the database manager.
        
        Args:
            db_path (str): Path to the SQLite database file
        """
        self.db_path = db_path
        self.connection = None
    
    @contextmanager
    def get_connection(self):
        """
        Context manager for database connections.
        Ensures connections are properly closed.
        
        Yields:
            sqlite3.Connection: Database connection object
        """
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row  # Enable column access by name
            yield self.connection
        finally:
            if self.connection:
                self.connection.close()
    
    def execute_query(self, query, params=None):
        """
        Execute a SELECT query and return results.
        
        Args:
            query (str): SQL query to execute
            params (tuple, optional): Query parameters
            
        Returns:
            list: Query results as list of Row objects
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
    
    def execute_update(self, query, params=None):
        """
        Execute an INSERT, UPDATE, or DELETE query.
        
        Args:
            query (str): SQL query to execute
            params (tuple, optional): Query parameters
            
        Returns:
            int: Number of affected rows
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()
            return cursor.rowcount
    
    def create_table(self, table_name, columns):
        """
        Create a new table in the database.
        
        Args:
            table_name (str): Name of the table to create
            columns (str): Column definitions (e.g., "id INTEGER PRIMARY KEY, name TEXT")
        """
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.execute_update(query)
    
    def drop_table(self, table_name):
        """
        Drop a table from the database.
        
        Args:
            table_name (str): Name of the table to drop
        """
        query = f"DROP TABLE IF EXISTS {table_name}"
        self.execute_update(query)


if __name__ == "__main__":
    # Example usage
    db = DatabaseManager("test.db")
    
    # Create a test table
    db.create_table("users", "id INTEGER PRIMARY KEY, name TEXT, email TEXT")
    
    # Insert test data
    db.execute_update("INSERT INTO users (name, email) VALUES (?, ?)", 
                     ("John Doe", "john@example.com"))
    
    # Query data
    results = db.execute_query("SELECT * FROM users")
    for row in results:
        print(f"ID: {row['id']}, Name: {row['name']}, Email: {row['email']}")
    
    # Clean up
    db.drop_table("users")
    print("Database operations completed successfully!")
