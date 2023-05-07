import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
from selenium.webdriver.chrome.options import Options

def get_items_urls(url):
    #
    with open(url, 'r', encoding='utf-8') as file:
        html = file.read()

    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table', {'class': 'data'})

    if table:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [col.text.strip() for col in cols]
            print(cols)
        return rows
    else:
        print('Table not found')


url = 'wather04-2000.html'
get_items_urls(url)