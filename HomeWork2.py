#четное/нечетное
i = int(input())
if i % 2:
  print('No')
else:
  print('Yes')

#большее
i1 = float(input())
i2 = float(input())
if i1 == i2:
  print('Равные')
elif i1 > i2:
  print(i1)
else:
  print(i2)

#Шахматная клетка
ix = int(input(''))
iy = int(input(''))
if (ix + iy) % 2:
    print('YES')
else:
    print('NO')
