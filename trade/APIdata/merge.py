fout=open("dataPom.csv","a")
for line in open("comtrade (1).csv"):
    fout.write(line)
for num in range(2,117):
    f = open("comtrade ("+str(num)+").csv")
    for line in f:
         fout.write(line)
    f.close()
fout.close()

import pandas as pd

df = pd.read_csv('data.csv')
  
df.drop_duplicates(subset=None, inplace=True)

df.to_csv('data.csv', index=False)