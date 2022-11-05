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
d0 = date(2020, 3, 3)
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
		if d.loc[(d.date==j) & (d.location==i),'total_deaths']:
			dd.loc[dd.date==j,'deaths']=d.loc[(d.date==j) & (d.location==i),'total_deaths']
		# print('int',int(d.loc[(d.date==j) & (d.location==i),'total_deaths'][0:1]))
		dd.loc[dd.date==j,'icu_patients']=d.loc[(d.date==j) & (d.location==i),'icu_patients']
	dd.to_csv(i+'.csv',index=False)

def main():
 for i in range(len(countries)):
  i=pd.read_csv(countries[i]+'.csv') 
  plt.ylabel('ICU')
  plt.plot(i.date,i.icu_patients)
  plt.xticks(np.arange(0,days,30*days/770),rotation=90)
  fig=plt.figure(1)
  fig.set_size_inches(10,3)
 plt.legend(countries)
 plt.savefig('result.png',dpi=fig.dpi,bbox_inches='tight')
 plt.show()

if __name__ == "__main__":
 main()