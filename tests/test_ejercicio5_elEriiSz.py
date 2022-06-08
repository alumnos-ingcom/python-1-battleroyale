################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Estos son los test correspondienets al archivo `ejercicio5.py` que esta en
`src`
"""

import pytest

from src.ejercicio5 import division_lenta

def test_pos_dos():
    numero = 10
    numero2 = 5
    resultado, resto = division_lenta(numero, numero2)
    assert isinstance(resultado, int), "el resultado debe ser un número entero"
    assert resultado == 2, "el resultado para los valores 10 y 5, debe ser 2"
    assert resto == 0, "el resultado para los valores 10 y 5, sebe ser 0"


def test_neg_up():
    numero = -10
    numero2 = 5
    resultado, resto = division_lenta(numero, numero2)
    assert isinstance(resultado, int), "el resultado debe ser un número entero"
    assert resultado == -2, "el resultado para los valores -10 y 5, debe ser -2"
    assert resto == 0, "el resultado para los valores 10 y 5, sebe ser 0"


def test_neg_down():
    numero = 10
    numero2 = -5
    resultado, resto = division_lenta(numero, numero2)
    assert isinstance(resultado, int), "el resultado debe ser un número entero"
    assert resultado == -2, "el resultado para los valores 10 y -5, debe ser -2"
    assert resto == 0, "el resultado para los valores 10 y 5, sebe ser 0"


def test_neg_dos():
    numero = -10
    numero2 = -5
    resultado, resto = division_lenta(numero, numero2)
    assert isinstance(resultado, int), "el resultado debe ser un número entero"
    assert resultado == 2, "el resultado para los valores -10 y -5, debe ser 2"
    assert resto == 0, "el resultado para los valores 10 y 5, sebe ser 0"
