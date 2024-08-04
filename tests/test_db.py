# tests/test_db.py
import unittest
from unittest.mock import patch, MagicMock
from src.functions.db import create_database, get_db_connection

class TestDatabaseFunctions(unittest.TestCase):

    @patch('src.functions.db.sqlite3')
    def test_create_database(self, mock_sqlite):
        mock_conn = MagicMock()
        mock_sqlite.connect.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor

        create_database()

        mock_sqlite.connect.assert_called_once_with('library.db')
        self.assertTrue(mock_cursor.execute.called)
        self.assertTrue(mock_conn.commit.called)
        self.assertTrue(mock_conn.close.called)

    @patch('src.functions.db.sqlite3')
    def test_get_db_connection(self, mock_sqlite):
        mock_conn = MagicMock()
        mock_sqlite.connect.return_value = mock_conn

        conn = get_db_connection()

        mock_sqlite.connect.assert_called_once_with('library.db')
        self.assertEqual(conn, mock_conn)

if __name__ == '__main__':
    unittest.main()
