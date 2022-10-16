my_dict = {
    'Charapter': {
        'HP': 3,
        'spell_slot': {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0
        },
        'initiative': 0
    }
}
print(my_dict)
print(my_dict['Charapter']['initiative'])

charapter_dict = {}
while True:
    request_hero = input('Хотите добавить героя?')
    if request_hero == 'y':
        name = input('Ваше имя?')
        charapter_dict.update({
    name: {
        'HP': 0,
        'spell_slot': {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0
        },
        'initiative': 0
    }
})
        hp = int(input('Ваше здоровье?'))
        charapter_dict[name]['HP'] = hp
        spell = input('У вас есть ячейки заклинаний?')
        if spell == 'y':
            x = input('Введите по порядку количество ваших ячеек от первого до 9 уровня')
            charapter_dict[name]['spell_slot'][1] = x[0]
            charapter_dict[name]['spell_slot'][2] = x[1]
            charapter_dict[name]['spell_slot'][3] = x[2]
            charapter_dict[name]['spell_slot'][4] = x[3]
            charapter_dict[name]['spell_slot'][5] = x[4]
            charapter_dict[name]['spell_slot'][6] = x[5]
            charapter_dict[name]['spell_slot'][7] = x[6]
            charapter_dict[name]['spell_slot'][8] = x[7]
            charapter_dict[name]['spell_slot'][9] = x[8]
        init = int(input('Ваша инициатива?'))
        charapter_dict[name]['initiative'] = init
        x = input('Ещё?')
        if x == 'y':
            continue
        else:
            print(charapter_dict)
            break

enemy_dict = {}
while True:
    request_enemy = input('Хотите добавить опонента?')
    if request_enemy == 'y':
        name = input('Ваше имя?')
        enemy_dict.update({
    name: {
        'HP': 0,
        'initiative': 0
    }
})
        hp = int(input('Ваше здоровье?'))
        enemy_dict[name]['HP'] = hp
        init = int(input('Ваша инициатива?'))
        enemy_dict[name]['initiative'] = init
        x = input('Ещё?')
        if x == 'y':
            continue
        else:
            print(enemy_dict)
            break
    else:
        break

calck_init = []

for i in charapter_dict.keys():
    calck_init.append(charapter_dict[i]['initiative'])

print(sorted(calck_init))

