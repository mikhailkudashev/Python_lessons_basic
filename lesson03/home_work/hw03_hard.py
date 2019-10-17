import sys
import os
# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - 2
# Вывод: -1 1/3


def transform_fraction(str_fraction):
    """
    Функция переводит строку с дробью 1 1/3 в список с целой частью, числителем и знаменателем простой дроби
    :param str_fraction: Входнач строка формата "целая_чать числитель/знаменатель"
    :return: [знак_дроби, целая_часть, числитель, знаменатель]. Если передана только целая часть, числитель
    и знаменатель возвращают None
    """
    ceiling = None
    floor = None
    if str_fraction.rfind('/') != -1:
        # ищем знаменатель дроби
        floor = str_fraction[str_fraction.rfind('/') + 1:].strip()
        if floor.isdigit():
            floor = int(floor)
            str_fraction = str_fraction[:str_fraction.rfind('/')].strip()
        else:
            return 'Необходимо вводить цифры в знаменателе дроби'

        # ищем числитель дроби
        cut = 0
        for i in range(len(str_fraction) - 1, -1, -1):
            if str_fraction[i:].isdigit():
                ceiling = int(str_fraction[i:])
            else:
                cut = i
                break
        str_fraction = str_fraction[:cut].strip()

        if not ceiling:
            return 'Необходимо вводить цифры в числителе дроби'

    # ищем знак дроби
    if str_fraction.find('-') != -1:
        sign = str_fraction[:str_fraction.find('-') + 1]
        str_fraction = str_fraction[str_fraction.find('-') + 1:].strip()
    elif str_fraction.find('+') != -1:
        sign = str_fraction[:str_fraction.find('+') + 1]
        str_fraction = str_fraction[str_fraction.find('+') + 1:].strip()
    else:
        sign = '+'

    # Ищем целую часть дроби
    if not str_fraction:
        integer_part = 0
    else:
        if str_fraction.isdigit():
            integer_part = int(str_fraction)
        else:
            return 'Необходимо вводить цифры в целой части дроби'

    return [sign, integer_part, ceiling, floor]


def to_common_denominator(fraction_lst):
    """
    Функция приводит записи дробей в элементах входящего списка к общему знаменателю
    :param fraction_lst: список, например [['-', 1, 4, 5], ['+', 7, 2, 6]]
    :return: Список, приведенный к общему знаменателю, например [['-', 1, 24, 30], ['+', 7, 10, 30]]
    """
    floor1 = fraction_lst[0][3]
    floor2 = fraction_lst[1][3]

    if floor1 != floor2 and bool(floor1) and bool(floor2):
        # Ищем общий знаменатель и коффициент умножения
        max_floor = max(floor1, floor2)
        min_floor = min(floor1, floor2)

        if max_floor % min_floor == 0:
            ratio_min = int(max_floor / min_floor)
            ratio_max = 1
        else:
            ratio_min = max_floor
            ratio_max = min_floor

        # Привоедим дробь к общему знаменателю
        fraction_lst[0][2] = fraction_lst[0][2] * ratio_max if floor1 > floor2 else fraction_lst[0][2] * ratio_min
        fraction_lst[0][3] = fraction_lst[0][3] * ratio_max if floor1 > floor2 else fraction_lst[0][3] * ratio_min
        fraction_lst[1][2] = fraction_lst[1][2] * ratio_min if floor1 > floor2 else fraction_lst[1][2] * ratio_max
        fraction_lst[1][3] = fraction_lst[1][3] * ratio_min if floor1 > floor2 else fraction_lst[1][3] * ratio_max

    return fraction_lst


def sum_fractions(fraction_lst):
    """
    Функция производит операцию суммы (или разности, в зависимости от знака дробей)
    :param fraction_lst: список с дробями
    :return: форматированная строка вывода
    """
    divider = '/'
    floor1 = fraction_lst[0][3]
    floor2 = fraction_lst[1][3]
    ceiling1 = fraction_lst[0][2] if fraction_lst[0][2] else 0
    ceiling2 = fraction_lst[1][2] if fraction_lst[1][2] else 0

    sign1 = 1 if fraction_lst[0][0] == '+' else -1
    sign2 = 1 if fraction_lst[1][0] == '+' else -1

    if floor1 is None and floor2 is None:
        result_integer = sign1 * fraction_lst[0][1] + sign2 * fraction_lst[1][1]
        result_ceiling = ''
        divider = ''
        result_floor = ''
    else:
        result_floor = floor1 if floor1 is not None else floor2
        result_ceiling = sign1 * (fraction_lst[0][1] * result_floor + ceiling1) + sign2 * (fraction_lst[1][1] *
                                                                                           result_floor + ceiling2)
        if result_ceiling % result_floor == 0:
            result_integer = result_ceiling // result_floor
            result_ceiling = ''
            divider = ''
            result_floor = ''
        else:
            result_integer = int(result_ceiling / result_floor)
            result_ceiling -= result_integer * result_floor

            if result_integer == 0:
                result_integer = ''
            else:
                result_integer = str(result_integer) + ' '
                result_ceiling = abs(result_ceiling)

    return f'{result_integer}{result_ceiling}{divider}{result_floor}'


user_string = input('Сложить или вычесть дробь в формате n x/y:\n')
fraction_list = []

if user_string.rfind('+') != -1:
    fraction_list.append(user_string[:user_string.rfind('+')].strip())
    fraction_list.append(user_string[user_string.rfind('+'):].strip())
elif user_string.rfind('-') != -1:
    fraction_list.append(user_string[:user_string.rfind('-')].strip())
    fraction_list.append(user_string[user_string.rfind('-'):].strip())
else:
    print('Ошибка в выражении, вводите только сложение или вычитание дробей')
    sys.exit()

fraction_list[0] = transform_fraction(fraction_list[0])
fraction_list[1] = transform_fraction(fraction_list[1])

if not isinstance(fraction_list[0], list) or not isinstance(fraction_list[1], list):
    # если внутри у нас строки, значит вернулись ошибки при разборе дробей
    print(fraction_list)
    sys.exit()

fraction_list = to_common_denominator(fraction_list)

print(sum_fractions(fraction_list))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

DIR = 'data'
workers_file = 'workers'
hours_file = 'hours_of'
workers_data = []

# читаем первый файл
with open(os.path.join(DIR, workers_file), 'r', encoding='UTF-8') as f:
    read_first_line = False

    for line in f:
        if not read_first_line:
            read_first_line = True
            continue
        current_data = line.strip().split()
        workers_data.append({'Name': current_data[0], 'Surname': current_data[1], 'Salary Norm': float(current_data[2]),
                             'Position': current_data[3], 'Hours Norm': int(current_data[4])})

# Добиваем каждый словарь в списке данными по фактической выработке
with open(os.path.join(DIR, hours_file), 'r', encoding='UTF-8') as f:
    read_first_line = False

    for line in f:
        if not read_first_line:
            read_first_line = True
            continue
        current_data = line.strip().split()

        for curr_worker in workers_data:
            if curr_worker['Name'] == current_data[0] and curr_worker['Surname'] == current_data[1]:
                curr_worker['Hours Fact'] = int(current_data[2])
                pay_per_hour = curr_worker['Salary Norm']/curr_worker['Hours Norm']
                if curr_worker['Hours Norm'] >= curr_worker['Hours Fact']:
                    curr_worker['Salary Fact'] = round(curr_worker['Hours Fact'] * pay_per_hour, 2)
                else:
                    hours_diff = curr_worker['Hours Fact'] - curr_worker['Hours Norm']
                    curr_worker['Salary Fact'] = round(curr_worker['Salary Norm'] + hours_diff * pay_per_hour * 2, 2)

print(workers_data)


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

letter_list = list(map(chr, range(ord('А'), ord('Я')+1)))
fruit_dict = {letter_list[i]: [] for i in range(len(letter_list))}

DIR = 'data'
fruit_file = 'fruits.txt'
with open(os.path.join(DIR, fruit_file), 'r', encoding='UTF-8') as f:
    for line in f:
        if len(line.strip()) != 0:
            fruit_dict[line.strip()[:1].upper()].append(line.strip())

DIR = 'data/fruits'
if not os.path.isdir(DIR):
    os.makedirs(DIR)

for key, itm in fruit_dict.items():
    if len(itm) != 0:
        fruit_file = 'fruits_' + key + '.txt'

        with open(os.path.join(DIR, fruit_file), 'w', encoding='UTF-8') as f:
            for list_itm in itm:
                f.write(str(list_itm + '\n'))
