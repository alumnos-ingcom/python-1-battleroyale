################
# Valentin Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio11 import es_multiplo
"""Test para comprobar si un número es
    multiplo de otro"""

def test_es_multiplo():
    """Test con un multiplo del número"""
    numero = 2
    multiplo = 52
    resultado = es_multiplo(numero, multiplo)
    assert isinstance (resultado, int), "El resultado debe ser un entero"
    assert resultado is True

def test_es_multiplo_no():
    """Test con un número no multiplo
    de otro"""
    numero = 5
    multiplo = 52
    resultado = es_multiplo(numero, multiplo)
    assert isinstance (resultado, int), "El resultado debe ser un entero"
    assert resultado is False
