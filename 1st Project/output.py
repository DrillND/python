print('hello 뭐여 파이썬')
print('파이썬')

# 파이썬 변수 한 줄 주석

'''
여러줄
주
석
'''

# 변수 선언 및 초기화
#int n = 10;
# 터미널창 초기화 : cls
# 컴파일 언어(C,C#) 와 스크립트 언어(파이썬)

num = 10
str = '홍길동'
print(str)
print('num: ', num)
print('문자열 str: ', str)

print('숫자: %d'% num)
print('문자열: %s'% str)
PI = 3.14152
print('실수 : %.2f'% PI)
print('')
# 변수를 사용해서 아래와 동일하게 출력
#------------------------------
# 개인 주소록
#------------------------------
# 1. 이름 : 홍길동
# 2. 성별 : 남
# 3. 나이 : 20살
# 4. 주소 : 대구 동구
# 5. 취미 : 
#-------------------------------

line = '---------------'
title = '개인 주소록'
name = '조용현'
sex = '남'
age = 300
adress = '대구 북구'
hobby = '프로그래밍'

print(line)
print(title)
print(line)
print('1. 이름 : %s'%name)
print('2. 성별 : %s'%sex)
print('3. 나이 : %d'%age +'살')
print('4. 주소 :',adress)
print('4. 주소 : %s'%adress)
print('5. 취미 : %s'%hobby)
print(line)


print('이름:{0}, 성별:{1}, 나이:{2}'.format(name, sex, age))
print('이름:%s, 성별:%s, 나이:%d' %(name, sex, age))

# do while, switch 없음
# sep 구분자
print(name, sex, age, adress, sep=':!:?:')
print(name, sex, age, adress, sep='/', end='!!')



