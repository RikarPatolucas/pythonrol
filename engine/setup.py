from core.game import Person, bcolors
from core.magic import Spell
from core.inventory import Item

def crear_personajes():
    espacio = "\n"
    per = 0
    clase = True
    decision = True

    print(bcolors.BOLD + "  Muy bien Guerrero!! ")
    print("  Lo primero es explicarte y formarte como guerrero.")
    print("  En esta aventura te acompañarán 3 grandes héroes a los cuales puedes asignar distintas clases:" + espacio)
    print(bcolors.BOLD + "    1." + bcolors.OKGREEN + " PALADÍN: " + bcolors.ENDC + "Guerrero con mucha vida y defensa, maná medio.")
    print(bcolors.BOLD + "    2." + bcolors.OKBLUE + " MAGO: " + bcolors.ENDC + "Alta potencia mágica y mucho maná.")
    print(bcolors.BOLD + "    3." + bcolors.FAIL + " ASESINO: " + bcolors.ENDC + "Daño físico alto, poca vida y maná.")
    input(espacio * 5 + "<Presiona Enter para continuar>" + espacio * 2)

    # Variables para atributos
    stats = []

    # Lista de nombres
    nombres = ["Zack", "Leon", "Sora"]

    while clase:
        if per < len(nombres):
            nombre = nombres[per]
            decision = True
            print(f"{espacio * 5}Escoge una clase para {bcolors.WARNING + nombre + bcolors.ENDC}")
            while decision:
                print(bcolors.BOLD +bcolors.OKGREEN  + "    1." +  " PALADÍN"+bcolors.ENDC)
                print(bcolors.BOLD +bcolors.OKBLUE  + "    2." +  " MAGO"+bcolors.ENDC)
                print(bcolors.BOLD +bcolors.FAIL    + "    3." +  " ASESINO"+bcolors.ENDC)
                clase1 = input("    ¿Qué clase será? ")

                if clase1.isdigit():
                    clase1 = int(clase1)
                    if clase1 == 1:
                        stats.append((nombre, 3000, 400, 110, 70))
                        print(f"    Muy bien, {nombre} será un {bcolors.OKGREEN}PALADÍN{bcolors.ENDC}")
                    elif clase1 == 2:
                        stats.append((nombre, 4500, 189, 220, 120))
                        print(f"    Muy bien, {nombre} será un {bcolors.OKBLUE}MAGO{bcolors.ENDC}")
                    elif clase1 == 3:
                        stats.append((nombre, 2400, 80, 400, 90))
                        print(f"    Muy bien, {nombre} será un {bcolors.FAIL}ASESINO{bcolors.ENDC}")
                    else:
                        print("    Opción no válida.")
                        continue

                    enter = input("    <Enter para continuar> o 0 para elegir otra clase: ")
                    if enter.isdigit() and int(enter) == 0:
                        stats.pop()
                        continue
                    else:
                        per += 1
                        decision = False
                else:
                    print("    Introduce un número válido.")
        else:
            clase = False

    # Crear hechizos
    player_spells = [
        Spell("Fire", 10, 150, "black"),
        Spell("Thunder", 12, 180, "black"),
        Spell("Ice", 15, 200, "black"),
        Spell("Queake", 11, 160, "black"),
        Spell("Meteor", 17, 210, "black"),
        Spell("Cure", 10, 70, "white"),
        Spell("CurePlus", 30, 600, "white")
    ]

    # Crear items
    player_items = [
        {"item": Item("Potion", "potion", "Heals 50 HP", 50), "quantity": 15},
        {"item": Item("High-Potion", "potion", "Heals 100 HP", 100), "quantity": 5},
        {"item": Item("Super Potion", "potion", "Heals 400 HP", 400), "quantity": 5},
        {"item": Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999), "quantity": 3},
        {"item": Item("MegaElixir", "elixir", "Fully restores party's HP/MP", 9999), "quantity": 1},
        {"item": Item("Grenade", "attack", "Deals 500 damage", 500), "quantity": 8}
    ]

    # Crear personajes
    players = []
    for i, (nombre, vit, mp, atk, defense) in enumerate(stats):
        players.append(Person(nombre + ":", vit, mp, atk, defense, player_spells, player_items, "no"))

    return players, player_spells, player_items
