from fuzzywuzzy import process
import sqlite3

def get_db_connection():
    """
    Establish a connection to the SQLite database.
    """
    try:
        conn = sqlite3.connect('library.db')
        return conn
    except sqlite3.Error as error:
        print(f"Error while connecting to sqlite: {error}")
        return None

def create_database():
    """
    Creates the books table in the library database if it doesn't already exist.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS books
                            (id INTEGER PRIMARY KEY,
                            title TEXT,
                            author TEXT)''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

def add_book():
    """
    Adds a new book to the library database.
    Prompts the user for book title and author,
    checks for similar existing book titles,
    and inserts the book into the database if no similar title is found.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            title = input("Enter book title: ")
            author = input("Enter book author: ")

            cursor.execute("SELECT title FROM books")
            existing_books = [row[0] for row in cursor.fetchall()]

            similar_titles = process.extract(title, existing_books, limit=3)

            if any(score > 80 for title, score in similar_titles):
                print("A book with a similar title already exists. Please choose a different title.")
            else:
                cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
                conn.commit()
                print("Book added successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

def remove_book():
    """
    Removes a book from the library database.
    Prompts the user for the book title,
    uses fuzzy matching to suggest similar titles,
    and deletes the book if found.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            title = input("Enter the title of the book to remove: ")

            cursor.execute("SELECT title FROM books")
            existing_books = [row[0] for row in cursor.fetchall()]

            similar_titles = process.extract(title, existing_books, limit=3)

            if similar_titles:
                print("Did you mean:")
                for i, (match_title, score) in enumerate(similar_titles):
                    print(f"{i + 1}: {match_title} (score: {score})")

                choice = int(input("Enter the number of the book to remove (0 to cancel): "))
                if 0 < choice <= len(similar_titles):
                    chosen_title = similar_titles[choice - 1][0]
                    cursor.execute("DELETE FROM books WHERE title = ?", (chosen_title,))
                    conn.commit()
                    print("Book removed successfully.")
                else:
                    print("Operation canceled.")
            else:
                print("No similar titles found.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        except ValueError:
            print("Invalid input. Please enter a number.")
        finally:
            conn.close()

def view_books():
    """
    Displays all books in the library database.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, author FROM books")
            books = cursor.fetchall()
            if books:
                print("Books in the library:")
                for book in books:
                    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")
            else:
                print("No books found in the library.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

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
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            view_books()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


