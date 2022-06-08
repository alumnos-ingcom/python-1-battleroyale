################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from src.ejercicio2 import signo

"""
Se prueba la funcion con cada valor que sea posible
"""

def test_signo_positivo():
    valor = 1
    resultado = signo(valor)
    assert isinstance( valor, int), "El numero deberia de ser entero"
    assert valor > 0, "El numero debe de ser positivo"

def test_signo_negativo():
    valor = -1
    resultado = signo(valor)
    assert isinstance( valor, int), "El numero deberia de ser entero"
    assert valor < 0, "El numero debe de ser negativo"

def test_signo_cero():
    valor = 0
    resultado = signo(valor)
    assert isinstance(valor, int), "El numero deberia de ser entero"
    assert valor == 0, "El numero debe de ser cero"
