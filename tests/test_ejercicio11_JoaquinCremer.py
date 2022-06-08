################
# Joaquín Cremer - @JoaquinCremer
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
    Estos son los test del ejercicio 11
"""
import pytest
from src.ejercicio11 import es_multiplo


def test_es_multiplo_true():
    """
       Este test prueba el caso en el que el segundo numero ingresado SI es multiplo del primero
    """
    numero = 5
    multiplo = 20
    resultado = es_multiplo(numero,multiplo)
    assert isinstance(resultado, bool), "El resultado tiene que ser booleano"
    assert resultado == True, "El resultado no es el esperado"
    pass

def test_es_multiplo_false():
    """
        Este test prueba el caso en el que el segundo numero NO es multiplo del primero
    """
    numero = 3
    multiplo = 10
    resultado = es_multiplo(numero,multiplo)
    assert isinstance(resultado, bool), "El resultado tiene que ser booleano"
    assert resultado == False, "El resultado no es el esperado"
    pass