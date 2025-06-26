from core.game import Person, bcolors
import random
import os
import time

def barra_estado(actual, maximo, longitud=30, color=bcolors.OKGREEN, mostrar_topes=True):
    proporción = max(0, actual) / maximo
    llenado = int(proporción * longitud)
    vacio = longitud - llenado
    barra = ""
    if mostrar_topes:
        barra += "|"
    barra += color + "█" * llenado + bcolors.ENDC
    barra += " " * vacio
    if mostrar_topes:
        barra += "|"
    return barra

def color_hp(valor, maximo):
    ratio = valor / maximo
    if ratio > 0.7:
        return bcolors.OKGREEN
    elif ratio > 0.3:
        return bcolors.WARNING
    else:
        return bcolors.FAIL

def mostrar_estado(players, enemies):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("                          ===========================")
    print(bcolors.OKGREEN + bcolors.BOLD + "                            ESTADO DE LOS JUGADORES" + bcolors.ENDC)
    print("                          ===========================\n")
    for player in players:
        indicadores = player.get_estados_abreviados()
        hp_color = color_hp(player.hp, player.maxhp)
        hp_bar = barra_estado(player.hp, player.maxhp)
        mp_bar = barra_estado(player.mp, player.maxmp, 20, color=bcolors.OKBLUE)
        print(f" {player.name.strip():<10} {indicadores}" + bcolors.OKGREEN + bcolors.BOLD + "HP" + bcolors.ENDC + f" {hp_bar} " + hp_color + f"{player.hp:>4}/{player.maxhp:<4}" + bcolors.ENDC)
        print(f"                  " + bcolors.OKBLUE + bcolors.BOLD + "MP" + bcolors.ENDC + f" {mp_bar} " + bcolors.OKBLUE + f"{player.mp:>4}/{player.maxmp:<4}" + bcolors.ENDC)
        print("")

    print("\n                          =========================")
    print(bcolors.OKGREEN + bcolors.WARNING + "                            ESTADO DE LOS ENEMIGOS" + bcolors.ENDC)
    print("                          =========================\n")
    for enemy in enemies:
        indicadores = enemy.get_estados_abreviados()
        if enemy.get_hp() == 0:
            print(f" {enemy.name.strip():<9} {indicadores}" + bcolors.FAIL + bcolors.BOLD + " HP| "  + "              KO" + bcolors.ENDC)
        else:
            bar = barra_estado(enemy.hp, enemy.maxhp, color=bcolors.FAIL)
            print(f" {enemy.name.strip():<10} {indicadores}" + bcolors.FAIL + bcolors.BOLD + "HP" + bcolors.ENDC + f"{bar} {enemy.hp:>4}/{enemy.maxhp:<4}")
    print()

def pedir_accion(player):
    while True:
        player.choose_action()
        choice = input("    Elige una acción: ")
        if not choice.isdigit():
            print(bcolors.FAIL + bcolors.BOLD + "    Elige una opción válida del menú." + bcolors.ENDC)
            time.sleep(1)
            return None
        index = int(choice)
        if index not in range(1, 5):
            print(bcolors.FAIL + bcolors.BOLD + "    Elige una opción válida del menú." + bcolors.ENDC)
            time.sleep(1)
            return None
        return index - 1

def iniciar_combate(players, player_spells, player_items):
    enemy1 = Person("Tiamazt  ", 1200, 400, 560, 25, [], [], "no")
    enemy2 = Person("Texter   ", 1250, 130, 560, 325, [], [], "no")
    enemy3 = Person("Slif     ", 1500, 150, 560, 325, [], [] , "no")
    enemies = [enemy1, enemy2, enemy3]
    allies = players
    running = True

    print("\\n" + bcolors.FAIL + bcolors.BOLD + "                             ¡LOS ENEMIGOS APARECEN!" + bcolors.ENDC)
    time.sleep(1.5)

    while running:
        mostrar_estado(players, enemies)
        print(bcolors.BOLD + bcolors.WARNING + "--- TURNO DEL JUGADOR ---" + bcolors.ENDC)
        time.sleep(1)

        for player in players:
            if player.get_hp() == 0:
                continue

            saltar_turno = player.procesar_estados()
            if saltar_turno:
                print(f"{player.name.strip()} pierde el turno.")
                time.sleep(1.5)
                continue

            while True:
                mostrar_estado(players, enemies)
                print(bcolors.BOLD + f"{player.name.strip()}" + bcolors.ENDC)
                index = pedir_accion(player)
                if index is None:
                    continue

                if index == 0:  # Attack
                    print(bcolors.WARNING + "TARGET:" + bcolors.ENDC)
                    for i, enemy in enumerate(enemies):
                        if enemy.get_hp() > 0:
                            print(f"    {i + 1}. {enemy.name.strip():<10}" +bcolors.BOLD + bcolors.FAIL +"HP" + bcolors.ENDC + \
                                  f" {barra_estado(enemy.hp, enemy.maxhp, color=bcolors.FAIL)}{enemy.hp}/{enemy.maxhp}")
                    print(bcolors.WARNING + bcolors.BOLD + "    0. Volver" + bcolors.ENDC)
                    enemy_index = int(input("    Elige target: ")) - 1
                    if enemy_index == -1 or enemies[enemy_index].get_hp() == 0:
                        continue
                    dmg = player.generate_damage()
                    enemies[enemy_index].take_damge(dmg)
                    print(bcolors.WARNING + f"    Atacas a {enemies[enemy_index].name.strip()} causando {dmg} de daño." + bcolors.ENDC)
                    time.sleep(1)
                    break

                elif index == 1:  # Magic
                    player.choose_magic()
                    magic_choice = int(input("    Elige Magia: ")) - 1
                    if magic_choice == -1:
                        continue
                    spell = player.magic[magic_choice]
                    if spell.cost > player.get_mp():
                        print(bcolors.FAIL + "    No tienes suficiente maná." + bcolors.ENDC)
                        continue
                    magic_dmg = spell.generate_damage()
                    player.reduce_mp(spell.cost)

                    if spell.type == "white":
                        for i, ally in enumerate(allies):
                            print(f"    {i + 1}. {ally.name.strip()}  HP: {ally.hp}/{ally.maxhp} {barra_estado(ally.hp, ally.maxhp)}")
                        print("    0. Return Menu")
                        ally_index = int(input("    Elige target: ")) - 1
                        if ally_index == -1:
                            continue
                        healed = min(magic_dmg, allies[ally_index].maxhp - allies[ally_index].hp)
                        allies[ally_index].heal(healed)
                        print(bcolors.OKBLUE + f"    {spell.name} cura {healed} HP a {allies[ally_index].name.strip()}" + bcolors.ENDC)
                        if spell.efecto:
                            allies[ally_index].add_estado(spell.efecto.copy())
                            print(f"{allies[ally_index].name.strip()} sufre el estado: {spell.efecto['nombre']}.")

                    elif spell.type == "black":
                        for i, enemy in enumerate(enemies):
                            if enemy.get_hp() > 0:
                                print(f"    {i + 1}. {enemy.name.strip()}  HP: {enemy.hp}/{enemy.maxhp} {barra_estado(enemy.hp, enemy.maxhp, color=bcolors.FAIL)}")
                        print("    0. Return Menu")
                        enemy_index = int(input("    Elige target: ")) - 1
                        if enemy_index == -1 or enemies[enemy_index].get_hp() == 0:
                            continue
                        enemies[enemy_index].take_damge(magic_dmg)
                        print(bcolors.OKBLUE + f"    {spell.name} inflige {magic_dmg} de daño a {enemies[enemy_index].name.strip()}" + bcolors.ENDC)
                        if spell.efecto:
                            enemies[enemy_index].add_estado(spell.efecto.copy())
                            print(f"{enemies[enemy_index].name.strip()} sufre el estado: {spell.efecto['nombre']}.")
                    time.sleep(1)
                    break

                elif index == 2:  # Items
                    player.choose_item()
                    item_choice = int(input("    Elige un ítem: ")) - 1
                    if item_choice == -1 or player.items[item_choice]["quantity"] == 0:
                        print(bcolors.FAIL + "    No quedan de ese ítem." + bcolors.ENDC)
                        continue

                    item = player.items[item_choice]["item"]
                    player.items[item_choice]["quantity"] -= 1

                    if item.type == "potion":
                        for i, ally in enumerate(allies):
                            print(f"    {i + 1}. {ally.name.strip()}  HP: {ally.hp}/{ally.maxhp} {barra_estado(ally.hp, ally.maxhp)}")
                        print("    0. Return Menu")
                        ally_index = int(input("    Elige target: ")) - 1
                        if ally_index == -1:
                            continue
                        healed = min(item.prop, allies[ally_index].maxhp - allies[ally_index].hp)
                        allies[ally_index].heal(healed)
                        print(bcolors.OKGREEN + f"    {item.name} cura {healed} HP a {allies[ally_index].name.strip()}" + bcolors.ENDC)
                        if item.efecto:
                            allies[ally_index].add_estado(item.efecto.copy())
                            print(f"{allies[ally_index].name.strip()} sufre el estado: {item.efecto['nombre']}.")

                    elif item.type == "elixir":
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                        print(bcolors.WARNING + f"    {item.name} restaura totalmente tu HP y MP." + bcolors.ENDC)

                    elif item.type == "attack":
                        for i, enemy in enumerate(enemies):
                            if enemy.get_hp() > 0:
                                print(f"    {i + 1}. {enemy.name.strip()}  HP: {enemy.hp}/{enemy.maxhp} {barra_estado(enemy.hp, enemy.maxhp, color=bcolors.FAIL)}")
                        print("    0. Return Menu")
                        enemy_index = int(input("    Elige target: ")) - 1
                        if enemy_index == -1 or enemies[enemy_index].get_hp() == 0:
                            continue
                        enemies[enemy_index].take_damge(item.prop)
                        print(bcolors.FAIL + f"    {item.name} inflige {item.prop} de daño a {enemies[enemy_index].name.strip()}" + bcolors.ENDC)
                        if item.efecto:
                            enemies[enemy_index].add_estado(item.efecto.copy())
                            print(f"{enemies[enemy_index].name.strip()} sufre el estado: {item.efecto['nombre']}.")
                    time.sleep(1)
                    break

        print("\\n" + bcolors.BOLD + bcolors.FAIL + "--- TURNO DE LOS ENEMIGOS ---" + bcolors.ENDC)
        time.sleep(1)

        for enemy in enemies:
            if enemy.get_hp() == 0:
                continue

            saltar_turno = enemy.procesar_estados()
            if saltar_turno:
                print(f"{enemy.name.strip()} está aturdido y pierde el turno.")
                time.sleep(1.5)
                continue

            vivos = [p for p in players if p.get_hp() > 0]
            if not vivos:
                break
            target = random.choice(vivos)
            dmg = enemy.generate_damage()
            target.take_damge(dmg)
            print(bcolors.FAIL + f"    {enemy.name.strip()} ataca a {target.name.strip()} causando {dmg} de daño." + bcolors.ENDC)
            time.sleep(1)
        input(bcolors.BOLD + "\nPulsa ENTER para continuar..." + bcolors.ENDC)

        if all(e.get_hp() == 0 for e in enemies):
            print(bcolors.OKGREEN + bcolors.BOLD + "    ¡Has ganado el combate!" + bcolors.ENDC)
            running = False
        elif all(p.get_hp() == 0 for p in players):
            print(bcolors.FAIL + bcolors.BOLD + "    Has sido derrotado..." + bcolors.ENDC)
            running = False