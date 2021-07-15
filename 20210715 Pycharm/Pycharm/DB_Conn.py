import pandas as pd
import pymysql
from sqlalchemy import create_engine

db = pymysql.connect(user = 'root', host = 'localhost', passwd = '1234', port = 3306, db = 'ng')# 데이터 베이스 이름 ng로 mysql에서 생성해놓고
cursor = db.cursor() #접속

f = open('C:\\Users\\KB\\Documents\\R\\result.csv')
df = pd.read_csv(f)
df.columns = ['newtitle', 'newscomname']
engine = create_engine("mysql+pymysql://root:1234@localhost/ng")
conn = engine.connect() #이게 연결
df.to_sql(name = "aaa", con = engine)#테이블 생성

conn.close()

#없어도 되는 부분, 그냥 실행.
sql = "select * from news limit 5"
pd.read_sql(sql,db)