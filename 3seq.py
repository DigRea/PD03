lst1 = (input(f'Введите цифры 1-го списка: ')).split(',')
lst2 = (input(f'Введите цифры 2-го списка: ')).split(',')

lst = list(set(lst1) - set(lst2))

print(lst)
