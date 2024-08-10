import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path="src/config/.env")

GOOGLE_BOOKS_API_KEY = os.getenv('GOOGLE_BOOKS_API_KEY')

def fetch_books_from_google_books(query, max_results=10):
    """
    Fetches books from Google Books API based on the query.

    Parameters:
    query (str): The search query for fetching books.
    max_results (int): Maximum number of results to fetch (default is 10).

    Returns:
    list: A list of dictionaries containing book titles and authors.
    """
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        'q': query,
        'maxResults': max_results,
        'key': GOOGLE_BOOKS_API_KEY
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        books = response.json().get('items', [])
        return [{'title': book['volumeInfo'].get('title', 'N/A'),
                 'authors': book['volumeInfo'].get('authors', ['N/A'])}
                for book in books]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Google Books API: {e}")
        return []
