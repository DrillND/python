################################
# 원의 면적 구하는 프로그램 작성
################################
# 1.원주율PI를 저장하는 실수형 변수 생성 PI=3.14
# 2.원의 반지름 입력받기 
# 3.원이 면적 구하기(반지름*반지름*PI)

################################
# 온도 구하는 프로그램
################################
# 1.화씨 온도 입력받기 (정수)
# 2.섭씨온도 = (화씨온도 -32)/1.8
# 3.섭씨온도 출력하기

#################################
# 총점과 평균 구하는 프로그램
#################################
# 1.국어, 영어, 수학 점수 입력받기
# 2.총점과 평균값 구하고 출력하기.

# 홀수, 짝수 판단 프로그램(3항 연산자)
# 1.숫자 1개 입력
# 2.홀짝 판단하여 "홀수", "짝수" 출력하기


PI = 3.14
'''
print('원의 반지름을 입력하세요 :' )
input1 = input()
sum1 = float(input1)*float(input1)*PI
print('원의 면적 : ' + sum1)
'''

round = int(input('반지름 입력: '))
sum = round*round*PI
print('원 면적:', sum)


print('화씨 온도를 입력하세요 :' )
input2 = float(input())
sum2 = (input2-32)/1.8
print('섭씨온도 : ', sum2)
hTemp = int(input('화씨온도입력 :'))
suTemp = (hTemp - 32)/1.8
print('섭씨 온도 출력 : %.1f℃'% suTemp)

print('국어 성적을 입력하세요')
koren = input()
print('영어 성적을 입력하세요')
eng = input()
print('수학 성적을 입력하세요')
math = input()

sum = int(koren)+int(eng)+int(math)
avg = float(sum)/3

#print('총점',sum + '평균',avg)
print('총점 평균 ',sum ,avg)

kor = int(input('국어점수 입력:'))
eng = int(input('영어점수 입력:'))
math = int(input('수학점수 입력:'))

sum = kor + eng + math
avg = sum/3
print('총점:{0}, 평균{1}'.format(sum, avg))
