def test_suma():
    assert 2 + 2 == 4

def test_texto():
    nombre = "Michell"
    assert nombre.upper() == "MICHELL"

def test_lista():
    numeros = [1, 2, 3]
    assert len(numeros) == 3

def test_que_falla_a_proposito():
    assert 5 == 5 
