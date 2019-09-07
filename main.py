#importamos las clases de game y magic
from classes.game import Person, bcolors
from classes.magic import  Spell
from classes.inventory import Item
import random

# Vamos a introducir la historia y eleccion de personajes
print(  bcolors.WARNING + "Bienvenido al juego de Rol de Rikarpatolucas, a partir de aqui, no existiran puntos de guardado ni vueltas atras, solo queremos a los guerreros mas fuertes y valientes de la region de Damasco." +
       ("\n") + "Si crees que es tu caso adelante pulsa" + bcolors.OKGREEN + bcolors.BOLD +" 0" + bcolors.ENDC+ bcolors.WARNING + ", te estamos esperando, en caso contrario pulsa" +
        bcolors.FAIL + bcolors.BOLD + " 1" +bcolors.ENDC + bcolors.WARNING +  ", una retirada a tiempo puede ser una victoria" + bcolors.ENDC)
print("\n")
firstdecision = int(input ("Cual es tu decision? "))
print ("\n")

if firstdecision == 0:


    print(bcolors.BOLD + "Muy bien Guerreo ")

    #Creamos las magias negras
    fire = Spell("Fire", 10, 150, "black")
    thunder = Spell("Thunde", 12, 180, "black")
    ice = Spell("Ice", 15, 200, "black")
    queake = Spell("Queake", 11, 160, "black")
    meteor = Spell("Meteor", 17, 210, "black")

    #Creamos las magias blancas
    cure= Spell("Cure", 10, 70, "white")
    cureP = Spell("CurePlus", 30, 600, "white")

    #Creamos los items
        #Efectos positivos
    potion = Item("Potion", "potion", "Heals 50 HP", 50)
    hipotion = Item("High-Potion","potion","Heals 100 HP", 100)
    superpotion = Item("Super Potion", "potion", "Heals 400 HP", 400)
    elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
    hielixir = Item("Elixir", "elixir", "Fully restores party's HP/MP", 9999)
        #Efectos de daño
    grenade = Item ("Grenade", "attack", "Deals 500 damage", 500)


    player_spells = [fire, thunder, ice, queake, meteor, cure, cureP]
    player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5}, {"item": superpotion, "quantity": 5},
                    {"item": elixir, "quantity": 3}, {"item": hielixir, "quantity": 1}, {"item": grenade, "quantity": 8}]
    #Personajes
    player1 = Person("Zack:", 3200, 132, 400, 34, player_spells , player_items, "no")
    player2 = Person("Leon:", 4500, 180, 400, 34, player_spells , player_items, "no")
    player3 = Person("Sora:", 3000, 166, 400, 34, player_spells , player_items, "no")

    players = [player1, player2, player3]

    enemy1 = Person("Tiamazt  ",1200, 400, 560, 25, [], [], "no")
    enemy2 = Person("Texter   ", 1250, 130, 560, 325, [], [], "no")
    enemy3 = Person("Slif     ", 1500, 150, 560, 325, [], [] , "no")
    #enemy5= Person("Sephiroth")

    allies = [player1, player2, player3]
    enemies = [ enemy1, enemy2, enemy3]
    running = True
    i = 0
    count = 0
    print("\n")








    print(bcolors.FAIL + bcolors.BOLD + "                             AN ENEMY ATTACKS!!" + bcolors.ENDC)

    #Bucle para correr el juego
    while running:
        print("                          ========================")
        print("\n")
        print("    NAME:               "+ " HP                                     "+ "MP             ")
      #Cogemos las stats de los jugadores
        for player in players:
            player.get_stats()

        print("\n")
     #Cogemos las stats de los enemigos
        for enemy in enemies:
            enemy.get_enemy_stats()
      #Vamos a ir a elegir las acciones por cada jugador
        for player in players:
            #print("\n")
            player.choose_action()

            choice = input("    Chose a action: ")
            index = int(choice) -1

            if index != 1 and index != 0 and index != 2 and index != 3:
                print("    Please take a option again: ")
                continue

            #Si es igual a 0 atacamos
            if index == 0:
                dmg = player.generate_damage()
                enemy =  player.choose_target(enemies)

                enemies[enemy].take_damge(dmg)
                print(bcolors.WARNING +"    You attacked "+ "for" , dmg , "points of damage to " +  enemies[enemy].name + bcolors.ENDC )

            #Si es igual a 1 entramos en las Magias
            elif index == 1:
                player.choose_magic()
                magic_choice= int(input("    Choose Magic: "))-1
                #Para volver atras
                if magic_choice == -1:
                    continue
                #Elegimos la magia y hacemos el daño
                spell = player.magic[magic_choice]
                magic_dmg=spell.generate_damage()

                current_mp=player.get_mp()
                print(bcolors.WARNING + "    The cost was", spell.cost, "and the  mp before attack was:" , current_mp, bcolors.ENDC)
                if spell.cost > current_mp:
                    print(bcolors.FAIL + " \n     You cant do this, no enough mana"+ bcolors.ENDC)
                    continue

                if spell.type == "white":

                    ally = player.choose_ally(allies)

                    curetotal = allies[ally].hp + magic_dmg
                    if curetotal > allies[ally].maxhp:
                        curepartial = allies[ally].maxhp - allies[ally].hp
                        allies[ally].heal(curepartial)
                        player.reduce_mp(spell.cost)
                        print(bcolors.OKBLUE + "\n    " + spell.name + " heals", str(curepartial),
                             "points of life, but not do a overheal"+ bcolors.ENDC)
                        continue

                    else:
                        allies[ally].heal(magic_dmg)
                        player.reduce_mp(spell.cost)
                        print(bcolors.OKBLUE + "\n    " + spell.name + " heals", str(magic_dmg),
                              "points of life" + bcolors.ENDC)
                        continue

                elif spell.type=="black":
                    player.reduce_mp(spell.cost)
                    enemy = player.choose_target(enemies)
                    enemies[enemy].take_damge(magic_dmg)
                    print(bcolors.OKBLUE + "\n    " + spell.name + " deals "+  str(magic_dmg), "points of damage to: " + enemies[enemy].name + bcolors.ENDC)
            #Si es igual a 2 elegimos los items
            elif index == 2:
                player.choose_item()
                item_choice = int(input("    Choose a item: ")) -1
                if player.items[item_choice]["quantity"] == 0:
                    print(bcolors.FAIL + "\n" + "    None left... " + bcolors.ENDC)
                    continue
                #Por si queremos volver atras
                if item_choice == -1:
                 magic_choice= int(input("    Choose Magic: "))-1
                 continue

                item = player_items[item_choice]["item"]
                player.items[item_choice]["quantity"] -= 1
                #Si son de tipo curacion
                if item.type == "potion":

                    ally = player.choose_ally(allies)

                    curetotal2 = allies[ally].hp + item.prop

                if spell.type == "white":

                    ally = player.choose_ally(allies)
                    if curetotal2 > allies[ally].maxhp:
                        curepartial2 = allies[ally].maxhp - allies[ally].hp
                        allies[ally].heal(curepartial2)
                        print(bcolors.OKGREEN + "\n    " + item.name + " heals for " + str(curepartial2), "HP" + bcolors.ENDC)
                    else:
                        allies[ally].heal(item.prop)
                        print(bcolors.OKGREEN + "\n    " + item.name + " heals for " + str(item.prop), "HP" + bcolors.ENDC)
                        print (bcolors.OKGREEN + "    HP " +  allies[ally].name + str(allies[ally].hp) + bcolors.ENDC)




                #Si son de tipo elixir
                if item.type == "elixir":
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(bcolors.WARNING + "\n" + item.name + " fully restores " + bcolors.OKGREEN + "Max HP " + bcolors.WARNING + "and " + bcolors.OKBLUE + "Max MP" + bcolors.ENDC )
                #Si son de tipo ataque
                if item.type == "attack":
                    enemy = player.choose_target(enemies)
                    enemies[enemy].take_damge(item.prop)
                    print(bcolors.WARNING + "\n" + item.name+ " deals: " + bcolors.FAIL + str(item.prop) + " points of damage to:_"+ enemies[enemy].name + bcolors.ENDC)
            elif index == 3:
                countpre = count
                decision = int(input ("    Are you sure? Pulse 0 for Return or 1 for continue: "))
                count =+ decision
                if countpre == count:
                    print




       #Aqui los jugadores ya han elegido y toca a los enemigos
        enemy_choice = 1
        target = random.randrange(0, 3)
        enemy_dmg = enemies[0].generate_damage()
        players[target].take_damge(enemy_dmg)
        print("\n")
        print(bcolors.FAIL + bcolors.BOLD + "    Enemy attacks for: " + str(enemy_dmg)  +" damage" + " to " + str(players[target].name)  + bcolors.ENDC + "\n")
       # print(bcolors.OKBLUE + "\n    " + spell.name + " deals " + str(magic_dmg), "points of damage to: " + enemies[enemy].name + bcolors.ENDC)

        print("-------------------------------")

        #Si los enemigos han llegado todos a cero
        if enemies[0].get_hp() ==0 and enemies[1].get_hp()==0 and enemies[2].get_hp()==0 :
           print(bcolors.OKGREEN + bcolors.BOLD + "You win" + bcolors.ENDC)
           running=False
        elif player.get_hp() == 0:
            print(bcolors.FAIL + " You loose" + bcolors.ENDC)
            running=False
else:
    print ("Vuelve cuando te sientas con fuerzas" + "\n\n" )