################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from src.ejercicio8 import es_primo

"""
Se testea la funcion es_primo y verifica que este sea
positivo, mayor que uno y que sea un numero primo
"""

def test_es_primo():
    """
    Se testea que el numero sea primo y cumpla con las caracteristicas de uno
    """
    numero = 3
    resultado = es_primo(numero)
    assert isinstance(numero, int), "El numero ingresado debe de ser entero"
    assert numero >= 1, "El primer numero primo es el dos"
    assert numero > 0, "El numero debe de ser positivo"
    assert resultado == True, "El numero ingresado no es primo"
    