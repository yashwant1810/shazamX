

import os
import sqlite3

DB_PATH = "shazam.db"

def test_database_initialization():
    assert os.path.exists(DB_PATH), "❌ Database file was not created"

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Check if the 'songs' table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='songs';")
    assert cursor.fetchone(), "❌ 'songs' table does not exist"

    # Check if the 'fingerprints' table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='fingerprints';")
    assert cursor.fetchone(), "❌ 'fingerprints' table does not exist"

    print("✅ Database and tables exist")

    conn.close()