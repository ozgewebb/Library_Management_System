from .db import get_db_connection
import sqlite3

def add_user():
    """
    Adds a new user to the users table in the database.
    Prompts the user for username, password, and role.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role: ")

            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
            conn.commit()
            print("User added successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

def view_user():
    """
    Displays all users in the library database.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT user_id, username, role FROM users")
            users = cursor.fetchall()
            if users:
                print("Users in the library:")
                for user in users:
                    print(f"User ID: {user[0]}, Username: {user[1]}, Role: {user[2]}")
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
            user_id = input("Enter the User ID of the user you want to update: ")
            new_username = input("Enter the new username for the user: ")
            new_password = input("Enter the new password for the user: ")
            new_role = input("Enter the new role for the user: ")

            cursor.execute("UPDATE users SET username = ?, password = ?, role = ? WHERE user_id = ?", 
                           (new_username, new_password, new_role, user_id))
            conn.commit()
            print("User updated successfully.")
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
            user_id = input("Enter the User ID of the user to remove: ")

            cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
            conn.commit()
            print("User removed successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()
