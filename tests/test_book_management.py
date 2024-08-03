import unittest
from unittest.mock import patch, MagicMock
from src.functions.book_management import add_book, remove_book, update_book, search_book, view_books
from src.functions.db import get_db_connection
import sqlite3

class TestBookManagement(unittest.TestCase):

    @patch('src.functions.book_management.get_db_connection')
    @patch('builtins.input', side_effect=['Test Book', 'Test Author'])
    def test_add_book(self, mock_input, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        add_book()

        mock_cursor.execute.assert_called_with(
            "INSERT INTO books (title, author) VALUES (?, ?)",
            ('Test Book', 'Test Author')
        )
        mock_conn.commit.assert_called()

    @patch('src.functions.book_management.get_db_connection')
    @patch('builtins.input', side_effect=['Old Title', 'New Title', 'New Author', '1'])
    def test_update_book(self, mock_input, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('Old Title',)]

        update_book()

        mock_cursor.execute.assert_any_call(
            "UPDATE books SET title = ?, author = ? WHERE title = ?",
            ('New Title', 'New Author', 'Old Title')
        )
        mock_conn.commit.assert_called()

    @patch('src.functions.book_management.get_db_connection')
    @patch('builtins.input', side_effect=['Test Book', ''])
    def test_search_book(self, mock_input, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('Test Book', 'Test Author')]

        with patch('builtins.print') as mock_print:
            search_book()
            mock_print.assert_any_call('Search results:')

    @patch('src.functions.book_management.get_db_connection')
    @patch('builtins.input', side_effect=['Test Book', '1', 'yes'])
    def test_remove_book(self, mock_input, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('Test Book',)]

        remove_book()

        mock_cursor.execute.assert_called_with(
            "DELETE FROM books WHERE title = ?",
            ('Test Book',)
        )
        mock_conn.commit.assert_called()

    @patch('src.functions.book_management.get_db_connection')
    def test_view_books(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [(1, 'Test Book', 'Test Author')]

        with patch('builtins.print') as mock_print:
            view_books()
            mock_print.assert_any_call('Books in the library:')

if __name__ == '__main__':
    unittest.main()
