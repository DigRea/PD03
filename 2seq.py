line = input('Введите цифры через запятую: ')
if ',' in line:
    spr = ','
elif ';' in line:
    spr = ';'
else:
    spr = '/'
lst = line.split(spr)
lst = set(lst)
print(lst)
