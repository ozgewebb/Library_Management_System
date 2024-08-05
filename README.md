# Library Management System

## Overview

The Library Management System is a comprehensive tool designed to manage books and users in a library. The system allows you to add, update, view, search, and remove books and users, as well as fetch book data from the Google Books API and save it to the database.

## Features

- Add, Update, View, Search, and Remove Books
- Add, Update, View, Search, and Remove Users
- Fetch Books from Google Books API and Save to Database

## Installation

1. Clone the repository:
    
    git clone https://github.com/ozgewebb/Library_Management_System.git
    cd Library_Management_System

2. Create a virtual environment and activate it:

    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. Install the dependencies:
    
    pip install -r requirements.txt
    
4. Set up your `.env` file with your Google Books API key:
    
    GOOGLE_BOOKS_API_KEY=your_google_books_api_key 

5. Create the database:

    python -m src.functions.db create_database

## Usage

1. Run the main program:
    
    python src/main.py
    
2. Follow the menu options to perform various operations on books and users.

## Testing

To run the tests, use:
    
    python -m unittest discover -s tests

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## Author

This project is developed by Ozge Jess Webb.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Date

Created on: 2024-08-01