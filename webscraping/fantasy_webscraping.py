from sys import argv
from requests import get
import pandas as pd
from bs4 import BeautifulSoup

def new_func():
    header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
    return header

header = new_func()

for year in range(2020, 2022):
    
    url = "https://www.pro-football-reference.com/years/{year}/fantasy.htm".format(year = year)

    response = get(url, headers = header)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'id': 'fantasy'})

    df = pd.read_html(str(table))[0]

    try:
        if argv[1] == '--save':
            df.to_csv('Datasets/Fantasy_data_{y}.csv'.format(y = year))
            print(year)
    except IndexError:
        pass