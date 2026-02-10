"""
Day 12: Database Testing
Testing database operations and data validation.
"""

import pytest


class TestDatabaseOperations:
    """Test suite for database CRUD operations."""
    
    def test_get_user_by_id(self, db_manager):
        """
        Test retrieving a user from the database by ID.
        Verifies that the database returns the correct user data.
        """
        print("\n   ---> Testing: Get User by ID")
        
        # Action: Query user with ID 1
        user = db_manager.get_user_by_id(1)
        
        # Assertions
        assert user is not None, "User should exist in database"
        assert user[0] == 1, "User ID should be 1"
        assert user[1] == "george.bluth@reqres.in", "Email should match"
        assert user[2] == "George", "First name should match"
        assert user[3] == "Bluth", "Last name should match"
    
    def test_get_multiple_users(self, db_manager):
        """
        Test retrieving multiple users from the database.
        Verifies all seeded users are present.
        """
        print("\n   ---> Testing: Get Multiple Users")
        
        # Test all three seeded users
        expected_users = [
            (1, "george.bluth@reqres.in", "George", "Bluth"),
            (2, "janet.weaver@reqres.in", "Janet", "Weaver"),
            (3, "emma.wong@reqres.in", "Emma", "Wong")
        ]
        
        for expected in expected_users:
            user = db_manager.get_user_by_id(expected[0])
            assert user is not None, f"User {expected[0]} should exist"
            assert user == expected, f"User {expected[0]} data should match"
    
    def test_user_not_found(self, db_manager):
        """
        Test querying for a non-existent user.
        Verifies the database returns None for invalid IDs.
        """
        print("\n   ---> Testing: User Not Found")
        
        # Action: Query for non-existent user
        user = db_manager.get_user_by_id(999)
        
        # Assertion
        assert user is None, "Non-existent user should return None"


class TestDatabaseIntegration:
    """Test suite for database integration scenarios."""
    
    def test_database_connection(self, db_manager):
        """
        Test that the database connection is established.
        Verifies the database manager is properly initialized.
        """
        print("\n   ---> Testing: Database Connection")
        
        assert db_manager.conn is not None, "Database connection should exist"
        assert db_manager.cursor is not None, "Database cursor should exist"
    
    @pytest.mark.parametrize("user_id,expected_email", [
        (1, "george.bluth@reqres.in"),
        (2, "janet.weaver@reqres.in"),
        (3, "emma.wong@reqres.in")
    ])
    def test_user_emails(self, db_manager, user_id, expected_email):
        """
        Parametrized test to verify user emails.
        Tests multiple users in a single test function.
        """
        print(f"\n   ---> Testing: User {user_id} Email")
        
        user = db_manager.get_user_by_id(user_id)
        assert user[1] == expected_email, f"Email for user {user_id} should match"


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v", "-s"])
