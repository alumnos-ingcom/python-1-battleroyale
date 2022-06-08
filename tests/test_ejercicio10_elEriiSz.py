################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Estos son los test correspondienets al archivo `ejercicio2.py` que esta en
`src`
"""

import pytest

from src.ejercicio10 import es_palindromo

def test_true():
    cadena = "oso"
    resultado = es_palindromo(cadena)
    assert isinstance(resultado, bool), "el resultado debe ser un valor booleano"
    assert resultado == True, "el resultado para el valor 'oso', debe ser True"


def test_false():
    cadena = "Hola Mundo"
    resultado = es_palindromo(cadena)
    assert isinstance(resultado, bool), "el resultado debe ser un valor booleano"
    assert resultado == False, "el resultado para el valor 'Hola Mundo', debe ser True"

def test_mayus():
    cadena = "Neuquen"
    resultado = es_palindromo(cadena)
    assert isinstance(resultado, bool), "el resultado debe ser un valor booleano"
    assert resultado == True, "el resultado para el valor 'Neuquen', debe ser True"

