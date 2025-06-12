from core.game import bcolors

def mostrar_intro():
    espacio = "\n"
    print(50 * espacio)
    print(bcolors.BOLD + bcolors.FAIL + "Primero vamos a ajustar la resolucion de la pantalla, este juego esta pensado para jugarlo con un tamaño de pantalla en concreto" + bcolors.ENDC)
    print("Ajusta el ancho de la pantalla para la siguiente linea:")
    print(bcolors.FAIL + "----------------------------------------------------------------------------------------------------------------------------------------" + bcolors.ENDC)

    for _ in range(10):
        print("|")
    print("Y asi de alto")
    input("  <Presiona Enter para continuar>")
    print(100 * espacio)

    print(bcolors.WARNING + "    Bienvenido al juego de Rol de Rikarpatolucas, a partir de aqui, puedes formarte como heroe, eso si... no hay vueltas atras!" +  "\n" +
          "    Solo queremos a los guerreros mas fuertes y valientes de la region de Damasco." +
          "\n\n    Si crees que es tu caso, pulsa" + bcolors.OKGREEN + bcolors.BOLD + " 1 (Adelante)" + bcolors.ENDC + bcolors.WARNING + ", te estamos esperando. Damasco necesita de heroes fuertes" +
          "\n    En caso contrario pulsa" +
          bcolors.FAIL + bcolors.BOLD + " 0 (Me Retiro)" + bcolors.ENDC + bcolors.WARNING + ", una retirada a tiempo puede ser una victoria" + bcolors.ENDC + "\n")
    print(espacio * 5 + "    " + bcolors.BOLD + "1." + bcolors.OKGREEN + " Adelante" + bcolors.ENDC)
    print( "    " + bcolors.BOLD + "0." + bcolors.FAIL + " Me Retiro" + bcolors.ENDC)
    
    val = None
    while True:
        
        choice = input("   ¿Cual es tu decision? ")
        
        if choice.isdigit():
            val = int(choice)
            break
        else:
            print(bcolors.FAIL + "   Introduce uno de los valores de las opciones" + "\n" + bcolors.ENDC)

    print(20 * espacio)
    return val

def contar_historia_post_setup():
    from core.game import bcolors
    espacio = "\n"
    print(60 * espacio)

    print(bcolors.BOLD + bcolors.FAIL + "                              UNA NUEVA AMENAZA SE AVECINA..." + bcolors.ENDC)
    print(3 * espacio)
    print("    Tras la formación del escuadrón de élite, algo oscuro comienza a manifestarse en las tierras de Damasco.")
    print("    La calma que reinaba en la región ha sido interrumpida por presencias desconocidas que emergen del abismo." + espacio)
    input("    <Presiona Enter para continuar>")
    print(60 * espacio)

    print("    " + bcolors.OKBLUE + "Zack:" + bcolors.ENDC + " Esto no es un entrenamiento cualquiera... siento que algo nos observa.")
    print("    " + bcolors.OKGREEN + "Leon:" + bcolors.ENDC + " Lo he notado también. El aire está cargado. Preparad vuestras armas.")
    print("    " + bcolors.FAIL + "Sora:" + bcolors.ENDC + " Sea lo que sea, estamos juntos en esto. ¡Por Damasco!")
    print(3 * espacio)
    input("    <Presiona Enter para continuar>")
    print(60 * espacio)

    print("    El cielo se oscurece repentinamente.")
    print("    Un rugido atraviesa las nubes como una cuchilla... una sombra titánica aparece en el horizonte.")
    print("    Las antiguas leyendas hablaban de una criatura que dormía bajo las ruinas de Midgard... ¿podría ser real?")
    print(3 * espacio)
    input("    <Presiona Enter para continuar>")
    print(60 * espacio)

    print(bcolors.FAIL + bcolors.BOLD + "                              ¡UN ENEMIGO SE ACERCA!" + bcolors.ENDC)
    print("    El suelo tiembla. De entre la tierra emerge una criatura formada de oscuridad pura: " + bcolors.FAIL + "TIAMAZT" + bcolors.ENDC)
    print("    Sus ojos brillan como carbones encendidos. Sin mediar palabra, desata una onda mágica que arrasa parte del bosque." + espacio)
    input("    <Presiona Enter para comenzar el combate>")
    print(40 * espacio)