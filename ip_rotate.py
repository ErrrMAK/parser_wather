import requests
import csv


def check_proxys():
    #Создаем список работающих IP
    proxys = []
    url = 'https://progr.interplanety.org/'
    cnt_200 = 0
    cnt_400 = 0
    with open('IP.csv', 'r') as csvfile:
        uncleaned_proxys = list(csv.reader(csvfile))
        for row in uncleaned_proxys:
            ip = row[0]
            try:
                response = requests.get(url, proxies={'http': ip, 'https': ip}, timeout=6)
                proxys.append(ip)
                cnt_200 += 1
                print('cnt_200 =', cnt_200)
            except requests.exceptions.RequestException:
                cnt_400 += 1
                print('cnt_400 =', cnt_400)
    print('cnt_200 =', cnt_200)
    print('cnt_400 =', cnt_400)

    # Транспонируем значения в столбец
    proxys_column = [[item] for item in proxys]
    return proxys_column

def save_to_csv(data):
    #Сорханяем список в файл
    with open('working_ip.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)



proxys = check_proxys()
save_to_csv(proxys)
