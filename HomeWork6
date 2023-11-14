#палиндром
def revers():
  text = input()
  text.lower
  text = text.replace('.','').replace(',','').replace(' ','')
  text2 = text[::-1]
  if text == text2:
    b00l = True
  else:
    b00l = False
  print(b00l)
revers()

#ФИО, год, регестрация
def registr():
  name = input('Имя Фамилия Отчество: ') #это если в порядке ИФО, а если ФИО, то просто:
  age = int(input())                     #print(name, 2023 - age, 'г.р. зарегистрирован')
  age = 2023 - age
  name = name.split()
  name = name[1] +' '+ name[0] +' '+ name[2]
  print(name, age, 'г.р. зарегистрирован')
registr()

#наибольшее из 2/3 
def maximum(a,b,c=0):
  if a == b == c:
    print('Все числа одинаковые')
  elif a > b and a > c:
    print(a)
  elif b > a and b > c:
    print(b)
  elif c > b and c > a:
    print(c)
  else:
    print('два одинаковых наибольших числа')
a, b, c = int(input()),int(input()),(input())
if len(c) > 0:
  c = int(c)
  maximum(a,b,c)
else:
  maximum(a,b)
