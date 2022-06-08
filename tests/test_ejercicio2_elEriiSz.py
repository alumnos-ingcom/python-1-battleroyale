################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Estos son los test correspondienets al archivo `ejercicio2.py` que esta en
`src`
"""

import pytest

from src.ejercicio2 import signo

def test_signo_positivo():
    numero = 10
    resultado = signo(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número entero"
    assert resultado == 1, "el resultado para el valor 0, debe ser 0"


def test_signo_cero():
    numero = 0
    resultado = signo(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número entero"
    assert resultado == 0, "el resultado para el valor 0, debe ser 0"


def test_signo_negativo():
    numero = -10
    resultado = signo(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número entero"
    assert resultado == -1, "el resultado para el valor 0, debe ser 0"
