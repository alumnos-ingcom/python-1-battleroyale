################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Estos son los test correspondienets al archivo `ejercicio2.py` que esta en
`src`
"""

import pytest

from src.ejercicio11 import es_multiplo

def test_true():
    numero = 10
    numero2 = 5
    resultado = es_multiplo(numero, numero2)
    assert isinstance(resultado, bool), "el resultado debe ser un valor booleano"
    assert resultado == True, "el resultado para el valor 10 y 5, debe ser True"


def test_false():
    numero = 11
    numero2 = 5
    resultado = es_multiplo(numero, numero2)
    assert isinstance(resultado, bool), "el resultado debe ser un valor booleano"
    assert resultado == False, "el resultado para el valor 11 y 5, debe ser False"

