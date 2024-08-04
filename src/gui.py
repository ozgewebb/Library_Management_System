from PyQt5.QtWidgets import QMessageBox, QPushButton, QApplication, QMainWindow

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

    def show_add_book_info(self):
        self.show_info("Add Book", "Add Book button clicked.")

    def show_update_book_info(self):
        self.show_info("Update Book", "Update Book button clicked.")

    def show_view_books_info(self):
        self.show_info("View Books", "View Books button clicked.")

    def show_search_book_info(self):
        self.show_info("Search Book", "Search Book button clicked.")

    def show_remove_book_info(self):
        self.show_info("Remove Book", "Remove Book button clicked.")

    def show_fetch_books_info(self):
        self.show_info("Fetch Books from Google Books", "Fetch Books button clicked.")

    def show_save_fetched_books_info(self):
        self.show_info("Save Fetched Books to Database", "Save Fetched Books button clicked.")

    def show_add_user_info(self):
        self.show_info("Add User", "Add User button clicked.")

    def show_update_user_info(self):
        self.show_info("Update User", "Update User button clicked.")

    def show_view_users_info(self):
        self.show_info("View Users", "View Users button clicked.")

    def show_search_user_info(self):
        self.show_info("Search User", "Search User button clicked.")

    def show_remove_user_info(self):
        self.show_info("Remove User", "Remove User button clicked.")

    def show_info(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec_()

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
