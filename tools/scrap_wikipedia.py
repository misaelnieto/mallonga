from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv


r = urlopen('https://en.wikipedia.org/wiki/User:West.andrew.g/Popular_pages')
soup = BeautifulSoup(r, 'html.parser')
tbody = soup.find('table', class_="wikitable").tbody
data = []
for row in tbody.find_all('tr'):
    cells = [c for c in row.findChildren('td')]
    if len(cells) != 16: 
        continue
    data.append((
        'https://en.wikipedia.org' + cells[1].a.attrs['href'],
        cells[1].getText().strip(),
        int(cells[-2].getText().strip().replace(',', '')),
    ))

with open('links.csv', 'w', newline='') as csvfile:
    cwr = csv.writer(csvfile)
    cwr.writerows(data)

