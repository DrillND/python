import requests
from bs4 import BeautifulSoup
import pandas as pd


req = requests.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=')
html = req.text
bsoup = BeautifulSoup(html, 'html.parser')
btab = bsoup.find("table",{"class":"num midsize"})
btrs = btab.find("tbody").find_all("tr")


lst1 = []
lst2 = []

for i in range(len(btrs)):
    lst1.append(btrs[i].text.strip())
    #lst2.append(newstitle[i].text.strip())
list = [] #모든 정보 리스트
regionlist = [] #지역 리스트
for i in btrs[1:]:
    dic = {}
    region = i.find_all("th")
    num = i.find_all("td")
    dic['region'] = region[0].text
    dic['num1'] = num[0].text
    dic['num2'] = num[1].text
    dic['num3'] = num[2].text
    dic['num4'] = num[3].text
    dic['num5'] = num[4].text
    dic['num6'] = num[5].text
    dic['num7'] = num[6].text
    dic['num8'] = num[7].text
    #dic['station'] = tds[0]
    list.append(dic)
    regionlist.append(region)
    print(region)
print(btrs)
#result_file = pd.DataFrame({'newstitle':lst2, 'newscomname':lst1})
#result_file.to_csv("C:\\Users\\KB\\Downloads\\result.csv", index=False,
 #                  encoding='euc-kr')


# utf-8, cp-949