import random
from constants import *


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
            vendor_name = random.choice(NAMEMAN) + " " + random.choice(FAMILY)
        else:
            vendor_name = random.choice(NAMEWOMAN) + " " + random.choice(FAMILY)
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


def personality_npc(personality_in_main: str) -> str:
    """
    :param personality_in_main: Если "" то Личность выбирается рандомно
    :return: Личность
    """
    npc_personality = ""
    if personality_in_main == "Случайно":
        npc_personality = random.choice(PERSONALITY)
    else:
        npc_personality = personality_in_main
    return npc_personality


def look_npc(look_in_main: str) -> str:
    """
    :param look_in_main: Если "" то Тип внешности выбирается рандомно
    :return: Тип внешности
    """
    npc_look = ""
    if look_in_main == "Случайно":
        npc_look = random.choice(LOOK)
    else:
        npc_look = look_in_main
    return npc_look


def voice_npc(voice_in_main: str) -> str:
    """
    :param voice_in_main: Если "" то Голос выбирается рандомно
    :return: Голос
    """
    npc_voice = ""
    if voice_in_main == "Случайно":
        npc_voice = random.choice(VOICE)
    else:
        npc_voice = voice_in_main
    return npc_voice

def money_vendor(vendor_money_in_main: str) -> int:
    """
    :param vendor_money_in_main: "Ужасная"/"Плохая"/"Средняя"/"Хорошая"/"Прекрасная"
    :return: Количество денег продавца
    """
    vendor_money = 0
    if vendor_money_in_main == "Ужасная":
        vendor_money += random.randint(1, 10) * 20
    elif vendor_money_in_main == "Плохая":
        vendor_money += random.randint(1, 10) * 50
    elif vendor_money_in_main == "Средняя":
        vendor_money += random.randint(1, 10) * 100
    elif vendor_money_in_main == "Хорошая":
        vendor_money += random.randint(1, 20) * 250
    elif vendor_money_in_main == "Прекрасная":
        vendor_money += random.randint(1, 30) * 500
    return vendor_money


def assortment_store(shop_type: str, shop_cost: str) -> str:
    '''
    DOCKSTRING: Присвоение ассортимента магазина в соответсвии с типом и стоймостью
    '''
    store_assortment = ""
    for i in sorted(SHOPDATA[shop_type][shop_cost]):
        store_assortment += i[0] + ": " + i[1] + "\n"
    return store_assortment
