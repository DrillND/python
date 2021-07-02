#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests 
from bs4 import BeautifulSoup 
#html에서 원하는 텍스트 데이터, 이전에 CMD에서 설치를 해야함 


url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="
htmlText = requests.get(url).text

bsoup = BeautifulSoup(htmlText,"html.parser") #파서가 뭐지? 
btab = bsoup.find("table",{"class":"num midsize"})
btrs = btab.find("tbody").find_all("tr")

#칼럼명
col1 = btab.find("tr").find("th") #시도명
col2 = btab.find_all("tr")[1].find_all("th") #시도명 외 칼럼명

list = [] #모든 정보 리스트
regionlist = [] #지역 리스트

for i in btrs[1:] :
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


# In[ ]:


from tkinter import Tk, ttk, Label, Button, Text, END
#import tkinter as tk
import tkinter as tk
OptionList = [] #콤보박스 내용 리스트

for i in range(0,18):
    regionlist[i][0].text
    OptionList.append(regionlist[i][0].text)
    
    
window = tk.Tk()
# 창에 대한 속성들
window.title("보건복지부 제공")
window.geometry("700x500")
#window.resizable(0,0)
variable = tk.StringVar(window)
variable.set("시도별 선택")

opt = tk.OptionMenu(window, variable, *OptionList)
opt.config(width=15, font=('Arial', 12))
opt.place(x = 15, y = 20)


labelTest = tk.Label(text="", font=('Arial', 12), fg='black')
#labelTest.pack(side="bottom")
labelTest.place(x = 40, y = 60)

def callback(*args):
    labelTest.configure(text="지금은 {}입니다".format(variable.get()))

variable.trace("w", callback)



title = "코로나 바이러스 시도별 발생현황"
title_feature = Label(window, text = title, font = ("Arial", 15))
title_feature.pack(padx = 10, pady = 10)

label = "시도별 선택2"
label_feature = Label(window, text = label, font = ("Arial", 10))
label_feature.pack(padx = 10, pady = 1)


treeTable = ttk.Treeview(window)

treeTable["columns"] = ("1","2","3","4","5","6","7","8","9")
treeTable.column("#0", width = 20, anchor = "center" )
treeTable.column("1", width = 50, anchor = "center" )
treeTable.column("2", width = 50, anchor = "center")
treeTable.column("3", width = 50, anchor = "center")
treeTable.column("4", width = 50, anchor = "center")
treeTable.column("5", width = 50, anchor = "center")
treeTable.column("6", width = 50, anchor = "center")
treeTable.column("7", width = 50, anchor = "center")
treeTable.column("8", width = 50, anchor = "center")
treeTable.column("9", width = 50, anchor = "center")

treeTable.heading("#0", text="번호", anchor = "center")
treeTable.heading("1", text="시도명", anchor = "center")
treeTable.heading("2", text="합계", anchor = "center")
treeTable.heading("3", text="국내발생", anchor = "center")
treeTable.heading("4", text="해외유입", anchor = "center")
treeTable.heading("5", text="확진환자", anchor = "center")
treeTable.heading("6", text="격리중", anchor = "center")
treeTable.heading("7", text="격리해제", anchor = "center")
treeTable.heading("8", text="사망자", anchor = "center")
treeTable.heading("9", text="발생률", anchor = "center")

# 컬럼 먼저 생성하고 헤딩 조작해야된다. 

treeTable.place(x=10, y=80, width=650, height=400)


def setTableItem() :
    treeTable.delete(*treeTable.get_children()) # 
    for idx,item in enumerate(list) : # idx로 passengers 갯수 만큼 숫자 
        region = item['region'] #station에 딕셔너리 station의 벨류 값을 넣는다.
        col1 = item['num1']
        col2 = item['num2']
        col3 = item['num3']
        col4 = item['num4']
        col5 = item['num5']
        col6 = item['num6']
        col7 = item['num7']
        col8 = item['num8']
        treeTable.insert("",'end', iid = None, text = str(idx), values = [region, col1, col2, col3, col4, col5, col6, col7, col8])
        #(조건1, 조건2, idx 값, values값)
        

        
setTableItem()




window.mainloop() #이게 실행

