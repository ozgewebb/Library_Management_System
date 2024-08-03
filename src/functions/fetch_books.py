import requests
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_BOOKS_API_KEY = os.getenv('GOOGLE_BOOKS_API_KEY')

def fetch_books_from_google_books(query, max_results=10):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        'q': query,
        'maxResults': max_results,
        'key': GOOGLE_BOOKS_API_KEY  # API key is added here
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        books = response.json().get('items', [])
        return [{'title': book['volumeInfo'].get('title', 'N/A'),
                 'authors': book['volumeInfo'].get('authors', ['N/A'])}
                for book in books]
    else:
        print("Error fetching data from Google Books API")
        return []
