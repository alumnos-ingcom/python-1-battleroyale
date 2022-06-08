################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Estos son los test correspondienets al archivo `ejercicio9.py` que esta en
`src`
"""

import pytest

from src.ejercicio9 import factores_primos

def test_funciona():
    decimal = 40
    resultado = factores_primos(decimal)
    assert isinstance(resultado, tuple), "el resultado debe ser un tuple"
    assert resultado[0] == 5, "el resultado para 40 debe ser 2 y 5"
    assert resultado[-1] == 2, "el resultado para 40 debe ser 2 y 5"

def test_mas_de_uno():
    decimal = 40
    resultado = factores_primos(decimal)
    assert isinstance(resultado, tuple), "el resultado debe ser un tuple"
    assert len(resultado) > 1, "el resultado para 40 debe tener 2 o mas factores"

