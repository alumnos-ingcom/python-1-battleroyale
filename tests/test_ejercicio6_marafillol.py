################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""TEST EJERCICIO 6
"""
from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor
def test_ordenar_mayor_a_menor_tres_numeros_positivos():
    """Esta función verifica si ordenar_mayor_a_menor funciona correctamente.
    """
    uno = 3
    dos = 2
    tres = 5
    resultado = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (5, 3, 2), "No se obtiene el resultado esperado."
def test_ordenar_mayor_a_menor_tres_numeros_negativos():
    """Esta función verifica si ordenar_mayor_a_menor funciona correctamente.
    """
    uno = -1
    dos = -8
    tres = -4
    resultado = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (-1, -4, -8), "No se obtiene el resultado esperado."
def test_ordenar_mayor_a_menor_tres_ceros():
    """Esta función verifica si ordenar_mayor_a_menor funciona correctamente.
    """
    uno = 0
    dos = 0
    tres = 0
    resultado = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (0, 0, 0), "No se obtiene el resultado esperado."
def test_ordenar_menor_a_mayor_tres_ceros():
    """Esta función verifica si ordenar_menor_a_mayor funciona correctamente.
    """
    uno = 0
    dos = 0
    tres = 0
    resultado = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (0, 0, 0), "No se obtiene el resultado esperado."
def test_ordenar_menor_a_mayor_tres_numeros_positivos():
    """Esta función verifica si ordenar_menor_a_mayor funciona correctamente.
    """
    uno = 6
    dos = 9
    tres = 3
    resultado = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (3, 6, 9), "No se obtiene el resultado esperado."
def test_ordenar_menor_a_mayor_tres_numeros_negativos():
    """Esta función verifica si ordenar_menor_a_mayor funciona correctamente.
    """
    uno = -5
    dos = -8
    tres = -3
    resultado = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (-8, -5, -3), "No se obtiene el resultado esperado."
