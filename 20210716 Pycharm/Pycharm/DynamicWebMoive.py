import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time

tlist = []
elist = []

browser = webdriver.Chrome('C:/Temp/chromedriver')
browser.get("https://www.lottecinema.co.kr/NLCHS/Movie/List?flag=5")
browser.implicitly_wait(3)

# 메뉴 선택 - 예매순
menu = browser.find_elements_by_css_selector('#contents div ul li a')
scd = None
for m in menu:
    if m.text == "예매순":
        mv = m
    #print(t.text)
mv.click()  # 클릭

ck = None
while True:
    try:
        sp = browser.find_elements_by_css_selector('#contents div button span')
        for i in sp :
            if i.text == '펼쳐보기':
                ck = i
        ck.click()
    except:
        break


# 영화 제목
title = browser.find_elements_by_css_selector('#contents div ul li.screen_add_box div.btm_info strong')
movie = None
for t in title :
    if t == 'tit_info':
        movie = t
   #print(t.text)
    tlist.append(t.text)
print(tlist)

# 예매율
em = browser.find_elements_by_css_selector('#contents div ul li div span span em')
per = None
for t in em:
    if t == 'tit_info':
        per = t
    #print(t.text)
    elist.append(t.text)

dict_data = zip(tlist, elist)
data = pd.DataFrame(dict_data, columns=['title', 'percent'])
print(data)

time.sleep(5)  # 5초 대기
browser.quit()  # 브라우저 종료