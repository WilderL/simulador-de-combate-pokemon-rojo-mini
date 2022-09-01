from random import randint, random
from time import sleep

# Wilder Lionel Menchú Calderón
# Proyecto 2 - Pokémon Rojo Mini

NOMBRES_Y_TIPOS_POKEMONS_BASE = [
    # Nombres de pokemon
    ["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Weedle", "Piggey", "Rattata", "Spearow", "Ekans", "Pikachu", "Sandshew", "Vulpix", "Jigglypuff", "Zubat", "Oddish", "Gloom", "Diglett", "Meowth", "Psyduck", "Mewtwo"],
    # Tipo de pokemon
    ["Planta", "Fuego", "Agua", "Bicho", "Bicho", "Volador", "Normal", "Volador", "Veneno", "Eléctrico", "Tierra", "Fuego", "Normal", "Veneno", "Planta", "Planta", "Tierra", "Normal", "Agua", "Psíquico"]
]

NUMERO_Y_ESTADISTICAS_POKEMONS_BASE = [
    # Numero del pokemon ID
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    # PS del pokemon
    [45, 39, 44, 45, 40, 40, 30, 40, 35, 35, 50, 38, 115, 40, 45, 60, 10, 40, 50, 106],
    # Atq del pokemon
    [49, 52, 48, 30, 35, 45, 56, 60, 60, 55, 75, 41, 45, 45, 50, 65, 55, 45, 52, 110],
    # Def del pokemon
    [49, 43, 65, 35, 30, 40, 35, 30, 44, 40, 85, 40, 20, 35, 55, 70, 25, 35, 48, 90],
    # Vel del pokemon
    [45, 65, 43, 45, 50, 56, 72, 70, 55, 90, 40, 65, 20, 55, 30, 40, 95, 90, 55, 130],
    # Exp. Base
    [64, 65, 66, 53, 52, 55, 57, 58, 62, 82, 93, 63, 76, 54, 78, 132, 81, 69, 80, 220]
]

NOMBRE_Y_TIPO_LISTADO_DE_MOVIMIENTOS = [
    # Nombre de los movimientos
    ["Látigo cepa", "Latigazo", "Rayo solar", "Ascuas", "Lanzallamas", "Puño fuego", "Hidrobomba", "Pistola de agua", "Rayo burbuja", "Chupa vidas", "Pin misil", "Tijera X", "Picotazo", "Pico taladro", "Tornado", "Agarre",
     "Ataque rápido", "Bomba huevo", "Vozarrón","Ácido", "Picotazo venenoso", "Residuos", "Puño trueno", "Trueno", "Rayo", "Hueso palo", "Huesomerang", "Terremoto", "Come sueños", "Bola neblina", "Resplandor"],
    # Tipo de movimiento
    ["Planta", "Planta", "Planta", "Fuego", "Fuego", "Fuego", "Agua", "Agua", "Agua", "Bicho", "Bicho", "Bicho", "Volador", "Volador", "Volador", "Normal", "Normal", "Normal", "Normal", "Veneno", "Veneno", "Veneno", "Eléctrico",
     "Eléctrico", "Eléctrico", "Tierra", "Tierra", "Tierra", "Psíquico", "Psíquico", "Psíquico"]
]

POTENCIA_PRECISION_LISTADO_DE_MOVIMIENTOS = [
    # Potencia de movimiento
    [35, 120, 120, 40, 90, 75, 120, 40, 65, 20, 14, 80, 35, 80, 40, 55, 40, 100, 90, 40, 55, 65, 75, 120, 95, 65, 50, 100, 100, 70, 70],
    # Precision de movimiento
    [100, 85, 100, 100, 100, 100, 80, 100, 100, 100, 85, 100, 100, 100, 100, 100, 100, 75, 100, 100, 100, 100, 100, 70, 100, 85, 90, 100, 100, 100, 100]
]

mi_pokemon = {
    # Datos basicos
    'id': 0,
    'nombre': "",
    'apodo': "",
    'nivel': 0,
    'experiencia_actual': 0,
    'experiencia_total': 0,
    'tipo': "",
    'movimiento_1': "",
    'movimiento_tipo_1': "",
    'precision_1': 0,
    'potencia_1': 0,
    'movimiento_2': "",
    'movimiento_tipo_2': "",
    'precision_2': 0,
    'potencia_2': 0,
    'movimiento_3': "",
    'movimiento_tipo_3': "",
    'precision_3': 0,
    'potencia_3': 0,
    'movimiento_4': "",
    'movimiento_tipo_4': "",
    'precision_4': 0,
    'potencia_4': 0,
    # Datos de combate
    'valor_inicial': 0,
    'puntos_salud': 0,
    'ataque': 0,
    'defensa': 0,
    'velocidad': 0
}


# Genera y devuelve un numero randon entre a al b
def generador_numero_random(a, b):
    return randint(a, b)


# Suspende la ejecucion por un tiempo en segundos
def pausar_temporalmente(time):
    sleep(time)


# Selecion del pokemon inicial
def seleccion_pokemon_inicial():
    while True:
        print("Pokemon inicial")
        print("1.- Bulbasuar")
        print("2.- Charmander")
        print("3.- Squirtle")
        opcion = int(input("Seleccione el pokemon inicial (1 al 3):\n"))

        if opcion >= 1 and opcion <= 3:
            while True:
                opcion1 = input("Seguro que escoger a este pokemon? Y/N\n")

                if opcion1 == 'Y':
                    pokemon_escogido(opcion)
                elif opcion1 == 'N':
                    opcion = 0

                break

            if opcion >= 1 and opcion <= 3:
                break

        else:
            print("No se a seleccionado pokemon inicial")


# se guarda el pokemon que escogio el usuario
def pokemon_escogido(opcion):
    global mi_pokemon

    for i in range(3):
        if NUMERO_Y_ESTADISTICAS_POKEMONS_BASE[0][i] == opcion:
            mi_pokemon['id'] = NUMERO_Y_ESTADISTICAS_POKEMONS_BASE[0][i]
            mi_pokemon['nombre'] = NOMBRES_Y_TIPOS_POKEMONS_BASE[0][i]

            opcion1 = input("¿Quieres poner mote al pokemon? S/N\n")

            while True:
                if opcion1 == 'S':
                    mi_pokemon['apodo'] = input("Ingrese mote:\n")
                    break
                elif opcion1 == 'N':
                    break
                else:
                    print("No a escogido una opcion")

            mi_pokemon['nivel'] = 5
            mi_pokemon['experiencia_total'] = experiencia_nivel(5)
            mi_pokemon['tipo'] = NOMBRES_Y_TIPOS_POKEMONS_BASE[1][i]

            for j in range(1, 3):
                movimiento(mi_pokemon['movimiento_1'], mi_pokemon['movimiento_2'], mi_pokemon['movimiento_3'], mi_pokemon['movimiento_4'], j, mi_pokemon, False)

            mi_pokemon['valor_inicial'] = generador_numero_random(1, 15)
            mi_pokemon['puntos_salud'] = puntos_salud(mi_pokemon['valor_inicial'], NUMERO_Y_ESTADISTICAS_POKEMONS_BASE[1][i], 5)
            mi_pokemon['ataque'] = dato_combate(mi_pokemon['valor_inicial'], NUMERO_Y_ESTADISTICAS_POKEMONS_BASE[2][i], 5)
            mi_pokemon['defensa'] = dato_combate(mi_pokemon['valor_inicial'], NUMERO_Y_ESTADISTICAS_POKEMONS_BASE[3][i], 5)
            mi_pokemon['velocidad'] = dato_combate(mi_pokemon['valor_inicial'], NUMERO_Y_ESTADISTICAS_POKEMONS_BASE[4][i], 5)

            break


# Asignacion o posible cambio de movimiento del pokemon
def movimiento(movimiento1, movimiento2, movimiento3, movimiento4, movimiento_seleccionado, pokemon, reemplazar):
    while True:
        aleatorio = generador_numero_random(0, len(NOMBRE_Y_TIPO_LISTADO_DE_MOVIMIENTOS[0]) - 1)

        if movimiento1 != NOMBRE_Y_TIPO_LISTADO_DE_MOVIMIENTOS[0][aleatorio] and movimiento2 != NOMBRE_Y_TIPO_LISTADO_DE_MOVIMIENTOS[0][aleatorio] and movimiento3 != NOMBRE_Y_TIPO_LISTADO_DE_MOVIMIENTOS[0][aleatorio] and movimiento4 != NOMBRE_Y_TIPO_LISTADO_DE_MOVIMIENTOS[0][aleatorio]:
            if reemplazar == False:
                pokemon[f'movimiento_{movimiento_seleccionado}'] = NOMBRE_Y_TIPO_LISTADO_DE_MOVIMIENTOS[0][aleatorio]
                pokemon[f'movimiento_tipo_{movimiento_seleccionado}'] = NOMBRE_Y_TIPO_LISTADO_DE_MOVIMIENTOS[1][aleatorio]
                pokemon[f'potencia_{movimiento_seleccionado}'] = POTENCIA_PRECISION_LISTADO_DE_MOVIMIENTOS[0][aleatorio]
                pokemon[f'precision_{movimiento_seleccionado}'] = POTENCIA_PRECISION_LISTADO_DE_MOVIMIENTOS[1][aleatorio]
                break

            elif reemplazar == True:
                print("Movimiento que quiere aprender:")
                print(f"Nombre: {NOMBRE_Y_TIPO_LISTADO_DE_MOVIMIENTOS[0][aleatorio]}")
                print(f"Tipo: {NOMBRE_Y_TIPO_LISTADO_DE_MOVIMIENTOS[1][aleatorio]}")
                print(f"Potencia: {POTENCIA_PRECISION_LISTADO_DE_MOVIMIENTOS[0][aleatorio]}")
                print(f"Precisión: {POTENCIA_PRECISION_LISTADO_DE_MOVIMIENTOS[1][aleatorio]}")
                print("***********************************************")

                for i in range(1, 5):
                    print(f"Movimiento {i}:")
                    print(f"Nombre: {pokemon[f'movimiento_{i}']}")
                    print(f"Tipo: {pokemon[f'movimiento_tipo_{i}']}")
                    print(f"Potencia: {pokemon[f'potencia_{i}']}")
                    print(f"Precisión: {pokemon[f'precision_{i}']}")
                    print("***********************************************")

                while True:
                    opcion = input("¿Quieres aprender el movimiento? S/N")

                    if opcion == 'S':

                        while True:
                            movimiento_seleccionado = int(input("Por cual lo quieres reemplzar: (1 al 4)"))

                            if movimiento_seleccionado >= 1 and movimiento_seleccionado <= 4:
                                pokemon[f'movimiento_{movimiento_seleccionado}'] = NOMBRE_Y_TIPO_LISTADO_DE_MOVIMIENTOS[0][aleatorio]
                                pokemon[f'movimiento_tipo_{movimiento_seleccionado}'] = NOMBRE_Y_TIPO_LISTADO_DE_MOVIMIENTOS[1][aleatorio]
                                pokemon[f'potencia_{movimiento_seleccionado}'] = POTENCIA_PRECISION_LISTADO_DE_MOVIMIENTOS[0][aleatorio]
                                pokemon[f'precision_{movimiento_seleccionado}'] = POTENCIA_PRECISION_LISTADO_DE_MOVIMIENTOS[1][aleatorio]
                                break
                        break
                    elif opcion == 'N':
                        break
                    else:
                        print("No se a ingresado opcion")


# Experiencia requerida de acuerdo a su nivel
# nivel: Nivel actual del pokemon
def experiencia_nivel(nivel):
    return int(0.8 * (nivel**3))


# Experiencia recibida al finalizar el combate si gana
# nivel: Nivel del pokemon rival
#     e: experiencia base del pokemon rival
def experiencia_recibida(nivel, e):
    return (e * nivel) / 7


# vi: valor individual de salud
# eb: estadistica base del dato de comabte respectivo
#  n: nivel actual del pokemon
def puntos_salud(vi, eb, n):
    return int(((vi + 2 * eb) * (n / 100)) + 10 + n)


# vi: valor individual del dato de comabte res[ectivo
# eb: estadistica base del dato de comabte respectivo
#  n: nivel actual del pokemon
def dato_combate(vi, eb, n):
    return int(((vi + 2 * eb) * (n / 100)) + 5)


# Genera un pokemon aleatorio para cada batalla
def generador_pokemon_enemigo(pokemon):

        id = generador_numero_random(1, 20)

        pokemon['nombre'] = NOMBRES_Y_TIPOS_POKEMONS_BASE[0][id - 1]
        pokemon['nivel'] = generador_numero_random(mi_pokemon['nivel'] - 4, mi_pokemon['nivel'] + 4)
        pokemon['tipo'] = NOMBRES_Y_TIPOS_POKEMONS_BASE[1][id - 1]
        pokemon['experiencia_base'] = NUMERO_Y_ESTADISTICAS_POKEMONS_BASE[5][id - 1]

        for j in range(1, 5):
            movimiento(pokemon['movimiento_1'], pokemon['movimiento_2'], pokemon['movimiento_3'], pokemon['movimiento_4'], j, pokemon, False)

        pokemon['valor_inicial'] = generador_numero_random(1, 15)
        pokemon['puntos_salud'] = puntos_salud(pokemon['valor_inicial'], NUMERO_Y_ESTADISTICAS_POKEMONS_BASE[1][id - 1], pokemon['nivel'])
        pokemon['ataque'] = dato_combate(pokemon['valor_inicial'], NUMERO_Y_ESTADISTICAS_POKEMONS_BASE[2][id - 1], pokemon['nivel'])
        pokemon['defensa'] = dato_combate(pokemon['valor_inicial'], NUMERO_Y_ESTADISTICAS_POKEMONS_BASE[3][id - 1], pokemon['nivel'])
        pokemon['velocidad'] = dato_combate(pokemon['valor_inicial'], NUMERO_Y_ESTADISTICAS_POKEMONS_BASE[4][id - 1], pokemon['nivel'])


# Da prioridad quien tenga mas velocidad y si tienen la misma velocidad es random quien es primero
def prioriodad(velocidad_pokemon_entrenador, velocidad_rival):
    if velocidad_pokemon_entrenador > velocidad_rival:
        return 1
    elif velocidad_rival > velocidad_pokemon_entrenador:
        return 2
    else:
        return generador_numero_random(1, 2)


def damage_salud(b, e, v, n, a, p, d):
    """
    :param b: Bonificacion en ataque si coinciden los tipos pokemon atacante, movimiento
    :param e: Efectividad del movimiento hacia el pokemon defensor
    :param v: Valor aleatorio entre 85 a 100
    :param n: Nivel del pokemon atacante
    :param a: Valor de ataque del pokemon atacante
    :param p: Valor de la potencia del movimiento del pokemon atacante
    :param d: Valor de la defensa del pokemon defensor
    :return: El daño que recibe a los puntos de salud del pokemon defensor
    """
    return int(0.01 * b * e * v * ((((0.2 * n + 1) * a * p)/(25 * d)) + 2))


def tabla_tipo(tipo_movimiento, tipo_pokemon):
    """
    :param tipo_movimiento: Tipo de movimiento del pokemon atacante
    :param tipo_pokemon: Tipo de pokemon defensor
    :return: Efectividad de la tabla de tipo
    """
    if tipo_movimiento == 'Normal':
        return 1
    elif tipo_movimiento == 'Planta':
        if tipo_pokemon == 'Planta':
            return 0.5
        if tipo_pokemon == 'Fuego':
            return 0.5
        if tipo_pokemon == 'Agua':
            return 2
        if tipo_pokemon == 'Bicho':
            return 0.5
        if tipo_pokemon == 'Volador':
            return 0.5
        if tipo_pokemon == 'Normal':
            return 1
        if tipo_pokemon == 'Veneno':
            return 0.5
        if tipo_pokemon == 'Eléctrico':
            return 1
        if tipo_pokemon == 'Tierra':
            return 2
        if tipo_pokemon == 'Psíquico':
            return 1
    elif tipo_movimiento == 'Fuego':
        if tipo_pokemon == 'Planta':
            return 2
        if tipo_pokemon == 'Fuego':
            return 0.5
        if tipo_pokemon == 'Agua':
            return 0.5
        if tipo_pokemon == 'Bicho':
            return 2
        if tipo_pokemon == 'Volador':
            return 1
        if tipo_pokemon == 'Normal':
            return 1
        if tipo_pokemon == 'Veneno':
            return 1
        if tipo_pokemon == 'Eléctrico':
            return 1
        if tipo_pokemon == 'Tierra':
            return 1
        if tipo_pokemon == 'Psíquico':
            return 1
    elif tipo_movimiento == 'Agua':
        if tipo_pokemon == 'Planta':
            return 0.5
        if tipo_pokemon == 'Fuego':
            return 2
        if tipo_pokemon == 'Agua':
            return 0.5
        if tipo_pokemon == 'Bicho':
            return 1
        if tipo_pokemon == 'Volador':
            return 1
        if tipo_pokemon == 'Normal':
            return 1
        if tipo_pokemon == 'Veneno':
            return 1
        if tipo_pokemon == 'Eléctrico':
            return 1
        if tipo_pokemon == 'Tierra':
            return 2
        if tipo_pokemon == 'Psíquico':
            return 1
    elif tipo_movimiento == 'Bicho':
        if tipo_pokemon == 'Planta':
            return 2
        if tipo_pokemon == 'Fuego':
            return 0.5
        if tipo_pokemon == 'Agua':
            return 1
        if tipo_pokemon == 'Bicho':
            return 1
        if tipo_pokemon == 'Volador':
            return 0.5
        if tipo_pokemon == 'Normal':
            return 1
        if tipo_pokemon == 'Veneno':
            return 0.5
        if tipo_pokemon == 'Eléctrico':
            return 1
        if tipo_pokemon == 'Tierra':
            return 1
        if tipo_pokemon == 'Psíquico':
            return 2
    elif tipo_movimiento == 'Volador':
        if tipo_pokemon == 'Planta':
            return 2
        if tipo_pokemon == 'Fuego':
            return 1
        if tipo_pokemon == 'Agua':
            return 1
        if tipo_pokemon == 'Bicho':
            return 2
        if tipo_pokemon == 'Volador':
            return 1
        if tipo_pokemon == 'Normal':
            return 1
        if tipo_pokemon == 'Veneno':
            return 1
        if tipo_pokemon == 'Eléctrico':
            return 0.5
        if tipo_pokemon == 'Tierra':
            return 1
        if tipo_pokemon == 'Psíquico':
            return 1
    elif tipo_movimiento == 'Veneno':
        if tipo_pokemon == 'Planta':
            return 2
        if tipo_pokemon == 'Fuego':
            return 1
        if tipo_pokemon == 'Agua':
            return 1
        if tipo_pokemon == 'Bicho':
            return 1
        if tipo_pokemon == 'Volador':
            return 1
        if tipo_pokemon == 'Normal':
            return 1
        if tipo_pokemon == 'Veneno':
            return 0.5
        if tipo_pokemon == 'Eléctrico':
            return 1
        if tipo_pokemon == 'Tierra':
            return 0.5
        if tipo_pokemon == 'Psíquico':
            return 1
    elif tipo_movimiento == 'Eléctrico':
        if tipo_pokemon == 'Planta':
            return 0.5
        if tipo_pokemon == 'Fuego':
            return 1
        if tipo_pokemon == 'Agua':
            return 2
        if tipo_pokemon == 'Bicho':
            return 1
        if tipo_pokemon == 'Volador':
            return 2
        if tipo_pokemon == 'Normal':
            return 1
        if tipo_pokemon == 'Veneno':
            return 1
        if tipo_pokemon == 'Eléctrico':
            return 0.5
        if tipo_pokemon == 'Tierra':
            return 0
        if tipo_pokemon == 'Psíquico':
            return 1
    elif tipo_movimiento == 'Tierra':
        if tipo_pokemon == 'Planta':
            return 2
        if tipo_pokemon == 'Fuego':
            return 2
        if tipo_pokemon == 'Agua':
            return 1
        if tipo_pokemon == 'Bicho':
            return 0.5
        if tipo_pokemon == 'Volador':
            return 0
        if tipo_pokemon == 'Normal':
            return 1
        if tipo_pokemon == 'Veneno':
            return 2
        if tipo_pokemon == 'Eléctrico':
            return 2
        if tipo_pokemon == 'Tierra':
            return 2
        if tipo_pokemon == 'Psíquico':
            return 1
    elif tipo_movimiento == 'Psíquico':
        if tipo_pokemon == 'Planta':
            return 1
        if tipo_pokemon == 'Fuego':
            return 1
        if tipo_pokemon == 'Agua':
            return 1
        if tipo_pokemon == 'Bicho':
            return 1
        if tipo_pokemon == 'Volador':
            return 1
        if tipo_pokemon == 'Normal':
            return 1
        if tipo_pokemon == 'Veneno':
            return 2
        if tipo_pokemon == 'Eléctrico':
            return 1
        if tipo_pokemon == 'Tierra':
            return 1
        if tipo_pokemon == 'Psíquico':
            return 0.5


def turno(atacante, defensor, movimiento):
    """
    :param atacante: Pokemon hace el movimiento
    :param defensor: Pokemon que recibe el daño
    :param movimiento: Movimiento escogido del pokemon atacante
    """
    print(f"El pokemon {atacante['nombre']} usa {atacante[f'movimiento_{movimiento}']} al pokemon {defensor['nombre']}")

    if atacante[f'precision_{movimiento}'] >= generador_numero_random(0, 100):
        if atacante['tipo'] == atacante[f'movimiento_tipo_{movimiento}']:
            bonus_tipo = 1.5
        else:
            bonus_tipo = 1

        efectividad = tabla_tipo(atacante[f'movimiento_tipo_{movimiento}'], defensor['tipo'])
        damage = damage_salud(bonus_tipo, efectividad, generador_numero_random(85, 100), atacante['nivel'], atacante['ataque'], atacante[f'potencia_{movimiento}'], defensor['defensa'])

        if random() <= 0.0625:
            damage = int(damage + damage * 0.5)
            print("Golpe Crítico")
            pausar_temporalmente(1)

        defensor['puntos_salud'] -= damage

        if efectividad == 0:
            print("Sin efecto")
        elif efectividad == 0.5:
            print("Poco eficaz")
        elif efectividad == 1:
            print("Normal")
        elif efectividad == 2:
            print("Muz eficaz")

        pausar_temporalmente(1)

    else:
        print(f"{atacante[f'movimiento_{movimiento}']} a fallado")

    pausar_temporalmente(1)


# Interfaz grafica mostrando los datos relevantes del combate
def interfaz_combate(pokemon_enemigo, pokemon_entrenador):
    print("Pokemon Enemigo")
    print(f"{pokemon_enemigo['nombre']} | Nivel: {pokemon_enemigo['nivel']}")
    print(f"Vida: {pokemon_enemigo['puntos_salud']}")
    print("-------------------------------------------------------------------------")
    print("{:>73}".format("Pokemon actual"))

    if pokemon_entrenador['apodo'] != "":
        print("{:>73}".format(f"{pokemon_entrenador['apodo']} :Apodo"))

    print("{:>73}".format(f"{pokemon_entrenador['nombre']} | Nivel: {pokemon_entrenador['nivel']}"))
    print("{:>73}".format(f"{pokemon_entrenador['puntos_salud']} :Vida"))


# a: velocidad del pokemon del entrenador
# b: velocidad del pokemon rival
def huir_combate(a, b):
    return (((a * 128) /b) + 30) % 256


# Verifica si solo aprende o pregunta para nuevo movimiento
def movimiento_nuevo():
    contador = 0
    for i in range(1, 5):
        if mi_pokemon[f'movimiento_{i}`'] == "":
            movimiento(mi_pokemon['movimiento_1'], mi_pokemon['movimiento_2'], mi_pokemon['movimiento_3'], mi_pokemon['movimiento_4'], i, mi_pokemon, False)
            break
        else:
            contador += 1

    if contador == 4:
        movimiento(mi_pokemon['movimiento_1'], mi_pokemon['movimiento_2'], mi_pokemon['movimiento_3'], mi_pokemon['movimiento_4'], 0, mi_pokemon, True)


# Verifica si puede subir el nivel el pokemon del entrenador
def subida_nivel():
    global mi_pokemon

    if mi_pokemon['experiencia_actual'] >= mi_pokemon['experiencia_total']:
        mi_pokemon['nivel'] += 1
        mi_pokemon['experiencia_actual'] -= mi_pokemon['experiencia_total']
        mi_pokemon['experiencia_total'] = experiencia_nivel(mi_pokemon['nivel'])
        mi_pokemon['puntos_salud'] = puntos_salud(mi_pokemon['valor_inicial'], NUMERO_Y_ESTADISTICAS_POKEMONS_BASE[1][mi_pokemon['id'] - 1], mi_pokemon['nivel'])
        mi_pokemon['ataque'] = dato_combate(mi_pokemon['valor_inicial'], NUMERO_Y_ESTADISTICAS_POKEMONS_BASE[2][mi_pokemon['id'] - 1], mi_pokemon['nivel'])
        mi_pokemon['defensa'] = dato_combate(mi_pokemon['valor_inicial'], NUMERO_Y_ESTADISTICAS_POKEMONS_BASE[3][mi_pokemon['id'] - 1], mi_pokemon['nivel'])
        mi_pokemon['velocidad'] = dato_combate(mi_pokemon['valor_inicial'], NUMERO_Y_ESTADISTICAS_POKEMONS_BASE[4][mi_pokemon['id'] - 1], mi_pokemon['nivel'])

        contador = mi_pokemon['nivel']

        for i in range(5, mi_pokemon['nivel'] + 1, 5):
            contador -= 5

        if contador == 0:
            movimiento_nuevo()


# Comienza el combate pokemon
def batalla():
    global mi_pokemon
    pokemon_entrenador = mi_pokemon.copy()
    pokemon_enemigo = {
        # Datos basicos
        'nombre': "",
        'nivel': 0,
        'tipo': "",
        'experiencia_base': 0,
        'movimiento_1': "",
        'movimiento_tipo_1': "",
        'precision_1': 0,
        'potencia_1': 0,
        'movimiento_2': "",
        'movimiento_tipo_2': "",
        'precision_2': 0,
        'potencia_2': 0,
        'movimiento_3': "",
        'movimiento_tipo_3': "",
        'precision_3': 0,
        'potencia_3': 0,
        'movimiento_4': "",
        'movimiento_tipo_4': "",
        'precision_4': 0,
        'potencia_4': 0,
        # Datos de combate
        'valor_inicial': 0,
        'puntos_salud': 0,
        'ataque': 0,
        'defensa': 0,
        'velocidad': 0
    }

    generador_pokemon_enemigo(pokemon_enemigo)

    # Bucle indefinido hasta que uno de los dos pokemon este debilitado
    while True:
        opcion1 = 0
        fuga_exitosa = True
        interfaz_combate(pokemon_enemigo, pokemon_entrenador)

        # Muestra el menu indefinidamente hasta que termine la batalla
        while True:
            print("Menu")
            print("1. Luchar")
            print("2. Huir")
            opcion = int(input("Selecciona una opcion (1 o 2):\n"))

            if opcion == 1:
                while True:
                    print("\nMovimientos:")

                    contador = 0

                    for i in range(4):
                        if pokemon_entrenador[f'movimiento_{i+1}'] != "":
                            print(f"{i+1}. {pokemon_entrenador[f'movimiento_{i+1}']}")
                            contador += 1

                        else:
                            break

                    opcion1 = int(input(f"Seleccione el movimiento (1 al {contador}):\n"))

                    if opcion1 >= 1 and opcion1 <= contador:
                        break

                break

            elif opcion == 2:
                fuga = huir_combate(pokemon_entrenador['velocidad'], pokemon_enemigo['velocidad'])

                if generador_numero_random(0, 255) < fuga:
                    fuga_exitosa = True
                    print("Has escapado exitosamente")
                    break
                else:
                    print("No se a podido escapar")
                    fuga_exitosa = False

            else:
                print("No se a seleeciona una opcion")

        orden = prioriodad(pokemon_entrenador['velocidad'], pokemon_enemigo['velocidad'])

        if orden == 1 and opcion == 1:
            turno(pokemon_entrenador, pokemon_enemigo, opcion1)

            if pokemon_enemigo['puntos_salud'] <= 0:
                print(f"El pokemon {pokemon_enemigo['nombre']} a sido debilitado.")
                pausar_temporalmente(1)
                experiencia_obtenida = int(experiencia_recibida(pokemon_enemigo['experiencia_base'], pokemon_enemigo['nivel']))
                mi_pokemon['experiencia_actual'] += experiencia_obtenida
                print(f"Gano {experiencia_obtenida} de experiencia.")
                pausar_temporalmente(1)
                break

            pausar_temporalmente(1)
            interfaz_combate(pokemon_enemigo, pokemon_entrenador)
            turno(pokemon_enemigo, pokemon_entrenador, generador_numero_random(1, 4))
            pausar_temporalmente(1)

            if pokemon_entrenador['puntos_salud'] <= 0:
                print(f"El pokemon {pokemon_entrenador['nombre']} a sido debilitado.")
                pausar_temporalmente(1)
                print("No recibes experiencia")
                pausar_temporalmente(1)
                break

        elif orden == 2 and opcion == 1:
            turno(pokemon_enemigo, pokemon_entrenador, generador_numero_random(1, 4))

            if pokemon_entrenador['puntos_salud'] <= 0:
                print(f"El pokemon {pokemon_entrenador['nombre']} a sido debilitado.")
                pausar_temporalmente(1)
                print("No recibes experiencia")
                pausar_temporalmente(1)
                break

            pausar_temporalmente(1)
            interfaz_combate(pokemon_enemigo, pokemon_entrenador)
            turno(pokemon_entrenador, pokemon_enemigo, opcion1)
            pausar_temporalmente(1)

            if pokemon_enemigo['puntos_salud'] <= 0:
                print(f"El pokemon {pokemon_enemigo['nombre']} a sido debilitado.")
                pausar_temporalmente(1)
                experiencia_obtenida = int(experiencia_recibida(pokemon_enemigo['experiencia_base'], pokemon_enemigo['nivel']))
                mi_pokemon['experiencia_actual'] += experiencia_obtenida
                pausar_temporalmente(1)
                print(f"Gano {experiencia_obtenida} de experiencia.")
                pausar_temporalmente(1)
                break

        elif opcion == 2 and fuga_exitosa == True:
            break

    print("Fin de la batalla")

    subida_nivel()

    pausar_temporalmente(1)


def estadistica():
    print("Dato             | Descripción")
    print("------------------------------")
    print(f"Nombre           | {mi_pokemon['nombre']}")
    print(f"Apodo            | {mi_pokemon['apodo']}")
    print(f"Nivel            | {mi_pokemon['nivel']}")
    print(f"Experiencia      | {mi_pokemon['experiencia_actual']}/{mi_pokemon['experiencia_total']}")
    print(f"Tipo             | {mi_pokemon['tipo']}")
    print("------------------------------")

    for i in range(1, 5):
        if mi_pokemon[f'movimiento_{i}'] != "":
            print(f"Movimiento {i}:")
            print(f"Nombre           | {mi_pokemon[f'movimiento_{i}']}")
            print(f"Tipo             | {mi_pokemon[f'movimiento_tipo_{i}']}")
            print(f"Potencia         | {mi_pokemon[f'potencia_{i}']}")
            print(f"Precisión        | {mi_pokemon[f'precision_{i}']}")
            print("******************************")
        else:
            break

    print("------------------------------")
    print("Datos de comabte ")
    print("------------------------------")
    print(f"Puntos de salud  | {mi_pokemon['puntos_salud']}")
    print(f"Ataque           | {mi_pokemon['ataque']}")
    print(f"Defensa          | {mi_pokemon['defensa']}")
    print(f"Velocidad        | {mi_pokemon['velocidad']}")
    print("------------------------------")


def menu_principal():
    while True:
        print("          Menu Pokémon")
        print("a. Batalla contra Pokémon salvaje")
        print("b. Ver estadísticas de mi pokémon")
        print("c. Salir del videojuego")
        opcion = input("Seleccione la opcion (a al c):\n")

        if opcion == 'a':
            batalla()
        elif opcion == 'b':
            estadistica()
        elif opcion == 'c':
            break
        else:
            print("No se a seleccionado las opciones del menu.")


def main():
    seleccion_pokemon_inicial()
    menu_principal()


main()
