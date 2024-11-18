from src.personajes import crear_personaje
from src.simulador import simular_batalla

# creacion de personajes usando diccionarios
personaje1 = crear_personaje("Guerrero", hp=120, ataque=25, defensa=10, pociones=2)
personaje2 = crear_personaje("Mago", hp=90, ataque=30, defensa=5, pociones=3)

# iniciar la simulacion
simular_batalla(personaje1, personaje2)
