from functions.book_management import add_book, remove_book, view_books, update_book, search_book
from functions.user_management import add_user, update_user, remove_user, view_users, search_user
from functions.db import create_database, get_db_connection
from functions.fetch_books import fetch_books_from_google_books
from dotenv import load_dotenv
import os
import sqlite3

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
GOOGLE_BOOKS_API_KEY = os.getenv('GOOGLE_BOOKS_API_KEY')

def main():
    """
    Main function to run the library management system.
    """
    create_database()
    while True:
        print("\nWelcome to the library management system")
        print("1. Add Book")
        print("2. Update Book")
        print("3. View Books")
        print("4. Search Book")
        print("5. Remove Book")
        print("6. Fetch Books from Google Books")
        print("7. Save Fetched Books to Database")
        print("8. Add User")
        print("9. Update User")
        print("10. View Users")
        print("11. Search User")
        print("12. Remove User")
        print("13. Exit")

        choice = input("Enter your choice (1-13): ")
        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            view_books()
        elif choice == '4':
            search_book()
        elif choice == '5':
            remove_book()
        elif choice == '6':
            query = input("Enter a search query: ")
            books = fetch_books_from_google_books(query)
            for book in books:
                print(f"Title: {book['title']}, Authors: {', '.join(book['authors'])}")
        elif choice == '7':   # save fetched books option
            query = input("Enter a search query: ")
            books = fetch_books_from_google_books(query)
            if books:
                conn = get_db_connection()
                if conn:
                    try:
                        cursor = conn.cursor()
                        for book in books:
                            title = book['title']
                            authors = ', '.join(book['authors'])
                            cursor.execute("INSERT INTO books (title, authors) VALUES (?, ?)", (title, authors))
                        conn.commit()
                        print("Fetched books saved to database successfully.")
                    except sqlite3.Error as e:
                        print(f"An error occurred: {e}")
                    finally:
                        conn.close()
            else:
                print("No books to save.")
        elif choice == '8':
            add_user()
        elif choice == '9':
            update_user()
        elif choice == '10':
            view_users()
        elif choice == '11':
            search_user()
        elif choice == '12':
            remove_user()
        elif choice == '13':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
