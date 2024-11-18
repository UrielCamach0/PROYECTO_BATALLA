import random
from src.personajes import atacar, usar_pocion, habilidad_especial

def simular_batalla(personaje1, personaje2):
    print("¡Comienza la batalla!\n")
    turno = 1
    while personaje1['hp'] > 0 and personaje2['hp'] > 0:
        print(f"--- Turno {turno} ---")

        # alternar turnos
        if turno % 2 != 0:
            turno_personaje(personaje1, personaje2)
        else:
            turno_personaje(personaje2, personaje1)

        turno += 1

    # determinar el ganador
    if personaje1['hp'] <= 0 and personaje2['hp'] <= 0:
        print("\n¡Es un empate! Ambos personajes han caido.")
    elif personaje1['hp'] <= 0:
        print(f"\n{personaje2['nombre']} ha ganado la batalla.")
    else:
        print(f"\n{personaje1['nombre']} ha ganado la batalla.")

def turno_personaje(atacante, defensor):
    accion = random.choice(["atacar", "pocion", "habilidad"])

    if accion == "atacar":
        atacar(atacante, defensor)
    elif accion == "pocion":
        usar_pocion(atacante)
    elif accion == "habilidad":
        habilidad_especial(atacante, defensor)
