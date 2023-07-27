# List
subway = [10,20,30]
print(subway)
subway = ["travis", "scott", "GOAT"]
print(subway.index("scott"))
subway.append("GANG")
print(subway.pop())
print(subway[2])
subway.insert(2,"Check")
print(subway[2])

numList = [5,2,7,1,3]
numList.sort()
print(numList)
numList.reverse()
print(numList)
mixList = ["boy", 20, True, False]
print(mixList)

girl = "girl"
mixList.extend([girl])
print(mixList)

# Dictionary
cabinet = {3:"gold", 5:"silver"}
print(cabinet[3])
print(cabinet.get(4,"new value"))
print(3 in cabinet)
cabinet[3] = 'bronze'
print(cabinet[3])
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
cabinet.clear()
print(cabinet)

# Tuple 
menu = ("meat", "snack")
print(menu[0])
print(menu[1])

name = "scott"
age = 20
(name, age) = ("travis", 20)
print(name)

# Set
my_set = {1,2,3,3,3}
print(my_set)
other_set = {3,4,5,6}
print(my_set & other_set) #intersection
print(my_set | other_set) #union
print(my_set.union(other_set)) #union
print(my_set.difference(other_set)) #difference
my_set.add(5)
print(my_set)
my_set.remove(5) 
print(my_set)

menu = {"coffee", "juice"}
print(menu, type(menu))
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))

#Quiz

from random import * 
users = range(1,21)
users = list(users)
print(users)
shuffle(users)
print(users)
rewards = sample(users, 4)
# print("치킨 당첨자: " + str(rewards[0]))
# print("커피 당첨자: " + str(rewards[1:4]))
print("치킨 당첨자:{0}".format(rewards[0]))
print("커피 당첨자:{0}" .format(rewards[1:]))




