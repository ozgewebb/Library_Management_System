import unittest
from unittest.mock import patch, MagicMock
from src.functions.book_management import add_book, remove_book, update_book, search_book, view_books
from src.functions.db import get_db_connection, create_database

class TestBookManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        create_database()  # Ensure the database and tables are created

    def setUp(self):
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

        # Clean up database before each test
        self.cursor.execute("DELETE FROM books")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    @patch('builtins.input', side_effect=['Test Book', 'Test Author'])
    def test_add_book(self, mock_input):
        with patch('src.functions.book_management.get_db_connection') as mock_conn:
            mock_conn.return_value.cursor.return_value = self.cursor
            add_book()
            self.cursor.execute("SELECT title, authors FROM books WHERE title=?", ('Test Book',))
            book = self.cursor.fetchone()
            self.assertIsNotNone(book)
            self.assertEqual(book[0], 'Test Book')
            self.assertEqual(book[1], 'Test Author')

    @patch('builtins.input', side_effect=['Old Title', 'New Title', 'New Author', 'New Description', '2025-01-01', '1234567890'])
    def test_update_book(self, mock_input):
        with patch('src.functions.book_management.get_db_connection') as mock_conn:
            mock_conn.return_value.cursor.return_value = self.cursor
            self.cursor.execute("INSERT INTO books (title, authors, description, published_date, isbn) VALUES (?, ?, ?, ?, ?)",
                                ('Old Title', 'Old Author', 'Old Description', '2023-01-01', '0987654321'))
            self.conn.commit()

            update_book()

            self.cursor.execute("SELECT title, authors, description, published_date, isbn FROM books WHERE title=?", ('New Title',))
            book = self.cursor.fetchone()
            self.assertIsNotNone(book)
            self.assertEqual(book[0], 'New Title')
            self.assertEqual(book[1], 'New Author')
            self.assertEqual(book[2], 'New Description')
            self.assertEqual(book[3], '2025-01-01')
            self.assertEqual(book[4], '1234567890')

    @patch('builtins.input', side_effect=['Test Book', 'Test Author'])
    def test_view_books(self, mock_input):
        with patch('src.functions.book_management.get_db_connection') as mock_conn:
            mock_conn.return_value.cursor.return_value = self.cursor
            add_book()
            with patch('builtins.print') as mock_print:
                view_books()
                mock_print.assert_any_call('Books in the library:')
                mock_print.assert_any_call('(1) Test Book by Test Author')

    @patch('builtins.input', side_effect=['Test Book', 'Test Author'])
    def test_search_book(self, mock_input):
        with patch('src.functions.book_management.get_db_connection') as mock_conn:
            mock_conn.return_value.cursor.return_value = self.cursor
            add_book()
            with patch('builtins.print') as mock_print:
                search_book(title_query='Test Book', author_query='Test Author')
                mock_print.assert_any_call('Search results:')
                mock_print.assert_any_call('Title: Test Book, Author: Test Author')

    @patch('builtins.input', side_effect=['Test Book'])
    def test_remove_book(self, mock_input):
        with patch('src.functions.book_management.get_db_connection') as mock_conn:
            mock_conn.return_value.cursor.return_value = self.cursor
            add_book()
            self.cursor.execute("SELECT title FROM books WHERE title=?", ('Test Book',))
            book = self.cursor.fetchone()
            if book:
                remove_book()
                self.cursor.execute("SELECT * FROM books WHERE title=?", ('Test Book',))
                book = self.cursor.fetchone()
                self.assertIsNone(book)

if __name__ == '__main__':
    unittest.main()
