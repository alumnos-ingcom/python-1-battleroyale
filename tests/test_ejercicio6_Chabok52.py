################
# Valentin Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor
"""Test con orden de numeros de mayor a menor"""

def test_ordenar_mayor_a_menor():
    """Test orden de numeros de mayor
    a menor"""
    uno = 52
    dos = -52
    tres = 5
    orden = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance (orden, tuple), "El orden debe estár representado en una tupla"
    assert orden == (52, 5, -52)

def test_ordenar_menor_a_mayor():
    """Test ordenar numeros de
    menor a mayor"""
    uno = 52
    dos = -52
    tres = 5
    orden = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance (orden, tuple), "El orden debe estár representado en una tupla"
    assert orden == (-52, 5, 52)
