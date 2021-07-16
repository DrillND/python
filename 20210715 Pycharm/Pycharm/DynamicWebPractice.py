#수업자료 연습
#나겸쌤 코드
from selenium import webdriver
import time

import requests
from bs4 import BeautifulSoup
import pandas as pd

browser = webdriver.Chrome('C:/Temp/chromedriver')
browser.get("https://www.naver.com/")

menus = browser.find_elements_by_css_selector('#container div ul li.category_item')
#print(menus.text.strip())
health = None
for i in menus:
    if i.text == "리빙":
        health = i
    print(i.text)
health.click()
# for i in menus :
#     print(i.text)
#print(menus)
#health.click()  # 클릭

#time.sleep(5)  # 5초 대기
#browser.quit()  # 브라우저 종료
