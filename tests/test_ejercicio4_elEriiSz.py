################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Estos son los test correspondienets al archivo `ejercicio4.py` que esta en
`src`
"""

import pytest

from src.ejercicio4 import suma_lenta

def test_pos():
    numero = 3
    numero2 = 5
    resultado = suma_lenta(numero, numero2)
    assert isinstance(resultado, int), "el resultado debe ser un número entero"
    assert resultado == 8, "el resultado para los valores 3 y 5, debe ser 8"


def test_neg():
    numero = 3
    numero2 = -5
    resultado = suma_lenta(numero, numero2)
    assert isinstance(resultado, int), "el resultado debe ser un número entero"
    assert resultado == -2, "el resultado para los valores 3 y -5, debe ser -2"

