from urllib.parse import urlparse

import requests
from pyquery import PyQuery as pq


def podcast_feed(url):
    headers = {
        'authority': 'podcasts.google.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
    }
    r = requests.get(url, headers=headers)
    result: str = pq(r.text)('[jscontroller="TV0WMc"]').attr('jsdata')
    extract = result.split(';', 1)[1]
    return urlparse(extract)._replace(query='').geturl()
