import sys
import random
game_name = 'Bot Small Talk'

# Структара хранения данных о пользователя с вопросами, которые надо задать
player = {'name': {'question': 'Как тебя зовут?', 'answer': None},
          'age': {'question': 'Сколько тебе лет?', 'answer': None},
          'gender': {'question': 'Укажите свой пол:', 'answer': None},
          'pet_name': {'question': 'Как зовут твоего питомца?', 'answer': None},
          'love_to_play': {'question': 'Ты любишь играть? (Да/Нет):', 'answer': None},
          }

# храним русский алфавит в виде строки
rus_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# список возможных вариентов ответов на вопрос о поле
male_gender_list = ['male', 'муж', 'мужчина', 'мужской', 'м', 'мальчик', 'male', 'm']
female_gender_list = ['female', 'жен', 'женщина', 'женский', 'ж', 'девочка', 'девушка', 'female', 'f']

# Начало игры
print('Добро пожаловть в игру', game_name)

for itm in player:

    while True:
        temp = input(player[itm]['question'] + '\n')

        # Проверки на ввод возраста
        if itm == 'age':
            if temp.isdigit():
                temp = int(temp)
            else:
                print('Необходимо ввести число')
                continue

        # Проверки на ввод пола
        if itm == 'gender':
            if temp.lower() in male_gender_list:
                temp = male_gender_list[0]
            elif temp.lower() in female_gender_list:
                temp = female_gender_list[0]
            else:
                print('Необходимо указать М/Ж')
                continue

        if itm == 'love_to_play':
            if temp.lower() == 'да':
                temp = True
            else:
                print('Тогда нет смысла играть. До свидания!')
                break

        # сохнаряем ответ в структура словаря
        player[itm]['answer'] = temp
        break

if int(player['age']['answer']) < 18:
    print('Ты еще молод, до 18 нельзя играть в эту игру. Пока!')
    sys.exit()
elif int(player['age']['answer']) >= 90:
    itm_confirm = True if input('Для Вас игра может быть утомительна. '
                                'Вы уверены, что хотите сыграть? (Да/Нет)\n').lower() == 'да' else False
    if itm_confirm:
        itm_confirm = True if input('Вы точно уверены? (Да/Нет)\n').lower() == 'да' else False

    if not itm_confirm:
        print('Всего наилучшего, ' + player['name']['answer'] + '. Приходите в следующий раз!')
        sys.exit()
    else:
        print('Хорошо, тогда начнем игру')

print('Привет, ' + player['name']['answer'] + '!')

print('Я могу назвать буквы алфавита, которых нет в твоем имени.')

for itm in rus_letters:
    if itm not in player['name']['answer'].lower():
        print(itm, end=' ')

# Игра на отгадывание места числа
numbers_list = [1, 16, 2, 15, 3, 14, 4, 13, 5, 7, 8, 12, 11, 9, 10, 6]
show_list = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
print('Я задумал 16 чисел от 1 - 16 и расположил их в произвольном порядке в строке. Скажи мне, где какое.')
string_to_show = '|{show_list[0]}|{show_list[1]}|{show_list[2]}|{show_list[3]}|{show_list[4]}|{show_list[5]}' \
                 '|{show_list[6]}|{show_list[7]}|{show_list[8]}|{show_list[9]}|{show_list[10]}|{show_list[11]}' \
                 '|{show_list[12]}|{show_list[13]}|{show_list[14]}|{show_list[15]}|'
current_attempt = 1
total_attempts: int = 0
break_game = False

while not break_game:
    if show_list == numbers_list:
        print(string_to_show.format(show_list=show_list))
        print('Разгаданы все числа. Молодец!\nВсего попыток:', total_attempts)
        break

    # Загадываем позицию числа
    while True:
        guess_number = random.randint(0, 15)
        if numbers_list[guess_number] == show_list[guess_number]:
            continue
        else:
            current_attempt = 1
            break
    # Разгадываем число в загаданой позиции, пока не угадаем.
    while not break_game:
        print(string_to_show.format(show_list=show_list))

        user_answer = input('Где находится число '+ str(numbers_list[guess_number]) + ':\n')
        if user_answer.isdigit() and int(user_answer) <= 16:
            user_answer = int(user_answer)
        elif user_answer == 'exit':
            break_game = True
            print('Игра прервана')
            continue
        else:
            print('Нужно вводить число от 1 до 16')
            continue

        if numbers_list[guess_number] == numbers_list[user_answer - 1]:
            print('Верно. Угадано с попытки', current_attempt)
            total_attempts += current_attempt
            show_list[guess_number] = numbers_list[guess_number]
            break
        else:
            current_attempt += 1
            print('Неверно. Попробуйте ещё.')
            continue
