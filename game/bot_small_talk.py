import sys
print('Добро пожаловть в игру Bot Small Talk')

player = {}
player['name'] = input('Как тебя зовут?\n')
player['age'] = int(input('Сколько тебе лет?\n'))

male_gender_list = ['муж', 'мужчина', 'мужской', 'м', 'мальчик', 'male', 'm']
female_gender_list = ['жен', 'женщина', 'женский', 'ж', 'девочка', 'девушка', 'female', 'f']

itm_gender = input('Укажите свой пол:\n').lower()

if itm_gender in male_gender_list:
    player['gender'] = 'male'
elif itm_gender in female_gender_list:
    player['gender'] = 'female'
else:
    player['gender'] = itm_gender

player['pet_name'] = input('Как зовут твоего питомца?\n')
player['love_to_play'] = True if input('Ты любишь играть? (Да/Нет):\n').lower() == 'да' else False

if player['age'] < 18:
    print('Ты еще молод, до 18 нельзя играть в эту игру. Пока!')
    sys.exit()
elif player['age'] >= 90:
    itm_confirm = True if input('Для Вас игра может быть утомительна. '
                                'Вы уверены, что хотите сыграть? (Да/Нет)\n').lower() == 'да' else False
    if itm_confirm:
        itm_confirm = True if input('Вы точно уверены? (Да/Нет)\n').lower() == 'да' else False

    if not itm_confirm:
        print('Всего наилучшего, ' + player['name'] + '. Приходите в следующий раз!')
        sys.exit()
    else:
        print('Хорошо, тогда начнем игру')

print('Привет, ' + player['name'] + '!')

print('Я могу назвать буквы алфавита, которых нет в твоем имени.')
rus_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for itm in rus_letters:
    if itm not in player['name'].lower():
        print(itm, end=' ')
