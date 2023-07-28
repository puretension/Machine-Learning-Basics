# 조건문
# weather = "rain"
# weather = input("weather? ")
# if weather ==  "rain" or weather == "snow":
#     print("rain!")
# elif weather == "sunny":
#     print("sunny!")
# else:
#     print("cloudy")

# temp = int(input("temperature? "))
# if temp >= 30:
#     print("So Hot")
# elif temp >= 10 and temp < 30:
#     print("Good")
# elif temp >= 0 and temp < 10:
#     print("Cold")
# else:
#     print("So cold")


#반복문
# for waitingNum in [0,1,2,3,4]:
#     print("waitingNum : {0}".format(waitingNum))

# for num in range(1,6):
#     print("num : {0}".format(num))

# stars = ["iron", "black", "hurk"]
# for a in stars:
#     print("{0}! ready".format(a))

# customer = "man"
# index = 3
# while index >= 1:
#     print("{0}, coffee ready. {1} chance ready".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("stop")


# customer = "iron"
# index = 4
# while True:
#     print("{0}, coffe ready. called you {1}times".format(customer,index)) # ctrl + c 강제종료


# customer = "scott"
# person = "unknown"

# while person != customer:
#     print("{0}, coffee ready.".format(customer))
#     person = input("your name? ")

# absent = [2,5]
# noBook = [7]
# for s in range(1,11): #1,2,3,4,5,6,7,8,9,10
#     if s in absent:
#         continue
#     elif s in noBook:
#         print("stop!")
#         break
#     print("{0}, read book!".format(s))

# #출석번호가 1,2,3,4, 앞에 100을 붙이기로함 -> 101,102,103,104...
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# # 학생 이름 길이로 변환 
# students = ["Iron man", "Thor", "Black"]
# students = [len(i) for i in students]
# print(students)

# #학생 이름 대문자로 변환
# students = ["Iron man", "Thor", "Black"]
# students = [i.upper() for i in students]
# print(students)

# Quiz
from random import * 
# customers = range(1,51)
# customers = list(customers)
# match = 0
# for i in customers:
#     idx = i
#     i = randint(5,50)
    
#     if i <= 15 and i >= 5:
#         match += 1
#         print("[O]{0}번째 손님 (소요시간 : {1}분".format(idx,i))
#     else:
#         print("[]{0}번째 손님 (소요시간 : {1}분".format(idx,i))

# print("총 탑승 승객 : {0}분".format(match))

cnt = 0
for i in range(1,51):
    time = randrange(1,51)
    if( 5 <= time <= 15):
        cnt += 1
        print("[O] {0}번째 손님 (소요시간: {1}분".format(i,time))
    else:
        print("[] {0}번째 손님 (소요시간: {1}분".format(i,time))
print("총 탑승 승객 : {0}분".format(cnt))
    
        
