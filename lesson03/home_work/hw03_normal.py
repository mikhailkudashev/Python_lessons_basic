# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    """
    Функция возвращаюет ряд Фибоначчи с n-элемента до m-элемента.
    :param n: начальный элемент рядя Фибоначчи
    :param m: Конечный элемент рядя Фибоначчи
    :return: Список от n до m
    """
    fib_list = []
    fib1 = fib2 = 1
    fib_list.append(fib1)
    fib_list.append(fib2)

    for i in range(1, m+1):
        if len(fib_list) == m:
            return fib_list[n - 1:m]

        fib1, fib2 = fib2, fib1 + fib2
        fib_list.append(fib2)


print(fibonacci(9, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    """
    Функция пузырьковой сортировки
    :param origin_list: входящйи список для сортировки
    :return: отсортированный список
    """
    for j in range(len(origin_list)):

        for i in range(len(origin_list) - (j + 1)):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]

    return origin_list


print(sort_to_max([[2, 10, -12, 2.5, 20, -11, 4, 4, 0]]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(filter_func, origin_list):
    """
    Функция-аналог функции filter
    :param filter_func: функция-условие для фильтра
    :param origin_list: список для фильтрации
    :return: отфильтрованный по условию список
    """
    return_list = []
    for itm in origin_list:
        if filter_func(itm):
            return_list.append(itm)
    return return_list


print(list(my_filter(len, ['', 'not null', 'bla', '', '10'])))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def is_parallelogram(*, a1, a2, a3, a4):
    """
    Функция определяем, являются ли точки с координатами вершинами параллелограмма
    :param a1: set из коррдинат вершины A1
    :param a2: set из коррдинат вершины A2
    :param a3: set из коррдинат вершины A3
    :param a4: set из коррдинат вершины A4
    :return: True, если точки являются вершинами параллелограмма, False, если не явлюятся
    """
    # находим точки середины диагонали параллелограмма между a1-a3 и a2-a4
    if list(map(lambda x, y: (x + y) / 2, a1, a3)) == list(map(lambda x, y: (x + y) / 2, a2, a4)):
        return True
    else:
        return False


print(is_parallelogram(a1=(-3, 11), a2=(12, -4), a3=(1, -7), a4=(-14, 8)))
