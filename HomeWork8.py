#максимальное из списка
def maximum(num, rezult = 0):
  if num == []:
    return rezult
  elif int(num[0]) > int(rezult):
    rezult = num[0]
    return maximum(num[1:], rezult)
  else:
    return maximum(num[1:], rezult)
print(maximum(input().split()))
