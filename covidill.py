#ライブラリ
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

#前処理1
df = pd.read_csv("domestic_daily.csv")
index = pd.date_range("2020-05-09", "2022-05-28", freq = "D")
df.index = index
df = df.drop(df.columns[2:], axis=1)
df = df.drop(df.columns[0], axis=1)
df = df.rename(columns={"ALL" : "Number of seriously injured"})
#前処理２
df1 = pd.read_csv("domestic_daily.csv")
index1 = pd.date_range("2020-05-09", "2022-05-28", freq = "D")
df1.index = index1
df1 = df1.drop(df1.columns[2:], axis=1)
df1 = df1.drop(df1.columns[0], axis=1)
df1 = df1.rename(columns={"ALL" : "Number of deaths"})

#作図
plt.figure(figsize= (15, 9))
plt.xlabel("Date")
plt.ylabel("Number of injured and deaths")
dmin = "2020-05-09"
dmax = "2022-05-28"
xmin = datetime.datetime.strptime(dmin, "%Y-%m-%d")
xmax = datetime.datetime.strptime(dmax, "%Y-%m-%d")
plt.xlim([xmin,xmax])
plt.ylim([0, 2300])
plt.grid(True)
plt.plot(df, color="red", label="injured")
plt.plot(df1, color="blue", label="deaths")
# def main():
plt.legend()
plt.savefig('result.png')
plt.show()
