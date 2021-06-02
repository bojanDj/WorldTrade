import requests
import json
import pandas as pd

df = pd.read_csv('APIdata/country-codes_csv.csv')
codes = df['ISO3166-1-numeric']

chunks = [codes[x:x+100] for x in range(0, len(codes), 100)]

pers = ['1965%2C1970%2C1975%2C1980%2C1985','1990%2C1995%2C2000%2C2005%2C2010','2015%2C2020']

for per in pers:
    f = open('APIdata/'+str(par)+'.csv', "a")
    for j in codes:
        response = requests.get("https://comtrade.un.org/api/get?max=100000&type=C&freq=A&px=HS&ps="+str(per)+"&r="+str(int(j))+"&p=all&rg=all&cc=TOTAL&uitoken=876de0f1c9ddf87ed64b9f69c18cf33d&fmt=csv")
        print(response.status_code)
        print("https://comtrade.un.org/api/get?max=100000&type=C&freq=A&px=HS&ps="+str(per)+"&r="+str(int(j))+"&p=all&rg=all&cc=TOTAL&uitoken=dd9df0fdbf9b219648145c7bae091339&fmt=csv")
        f.write(response.text)
f.close()
