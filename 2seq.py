line = input('Введите цифры через запятую: ')
if ',' in line:
    spr = ','
elif ';' in line:
    spr = ';'
else:
    spr = '/'
lst = line.split(spr)
res = []
for i in lst:
    if lst.count(i) == 1:
        res.append(i)
print(res)
