#. 변수
# Quiz
station = "사당"
print(station + "행 열차가 들어오고 있습니다")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다")

# 수식 
print(abs(-10)) #5
print(pow(4,2)) #4^2
print(max(5,12)) # 12

from math import *
from random import *
print(floor(4.99))
print(ceil(3.14))
print(sqrt(16))

print(random())
print(random() * 10)
print(int(random() * 10))
print(int(random() * 10)+ 1)
print(int(random() * 45) + 1)
print(randint(1,45))
print(randrange(1,46))

# Quiz
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다")

# 문자열
jumin = "990120-1234567"

print("성별: " + jumin[7])
print("연: " + jumin[0:2]) # 0부터 2직전까지
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])
print("생년월일: " + jumin[0:6])
print("생년월일: " + jumin[:6])
print("뒤 7자리: " + jumin[7:])
print(jumin[-14:])

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)
print(python.find('g'))
print(python.count("n"))

myAge = 5
print("나는 %d살입니다." %myAge)
print("나는 %s을 좋아해요" %"파이썬 ")
print("Apple은 %c로 시작해요." %"A")
print("나는 %s색과 %s색을 좋아해요." % ("파란","빨간"))
print("나는 {}살입니다.".format(50))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {age}살이며 {color}색 좋아해요".format(age = 4, color = "빨간"))
age = 20
color = "빨간"
print(f"나는 {age}살이며 {color}색 좋아해요")

print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# Quiz
# 비밀번호 만들어주는 프로그램 => url 입력시 password 자동변형
url = "http://youtube.com"
my_str = url.replace("http://", "") # 규칙 1
# print(my_str[0:3] + str(len(my_str)) + str(my_str.find("e")) + "!")
my_str = my_str[:my_str.index(".")] # 규칙 2
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" 
print("{0}의 비밀번호는 {1}입니다.".format(url, password))

# print("생성된 비밀번호 : " +  site[7:10] + site[7:12].count + "!")

