################
# Valentin Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio10 import es_palindromo
"""Test con palabras palíndromas y no
    palíndromas"""

def test_es_palindromo():
    """Test con una palabra palíndroma"""
    texto = "reconocer"
    palabra = es_palindromo(texto)
    assert palabra is True, "La palabra es palíndroma"

def test_es_palindromo_no():
    """Test con un una palabra normal"""
    texto = "Martin_me_aprobás_plis?"
    palabra = es_palindromo(texto)
    assert palabra is False, "Es una frase, por lo que no es palíndroma"
