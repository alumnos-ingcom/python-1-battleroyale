################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal

"""
Se prueban las dos funciones
"""

def test_sexadecimal_a_decimal():
    """
    Se prueba la funcion sexadecimal_a_decimal y se verifica
    que los valores no se pasen de 60
    """
    horas = 50
    minutos = 25 
    segundos = 10
    resultado = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(horas, int), "Debe de ser un numero entero"
    assert isinstance(minutos, int), "Debe de ser un numero entero"
    assert isinstance(segundos, int), "Debe de ser un numero entero"
    assert isinstance(resultado, float), "El resultado debe de ser un numero flotante"
    assert horas <= 60 and minutos <= 60 and segundos <= 60, "Las horas, minutos y segundos no son mayores a 60 °"

def test_decimal_a_sexadecimal():
    """
    Se prueba la funcion decimal_a_sexadecimal y se verifica
    que de el resultado que debe dar
    """
    numero = 50.419444444444444
    resultado = decimal_a_sexadecimal(numero)
    assert isinstance(numero, float), "Debe de ser un numero flotante"
    assert resultado == (50, 25, 10)