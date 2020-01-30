import pandas as pd
import numpy as np

#declaration
#get data from https://www.bka.de/DE/AktuelleInformationen/StatistikenLagebilder/PolizeilicheKriminalstatistik/PKS2018/Standardtabellen/standardtabellenTatverdaechtige.html?nn=108686
#download excel
file = pd.read_excel("STD-TV-01-T20-Tatverdaechtige_excel.xlsx" , usecols ="B,C,D", skiprows=8)
save = pd.DataFrame(columns=['Verbrechen'])
len = file.shape
crimes = [[],[],[],[],[]]
temp = 0


for i in range(0, len[0], 3):

    #evaluate percent
    
    if file.iloc[i+1,2] > 0:
        temp = file.iloc[i+1,2]/file.iloc[i+2,2]*100
    else:
        temp = 0

    #check percent change the range to whatever
    if temp>50 and temp<=100:
        crimes[0].append(str(file.iloc[i,0]))
        crimes[1].append(temp.round(2))
        crimes[2].append(file.iloc[i,2])
        crimes[3].append(file.iloc[i+1,2])
        crimes[4].append(file.iloc[i+2,2])
        
#add to pandas dataframe      
save['Verbrechen'] = crimes[0]
save['Prozentualer Anteil'] = crimes[1]
save['Anzahl Männer'] = crimes[2]
save['Anzahl Frauen'] = crimes[3]
save['Gesamt'] = crimes[4]

print(save)
save.to_csv('result.csv')