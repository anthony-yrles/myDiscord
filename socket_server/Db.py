import mysql.connector

class Db:
    """
    A class representing a database connection.
    """

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        """
        Establishes a connection to the database.
        """
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        """
        Closes the database connection.
        """
        self.connection.close()

    def executeQuery(self, query, params=None):
        """
        Executes a SQL query.

        """
        self.connect()
        self.cursor.execute(query, params or ())
        self.connection.commit()
        self.disconnect()

    def fetch(self, query, params=None):
        """
        Executes a SQL query and returns the result.

        """
        self.connect()
        self.cursor.execute(query, params or ())
        result = self.cursor.fetchall()
        self.disconnect()
        return result