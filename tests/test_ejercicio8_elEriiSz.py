################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Estos son los test correspondienets al archivo `ejercicio2.py` que esta en
`src`
"""

import pytest

from src.ejercicio8 import es_primo

def test_true():
    numero = 11
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "el resultado debe ser un valor booleano"
    assert resultado == True, "el resultado para el valor 11, debe ser True"


def test_false():
    numero = 10
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "el resultado debe ser un valor booleano"
    assert resultado == False, "el resultado para el valor 10, debe ser False"

