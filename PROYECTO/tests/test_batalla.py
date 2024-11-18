from src.personajes import crear_personaje, atacar, usar_pocion

def test_crear_personaje():
    personaje = crear_personaje("Guerrero", 120, 25, 10, 2)
    assert personaje['nombre'] == "Guerrero"
    assert personaje['hp'] == 120
    assert personaje['ataque'] == 25
    assert personaje['defensa'] == 10
    assert personaje['pociones'] == 2

def test_atacar():
    p1 = crear_personaje("Guerrero", 100, 20, 5, 2)
    p2 = crear_personaje("Mago", 100, 15, 3, 3)
    atacar(p1, p2)
    assert p2['hp'] < 100  # la vida del mago debe haber disminuido

def test_usar_pocion():
    p1 = crear_personaje("Guerrero", 50, 20, 5, 1)
    usar_pocion(p1)
    assert p1['hp'] > 50  # la vida del guerrero debe haber aumentado
    assert p1['pociones'] == 0  # la pocion debe haberse consumido
