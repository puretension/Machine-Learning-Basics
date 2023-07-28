# def
# def openAccount():
#     print("new bankaccount!!")
# openAccount()

# parameter
# def deposit(balance, money):
#     print("completed. you have {0}won".format(balance + money))
#     return balance + money

# deposit(10000,1000)

# def withdraw(balance, money):
#     if money > balance:
#         print("empty")
#     else:
#         print("completed. you have {0}won".format(balance - money))

# withdraw(10000,2000)

# return tuple 

# def withdrawNight(balance, money):
#     commission = 100
#     return commission, balance - money - commission
# balance = 10000
# commission, balance = withdrawNight(balance,500)
# print("commission: {0}, you have {1}".format(commission,balance))

# # primitive value
# def profile(name, age, lang):
#     print("name : {0}\nage: {1}\nlanguage: {2}".format(name,age,lang))
# profile("scott",32,"eng")
# def profile(name, age = 20, lang = "Kor"):
#     print("name : {0}\nage: {1}\nlanguage: {2}".format(name,age,lang))
# profile("james")

# keyword
# def profile(name,age,lang):
#     print(name,age,lang)

# profile(lang="Kor", name="shout", age=20)

# variable argument
# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("name: {0}\tage: {1}\t".format(name,age), end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)

# profile("gang",20,"py","c","c#","c++","swift")

# def profile(name,age,*lang):
#     print("name: {0}\tage: {1}\t".format(name,age), end=" ")
#     for i in lang:
#         print(i, end=" ")
#     print()

# profile("gang",20,"py","c","c#","c++","swift","java","javascript")

# # local variable
# gun = 10
# def checkpoint(soldiers):
#     global gun#전역 공간에 있는 gun
#     gun = gun - soldiers
#     print("left gun: {0}".format(gun))

# def checkpointRet(gun, soldiers):
#     gun = gun - soldiers
#     print("in function left gun: {0}".format(gun))
#     return gun

# print("sum of gun: {0}".format(gun))
# checkpoint(2)
# print("left sum of gun: {0}".format(gun))
# gun = checkpointRet(gun, 2)
# print("left gun: {0}".format(gun))

#Quiz

# def std_weight(height,gender):
#     if gender == "남자":
#         return height*height*22
#     else: return height * height * 21

# height = 175
# gender = "남자"
# weight = round(std_weight(height/100,gender), 2)
# print("키 {0}cm {1}의 표준체중은 {2}kg입니다.".format(height, gender, weight))

# def std_weight(h,g):
#     weight = 0
#     if(g == "M"):
#         weight = h*h*22/10000
#         print("키 {0} 남자 표준 체중은 {1}입니다.".format(h,weight))
#     else:
#         weight = h*h*21/10000
#         print("키 {0} 여자 표준 체중은 {1}입니다.".format(h,weight))

# std_weight(175,"M")
