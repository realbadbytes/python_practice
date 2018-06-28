# Database connection context manager

import mysql.connector

class UseDatabase:

    # Called before __enter__()
    def __init__(self, config: dict) -> None:
        self.configuration = config

    # Called when using 'with'
    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    # Called when 'with' block ends
    # If these ops fail, exception data will be thrown by interpreter
    # Handle exc_type, exc_value, and exc_trace
    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
