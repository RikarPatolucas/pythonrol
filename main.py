from engine.story import mostrar_intro, contar_historia_post_setup
from engine.setup import crear_personajes
from engine.battle import iniciar_combate
def main():
    val = mostrar_intro()
    if val == 1:
        print("Has decidido continuar la aventura...")
        contar_historia_post_setup()
        # Importar las funciones necesarias para crear personajes
        players, player_spells, player_items = crear_personajes()
        iniciar_combate(players, player_spells, player_items)
    else:
        print("Vuelve cuando te sientas con fuerzas.\n")

if __name__ == "__main__":
    main()