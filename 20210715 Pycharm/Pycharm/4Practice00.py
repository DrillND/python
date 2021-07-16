#4번 실행 해보는 파일
import requests
from bs4 import BeautifulSoup
import pandas as pd


req = requests.get('http://media.daum.net/ranking/popular/')
#print(req)
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

print((result_file))
# utf-8, cp-949