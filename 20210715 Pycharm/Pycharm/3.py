import pandas as pd

# 원본
df2=pd.DataFrame([[90,98,85,100],[80,89,95,90],[70,95,100,90]],index=['서준','우현','인아'],columns=['수학','영어','음악','체육'])
print(df2)

print('\n')

# 행 삭제
df3=df2.drop('우현')
print(df3)

print('\n')

# 열 삭제
df4=df3.drop(['수학','체육'], axis=1)
print(df4)