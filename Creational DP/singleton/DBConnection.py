import threading

class DatabaseConnection:

    def __init__(self, db_url):
        self.db_url = db_url
        print(f"Connecting to the database at {db_url}")
    
    def query(self, sql):
        """Simulates executing a SQL query."""
        print(f"Executing query: {sql}")
        return f"Results for {sql}"

class DatabaseConnectionManager:
    _instance = None
    _lock = threading.Lock()
    _db_connection = None

    def __init__(self, db_url):
        if DatabaseConnectionManager._instance is not None:
            raise Exception("This class is a singleton!")
        self.db_url = db_url
        DatabaseConnectionManager._instance = self

    @classmethod
    def get_instance(cls, db_url=None):
        with cls._lock:
            if cls._instance is None:
                if db_url is None:
                    raise Exception("Database URL must be provided for the first time.")
                cls._instance = DatabaseConnectionManager(db_url)
                cls._instance._db_connection = DatabaseConnection(db_url)
            else: 
               if db_url is not None and db_url!=cls._instance.db_url:
                       raise Exception(f"Cannot reinitialize the singleton with a diff DB URL : {db_url}")
            return cls._instance

    def get_connection(self):
        return self._db_connection


# def main():
#     db_manager = DatabaseConnectionManager.get_instance("postgres://localhost:5432/mydb")

#     connection = db_manager.get_connection()
#     print(connection.query("SELECT * FROM users"))

#     another_db_manager = DatabaseConnectionManager.get_instance()
#     print("Is same instance:", db_manager is another_db_manager)

#     try:
#         db_manager2 = DatabaseConnectionManager.get_instance("postgres://localhost:5432/anotherdb")
#     except Exception as e:
#         print(e)


# if __name__ == "__main__":
#     main()
