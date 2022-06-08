################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor

"""
En ambas funciones se testea con los valores positivos y negativos
y que la entrada y la salida sea la requerida
"""

def test_ordenar_mayor_a_menor_positivo():
    """
    Se testea la funcion con numeros positivos
    """
    uno = 25
    dos = 50
    tres = 75
    resultado = ordenar_mayor_a_menor(uno,dos,tres)
    assert isinstance(uno, int), "Los numeros deben de ser enteros"
    assert isinstance(dos, int), "Los numeros deben de ser enteros"
    assert isinstance(tres, int), "Los numeros deben de ser enteros"
    assert resultado == (75, 50, 25), "No esta ordenado de mayor a menor"
    assert isinstance(resultado, tuple), "El resultado debe de ser una tupla"

def test_ordenar_mayor_a_menor_negativo():
    """
    Se testea la funcion con numeros negativos
    """
    uno = -25
    dos = -50
    tres = -75
    resultado = ordenar_mayor_a_menor(uno,dos,tres)
    assert isinstance(uno, int), "Los numeros deben de ser enteros"
    assert isinstance(dos, int), "Los numeros deben de ser enteros"
    assert isinstance(tres, int), "Los numeros deben de ser enteros"
    assert resultado == (-25, -50, -75), "No esta ordenado de mayor a menor"
    assert isinstance(resultado, tuple), "El resultado debe de ser una tupla"
    
def test_ordenar_menor_a_mayor_positivo():
    """
    Se testea la funcion con numeros positivos
    """
    uno = 25
    dos = 50
    tres = 75
    resultado = ordenar_menor_a_mayor(uno,dos,tres)
    assert isinstance(uno, int), "Los numeros deben de ser enteros"
    assert isinstance(dos, int), "Los numeros deben de ser enteros"
    assert isinstance(tres, int), "Los numeros deben de ser enteros"
    assert resultado == (25, 50, 75), "No esta ordenado de menor a mayor"
    assert isinstance(resultado, tuple), "El resultado debe de ser una tupla"

def test_ordenar_menor_a_mayor_negativo():
    """
    Se testea la funcion con numeros negativos
    """
    uno = -25
    dos = -50
    tres = -75
    resultado = ordenar_menor_a_mayor(uno,dos,tres)
    assert isinstance(uno, int), "Los numeros deben de ser enteros"
    assert isinstance(dos, int), "Los numeros deben de ser enteros"
    assert isinstance(tres, int), "Los numeros deben de ser enteros"
    assert resultado == (-75, -50, -25), "No esta ordenado de menor a mayor"
    assert isinstance(resultado, tuple), "El resultado debe de ser una tupla"
    