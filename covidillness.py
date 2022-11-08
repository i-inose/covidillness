import pandas as pd
import subprocess as sp
import sys
import numpy as np
import matplotlib.pyplot as plt
sp.call('wget -nc https://covid.ourworldindata.org/data/owid-covid-data.csv', shell=True)

d=pd.read_csv('owid-covid-data.csv')
d.fillna(0,inplace=True)
lastday=str(d.date.iloc[-1:]).split()[1]
print(lastday)

n=len(sys.argv)-1
print('countries',n)

countries=[]
for i in range(n):
	countries.append(sys.argv[i+1])
# print(countries)

from datetime import date
d0 = date(2020, 2, 29)
d1 = date(int(lastday.split('-')[0]),int(lastday.split('-')[1]),int(lastday.split('-')[2]))
delta = d1 - d0 
days=delta.days

daysdate=sorted(d.date.unique())
daysdate=daysdate[len(daysdate)-days:-1]
# print(daysdate)

dd=pd.DataFrame(
  {
   "date": daysdate,
   "deaths": range(len(daysdate)),
   "icu_patients": range(len(daysdate)),
  })

for i in countries:
    print(i)
    for j in daysdate:
        if d.loc[(d.date == j) & (d.location == i), 'total_deaths'].any():
            dd.loc[dd.date == j, 'deaths'] = d.loc[(d.date == j) & (d.location == i), 'total_deaths'].values[0]
        dd.loc[dd.date == j, 'icu_patients'] = d.loc[(d.date == j) & (d.location == i), 'icu_patients'].values[0]
    dd.to_csv(i+'.csv', index=False)

def main():
 for i in range(len(countries)):
  i=pd.read_csv(countries[i]+'.csv') 
  plt.subplot(211, title="The number of deaths due to Covid19", ylabel="Covid-19")
  plt.plot(i.date, i.deaths)
  plt.xticks(np.arange(0,days,30*days/770),rotation=90)
  plt.tight_layout()
  plt.legend(countries)
  plt.subplot(212, title="The number of Icu patients", xlabel="Date", ylabel="Icu Patients")
  plt.plot(i.date, i.icu_patients)
  plt.xticks(np.arange(0,days,30*days/770),rotation=90)
  plt.tight_layout()
  plt.legend(countries)
  fig = plt.figure(1)
 plt.savefig('result.png',dpi=fig.dpi,bbox_inches='tight')
 plt.show()

if __name__ == "__main__":
 main()