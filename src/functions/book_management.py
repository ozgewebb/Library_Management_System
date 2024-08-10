import sqlite3
from .db import get_db_connection
from fuzzywuzzy import fuzz, process

def add_book():
    """
    Adds a new book to the books table in the database.
    Prompts the user for title, author, description, published date, and ISBN.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            title = input("Enter title: ")
            authors = input("Enter authors: ")
            description = input("Enter description: ")
            published_date = input("Enter published date: ")
            isbn = input("Enter ISBN: ")

            cursor.execute("""
                INSERT INTO books (title, authors, description, published_date, isbn)
                VALUES (?, ?, ?, ?, ?)
            """, (title, authors, description, published_date, isbn))
            conn.commit()
            print("Book added successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

def view_books():
 def view_books():
    """
    Displays all books in the library database.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, authors FROM books")
            books = cursor.fetchall()
            return [{'id': book[0], 'title': book[1], 'authors': book[2]} for book in books]  # Convert to list of dictionaries
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []  # Return an empty list in case of error
        finally:
            conn.close()
    return []  # Return an empty list if connection fails

def search_book(query):
    """
    Searches for books in the library database based on the title.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, authors FROM books WHERE title LIKE ?", ('%' + query + '%',))
            books = cursor.fetchall()
            return [{'id': book[0], 'title': book[1], 'authors': book[2]} for book in books]  # Convert to list of dictionaries
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []  # Return an empty list in case of error
        finally:
            conn.close()
    return []  # Return an empty list if connection fails

def update_book():
    conn = get_db_connection()
    cursor = conn.cursor()

    book_title = input("Enter the title of the book to update: ")

    # Fetch all book titles from the database
    cursor.execute("SELECT id, title FROM books")
    books = cursor.fetchall()
    
    # Use fuzzy matching to find possible matches
    titles = [book[1] for book in books]
    matches = process.extract(book_title, titles, limit=5)
    
    if matches:
        print("Possible matches found:")
        for idx, match in enumerate(matches):
            print(f"{idx + 1}. {match[0]} (Score: {match[1]})")
        print("0. Cancel")

        choice = int(input("Select the correct book to update (or 0 to cancel): "))
        if choice == 0:
            print("Operation canceled.")
        else:
            selected_title = matches[choice - 1][0]
            # Find the book ID corresponding to the selected title
            book_id = [book[0] for book in books if book[1] == selected_title][0]
            
            # Collect new details for the book
            new_title = input("Enter the new title: ")
            new_author = input("Enter the new author: ")
            new_published_date = input("Enter the new published date (YYYY-MM-DD): ")

            # Update the book details in the database
            cursor.execute("""
                UPDATE books
                SET title = ?, author = ?, published_date = ?
                WHERE id = ?
            """, (new_title, new_author, new_published_date, book_id))
            conn.commit()
            print(f"Book '{selected_title}' has been updated.")
    else:
        print("No matches found. Operation canceled.")
    
    conn.close()


def remove_book():
    """
    Removes a book from the database.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            search_query = input("Enter the title of the book to remove: ")
            cursor.execute("SELECT id, title FROM books")
            books = cursor.fetchall()
            if books:
                titles = {book[1]: book[0] for book in books}
                matched_titles = process.extract(search_query, titles.keys(), scorer=fuzz.partial_ratio, limit=5)
                if matched_titles:
                    print("Did you mean:")
                    for idx, (title, score) in enumerate(matched_titles, start=1):
                        print(f"{idx}. {title} (Score: {score})")
                    print("0. Cancel")
                    choice = int(input("Enter the number of the correct title (0 to cancel): "))
                    if choice == 0:
                        print("Removal cancelled.")
                    elif 1 <= choice <= len(matched_titles):
                        selected_title = matched_titles[choice-1][0]
                        book_id = titles[selected_title]
                        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
                        conn.commit()
                        print("Book removed successfully.")
                    else:
                        print("Invalid choice. Removal cancelled.")
                else:
                    print("No close matches found.")
            else:
                print("No books found in the database.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()
