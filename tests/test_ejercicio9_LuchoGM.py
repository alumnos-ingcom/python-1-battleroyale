################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from src.ejercicio9 import factores_primos

"""
Se prueba lo que la salida sea la deseada y que el numero sea positivo entero
"""

def test_factores_primos():
    """
    Se testea la funcion verificando que el resultado sea una tupla
    """
    numero = 4
    resultado = factores_primos(numero)
    assert isinstance (numero, int), "El numero deberia de ser entero"
    assert numero > 0, "El numero deberia de ser positivo"
    assert isinstance (resultado, tuple), "El resultado deberia de ser una tupla"
    