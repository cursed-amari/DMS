import re
import random


class Enemy:
    def __init__(self, name, hp, initiative, num, token, data):
        self.name = name
        self.hp = hp
        self.initiative = initiative
        self.data = data
        self.token = token
        self.num = num
        self.generating_monster = False
        self.name = self.name.replace(str(self.num), "")
        if self.name in self.data.keys():
            self.generating_monster = True
            args = self.data.get(self.name)
            self.ac = args.get("ac")
            self.hp = args.get("hit")
            self.speed = args.get("speed")
            self.strength = args.get("str")
            self.dexterity = args.get("dex")
            self.constitution = args.get("con")
            self.intelligence = args.get("int")
            self.wisdom = args.get("wis")
            self.charisma = args.get("cha")
            self.skill = args.get("skill")
            self.sense = args.get("sense")
            self.immun_damage = args.get("immun_damage")
            self.immun_constitution = args.get("immun_constitution")
            self.saving_throws = args.get("saving_throws")
            self.language = args.get("language")
            self.danger = args.get("danger")
            self.exp = args.get("exp")
            self.mastery = args.get("mastery")
            self.ability = args.get("ability")
            self.actions = args.get("actions")
            self.description = args.get("description")

        self.name += str(self.num)

        self.app_func()

    def __str__(self) -> str:
        return self.name

    def app_func(self):
        if self.generating_monster:
            self.__counting_hp()
            self.__counting_stats()

    def __counting_hp(self):
        if re.search(r"(\d)к(\d*) \+ (\d*)", str(self.hp)):
            split_hp = re.split(r"(\d)к(\d*) \+ (\d*)", str(self.hp))
            hp = 0
            for i in range(int(split_hp[2])):
                hp += random.randint(0, int(split_hp[1]))
            self.hp = hp + int(split_hp[3])
        else:
            split_hp = re.split(r"(\d)к(\d*)", str(self.hp))
            hp = 0
            for i in range(int(split_hp[1])):
                hp += random.randint(1, int(split_hp[2]))
            self.hp = hp

    def __counting_stats(self):
        self.strength = int(re.split(r"(\d*)([+-]\d*)", self.strength)[2])
        self.dexterity = int(re.split(r"(\d*)([+-]\d*)", self.dexterity)[2])
        self.constitution = int(re.split(r"(\d*)([+-]\d*)", self.constitution)[2])
        self.intelligence = int(re.split(r"(\d*)([+-]\d*)", self.intelligence)[2])
        self.wisdom = int(re.split(r"(\d*)([+-]\d*)", self.wisdom)[2])
        self.charisma = int(re.split(r"(\d*)([+-]\d*)", self.charisma)[2])

    def get_modifier_initiative(self):
        if self.initiative == "":
            return self.dexterity
        else:
            return self.initiative

    def get_initiative(self) -> int:
        if self.generating_monster:
            return random.randint(1, 20) + self.dexterity
        else:
            return random.randint(1, 20) + self.initiative

    def get_save_stats(self):
        return self.name, self.hp, self.initiative, self.num, self.token

