count = int(input('Введите количество элементов: '))
lst = []
for i in range(0, count):
    element = int(input(f'Введите {i+1}-й элемент: '))
    lst.append(element)
print('Вывод списка: ', lst)
