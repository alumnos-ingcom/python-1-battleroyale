################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio8 import es_primo
"""
En este test se prueba la funcionalidad del programa para definir si un numero es primo
"""
def test_es_primo_true():
    numero = 7
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "La función debe retornar un valor booleano"
    assert resultado == True, "Para un numero primo debe retornar el valor True"
def test_es_primo_false():
    numero = 10
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "La función debe retornar un valor booleano"
    assert resultado == False, "Para un numero primo debe retornar el valor False"    