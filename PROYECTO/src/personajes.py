import random

def crear_personaje(nombre, hp, ataque, defensa, pociones):
    return {
        "nombre": nombre,
        "hp": hp,
        "ataque": ataque,
        "defensa": defensa,
        "pociones": pociones
    }

def atacar(atacante, defensor):
    critico = random.choice([False] * 3 + [True])  # 25% de probabilidad de critico
    fallo = random.choice([False] * 3 + [True])  # 25% de probabilidad de fallo

    if fallo:
        print(f"{atacante['nombre']} intenta atacar a {defensor['nombre']}, ¡pero falla!\n")
        return

    dano = random.randint(1, atacante['ataque'])

    if critico:
        dano *= 2
        print(f"¡Golpe critico de {atacante['nombre']}!")

    # para considerar la defensa del otro personaje
    dano = max(0, dano - defensor['defensa'])
    defensor['hp'] -= dano
    defensor['hp'] = max(0, defensor['hp'])  # para evitar hp negativo

    print(f"{atacante['nombre']} ataca a {defensor['nombre']} y causa {dano} puntos de dano.")
    print(f"{defensor['nombre']} ahora tiene {defensor['hp']} puntos de vida.\n")

def usar_pocion(personaje):
    if personaje['pociones'] > 0:
        curacion = random.randint(15, 30)
        personaje['hp'] += curacion
        personaje['pociones'] -= 1
        print(f"{personaje['nombre']} usa una pocion y recupera {curacion} puntos de vida.")
        print(f"{personaje['nombre']} ahora tiene {personaje['hp']} puntos de vida.\n")
    else:
        print(f"{personaje['nombre']} intenta usar una pocion, ¡pero ya no le quedan mas pociones!\n")

def habilidad_especial(atacante, defensor):
    dano = random.randint(atacante['ataque'], atacante['ataque'] * 2)
    defensor['hp'] -= dano
    defensor['hp'] = max(0, defensor['hp'])
    print(f"{atacante['nombre']} usa su habilidad especial y causa {dano} puntos de dano a {defensor['nombre']}.")
    print(f"{defensor['nombre']} ahora tiene {defensor['hp']} puntos de vida.\n")
