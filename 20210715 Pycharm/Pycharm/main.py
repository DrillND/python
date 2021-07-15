import pandas as pd

dict_data = {'a':1,'b':2, 'c':3}
list_data = [1,2,3,4,5]

sr = pd.Series(dict_data)
print(sr[[0]])
print(sr[0])
print(sr['b'])

print(sr.index)
print(sr.values)
sr2= pd.Series(list_data)

print(sr2)

date=("사람","2021", "없음",False)
sr3=pd.Series(date, index =['이름','생년월일','성별','학생여부'])
print(sr3['생년월일'])
