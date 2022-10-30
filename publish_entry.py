import requests


STRAPI_PUBLISH_URL = 'http://localhost:1337/content-manager/collection-types/api::book.book'
HEADERS = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        }


def publish_entry(id):
    try:
        url = STRAPI_PUBLISH_URL+'/'+str(id)+'/actions/publish'
        requests.post(url, headers = HEADERS)
    except Exception as e:
        print(e)

for id in range(1, 783):
    publish_entry(id)