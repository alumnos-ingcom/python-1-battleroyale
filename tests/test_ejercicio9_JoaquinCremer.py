################
# Joaquín Cremer - @JoaquinCremer
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
    Estos son los test del ejercicio 9
"""
import pytest
from src.ejercicio9 import factores_primos


def test_factores_primos():
    """
       En este test se prueba el caso de cuando el numero ingresado es un numero entero positivo

    """
    numero = 24
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla"
    assert resultado == (2, 2, 2, 3), "El resultado no es el esperado"
    pass

