import sqlite3
from datetime import datetime
from typing import List, Optional, Dict
import json

class Database:
    # Main database handler for MyFeed
    def __init__(self, db_path: str = "myfeed.db"):
        self.db_path = db_path
        self.conn = None
        self.init_database()

    def init_database(self):
        # Initialize database connection and create tables
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.create_tables()

    def create_tables(self):
        # Create all necessary tables
        cursor = self.conn.cursor()

        # Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                display_name TEXT,
                bio TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

    def close(self):
        # Close database connection
        if self.conn:
            self.conn.close()

class User:
    # User model
    def __init__(self, db: Database):
        self.db = db