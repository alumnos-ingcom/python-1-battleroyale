################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from src.ejercicio10 import es_palindromo

"""
Se testea que los datos de entrada y salida sean los correctos
"""

def test_es_palindromo():
    """
    Se prueba que la entrada y la salida sean las correctas
    """
    texto = "neuquen"
    resultado = es_palindromo(texto)
    assert isinstance(texto, str),"Debe de ingresar una palabra"
    assert isinstance(resultado, bool), "El resultado deberia de ser un valor logico"