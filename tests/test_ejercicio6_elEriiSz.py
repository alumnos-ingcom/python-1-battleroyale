################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Estos son los test correspondienets al archivo `ejercicio6.py` que esta en
`src`
"""

import pytest

from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor

def test_me_ma():
    numero = 10
    numero2 = 5
    numero3 = 20
    menor, medio, mayor = ordenar_menor_a_mayor(numero, numero2, numero3)
    assert isinstance(menor, int), "el resultado debe ser un número entero"
    assert isinstance(medio, int), "el resultado debe ser un número entero"
    assert isinstance(mayor, int), "el resultado debe ser un número entero"
    assert menor == 5, "el resultado menor para los valores 10, 5 y 20, debe ser 5"
    assert medio == 10, "el resultado medio para los valores 10, 5 y 20 sebe ser 10"
    assert mayor == 20, "el resultado mayor para los valores 10, 5 y 20 deber ser 20"


def test_ma_me():
    numero = 10
    numero2 = 5
    numero3 = 20
    mayor, medio, menor = ordenar_mayor_a_menor(numero, numero2, numero3)
    assert isinstance(menor, int), "el resultado debe ser un número entero"
    assert isinstance(medio, int), "el resultado debe ser un número entero"
    assert isinstance(mayor, int), "el resultado debe ser un número entero"
    assert menor == 5, "el resultado menor para los valores 10, 5 y 20, debe ser 5"
    assert medio == 10, "el resultado medio para los valores 10, 5 y 20 sebe ser 10"
    assert mayor == 20, "el resultado mayor para los valores 10, 5 y 20 deber ser 20"


def test_ma_me_neg():
    numero = -10
    numero2 = 5
    numero3 = 20
    mayor, medio, menor = ordenar_mayor_a_menor(numero, numero2, numero3)
    assert isinstance(menor, int), "el resultado debe ser un número entero"
    assert isinstance(medio, int), "el resultado debe ser un número entero"
    assert isinstance(mayor, int), "el resultado debe ser un número entero"
    assert menor == -10, "el resultado menor para los valores -10, 5 y 20, debe ser -10"
    assert medio == 5, "el resultado medio para los valores -10, 5 y 20 sebe ser 5"
    assert mayor == 20, "el resultado mayor para los valores -10, 5 y 20 deber ser 20"


def test_me_ma_neg():
    numero = -10
    numero2 = 5
    numero3 = 20
    menor, medio, mayor = ordenar_menor_a_mayor(numero, numero2, numero3)
    assert isinstance(menor, int), "el resultado debe ser un número entero"
    assert isinstance(medio, int), "el resultado debe ser un número entero"
    assert isinstance(mayor, int), "el resultado debe ser un número entero"
    assert menor == -10, "el resultado menor para los valores -10, 5 y 20, debe ser -10"
    assert medio == 5, "el resultado medio para los valores -10, 5 y 20 sebe ser 5"
    assert mayor == 20, "el resultado mayor para los valores -10,ayor_a_menorr ser 20"
