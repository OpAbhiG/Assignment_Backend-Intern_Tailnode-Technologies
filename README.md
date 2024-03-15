# Assignment README

## How to Run

1. Make sure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the `assignment_BE_intern_Tailnode.py` file.
4. Run the script using the following command:
   ```
   python assignment_BE_intern_Tailnode.py
   ```

## Instructions

### Part A: Getting Users and Their Posts

#### Getting Users
- The script fetches user data from a special website API.
- It requests information such as users' names and emails.

#### Getting Posts
- After obtaining user data, the script fetches posts made by each user from another API endpoint.
- User data is stored along with their corresponding posts in the database.

### Part B: Collecting Books Data

#### Collecting Books
- The script visits a website containing a variety of books.
- It collects information on each book's title, price, availability, and rating.

## How It's Done

- Python libraries such as `requests` and `BeautifulSoup` are used to interact with websites and extract data.
- The retrieved data is stored in a database for future use and analysis.

## Why It Matters

- By saving this information, we can analyze trends and preferences among users and the popularity of books.
- This analysis helps in making informed decisions and recommendations based on user interests.