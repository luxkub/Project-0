from core.session import Sessions, UserSession
from database.db import Database
import app

def test_perform_search() -> tuple:
    """
    Tests that the Sessions class is initialized correctly.

     args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """
    db = Database("database/storeRecords.db")
    query = "apple"
    search_results = app.perform_search(query, db)
    expected_results = db.execute("SELECT * FROM inventory WHERE item_name LIKE :query", {"query": f"%{query}%"}).fetchall()

    if search_results != expected_results:
        error = f"Error in test_perform_search: Search results are not as expected.\n  - Query: {query}\n  - Expected: {expected_results}\n  - Actual: {search_results}"
        return False, error
    else:
        return True, "Search results are as expected."

def test_search() -> tuple:
    """
    Tests that the Sessions class is initialized correctly.

     args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """
    query = "apple"
    search_results = app.search(query)
    expected_results = app.perform_search(query, app.db)

    if search_results != expected_results:
        error = f"Error in test_search: Search results are not as expected.\n  - Query: {query}\n  - Expected: {expected_results}\n  - Actual: {search_results}"
        return False, error
    else:
        return True, "Search results are as expected."


def test_init_sessions() -> tuple:
    """
    Tests that the Sessions class is initialized correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    sessions = Sessions()

    if len(sessions.sessions) != 0:
        error = f"Error in test_init_sessions: Sessions dictionary is not empty.\n  - Actual: {len(sessions.sessions)}"
        return False, error
    else:
        return True, "Sessions dictionary is empty."


def test_add_new_session() -> tuple:
    """
    Tests that a new session is added correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/storeRecords.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)

    if len(sessions.sessions) == 0:
        error = f"Error in test_add_new_session: Sessions dictionary is empty.\n  - Actual: {len(sessions.sessions)}"
        return False, error
    else:
        return True, "Sessions dictionary is not empty."


def test_get_session() -> tuple:
    """
    Tests that a session is retrieved correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/storeRecords.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)
    session = sessions.get_session("test")

    if not isinstance(session, UserSession):
        error = f"Error in test_get_session: Session is not a UserSession object.\n  - Actual: {type(session)}"
        return False, error
    else:
        return True, "Session is a UserSession object."


def test_get_session_username() -> tuple:
    """
    Tests that a session's username is retrieved correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/storeRecords.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)
    session = sessions.get_session("test")

    if session.username != "test":
        error = f"Error in test_get_session_username: Session's username is incorrect.\n  - Expected: test\n  - Actual: {session.username}"
        return False, error
    else:
        return True, "Session's username is correct."


def test_get_session_db() -> tuple:
    """
    Tests that a session's database is retrieved correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/storeRecords.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)
    session = sessions.get_session("test")

    if session.db != db:
        error = f"Error in test_get_session_db: Session's database is incorrect.\n  - Expected: {db}\n  - Actual: {session.db}"
        return False, error
    else:
        return True, "Session's database is correct."
        
def test_checkout() -> tuple:

	"""
	Tests that a session has a checkout button on the last page
	args:
		-None
	
	returns:
		-error_report: A tuple containing a boolean and a description of the reason for the boolean
	"""
        # Create a new session and add items to the cart
# Check out an item with sufficient inventory
    result = self.inventory.checkout("item_1", 3)
    self.assertEqual(result, (True, "Checkout successful"))

    # Check out an item with insufficient inventory
    result = self.inventory.checkout("item_1", 8)
    self.assertEqual(result, (False, "Insufficient inventory"))
    
    # Check out an item that does not exist in the inventory
    result = self.inventory.checkout("item_4", 2)
    self.assertEqual(result, (False, "Item not found"))