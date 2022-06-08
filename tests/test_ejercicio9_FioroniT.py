################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio9 import factores_primos
"""
En este test se debe encontrar los factores primos del número indicado
"""
def test_factores_primos():
    numero = 60
    resultado = factores_primos(numero)
    assert isinstance(numero, int), "El valor de entrada debe ser un entero"
    assert isinstance(resultado, tuple), "El valor de salida debe ser una tupla"
    assert resultado == (2, 2, 3, 5), "El valor de salida no es el esperado"
    assert numero >= 0, "El valor de entrada debe ser positivo"
    