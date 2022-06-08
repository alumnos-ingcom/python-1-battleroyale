################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Estos son los test correspondienets al archivo `ejercicio1.py` que esta en
`src`
"""

import pytest

from src.ejercicio1 import convertir_a_fahrrenheit, convertir_a_centigrados

def test_f_c():
    numero = 32
    resultado = convertir_a_centigrados(numero)
    assert isinstance(resultado, (int, float)), "el resultado debe ser un número"
    assert resultado == 0, "el resultado para el valor 0, debe ser 0"


def test_c_f():
    numero = 0
    resultado = convertir_a_fahrrenheit(numero)
    assert isinstance(resultado, (int, float)), "el resultado debe ser un número"
    assert resultado == 32, "el resultado para el valor 0, debe ser 0"

