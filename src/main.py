from library_management_system import functions

def main():
    """
    Main function to run the library management system.
    """
    functions.create_database()
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
            functions.add_book()
        elif choice == '2':
            functions.remove_book()
        elif choice == '3':
            functions.view_books()
        elif choice == '4':
            functions.update_book()
        elif choice == '5':
            functions.search_book()
        elif choice == '6':
            functions.add_user()
        elif choice == '7':
            functions.update_user()
        elif choice == '8':
            functions.remove_user()
        elif choice == '9':
            functions.view_user()
        elif choice == '10':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
