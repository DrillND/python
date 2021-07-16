from selenium import webdriver
import time

browser = webdriver.Chrome('C:/Temp/chromedriver')
browser.get("http://python.org")

menus = browser.find_elements_by_css_selector('#top ul.menu li')

pypi = None
for m in menus:
    if m.text == "PyPI":
        pypi = m
    print(m.text)

pypi.click()  # 클릭

time.sleep(5)  # 5초 대기
browser.quit()  # 브라우저 종료

#브라우저 드라이버가 대체 먼지? 동적페이지 찾기 위한 도구
#메뉴에 주소는 어떻게 찾은 것인지? F12
#클릭 왜 하는지? 동적이라서? 클릭을 눌렀을 때의 상태를 보고 싶은것 (동적에서 클릭을 누르기 전 후 주소가 같아서)
#동적 페이지 정적 페이지 확실한 구분법? (ppt참고, 동작했을때 주소가 안바뀌는 것 동적 페이지)