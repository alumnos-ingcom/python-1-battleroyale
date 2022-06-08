################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from src.ejercicio3 import compara

"""
Se testea las posobilidades de que el primer valor sea
mayor, menor o igual al segundo valor.
"""

def test_compara_mayor():
    """
    Prueba que el primer numero ingresado es el mayor
    """
    valor1 = 10
    valor2 = 5
    resultado = compara(valor1, valor2)
    assert isinstance(resultado, int), "Deberia de ser un numero entero"
    assert resultado == 1, "El primer valor deberia de ser mayor que el segundo"
    assert valor1 > valor2, "Para que retorne 1 se necesita que el primer valor sea el mayor"

def test_compara_iguales():
    """
    Prueba que los numeros son iguales
    """
    valor1 = 10
    valor2 = 10
    resultado = compara(valor1, valor2)
    assert isinstance(resultado, int), "Deberia de ser un numero entero"
    assert resultado == 0, "Los numeros deben de ser iguales"
    assert valor1 == valor2, "Para que retorne 0 se necesita que los valores sean iguales"

def test_compara_menor():
    """
    Prueba que el primer numero ingresasdo es menor que el primero
    """
    valor1 = 5
    valor2 = 10
    resultado = compara(valor1, valor2)
    assert isinstance(resultado, int), "Deberia de ser un numero entero"
    assert resultado == -1, "El primer valor deberia de ser menor que el segundo"
    assert valor1 < valor2, "Para que retorne -1 se necesita que el primer valor sea el menor"
