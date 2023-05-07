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


def get_sourse_html(link, month, year):
    #     # Открываем в браузере ссылку
    #     driver = webdriver.Chrome(options=options)
    # with open('IP.csv', 'r') as csvfile:
    #     proxys = list(csv.reader(csvfile))
    for proxy in ip_list:
        options = webdriver.ChromeOptions()
        options.add_argument(f"--proxy-server={proxy}")
        print(proxy)
        driver = webdriver.Chrome(options=options)
        try:
            driver.get(url=link)
            time.sleep(2)
            # Сохраняем страницу
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


def main(month, year):
    # Подготавливаем динамическую ссылку для циклов
    get_sourse_html(
        'http://www.meteomanz.com/sy1?ty=hp&l=1&cou=6216&ind=13274&d1=02&m1='
        + month
        + '&y1='
        + year
        + '&h1=00Z&d2=12&m2=01&y2=2000&h2=23Z'
        , month, year)


ip_file = 'working_ip.csv'
ip_list = csv_reader(ip_file)

if __name__ == "__main__":
    main('2000', '01')
