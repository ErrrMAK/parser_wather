import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
from selenium.webdriver.chrome.options import Options


def csv_reader(massive):
    with open(massive, 'r') as file:
        reader = csv.reader(file)
        list_ip = []
        for row in reader:
            list_ip.append(''.join(list(row)))
    return list_ip


def get_sourse_html():
    # Запускаем перебор
    ip_list = csv_reader(ip_file)
    months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
             '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
    for i, year in enumerate(years):
        for j, month in enumerate(months):
            ip = ip_list[(i * len(months) + j) % len(ip_list)]
            # Открываем в браузере ссылку
            link = 'http://www.meteomanz.com/sy1?ty=hp&l=1&cou=6216&ind=13274&d1=02&m1=' + month + '&y1=' + year + '&h1=00Z&d2=12&m2=' + month + '&y2=' + year + '&h2=23Z'
            options = webdriver.ChromeOptions()
            options.add_argument(f"--proxy-server={ip}")
            print(ip, year, month)
            driver = webdriver.Chrome(options=options)
            try:
                driver.get(url=link)
                time.sleep(2)
                # Сохраняем страницу в файл
                file_html = "wather" + month + "-" + year + ".html"
                with open(file_html, mode="w", encoding="utf-8") as file:
                    file.write(driver.page_source)
            except Exception as _ex:
                print(_ex)
            finally:
                driver.quit()


# def get_items_urls(file_path):
#     #
#     with open(file_path) as file:
#         src = file.read()
#
#     soup = BeautifulSoup(src, "lxml")
#     item_divs = soup.find_all("div", class_='data')
#     print(item_divs)
#
#     for item in items_divs:
#         item_url = item.find('tr', )


ip_file = 'working_ip.csv'
get_sourse_html()

