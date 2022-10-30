import json
from time import sleep
import requests
from requests.adapters import HTTPAdapter, Retry


STRAPI_POST_URL = 'http://localhost:1337/content-manager/collection-types/api::book.book'
HEADERS = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        }

with open('booksdb.json') as booksdb:
  books = json.load(booksdb)['books']

def create_entry(book):
    try:
        body = json.dumps(book, ensure_ascii=True).encode("utf-8")
        requests.post(STRAPI_POST_URL, data = body, headers = HEADERS)
    except Exception as e:
        print(e)

for book in books:
    create_entry(book)
    print(book['title'])
    sleep(0.5)