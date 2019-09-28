# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
list_fruits = ["яблоко", "банан", "киви", "арбуз"]
for idx, itm in enumerate(list_fruits):
    print('{idx:<4}'.format(idx=str(idx + 1) + '.') + '{itm:>12}'.format(itm=itm))
# Как вместо {itm:>12} вывести len(max(list_fruits))?

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list_one = ["яблоко", "банан", "киви", "арбуз"]
list_two = ["яблоко", "арбуз"]
print(list(set(list_one).difference(set(list_two))))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
list_of_ints = [1, 2, 3, 4, 5, 6]
new_list = []
for itm in list_of_ints:
    if itm % 2 == 0:
        new_list.append(itm / 4)
    else:
        new_list.append(itm * 2)
print(new_list)