################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Estos son los test correspondienets al archivo `ejercicio3.py` que esta en
`src`
"""

import pytest

from src.ejercicio3 import compara

def test_menor():
    numero = 10
    numero2 = 11
    resultado = compara(numero, numero2)
    assert isinstance(resultado, (int, float)), "el resultado debe ser un número entero"
    assert resultado == -1, "el resultado para valores diferentes, debe ser 1 o -1"


def test_igual():
    numero = 1
    numero2 = 1
    resultado = compara(numero, numero2)
    assert isinstance(resultado, (int, float)), "el resultado debe ser un número entero"
    assert resultado == 0, "el resultado para valores iguales, debe ser 0"


def test_mayor():
    numero = 11
    numero2 = 10
    resultado = compara(numero, numero2)
    assert isinstance(resultado, (int, float)), "el resultado debe ser un número entero"
    assert resultado == 1, "el resultado para valores distintos, debe ser 1 o -1"


def test_menor_neg():
    numero = -11
    numero2 = -10
    resultado = compara(numero, numero2)
    assert isinstance(resultado, (int, float)), "el resultado debe ser un número entero"
    assert resultado == -1, "el resultado para valores diferentes, debe ser 1 o -1"


def test_mayor_neg():
    numero = -10
    numero2 = -11
    resultado = compara(numero, numero2)
    assert isinstance(resultado, (int, float)), "el resultado debe ser un número entero"
    assert resultado == 1, "el resultado para valores distintos, debe ser 1 o -1"
