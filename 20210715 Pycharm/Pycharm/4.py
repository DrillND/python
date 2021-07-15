import requests
from bs4 import BeautifulSoup
import pandas as pd


req = requests.get('http://media.daum.net/ranking/popular/')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
newstitle = soup.select('a.link_txt')
newscomname = soup.select('.info_news')

lst1 = []
lst2 = []

for i in range(len(newscomname)):
    lst1.append(newscomname[i].text.strip())
    lst2.append(newstitle[i].text.strip())

result_file = pd.DataFrame({'newstitle':lst2, 'newscomname':lst1})
result_file.to_csv("C:\\Users\\KB\\Documents\\R\\result.csv", index=False,
                   encoding='euc-kr')
# utf-8, cp-949