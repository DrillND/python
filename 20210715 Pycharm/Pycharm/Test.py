#동적 크롤링 + CSV만들기 제출자료

from selenium import webdriver
import time

import requests
from bs4 import BeautifulSoup
import pandas as pd

browser = webdriver.Chrome('C:/Temp/chromedriver')
browser.get("https://www.naver.com/")

menus = browser.find_elements_by_css_selector('#container div ul li.category_item')

living = None
for i in menus:
    if i.text == "리빙":
        living = i
        #print(i.text)
living.click() #클릭
living.click() #클릭
living.click() #클릭
'''
while True:
    try:
        menus = browser.find_elements_by_css_selector('#container div ul li.category_item')
        for i in menus:
            if i.text == "리빙":
                living = i
        living.click()
    except:
        break
'''



source = browser.page_source #동적 페이지 이후의 소스 가져오는 것
#print(source)

#req = requests.get()
#html = source.text
soup = BeautifulSoup(source, 'html.parser')

#title1 = soup.select('#wrap a.theme\\_info em.theme\\_category')
# title2 = soup.select('#wrap a.theme\\_info strong.title.elss')
title1 = soup.select('#container div ul li.theme_item a strong')
title2 = soup.select('#container div ul li.theme_item a em')
#for i in title1 :
 #   print(i.text)

#print(title2)
lst1 = []
lst2 = []

for i in range(len(title2)):
     lst1.append(title1[i].text.strip())
     lst2.append(title2[i].text.strip())

result_file = pd.DataFrame({'제목':lst1, '카테고리':lst2})

print((result_file))

result_file.to_csv("C:\\Users\\KB\\Downloads\\result.csv", index=False,
                   encoding='euc-kr')

# #time.sleep(5)  # 5초 대기
# #browser.quit()  # 브라우저 종료
