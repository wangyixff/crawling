import urllib.request
import requests
import pandas as pd
from requests import get
import matplotlib.pyplot as plt
from lxml.html import fromstring,tostring #lxml library is faster
from throttle import Throttle


from bs4 import BeautifulSoup
import json


def download(url, num_retries=2, user_agent='wswp', proxies=None):
    """ Download a given URL and return the page content
        args:
            url (str): URL
            user_agent (str): user agent (default: wswp)
            proxies (dict): proxy dict w/ keys 'http' and 'https', values
                            are strs (i.e. 'http(s)://IP') (default: None)
            num_retries (int): # of retries if a 5xx error is seen (default: 2)
    """
    print('Downloading:', url)
    headers = {'User-Agent': user_agent}
    try:
        resp = requests.get(url, headers=headers, proxies=proxies)
        html = resp.text
        if resp.status_code >= 400:
            print('Download error:', resp.text)
            html = None
            if num_retries and 500 <= resp.status_code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries - 1)
    except requests.exceptions.RequestException as e:
        print('Download error:', e)
        html = None
    return html

content = download(webpage)
soup = BeautifulSoup(content, "lxml")
container = soup.find("div",attrs={'class': 'content-area'})
para_list = []
for p in container.find_all("p"):
    para_list.append(p.text)
print(para_list)

para_list2 = ['dsa','dsafdsafsa']
for index, (first, second) in enumerate(zip(para_list, para_list2)):
    if first != second:
        print(index, first)

while 1:
        url = crawl_queue.pop()
        throttle.wait(url)
        html = download(url, user_agent=user_agent, proxy=proxy)
        #todo