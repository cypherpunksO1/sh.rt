import requests
import threading

path = 'http://127.0.0.1:8000/api/v1/cutLink/'
site = 'https://google.com'


def request():
    for _ in range(100000):
        requests.post(path, data={'link': site})


for _ in range(10):
    th = threading.Thread(target=request)
    th.start()
