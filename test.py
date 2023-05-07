months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
for year in (2000, 2024):
    year = str(year)
    for month in months:
        link = 'http://www.meteomanz.com/sy1?ty=hp&l=1&cou=6216&ind=13274&d1=02&m1=' + month + '&y1=' + year + '&h1=00Z&d2=12&m2=' + month + '&y2=' + year + '&h2=23Z'
        print(link)