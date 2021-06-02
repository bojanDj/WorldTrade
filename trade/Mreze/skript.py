import json

lista = []
for num in range(1980,2021,5):
    try:
        with open(str(num) + '.txt') as json_file:
            data = json.load(json_file)
            lista = lista + list(set(data.keys()) - set(lista))
    except:
        print("a")

print(lista)

obj = {}
for con in lista:
    ja = []
    for num in range(1980,2021,5):
        try:
            with open(str(num) + '.txt') as json_file:
                data = json.load(json_file)
                god = {}
                god['year'] = num
                god['degree'] = data[con]
                ja.append(god)
        except:
            print("a")
    obj[con] = ja

print(obj)

import pandas as pd
df = pd.json_normalize(obj)
#df.to_excel('degrees.xlsx')

listaNapredak = []
for coun in obj:
    print(coun)
    print(obj[coun]) 
    test_list = []
    for k in obj[coun]:
        print(k['degree'])
        test_list.append(k['degree'])
    if(test_list == sorted(test_list) and len(test_list) > 3):
        listaNapredak.append(coun)
        
print(sorted(listaNapredak))

listaNazad = []
for coun in obj:
    #print(coun)
    #print(obj[coun]) 
    test_list = []
    for k in obj[coun]:
        #print(k['degree'])
        test_list.append(k['degree'])
    if(test_list == sorted(test_list, reverse = True) and len(test_list) > 1):
        listaNazad.append(coun)
        
print(sorted(listaNazad))

from operator import itemgetter
print('Pocetak')
listaPad = []
test_list1 = []
for coun in obj:
    print(coun)
    print(obj[coun])    
    test_list = []
    d2020 = []
    d2015 = []
    for k in obj[coun]:
        print(k['degree'])
        if (k['year'] == 2020): 
            d2020.append(k['degree'])
            print('Da')
        if (k['year'] == 2015): 
            d2015.append(k['degree'])
            print('Ne')
        test_list.append(k['degree'])
    try:
        pom = {}
        pom['Country'] = coun
        pom['Per'] = str(d2015[0] / d2020[0])
        print('Mozda' + pom['Per'])
        listaPad.append(pom)
    except:
        print('Mozda2')
    # test_list1 = sorted(test_list, reverse = True)
    # if(len(test_list1) > 1):
        # pom['Country'] = coun
        # pom['Per'] = test_list1[1] / test_list1[0]
        # listaPad.append(pom)
print('Kraj')        
print(sorted(listaPad, key=itemgetter('Per'), reverse=True))
                
                
    