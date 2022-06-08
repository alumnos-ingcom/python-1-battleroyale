################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from src.ejercicio11 import es_multiplo

"""
Se prueba que la entrada y la salida sea la requerida
"""

def test_es_multiplo():
    """
    Se testea que la entrada y la salida sea la deseada
    """
    numero = 25
    multiplo = 5
    resultado = es_multiplo(numero, multiplo)
    modulo = numero % multiplo
    assert isinstance (numero, int), "El numero deberia de ser entero"
    assert isinstance (multiplo, int), "El multiplo deberia de ser entero"
    assert isinstance (resultado, bool), "El resultado deberia de ser un booleano"
    assert modulo == 0, "Para que sea multiplo el modulo debe de ser 0"
    