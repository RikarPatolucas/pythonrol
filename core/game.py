import random
import json
import pprint
from .magic import Spell
espacio = "\n"
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

    def fight(self, players, enemies, allies, player_items):
        running = True
        while running:
            print(bcolors.BOLD + bcolors.WARNING + "                               TOTAL STATS")
            print("                          ========================" + bcolors.ENDC)
            print("\n")
            print("    NAME:               " + " HP                                     " + "MP             ")
            # Cogemos las stats de los jugadores
            for player in players:
                player.get_stats()

            print("\n")
            # Cogemos las stats de los enemigos
            for enemy in enemies:
                enemy.get_enemy_stats()
            # Vamos a ir a elegir las acciones por cada jugador
            for player in players:
                turn=True
                while turn:
                    i=0
                    for enemy in enemies:
                        i=+1
                    if i == 0:
                        turn=False
                        running=False
                        continue
                    input("    <Continue>")
                    print(espacio*40)
                    player.choose_action()
                    # player.load_allies()

                    choice=input("    Chose a action: ")
                    if (choice.isdigit()):
                        index = int(choice) - 1
                        if index != 1 and index != 0 and index != 2 and index != 3:
                            print("    Please take a option again: ")
                            continue
                    else:
                        print( " Please pulse the number's key")
                        continue
                    # Si es igual a 0 atacamos
                    if index == 0:
                        dmg=player.generate_damage()
                        enemy=player.choose_target(enemies)

                        if enemy != -1:
                            enemies[enemy].take_damge(dmg)
                            print(bcolors.WARNING + "    You attacked " + "for", dmg,
                                  "points of damage to " + enemies[enemy].name + bcolors.ENDC)
                            turn=False
                        if enemies[enemy].get_hp()== 0:
                                 del enemies[enemy]
                        elif enemy == -1:
                            continue

                    # Si es igual a 1 entramos en las Magias
                    elif index == 1:
                        player.choose_magic()
                        magic_choice=int(input("    Choose Magic: ")) - 1
                        # Para volver atras
                        if magic_choice == -1:
                            continue
                        # Elegimos la magia y hacemos el daño
                        spell=player.magic[magic_choice]
                        magic_dmg=spell.generate_damage()

                        current_mp=player.get_mp()
                        print(bcolors.WARNING + "    The cost was", spell.cost,
                              "and the  mp before attack was:",
                              current_mp, bcolors.ENDC)
                        if spell.cost > current_mp:
                            print(bcolors.FAIL + " \n     You cant do this, no enough mana" + bcolors.ENDC)
                            continue

                        if spell.type == "white":

                            ally=player.choose_ally(allies)

                            curetotal=allies[ally].hp + magic_dmg
                            if curetotal > allies[ally].maxhp:
                                curepartial=allies[ally].maxhp - allies[ally].hp
                                allies[ally].heal(curepartial)
                                player.reduce_mp(spell.cost)
                                print(bcolors.OKBLUE + "\n    " + spell.name + " heals", str(curepartial),
                                      "points of life, but not do a overheal" + bcolors.ENDC)
                                turn=False
                                continue

                            else:
                                allies[ally].heal(magic_dmg)
                                player.reduce_mp(spell.cost)
                                print(bcolors.OKBLUE + "\n    " + spell.name + " heals", str(magic_dmg),
                                      "points of life" + bcolors.ENDC)
                                turn=False
                                continue

                        elif spell.type == "black":
                            player.reduce_mp(spell.cost)
                            enemy=player.choose_target(enemies)
                            enemies[enemy].take_damge(magic_dmg)
                            print(bcolors.OKBLUE + "\n    " + spell.name + " deals " + str(magic_dmg),
                                  "points of damage to: " + enemies[enemy].name + bcolors.ENDC)
                            turn=False
                    # Si es igual a 2 elegimos los items
                    elif index == 2:
                        player.choose_item()
                        item_choice=int(input("    Choose a item: ")) - 1
                        if player.items[item_choice]["quantity"] == 0:
                            print(bcolors.FAIL + "\n" + "    None left... " + bcolors.ENDC)
                            continue
                        # Por si queremos volver atras
                        if item_choice == -1:
                            continue

                        item=player_items[item_choice]["item"]
                        player.items[item_choice]["quantity"]-=1
                        # Si son de tipo curacion
                        if item.type == "potion":

                            ally=player.choose_ally(allies)

                            curetotal2=allies[ally].hp + item.prop

                            if curetotal2 > allies[ally].maxhp:
                                curepartial2=allies[ally].maxhp - allies[ally].hp
                                allies[ally].heal(curepartial2)
                                print(
                                    bcolors.OKGREEN + "\n    " + item.name + " heals for " + str(curepartial2),
                                    "HP" + bcolors.ENDC)
                                turn=False
                            else:
                                allies[ally].heal(item.prop)
                                print(bcolors.OKGREEN + "\n    " + item.name + " heals for " + str(item.prop),
                                      "HP" + bcolors.ENDC)
                                print(bcolors.OKGREEN + "    HP " + allies[ally].name + str(
                                    allies[ally].hp) + bcolors.ENDC)
                                turn=False

                        # Si son de tipo elixir
                        if item.type == "elixir":
                            player.hp=player.maxhp
                            player.mp=player.maxmp
                            print(
                                    bcolors.WARNING + "\n" + item.name + " fully restores " + bcolors.OKGREEN + "Max HP " + bcolors.WARNING + "and " + bcolors.OKBLUE + "Max MP" + bcolors.ENDC)
                            turn=False
                        # Si son de tipo ataque
                        if item.type == "attack":
                            enemy=player.choose_target(enemies)
                            if enemy == -1:
                                continue
                            enemies[enemy].take_damge(item.prop)
                            print(bcolors.WARNING + "\n" + item.name + " deals: " + bcolors.FAIL + str(
                                item.prop) + " points of damage to:_" + enemies[enemy].name + bcolors.ENDC)
                            turn=False

                    elif index == 3:
                        decision=int(input("    Are you sure? Pulse 0 for Return or 1 for continue: "))
                        if decision == 1:
                            turn=False
                            continue
                        else:
                            continue
                    i=0
                    print(espacio *3)
                    for enemy in enemies:
                        enemy.get_enemy_stats()
                    for enemy in enemies:
                        i=+1
                    if i == 0:
                        turn=False
                        running= False
                        continue

            # Aqui los jugadores ya han elegido y toca a los enemigos
            enemy_choice=1
            if i !=0:
                x=i
                print(bcolors.WARNING + "    Turno del enemigo:" + bcolors.ENDC)
                input("    <Press Enter>")
                print(espacio*20)
                for enemy in enemies:
                    print(bcolors.FAIL + bcolors.BOLD + "     " + str(enemies[x].name) + " ATTACKS!!!!" +bcolors.ENDC)
                    print(espacio*2)
                    alive = True
                    while alive:
                        target=random.randrange(0, 3)
                        if players[target].get_hp()>= 0:
                            enemy_dmg=enemies[x].generate_damage()
                            alive = False
                    players[target].take_damge(enemy_dmg)
                    print("     " +bcolors.WARNING + bcolors.BOLD + str(enemies[x].name) + " attacks for: " + bcolors.FAIL + str(
                        enemy_dmg) + bcolors.WARNING + " damage" + " to " + bcolors.OKGREEN + str(players[target].name) + bcolors.ENDC + "\n")
                    print(espacio *2)
                    print(players[target].get_stats())
                    input("    <Continue>")
                    print(espacio *40)
                    x -=1
                # print(bcolors.OKBLUE + "\n    " + spell.name + " deals " + str(magic_dmg), "points of damage to: " + enemies[enemy].name + bcolors.ENDC)

            # Si los enemigos han llegado todos a cero
            if i== 0:
                print(bcolors.OKGREEN + bcolors.BOLD + "You win" + bcolors.ENDC)
                running=False
            elif player.get_hp() == 0:
                print(bcolors.FAIL + " You loose" + bcolors.ENDC)
                running=False

        return running

