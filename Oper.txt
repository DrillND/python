num1 = 3
num2 = 4
print(type(num1))
# 산술 연산자
print('덧셈:', num1+num2)
print('곱셈:', num1*num2)
print('나머지:', num2%num1)

res = num1 + num2
print('res : ', res)
res += num1
print('res :', res)
# ++,-- 지원 안함
# res = res++
res += 1
res = res + 1

# 비교연산자
# 참, 거짓 --> True, False
print(num1>num2)
print(num1 == num2)
print(num1 != num2)

# 논리연산자
print(num1 > num2 and num1 < num2)
print(num1 > num2 or num1<num2)
print(not(num1>num2))

# 3항 연산자 다시 보기
result = (num1 > num2) and \
'num1이 num2보다 크다' or \
'num1이 num2보다 작다'
print(result)

# 문자열
str1 = '홍길동'
str2 = '입니다.'
# 문자열 연결
fullStr = str1+str2
print('문자열 연결 : ',fullStr)
fullStr = fullStr + '\n' + '안녕하세요'
# \n, \t 사용 쌉가능
print('개행문자:', fullStr)

# 문자열 인덱싱(indexing)
# 배열과 비슷함
print(str1[0], str1[1], str1[2])

# [] --> 리스트(list)
# 문자열 자르기(slicing)
fullStr = '홍길동입니다.'
print(fullStr[0:2]) # 0에서 1까지
print(fullStr[1:]) # 1에서 끝까지
print(fullStr[:3]) # 처음부터 2까지
print(fullStr[1:5:2]) # 1부터 5까지 2번째 위치만
print(fullStr[1::2]) # 1부터 끝까지 2번째 위치만

# in 연산자
search = '홍길당' in fullStr
print(search)

length = len(fullStr)
print('변수값 크기:', length)

# 입력 처리
print('1번째 숫자를 입력하세요: ')
input1 = input()
print(type(input1))
input2 = input('2번재 숫자 입력: ')
print(input2)

# 문자열->숫자
sum = input1 + input2
print('숫자 덧셈:', sum)

#int() 문자열 -> 숫자
#str() : 숫자 -> 문자열
sum = int(input1)+int(input2)
print('숫자 덧셈:', sum)
input3 = int(input('3번째 숫자 입력:'))
print(type(input3))

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

PI = 3.14
print('원의 반지름을 입력하세요 :' )
input1 = input()
print('원의 면적 : ' + type(input1*input1)*PI)



