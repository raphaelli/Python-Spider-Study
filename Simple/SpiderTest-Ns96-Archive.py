
# coding: utf-8

import os
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
target_Url = "https://ns96.com/archives/"
ext_html = requests.get(target_Url,headers=headers) 

soup = BeautifulSoup(ext_html.text,'lxml')
urls = soup.select('a.archive-title')

for link in urls:
    print("https://www.ns96.com"+link.get('href'))
