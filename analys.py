import pandas as pd

df = pd.read_csv('weather_data.csv')

avg_tmp = df[['temp','utc_time']].groupby('utc_time').min()




print(avg_tmp)

