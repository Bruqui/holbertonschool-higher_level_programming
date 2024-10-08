import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from a url and prints the title of each post
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"Title: {post['title']}")


def fetch_and_save_posts():
    """
    Fetches posts from a URL and saves them into a CSV file
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    posts = response.json()
    with open('posts.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        fields = ['id', 'title', 'body']
        writer.writerow(fields)
        for post in posts:
            writer.writerow([post['id'], post['title'], post['body']])