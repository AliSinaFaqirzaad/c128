from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(url)
soup=bs(page.text,'html.parser')
star_table=soup.find_all('table')
table_rows=star_table[7].find_all('tr')
Temp_list=[]
for i in table_rows:
    td=i.find_all("td")
    row=[j.text.rstrip() for j in td]
    Temp_list.append(row)
star=[]
distance=[]
mass=[]
radius=[]
for i in range(1,len(Temp_list)):
    star.append(Temp_list[i][1])
    distance.append(Temp_list[i][2])
    mass.append(Temp_list[i][3])
    radius.appemd(Temp_list[i][4])


    