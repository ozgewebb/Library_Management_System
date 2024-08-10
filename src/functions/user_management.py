import sqlite3
from .db import get_db_connection
from fuzzywuzzy import fuzz, process

def add_user():
    """
    Adds a new user to the users table in the database.
    Prompts the user for username, password, email, and role.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            role = input("Enter role: ")

            cursor.execute("INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, ?)", (username, password, email, role))
            conn.commit()
            print("User added successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

def view_users():
    """
    Displays all users in the database.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT username, role FROM users")
            users = cursor.fetchall()
            return [{'username': user[0], 'role': user[1]} for user in users]  # Convert to list of dictionaries
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []  # Return an empty list in case of error
        finally:
            conn.close()
    return []  # Return an empty list if connection fails

def search_user():
    """
    Searches for users in the library database based on the username using fuzzy matching.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            search_query = input("Enter username to search: ")
            cursor.execute("SELECT user_id, username, email, role FROM users")
            users = cursor.fetchall()
            if users:
                usernames = {user[1]: (user[0], user[2], user[3]) for user in users}
                matched_usernames = process.extract(search_query, usernames.keys(), scorer=fuzz.partial_ratio, limit=5)
                if matched_usernames:
                    print("Did you mean:")
                    for idx, (username, score) in enumerate(matched_usernames, start=1):
                        print(f"{idx}. {username} (Score: {score})")
                    print("0. Cancel")
                    choice = int(input("Enter the number of the correct username (0 to cancel): "))
                    if choice == 0:
                        print("Search cancelled.")
                    elif 1 <= choice <= len(matched_usernames):
                        selected_username = matched_usernames[choice-1][0]
                        user_id, email, role = usernames[selected_username]
                        print(f"User ID: {user_id}, Username: {selected_username}, Email: {email}, Role: {role}")
                    else:
                        print("Invalid choice. Search cancelled.")
                else:
                    print("No close matches found.")
            else:
                print("No users found in the database.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

def update_user():
    """
    Updates the details of an existing user in the database.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            search_query = input("Enter the username of the user you want to update: ")
            cursor.execute("SELECT user_id, username, email, role FROM users")
            users = cursor.fetchall()
            if users:
                usernames = {user[1]: (user[0], user[2], user[3]) for user in users}
                matched_usernames = process.extract(search_query, usernames.keys(), scorer=fuzz.partial_ratio, limit=5)
                if matched_usernames:
                    print("Did you mean:")
                    for idx, (username, score) in enumerate(matched_usernames, start=1):
                        print(f"{idx}. {username} (Score: {score})")
                    print("0. Cancel")
                    choice = int(input("Enter the number of the correct username (0 to cancel): "))
                    if choice == 0:
                        print("Update cancelled.")
                    elif 1 <= choice <= len(matched_usernames):
                        selected_username = matched_usernames[choice-1][0]
                        user_id, _, _ = usernames[selected_username]
                        new_username = input("Enter the new username: ")
                        new_password = input("Enter the new password: ")
                        new_email = input("Enter the new email: ")
                        new_role = input("Enter the new role: ")

                        cursor.execute("""
                            UPDATE users
                            SET username = ?, password = ?, email = ?, role = ?
                            WHERE user_id = ?
                        """, (new_username, new_password, new_email, new_role, user_id))
                        conn.commit()
                        print("User updated successfully.")
                    else:
                        print("Invalid choice. Update cancelled.")
                else:
                    print("No close matches found.")
            else:
                print("No users found in the database.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

def remove_user():
    """
    Removes a user from the database.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            search_query = input("Enter the username of the user to remove: ")
            cursor.execute("SELECT user_id, username FROM users")
            users = cursor.fetchall()
            if users:
                usernames = {user[1]: user[0] for user in users}
                matched_usernames = process.extract(search_query, usernames.keys(), scorer=fuzz.partial_ratio, limit=5)
                if matched_usernames:
                    print("Did you mean:")
                    for idx, (username, score) in enumerate(matched_usernames, start=1):
                        print(f"{idx}. {username} (Score: {score})")
                    print("0. Cancel")
                    choice = int(input("Enter the number of the correct username (0 to cancel): "))
                    if choice == 0:
                        print("Removal cancelled.")
                    elif 1 <= choice <= len(matched_usernames):
                        selected_username = matched_usernames[choice-1][0]
                        user_id = usernames[selected_username]
                        cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
                        conn.commit()
                        print("User removed successfully.")
                    else:
                        print("Invalid choice. Removal cancelled.")
                else:
                    print("No close matches found.")
            else:
                print("No users found in the database.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()
