from sys import argv
from requests import get
import pandas as pd
from bs4 import BeautifulSoup

def parse_ht(ht):
    # format: 6-0
    ht_ = ht.split("-")
    ft_ = float(ht_[0])
    in_ = float(ht_[1])
    height = (12*ft_) + in_
    
    return height

def new_func():
    header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
    return header

header = new_func()
dictionary = {'-' : 'ft'}

for year in range(2020, 2022):
    
    url = "https://www.pro-football-reference.com/draft/{year}-combine.htm".format(year = year)

    response = get(url, headers = header)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'id': 'combine'})

    df = pd.read_html(str(table))[0]
    df.fillna("UNK", inplace = True)
    df.drop(df[df['Player'] == 'Player'].index, inplace = True)
    df["Ht"] = df["Ht"].apply(lambda x:parse_ht(x))

    try:
        if argv[1] == '--save':
            df.to_csv('Datasets/Combine_data_{y}.csv'.format(y = year))
            print(year)
    except IndexError:
        pass