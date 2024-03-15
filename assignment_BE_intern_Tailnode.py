import requests
import sqlite3
from bs4 import BeautifulSoup

def scrape_books_data(url):
    """Scrape books data from the website."""
    books_data = []

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Website accessed successfully")
            soup = BeautifulSoup(response.text, 'html.parser')
            book_containers = soup.find_all('article', class_='product_pod')

            for book in book_containers:
                title = book.h3.a['title']
                price = book.find('p', class_='price_color').text
                availability = book.find('p', class_='instock availability').text.strip()
                rating = book.find('p', class_='star-rating')['class'][1]
                books_data.append({'title': title, 'price': price, 'availability': availability, 'rating': rating})
        else:
            print("Error: Failed to access website. Status code:", response.status_code)
    except requests.RequestException as e:
        print("Error: Failed to access website:", e)

    return books_data

def store_books_data(books_data):
    """Store scraped books data in the database."""
    try:
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        price TEXT,
                        availability TEXT,
                        rating TEXT)''')

        for book in books_data:
            cursor.execute('''INSERT INTO books (title, price, availability, rating)
                            VALUES (?, ?, ?, ?)''', (book['title'], book['price'], book['availability'], book['rating']))

        conn.commit()
        conn.close()
        
        print("Books data stored successfully in the database.")

    except sqlite3.Error as e:
        print("Error storing books data in the database:", e)

def fetch_and_store_users(api_url, headers):
    """Fetch users data from API and store it in the database."""
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            users_data = response.json()['data']
            conn = sqlite3.connect('books.db')
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id TEXT PRIMARY KEY,
                                firstName TEXT,
                                lastName TEXT,
                                email TEXT)''')

            for user in users_data:
                cursor.execute("SELECT COUNT(*) FROM users WHERE id = ?", (user['id'],))
                count = cursor.fetchone()[0]
                if count == 0:
                    cursor.execute('''INSERT INTO users (id, firstName, lastName, email)
                                    VALUES (?, ?, ?, ?)''', (user['id'], user['firstName'], user['lastName'], user.get('email', 'No email provided')))

            conn.commit()
            conn.close()
            print("Users data fetched and stored successfully in the database.")
        else:
            print("Error: Failed to fetch users data. Status code:", response.status_code)
    except requests.RequestException as e:
        print("Error: Failed to fetch users data:", e)

def main():
    api_url_users = 'https://dummyapi.io/data/v1/user'
    headers = {'app-id': '65f197eae5c0462c46037594'}
    fetch_and_store_users(api_url_users, headers)

    url_books = 'http://books.toscrape.com'
    books_data = scrape_books_data(url_books)
    if books_data:
        store_books_data(books_data)

if __name__ == "__main__":
    main()
