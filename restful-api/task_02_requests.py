import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from the JSONPlaceholder API and prints their titles.
    This function sends a GET request to the JSONPlaceholder API to retrieve
    posts. It prints the  HTTP status code to indicate the success or failure
    of the request. If successful (status code 200), it parses the JSON
    response and iterates over the posts, printing each post's title.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print('Status Code: {}'.format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print('Failed to fetch posts.')


def fetch_and_save_posts():
    """
    Fetches posts from the JSONPlaceholder API and saves them to a CSV file.
    This function sends a GET request to the JSONPlaceholder API to retrieve
    posts. If the request is successful (status code 200), it parses the JSON
    data and extracts the post ID, title, and body. The extracted data is
    written into a CSV file named 'posts.csv', with each post as a row in
    the file. The CSV contains three columns: 'id', 'title', and 'body'.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        csv_data = [{'id': post['id'], 'title': post['title'], 'body':
        post['body']} for post in posts]
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerow(csv_data)
        print('Posts have been saved to posts.csv.')
    else:
        print('Failed to fetch posts.')
