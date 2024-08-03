from functions.book_management import add_book, remove_book, view_books, update_book, search_book
from functions.user_management import add_user, update_user, remove_user, view_user
from functions.db import create_database

def main():
    """
    Main function to run the library management system.
    """
    create_database()
    while True:
        print("\nWelcome to the library management system")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View Books")
        print("4. Update Book")
        print("5. Search Book")
        print("6. Add User")
        print("7. Update User")
        print("8. Remove User")
        print("9. View Users")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")
        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            view_books()
        elif choice == '4':
            update_book()
        elif choice == '5':
            search_book()
        elif choice == '6':
            add_user()
        elif choice == '7':
            update_user()
        elif choice == '8':
            remove_user()
        elif choice == '9':
            view_user()
        elif choice == '10':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

