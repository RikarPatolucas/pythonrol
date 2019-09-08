#importamos las clases de game y magic
from classes.game import Person, bcolors
from classes.magic import  Spell
from classes.inventory import Item
import random
import json
# Vamos a introducir la historia y eleccion de personajes
print ("\n")
print(  bcolors.WARNING + "Bienvenido al juego de Rol de Rikarpatolucas, a partir de aqui, no existiran puntos de guardado ni vueltas atras." +  ("\n") +
        "Solo queremos a los guerreros mas fuertes y valientes de la region de Damasco." +
       ("\n") + ("\n")+ "Si crees que es tu caso, escribe" + bcolors.OKGREEN + bcolors.BOLD +" Adelante" + bcolors.ENDC+ bcolors.WARNING + ", te estamos esperando. Damasco necesita de heroes fuertes"
        + ("\n") + "En caso contrario pulsa" +
        bcolors.FAIL + bcolors.BOLD + " Me Retiro" +bcolors.ENDC + bcolors.WARNING +  ", una retirada a tiempo puede ser una victoria" + bcolors.ENDC + ("\n"))
#print("\n")
firstdecision = str( input ("Cual es tu decision? "))
print ("\n")
per=0
clase = True

while clase:

    print(bcolors.BOLD + "Muy bien Guerreo ")
    print("Lo primero es explicarte las distintas clases en las que como guerrero te puedes especializar: " + "\n" )
    print(bcolors.BOLD + "    1."+ bcolors.OKGREEN + "PALADIN: " + bcolors.ENDC + bcolors.BOLD + "Guerrero especializado en las peleas cuerpo a cuerpo, gran cantidad de vida y defensa, tiene una cantidad de mana media ")
    print(bcolors.BOLD + "    2." + bcolors.OKBLUE + "MAGO: " + bcolors.ENDC + bcolors.BOLD + "Guerrero especializado en ataques magicos y potencia de ataques magicos, la cantidad de puntos magicos y mana es muy altos")
    print(bcolors.BOLD + "    3." + bcolors.FAIL + "ASESINO: " + bcolors.ENDC + bcolors.BOLD + "Guerrero especializado en hacer daño de forma elevada en sus ataques fisicos, su cantidad de vida y mana es menor")
    print("\n")
    if per ==0:
        print("     En primer lugar tenemos a Leon, mitico guerreo de la saga FF, fuerte y noble blandiendo su espada revolver. ")
        clase1 = int(input("    ¿Cual sera la clase de Leon? "))

        if clase1 == 2:
            vit1= 3000
            mp1 = 400
            atk1=110
            def1=70
        elif clase1 == 1:
            vit1=4500
            mp1=189
            atk1=220
            def1=120
        elif clase1 == 2:
            vit1=2400
            mp1=80
            atk1=400
            def1=90



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
    player2 = Person("Leon:", vit1, mp1, atk1, def1, player_spells , player_items, "no")
    player3 = Person("Sora:", 3100, 166, 400, 34, player_spells , player_items, "no")

    players = [player1, player2, player3]

    enemy1 = Person("Tiamazt  ",1200, 400, 560, 25, [], [], "no")
    enemy2 = Person("Texter   ", 1250, 130, 560, 325, [], [], "no")
    enemy3 = Person("Slif     ", 1500, 150, 560, 325, [], [] , "no")
    #enemy5= Person("Sephiroth")

    allies = [player1, player2, player3]
    enemies = [ enemy1, enemy2, enemy3]
    running = True
    turn = True
    i = 0
    count = 0
    print("\n")



    prueba = int(input( " prueba 1 "))
    if prueba == 1:
        for player in players:
            player.save_ally(allies)

    countP = 0
    with open('data.json') as file:
        data=json.load(file)

    for player in players:
        for ally in data['aliados']:
            if player.name == ally['name']:
                countP +=1
        if countP == 3:
          print("Parece que hay una partida guardada.")
          print("    1. Quiero reaundarla")
          print("    2. Quiero empezar una de nuevo")
          empezar= int(input("    ¿Cual es tu decision?"))
          if empezar == 1:
              for ally in data['aliados']:
                  if player.name == ally['name']:
                      player.hp = ally['HP']

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
            turn= True
            while turn:

                player.choose_action()
                #player.load_allies()

                choice=input("    Chose a action: ")
                index=int(choice) - 1

                if index != 1 and index != 0 and index != 2 and index != 3:
                    print("    Please take a option again: ")
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
                    print(bcolors.WARNING + "    The cost was", spell.cost, "and the  mp before attack was:",
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
                            print(bcolors.OKGREEN + "\n    " + item.name + " heals for " + str(curepartial2),
                                  "HP" + bcolors.ENDC)
                            turn=False
                        else:
                            allies[ally].heal(item.prop)
                            print(bcolors.OKGREEN + "\n    " + item.name + " heals for " + str(item.prop),
                                  "HP" + bcolors.ENDC)
                            print(bcolors.OKGREEN + "    HP " + allies[ally].name + str(allies[ally].hp) + bcolors.ENDC)
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