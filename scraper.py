from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome(".\chromedriver")
browser.get(START_URL)
time.sleep(10)
soup = BeautifulSoup(browser.page_source, "html.parser")
dwarf_table = soup.find_all('table')
temp_list = []
table_row = dwarf_table[7].find_all('tr')
for tr in table_row:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
Star = []
Distance = []
Mass = []
Radius = []

for i in range(1,len(temp_list)):
    Star.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][8])
    Radius.append(temp_list[i][9])

df = pd.DataFrame(list(zip(Star,Distance,Mass,Radius)),columns = ['Star','Distance','Mass','Radius'])
df.to_csv('dwarf_star.csv')