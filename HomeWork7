#сложение списков
list1, list2 = input().split(), input().split()
print(list(map(lambda x, y: int(x) + int(y), list1, list2)))

#ИСПРАВЛЕННО: сложение списков
list1, list2 = input().split(), input().split()
list1, list2 = list(map(int, list1)), list(map(int, list2))
num = list(map(lambda x, y: x + y, list1, list2))
if len(list1) > len(list2):
  num += list1[len(list2):]
elif len(list2) > len(list1):
  num += list2[len(list1):]
print(num)

#кратные 12 и 13
numbers = input().split()
print(list(filter(lambda x: int(x) % 12 == 0 or int(x) % 13 == 0, numbers)))

#наибольший элемент списка
from functools import reduce
nums = input().split()
print(str(reduce(lambda x, y = 0: y if x < y else x, nums)))
