import pandas as pd 
from pandas import DataFrame,Series
rawdata=pd.read_csv('metal1.csv')
rawdata1=DataFrame(rawdata)
def find(rawdata1,str):
	strdata=rawdata1[rawdata1['m3'].str.contains(str)]
    return strdata

metaldata={}
inlist=['Be','Al','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Y','Zr','Nb','Mo','Sn','Hf','Ta','W','Au']
for str in inlist:
	metaldata[str]=find(rawdata1,str)



def query(a,b):
    datamer=metaldata[a[0]]
    for str in a:
   	    datamer=pd.merge(metaldata[str],datamer)
    datamer2=metaldata[b[0]]
    if len(b)==0:
        b=a
    for str in b:
   	    datamer2=pd.merge(metaldata[str],datamer2,how='outer')
    datamer=pd.merge(datamer,datamer2)
    return datamer

