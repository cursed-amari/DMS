import random
from generators_data import *
from shop_data import *


def sex_npc(npc_sex_in_main: str) -> str:
    """
    :param npc_sex_in_main: Если "" то пол выбирается рандомно
    :return: Пол
    """
    vendor_sex = ""
    if npc_sex_in_main == "Случайно":
        sex = ["Мужчина", "Женщина"]
        vendor_sex = random.choice(sex)
    else:
        vendor_sex = npc_sex_in_main
    return vendor_sex


def name_npc(sex_npc_in_main: str, npc_name_in_main: str) -> str:
    """
    :param sex_npc_in_main: Мужчина/Женщина
    :param npc_name_in_main: Если "" то имя выбирается рандомно
    :return: Полное имя в соответствии с полом
    """
    vendor_name = ""
    if npc_name_in_main == "":
        if sex_npc_in_main == "Мужчина":
            vendor_name = random.choice(name_man) + " " + random.choice(family)
        else:
            vendor_name = random.choice(name_woman) + " " + random.choice(family)
    else:
        vendor_name = npc_name_in_main
    return vendor_name


def age_npc(age_npc_in_main: str) -> str:
    """
    :param age_npc_in_main: Если "" то возраст выбирается рандомно
    :return: Возраст
    """
    vendor_age = ""
    if age_npc_in_main == "Случайно":
        age = ["Молодой", "Средний", "Пожилой"]
        vendor_age = random.choice(age)
    else:
        vendor_age = age_npc_in_main
    return vendor_age


def race_npc(race_npc_in_main: str) -> str:
    """
    :param race_npc_in_main: Если "" то расса выбирается рандомно
    :return: Расса
    """
    vendor_race = ""
    if race_npc_in_main == "Случайно":
        vendor_race = random.choice(["Человек",
                                     "Дварф",
                                     "Эльф",
                                     "Полу-эльф",
                                     "Орк",
                                     "Полу-орк",
                                     "Полурослик",
                                     "Драконорождённый",
                                     "Табакси",
                                     "Тифлинг"])
    else:
        vendor_race = race_npc_in_main
    return vendor_race


def money_vendor(vendor_money_in_main: str) -> int:
    """
    :param vendor_money_in_main: "Ужасная"/"Плохая"/"Средняя"/"Хорошая"/"Прекрасная"
    :return: Количество денег продавца
    """
    vendor_money = 0
    if vendor_money_in_main == "Ужасная":
        vendor_money += random.randint(1, 10) * 20
    if vendor_money_in_main == "Плохая":
        vendor_money += random.randint(1, 10) * 50
    if vendor_money_in_main == "Средняя":
        vendor_money += random.randint(1, 10) * 100
    if vendor_money_in_main == "Хорошая":
        vendor_money += random.randint(1, 10) * 250
    if vendor_money_in_main == "Прекрасная":
        vendor_money += random.randint(1, 10) * 500
    return vendor_money


def assortment_store(shop_type: str, shop_cost: str) -> str:
    '''
    DOCKSTRING: Присвоение ассортимента магазина в соответсвии с типом и стоймостью
    '''
    store_assortment = ""
    if shop_type == "Таверна":
        if shop_cost == "Ужасная":
            for i in sorted(tavern_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(tavern_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(tavern_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(tavern_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(tavern_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Алкоголь и напитки":
        if shop_cost == "Ужасная":
            for i in sorted(alcohol_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(alcohol_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(alcohol_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(alcohol_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(alcohol_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Оружие":
        if shop_cost == "Ужасная":
            for i in sorted(weapon_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(weapon_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(weapon_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(weapon_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(weapon_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Доспехи (щиты)":
        if shop_cost == "Ужасная":
            for i in sorted(armor_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(armor_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(armor_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(armor_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(armor_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Еда и части животных":
        if shop_cost == "Ужасная":
            for i in sorted(eat_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(eat_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(eat_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(eat_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(eat_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Зелья, яды и травы":
        if shop_cost == "Ужасная":
            for i in sorted(poison_herbs_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(poison_herbs_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(poison_herbs_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(poison_herbs_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(poison_herbs_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Книги заклинаний":
        if shop_cost == "Ужасная":
            for i in sorted(poison_herbs_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(poison_herbs_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(poison_herbs_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(poison_herbs_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(poison_herbs_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Песни и инструменты":
        if shop_cost == "Ужасная":
            for i in sorted(music_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(music_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(music_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(music_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(music_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Религиозные товары":
        if shop_cost == "Ужасная":
            for i in sorted(religion_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(religion_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(religion_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(religion_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(religion_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Транспорт":
        if shop_cost == "Ужасная":
            for i in sorted(transport_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(transport_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(transport_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(transport_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(transport_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Животные":
        if shop_cost == "Ужасная":
            for i in sorted(beast_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(beast_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(beast_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(beast_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(beast_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Книги и карты":
        if shop_cost == "Ужасная":
            for i in sorted(book_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(book_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(book_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(book_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(book_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Цветы":
        if shop_cost == "Ужасная":
            for i in sorted(flower_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(flower_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(flower_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(flower_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(flower_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Мебель":
        if shop_cost == "Ужасная":
            for i in sorted(furniture_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(furniture_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(furniture_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(furniture_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(furniture_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Высокая мода":
        if shop_cost == "Ужасная":
            for i in sorted(fashion_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(fashion_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(fashion_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(fashion_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(fashion_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Ювелирные изделия":
        if shop_cost == "Ужасная":
            for i in sorted(jeweler_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(jeweler_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(jeweler_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(jeweler_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(jeweler_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Безделушки":
        if shop_cost == "Ужасная":
            for i in sorted(bauble_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(bauble_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(bauble_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(bauble_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(bauble_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Изделия из кожи":
        if shop_cost == "Ужасная":
            for i in sorted(leather_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(leather_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(leather_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(leather_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(leather_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Механические пр.":
        if shop_cost == "Ужасная":
            for i in sorted(mechanics_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(mechanics_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(mechanics_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(mechanics_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(mechanics_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Воровские пр.":
        if shop_cost == "Ужасная":
            for i in sorted(thief_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(thief_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(thief_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(thief_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(thief_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    elif shop_type == "Инструменты":
        if shop_cost == "Ужасная":
            for i in sorted(tools_1):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Плохая":
            for i in sorted(tools_2):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Средняя":
            for i in sorted(tools_3):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Хорошая":
            for i in sorted(tools_4):
                store_assortment += i[0] + ": " + i[1] + "\n"
        if shop_cost == "Прекрасная":
            for i in sorted(tools_5):
                store_assortment += i[0] + ": " + i[1] + "\n"
    return store_assortment
