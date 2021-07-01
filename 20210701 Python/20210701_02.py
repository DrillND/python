#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests 
from bs4 import BeautifulSoup #html에서 원하는 텍스트 데이터, 이전에 CMD에서 설치를 해야함 

url = "http://www.kric.go.kr/jsp/industry/rss/citystapassList.jsp?q_org_cd=A010010024&q_fdate=2021"
#url은 변수명(변경가능)
htmlText = requests.get(url).text #겟방식으로 불러오기

bsoup = BeautifulSoup(htmlText,"html.parser")
btab = bsoup.find("table",{"class":"listtbl_c100"})
btrs = btab.find("tbody").find_all("tr")

#컬럼명 가져오기
btdcols = btrs[1].find_all("td",{"class":"tdcol"})
btds = btrs[1].find_all("td")

passengers = []
 # 1부터 시작
    
for tr in btrs[1:] :
    dic = {}
    tds = tr.find_all("td")
    dic['station'] = tds[0].text
    dic['ride'] = tds[2].text
    dic['alight'] = tds[3].text
    #dic['station'] = tds[0]
    passengers.append(dic)


# In[8]:


from tkinter import Tk, ttk, Label, Button, Text, END


window = Tk()
# 창에 대한 속성들
window.title("인원관리 프로그램")
window.geometry("400x400")
window.resizable(0,0)

title = "지하철 승하차 인원관리"
title_feature = Label(window, text = title, font = ("Arial", 20))
title_feature.pack(padx = 10, pady =15)

treeTable = ttk.Treeview(window)
treeTable["columns"] = ("station","ride","alight")
treeTable.column("#0", width = 30, anchor = "center" )
treeTable.column("station", width = 50, anchor = "center")
treeTable.column("ride", width = 50, anchor = "center")
treeTable.column("alight", width = 50, anchor = "center")

treeTable.place(x=10, y=90, width=380, height=200)

treeTable.heading("#0", text="No.", anchor = "center")
treeTable.heading("station", text="역이름", anchor = "center")
treeTable.heading("ride", text="승차인원", anchor = "center")
treeTable.heading("alight", text="하차인원", anchor = "center")


def setTableItem() :
    treeTable.delete(*treeTable.get_children())
    for idx,report in enumerate(passengers) : # idx로 passengers 갯수 만큼 숫자 
        station = report['station'] 
        ride = report['ride']
        alight = report['alight']
        treeTable.insert("",'end', iid = None, text = str(idx), values = [station, ride, alight])
        
        
setTableItem()



window.mainloop() #이게 실행?


# In[ ]:




