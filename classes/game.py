import random
import json
import pprint
from .magic import Spell
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items, turn):
        self.maxhp=hp
        self.hp=hp
        self.maxmp=mp
        self.mp=mp
        self.atk = atk
        self.atkl=atk -10
        self.atkh=atk +10
        self.df=df
        self.magic= magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items", "Exit (Pass)"]
        self.name = name
        self.turn = turn

    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)

    def generate_spell_damage(self,i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def take_damge(self, dmg):
        self.hp -= dmg
        if  self.hp<0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp <0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self,cost):
        self.mp -= cost

    def choose_action(self):
        i=1
        print("\n" "    "+ bcolors.BOLD + self.name + bcolors.ENDC )
        print(bcolors.OKBLUE + bcolors.BOLD + "    Actions" + bcolors.ENDC)
        for item in self.actions:
            print("    ", str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n"+  bcolors.OKBLUE + bcolors.BOLD + "    Magic" + bcolors.ENDC)
        for spell in self.magic:
            print("    ",str(i) + ":", spell.name, "(cost:", str(spell.cost) , " Damage:", str(spell.dmg) + ")" )
            i += 1

    def choose_item(self):
        i=1
        print("\n"+ bcolors.OKGREEN + bcolors.BOLD + "    ITEMS" + bcolors.ENDC)
        for item in self.items:
                print("    ", str(i) + ".", item["item"].name, ":",  item["item"].description, "(x" + str(item["quantity"]) + ")")
                i += 1
        print(("\n") + bcolors.FAIL +"     0. Return Menu" + bcolors.ENDC)

    def choose_target(self, enemies):
        i=1



        print("\n" + bcolors.FAIL + bcolors.BOLD + "     TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() !=  0:
                partial = enemy.maxhp / enemy.hp
                if partial < 2.0:
                    print("       " + str(i) + "." + enemy.name + "actually HP: " + bcolors.WARNING +
                          str(enemy.hp) +  "/" +str(enemy.maxhp) + bcolors.ENDC)
                elif partial >2.0 and  partial >0:
                    print("       " + str(i) + "." + enemy.name + "actually HP: " + bcolors.FAIL +
                          str(enemy.hp) + "/" + str(enemy.maxhp) + bcolors.ENDC)

                i +=1
        print(("\n") + bcolors.FAIL +"       0. Return Menu" + bcolors.ENDC)
        choice = int (input("    Choose target:")) -1
        return  choice

    def choose_ally(self, allies):
        i=1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "     TARGET:" + bcolors.ENDC)
        for ally in allies:
            partial = ally.hp
            partial2 = ally.maxhp
            partial3 = partial2 / partial
            if partial3  <2.0:
                print("        " + str(i) + "." + ally.name + "actually HP: "  +bcolors.WARNING + str(ally.hp) + "/" + str(ally.maxhp) + bcolors.ENDC)
                i += 1
            elif partial3 >=2.0:
                print("        "  + str(i) + "." + ally.name + " actually HP: " + bcolors.FAIL + str(ally.hp) + "/" + str(ally.maxhp) +bcolors.ENDC)
                i += 1
        print(("\n") + bcolors.FAIL +"       0. Return Menu" + bcolors.ENDC)
        choice = int(input("    Choose target:")) - 1
        return choice

    def get_enemy_stats(self):
        global hp_bar
        hp_bar =""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while bar_ticks > 0:
            hp_bar +="\u2588"
            bar_ticks -= 1

        while len(hp_bar)< 50 :
            hp_bar +=" "
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp=""

        if len(hp_string)<9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -=1
            current_hp += hp_string
        else:
            current_hp = hp_string

        if self.hp > 0:
            print("    " + bcolors.BOLD + self.name + "             " +current_hp + bcolors.FAIL  +
              "|" + hp_bar + "|" + bcolors.ENDC + "\n")
        else:
            print("    " + bcolors.BOLD + self.name + "             " + current_hp + bcolors.FAIL +
              "                        IS DEAD                                 " + bcolors.ENDC + "\n" )

    def get_stats(self):
        #Calcular las barras de vida
        hp_bar = ""
        bar_ticks= (self.hp / self.maxhp) * 100 / 4
        while bar_ticks > 0:
            hp_bar += "\u2588"
            bar_ticks -=1

        while len(hp_bar)<25:
            hp_bar += " "
        #Calcular las barras de magia
        mp_bar=""
        mp_ticks= (self.mp / self.maxmp) * 100 / 10

        while mp_ticks > 0:
            mp_bar += "\u2588"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        #Para cuadrar los espacios de la vida
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp=""
        if len(hp_string)<9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -=1
            current_hp += hp_string
        else:
            current_hp = hp_string

        # Para cuadrar los espacios de la magia
        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""
        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)

            while decreased > 0:
                current_mp += " "
                decreased -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string

        print(

            "    "+bcolors.BOLD + str(self.name) +"      " +
            current_hp + bcolors.OKGREEN + "|" + hp_bar + "|    " + bcolors.ENDC +
            current_mp + bcolors.OKBLUE + "|" + mp_bar + "|" + bcolors.ENDC)

    def save_ally(self, allies):
        data={}
        data['aliados']=[]
        for player in allies:
            data['aliados'].append({
                'name': player.name,
                'HP': player.hp,
                'MP': player.mp,
                'Atck': player.atk,
                'Df': player.df,
                'Estado': player.turn

            })

            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)

    def load_allies(self):
        print("o estamos aquisds")
        with open('data.json') as file:
            data=json.load(file)
            print("estmos aqui")
            for ally in data['aliados']:
                print('First name:', ally['name'])
                print('Last name:', ally['HP'])
                print('Age:', ally['MP'])
                print('Amount:', ally['Atck'])
                print('')