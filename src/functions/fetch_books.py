import requests

def fetch_books_from_google_books(query, max_results=10):
    """
    Fetch books from Google Books API based on a search query.
    
    :param query: Search query string
    :param max_results: Maximum number of results to fetch
    :return: List of books with title and author
    """
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        'q': query,
        'maxResults': max_results
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

