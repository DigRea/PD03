count = int(input('Введите количество элементов: '))
lst = []
for i in range(count):
    element = int(input(f'Введите {i+1}-й элемент: '))
    lst.append(element)
lst.sort()
print('Вывод списка: ', lst)
