import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Management System GUI")
        self.setGeometry(100, 100, 800, 600)
        
        # Set central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Create and add buttons to the layout
        self.add_button = QPushButton("Add Book")
        self.update_button = QPushButton("Update Book")
        self.view_button = QPushButton("View Books")
        self.search_button = QPushButton("Search Book")
        self.remove_button = QPushButton("Remove Book")
        self.fetch_button = QPushButton("Fetch Books from Google Books")
        self.save_button = QPushButton("Save Fetched Books to Database")
        self.add_user_button = QPushButton("Add User")
        self.update_user_button = QPushButton("Update User")
        self.view_users_button = QPushButton("View Users")
        self.search_user_button = QPushButton("Search User")
        self.remove_user_button = QPushButton("Remove User")
        
        buttons = [self.add_button, self.update_button, self.view_button, self.search_button, 
                   self.remove_button, self.fetch_button, self.save_button, self.add_user_button, 
                   self.update_user_button, self.view_users_button, self.search_user_button, 
                   self.remove_user_button]

        for button in buttons:
            layout.addWidget(button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
