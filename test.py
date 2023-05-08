import requests
def get_sourse_html():
    # Запускаем перебор
    ip_list = ['34.139.55.89:8585', '34.145.186.193:8585', '34.174.62.103:8585']
    months = ["01", "02", "03"]
    # months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    years = ['2000']
    # years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
    #          '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
    data = []
    id_ip = 0
    for i, year in enumerate(years):
        for j, month in enumerate(months):
            while True:
                if id_ip > len(ip_list):
                    id_ip = 0
                ip = ip_list[id_ip]
                link = 'http://www.meteomanz.com/sy1?ty=hp&l=1&cou=6216&ind=13274&d1=01&m1=' + month + '&y1=' + year + '&h1=00Z&d2=31&m2=' + month + '&y2=' + year + '&h2=23Z'
                response = requests.get(link, proxies={'http': ip, 'https': ip}, timeout=6)
                if response.status_code == 200:
                    print(id_ip, '200')
                    break
                else:
                    id_ip += 1
                    print(id_ip, '400')
                    continue

get_sourse_html()