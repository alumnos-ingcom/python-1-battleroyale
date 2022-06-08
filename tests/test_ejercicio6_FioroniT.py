################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor 
"""
Estas funciones tienen como labor ordenar, de mayor a menor y menor a mayor, un conjunto de 3 números.
"""
def test_ordenar_mayor_a_menor():
    uno = 2
    dos = 4
    tres = 6
    resultado = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe estar en una tupla"
    assert resultado == ("6", "4", "2")
def test_ordenar_menor_a_mayor():
    uno = 2
    dos = 4
    tres = 6
    resultado = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe estar en una tupla"
    assert resultado == ("2", "4", "6")