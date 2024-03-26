from sys import argv
from requests import get
import pandas as pd
from bs4 import BeautifulSoup

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

for year in range(1998, 2017):
    
    url = "https://www.sports-reference.com/cfb/years/{year}-rushing.html".format(year = year)

    response = get(url, headers = header)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'id': 'rushing'})

    df = pd.read_html(str(table))[0]

    try:
        if argv[1] == '--save':
            df.to_csv('Datasets/NCAA_rushing_data_{y}.csv'.format(y = year))
            print(year)
    except IndexError:
        pass