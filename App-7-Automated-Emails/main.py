# API key: 9433aabae9424b57a3278ee642f1325a
import requests
from pprint import pprint

class NewsFeed:

    def __init__(self, data):
        self.data = data

    def get(self):
        pass
url = "https://newsapi.org/v2/everything?"\
    "qInTitle=tesla&"\
        "from=2023-07-09&"\
            "to=2023-08-09&"\
                "language=en&"\
                "apiKey=9433aabae9424b57a3278ee642f1325a"

response = requests.get(url)
content = response.text
pprint(content)