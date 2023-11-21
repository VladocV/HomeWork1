#наименьшее кратное
def maximum():
  a, b = int(input()), int(input())
  maxAB = max(a,b)
  while True:
    if maxAB % a == 0 and maxAB % b == 0:
      return maxAB
    else:
      maxAB += 1
maximum()

#простые числа
n = int(input())
nums = []
for num in range(2, n+1):
  simple = True
  for nu in range(2, num):
    if num % nu == 0:
      simple = False
      break
  if simple == True:
    nums.append(num)
print(nums)

#делители n
n = int(input())
nums = []
for num in range(1, n+1):
  if n % num == 0:
    nums.append(num)
print(nums)
