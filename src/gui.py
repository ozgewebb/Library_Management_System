from PyQt5.QtWidgets import QMessageBox, QPushButton, QApplication, QMainWindow, QInputDialog, QTextEdit
from functions.fetch_books import fetch_books_from_google_books
from functions.db import get_db_connection, create_database
from functions.book_management import add_book, remove_book, view_books, update_book, search_book
from functions.user_management import add_user, update_user, remove_user, view_users, search_user

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Library Management System')
        self.setGeometry(100, 100, 800, 600)

        # Add Book Button
        self.add_book_button = QPushButton('Add Book', self)
        self.add_book_button.setGeometry(50, 50, 200, 50)
        self.add_book_button.clicked.connect(self.show_add_book_info)

        # Update Book Button
        self.update_book_button = QPushButton('Update Book', self)
        self.update_book_button.setGeometry(50, 110, 200, 50)
        self.update_book_button.clicked.connect(self.show_update_book_info)

        # View Books Button
        self.view_books_button = QPushButton('View Books', self)
        self.view_books_button.setGeometry(50, 170, 200, 50)
        self.view_books_button.clicked.connect(self.show_view_books_info)

        # Search Book Button
        self.search_book_button = QPushButton('Search Book', self)
        self.search_book_button.setGeometry(50, 230, 200, 50)
        self.search_book_button.clicked.connect(self.show_search_book_info)

        # Remove Book Button
        self.remove_book_button = QPushButton('Remove Book', self)
        self.remove_book_button.setGeometry(50, 290, 200, 50)
        self.remove_book_button.clicked.connect(self.show_remove_book_info)

        # Fetch Books from Google Books Button
        self.fetch_books_button = QPushButton('Fetch Books Online', self)
        self.fetch_books_button.setGeometry(50, 350, 200, 50)
        self.fetch_books_button.clicked.connect(self.show_fetch_books_info)

        # Save Fetched Books to Database Button
        self.save_fetched_books_button = QPushButton('Save Fetched Books', self)
        self.save_fetched_books_button.setGeometry(50, 410, 200, 50)
        self.save_fetched_books_button.clicked.connect(self.show_save_fetched_books_info)

        # Add User Button
        self.add_user_button = QPushButton('Add User', self)
        self.add_user_button.setGeometry(50, 470, 200, 50)
        self.add_user_button.clicked.connect(self.show_add_user_info)

        # Update User Button
        self.update_user_button = QPushButton('Update User', self)
        self.update_user_button.setGeometry(50, 530, 200, 50)
        self.update_user_button.clicked.connect(self.show_update_user_info)

        # View Users Button
        self.view_users_button = QPushButton('View Users', self)
        self.view_users_button.setGeometry(50, 590, 200, 50)
        self.view_users_button.clicked.connect(self.show_view_users_info)

        # Search User Button
        self.search_user_button = QPushButton('Search User', self)
        self.search_user_button.setGeometry(50, 650, 200, 50)
        self.search_user_button.clicked.connect(self.show_search_user_info)

        # Remove User Button
        self.remove_user_button = QPushButton('Remove User', self)
        self.remove_user_button.setGeometry(50, 710, 200, 50)
        self.remove_user_button.clicked.connect(self.show_remove_user_info)

        # TextEdit widget for displaying information
        self.info_text = QTextEdit(self)
        self.info_text.setGeometry(300, 50, 450, 500)
        self.info_text.setReadOnly(True)

        # Create the database tables if they do not exist
        create_database()

    def show_add_book_info(self):
        title, ok = QInputDialog.getText(self, 'Add Book', 'Enter title:')
        if ok and title:
            authors, ok = QInputDialog.getText(self, 'Add Book', 'Enter authors:')
            if ok and authors:
                description, ok = QInputDialog.getText(self, 'Add Book', 'Enter description:')
                if ok and description:
                    published_date, ok = QInputDialog.getText(self, 'Add Book', 'Enter published date:')
                    if ok and published_date:
                        isbn, ok = QInputDialog.getText(self, 'Add Book', 'Enter ISBN:')
                        if ok and isbn:
                            add_book(title, authors, description, published_date, isbn)
                            self.show_info("Success", "Book added successfully.")

    def show_update_book_info(self):
        update_book()  # Call the update_book function
        self.show_info("Update Book", "Update Book action performed.")

    def show_view_books_info(self):
        books = view_books()  # Call the view_books function
        if books:
            book_info = "\n".join([f"ID: {book['id']}, Title: {book['title']}, Authors: {book['authors']}" for book in books])
        else:
            book_info = "No books found in the library."
    
        self.info_text.setPlainText(book_info)

    def show_search_book_info(self):
        query, ok = QInputDialog.getText(self, 'Search Book', 'Enter search term:')
        if ok and query:
            books = search_book(query)  # Call the search_book function
            if books:
                book_info = "\n".join([f"Title: {book['title']}, Authors: {book['authors']}" for book in books])
                self.info_text.setPlainText(book_info)
            else:
                self.show_info("No Books Found", "No books found matching the search term.")

    def show_remove_book_info(self):
        query, ok = QInputDialog.getText(self, 'Remove Book', 'Enter book title to remove:')
        if ok and query:
            remove_book(query)  # Call the remove_book function
            self.show_info("Remove Book", "Remove Book action performed.")

    def show_fetch_books_info(self):
        query, ok = QInputDialog.getText(self, 'Fetch Books', 'Enter search term:')
        if ok and query:
            books = fetch_books_from_google_books(query)  # Fetch books
            if books:
                book_info = "\n".join([f"Title: {book['title']}, Authors: {', '.join(book['authors'])}" for book in books])
                self.info_text.setPlainText(book_info)
                self.fetched_books = books  # Store fetched books
            else:
                self.show_info("No Books Found", "No books found for the given search term.")

    def show_save_fetched_books_info(self):
        if hasattr(self, 'fetched_books') and self.fetched_books:
            conn = get_db_connection()
            if conn:
                cursor = conn.cursor()
                for book in self.fetched_books:
                    cursor.execute('INSERT INTO books (title, authors) VALUES (?, ?)',
                                   (book['title'], ', '.join(book['authors'])))
                conn.commit()
                conn.close()
                self.show_info("Success", "Books saved to database.")
        else:
            self.show_info("No Books to Save", "No books available to save.")

    def show_add_user_info(self):
        username, ok = QInputDialog.getText(self, 'Add User', 'Enter username:')
        if ok and username:
            password, ok = QInputDialog.getText(self, 'Add User', 'Enter password:')
            if ok and password:
                email, ok = QInputDialog.getText(self, 'Add User', 'Enter email:')
                if ok and email:
                    role, ok = QInputDialog.getText(self, 'Add User', 'Enter role:')
                    if ok and role:
                        add_user(username, password, email, role)
                        self.show_info("Success", "User added successfully.")

    def show_update_user_info(self):
        update_user()  # Call the update_user function
        self.show_info("Update User", "Update User action performed.")

    def show_view_users_info(self):
        users = view_users()  # Call the view_users function
        if users:
            user_info = "\n".join([f"Username: {user['username']}, Role: {user['role']}" for user in users])
        else:
            user_info = "No users found in the database."
    
        self.info_text.setPlainText(user_info)

    def show_search_user_info(self):
        query, ok = QInputDialog.getText(self, 'Search User', 'Enter search term:')
        if ok and query:
            users = search_user(query)  # Call the search_user function
            if users:
                user_info = "\n".join([f"Username: {user['username']}, Role: {user['role']}" for user in users])
                self.info_text.setPlainText(user_info)
            else:
                self.show_info("No Users Found", "No users found matching the search term.")

    def show_remove_user_info(self):
        query, ok = QInputDialog.getText(self, 'Remove User', 'Enter username to remove:')
        if ok and query:
            remove_user(query)  # Call the remove_user function
            self.show_info("Remove User", "Remove User action performed.")

    def show_info(self, title, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
