#строка в обратном порядке
string = input()
abc = string.split(' ')
abc = abc[::-1]
print(abc)

#четные символы
string = str(input())  # ну либо print(input()[0::2])
i = len(string)
if i < 15:
  print('Слишком короткая строка')
else:
  gnirts = string[0::2]
  print(gnirts)

#список в степени n
ii = input()
ii = ii.split(' ')
n = int(ii[-1])
ii = ii[:-1]
ilist = []
for i in ii:
  i = int(i)
  i **= n
  ilist.append(i)
print(ilist)

#удвоинный символ
text = str(input())
simvol = text[-1]
simvol2 = simvol + simvol
text = text[:-1]
text = text.replace(simvol, simvol2)
print(text)

#количество х и у
text = input()
x = text.count('x')
y = text.count('y')
print(f'x: {x}, y: {y}')

#текст без скобок
text = input()
s1 = 1 # просто число больше 0
cut = ''
while s1 > 0:
  s1 = text.find('(') - 1
  s2 = text.find(')') + 1
  cut += text[s1 + 2: s2 - 1] + '; '
  text = text[:s1] + text[s2:]
  s1 = text.find('(')
print(text)
print(cut)
