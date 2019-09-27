import sys
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

