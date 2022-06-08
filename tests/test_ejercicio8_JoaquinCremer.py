################
# Joaquín Cremer - @JoaquinCremer
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los tests del ejercicio 8
"""
import pytest
from src.ejercicio8 import es_primo


def test_es_primo_true():
    """
       Este test demuestra el caso en el que el numero ingresado si es primo.
    """
    numero = 7
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado tiene que ser booleano"
    assert resultado == True, "El resultado no es el esperado"
    pass
def test_es_primo_false():
    """
        Este test demuestra el caso en el que el numero ingresado no es primo
    """
    numero = 4
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado tiene que ser booleano"
    assert resultado == False, "El resultado no es el esperado"
    pass

