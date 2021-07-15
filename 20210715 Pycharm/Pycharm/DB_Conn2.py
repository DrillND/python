import requests
from bs4 import BeautifulSoup
import pandas as pd
import pymysql
from sqlalchemy import create_engine

db = pymysql.connect(user = 'root', host = 'localhost', passwd = '1234', port = 3306, db = 'ng')
cursor = db.cursor()

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

file = pd.DataFrame({'뉴스제목':lst2, '언론사':lst1})
file.columns = ['title', 'comp']
engine = create_engine("mysql+pymysql://root:1234@localhost/ng")
conn = engine.connect()
file.to_sql(name = "ranking", con = engine)

conn.close()