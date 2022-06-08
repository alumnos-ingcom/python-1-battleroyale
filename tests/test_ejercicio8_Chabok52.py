################
# Valentin Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio8 import es_primo
"""Test con números primos y no primos"""

def test_es_primo():
    """Test con un número primo"""
    numero = 5
    primo = es_primo(numero)
    assert primo is True, "El número es primo"

def test_es_primo_no():
    """Test con un número no primo"""
    numero = 52
    primo = es_primo(numero)
    assert primo is False, "El número no es primo"
