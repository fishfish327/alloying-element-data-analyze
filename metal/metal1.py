import pandas as pd 
from pandas import DataFrame,Series
rawdata=pd.read_csv('metal1.csv')
rawdata1=DataFrame(rawdata)
def find(rawdata1,str):
	strdata=rawdata1[rawdata1['m3'].str.contains(str)]
    return strdata

metallist=['Li','Be',
           'Na','Mg','Al',
           'K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge'
           'Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb'
           'Cs','Ba','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi'
           'La','Ce','Pr','Nd','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu'
	       
]
inlist=[]


for str in metallist:
	i=0
	for str1 in rawdata1['m3']:
		  if str in str1:
			i=i+1
	if i>0:
			inlist.append(str)


metaldata={}

for str in inlist:
	metaldata[str]=find(rawdata1,str)

inlist=['Be','Al','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Y','Zr','Nb','Mo','Sn','Hf','Ta','W','Au']

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

