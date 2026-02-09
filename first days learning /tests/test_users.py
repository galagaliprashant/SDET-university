"""
Day 12: User Database Testing
Testing user-related database operations.
"""

import pytest


class TestUserDatabase:
    """Test suite for user database operations."""
    
    def test_verify_user_exists(self, db_manager):
        """
        Test that a specific user exists in the database.
        """
        print("\n   ---> Testing: Verify User Exists")
        
        # Action
        user = db_manager.get_user_by_id(1)
        
        # Assertions
        assert user is not None, "User with ID 1 should exist"
        assert len(user) == 4, "User record should have 4 fields"
    
    def test_user_email_format(self, db_manager):
        """
        Test that user emails follow the expected format.
        """
        print("\n   ---> Testing: User Email Format")
        
        # Get all users
        for user_id in [1, 2, 3]:
            user = db_manager.get_user_by_id(user_id)
            email = user[1]
            
            # Assertions
            assert "@" in email, f"User {user_id} email should contain @"
            assert email.endswith("@reqres.in"), f"User {user_id} email should end with @reqres.in"
    
    @pytest.mark.parametrize("user_id,first_name,last_name", [
        (1, "George", "Bluth"),
        (2, "Janet", "Weaver"),
        (3, "Emma", "Wong")
    ])
    def test_user_names(self, db_manager, user_id, first_name, last_name):
        """
        Parametrized test to verify user names.
        """
        print(f"\n   ---> Testing: User {user_id} Name")
        
        user = db_manager.get_user_by_id(user_id)
        
        assert user[2] == first_name, f"First name should be {first_name}"
        assert user[3] == last_name, f"Last name should be {last_name}"
    
    def test_invalid_user_id(self, db_manager):
        """
        Test querying with invalid user IDs.
        """
        print("\n   ---> Testing: Invalid User IDs")
        
        invalid_ids = [0, -1, 999, 10000]
        
        for invalid_id in invalid_ids:
            user = db_manager.get_user_by_id(invalid_id)
            assert user is None, f"User with ID {invalid_id} should not exist"


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v", "-s"])
