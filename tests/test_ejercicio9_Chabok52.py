################
# Valentin Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio9 import factores_primos
"""Test con diferentes numeros, primos y
    no primos"""

def test_factores_primos():
    """Test con un número no primo"""
    numero = 52
    resultado = factores_primos(numero)
    assert isinstance (resultado, tuple), "El resultado debe estár en una tupla"
    assert resultado == (2, 2, 13)

def test_factores_primos_primos():
    """Test con un número primo"""
    numero = 5
    resultado = factores_primos(numero)
    assert isinstance (resultado, tuple), "El resultado debe estár en una tupla"
    assert resultado == (5,)
