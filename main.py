import requests
import codecs
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd


results = []

postalcode = []

'''
with open('postalcode_2.csv', 'r') as q:
    csv_reader = csv.reader(q)
    for row in csv_reader:
        states.append(row[0])
        print(states)
'''

url = 'https://www.unitedstateszipcodes.org/co/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

#f = open('./zip.html', 'wb')
#f.write(r.content)
#f.close()
'''
file = codecs.open('zip.html', 'r', 'utf-8')
info = file.read()
soup = BeautifulSoup(info, 'html.parser')
'''

content = soup.find_all('div', {'class': 'list-group-item'})

for item in content:
    zipcode = item.find('div', {'class': 'col-xs-12 prefix-col1'}).text.strip()
    type = item.find('div', {'class': 'col-xs-12 prefix-col2'}).text.strip()
    commoncity = item.find('div', {'class': 'col-xs-12 prefix-col3'}).text.strip()
    county = item.find('div', {'class': 'col-xs-12 prefix-col4'}).text.strip()
    areacode = item.find('div', {'class': 'col-xs-12 prefix-col5'}).text.strip()

    zipdata = {
        'zipcode': zipcode,
        'type': type,
        'commoncity': commoncity,
        'county': county,
        'areacode': areacode
    }

    results.append(zipdata)
    time.sleep(2)
    print('zipcode found: ', len(results))

df = pd.DataFrame(results)
print(df.head(), df.tail())
df.to_csv('colorado.csv')
df.to_json('colorado.json')

