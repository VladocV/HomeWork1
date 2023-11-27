#одинаковые города
n = int(input())
text = input().split(' ')
text = set(text)  #надеюсь, так можно...
n = (n - int(len(text))) * 2
print('Количество городов, названия которых повторяются:', n)

#заглавные буквы
text = input()
next = True
result = ''
for char in text:
  if next and char.isalpha():
    result += char.upper()
    next = False
  else:
    result += char
  if char in ['.','!','?']:
    next = True
print(result)

#анаграммы
text1, text2 = input(), input()
text1 = text1.replace(' ', '').lower()
text2 = text2.replace(' ', '').lower()
if len(text1) == len(text2):
  text = set(text1) | set(text2)
  if len(text) == len(text1):
    print('Это анаграммы!')
  else:
    print('Это не анаграммы (•_•)')
else:
  print('Разное количистово символов, это не анаграмма')

#олимпиада
task_a = input('Решившие Алгебру: ').split(' ')
task_g = input('Решившие Геометрию: ').split(' ')
task_t = input('Решившие Тригонометрию: ').split(' ')
result = ''
for surname in task_a:
  if surname in task_g and surname in task_t:
    result += surname
result = result.split()
if len(result) > 0:
  result.sort()
  print(' '.join(result))
else:
  print('Все три задачи никто не решил (•_•)')
