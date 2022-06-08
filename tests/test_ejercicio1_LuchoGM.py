################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest
from src.ejercicio1 import convertir_a_fahrrenheit, convertir_a_centigrados
"""
Se estan probando ambas funciones tanto con valores positivos
o valores negativos
"""

def test_convertir_a_fahrrenheit_positivos():
    """
    Testear numeros positivos
    """
    centigrados = 10000
    en_funcion = convertir_a_fahrrenheit(centigrados)
    assert isinstance(en_funcion, float), "Deberia de ser un numero flotante"
    assert en_funcion >= 0, "Deberia de ser un numero positivo"
    
def test_convertir_a_fahrrenheit_negativos():
    """
    Testear numero negativos
    """
    centigrados = -18
    en_funcion = convertir_a_fahrrenheit(centigrados)
    assert isinstance(en_funcion, float), "Deberia de ser un numero flotante"
    assert en_funcion <= 0, "Deberia de ser un numero negativo"
    assert centigrados <= -17.7778, "Para que de un numero negativo se necesita que se menor que -17.7778"

def test_convertir_a_centigrados_positivos():
    """
    Testear con numero positivos
    """
    fahrenheit = 32
    en_funcion = convertir_a_centigrados(fahrenheit)
    assert isinstance(en_funcion, float), "Deberia de ser un numero flotante"
    assert fahrenheit >= 32, "Para que sea positivo se espera un numero mayor que 32"
    assert en_funcion >= 0, "Deberia de ser un numero positivo"

def test_convertir_a_centigrados_negativos():
    """
    Testear con numero negativos
    """
    fahrenheit = 31
    en_funcion = convertir_a_centigrados(fahrenheit)
    assert isinstance(en_funcion, float), "Deberia de ser un numero flotante"
    assert fahrenheit < 32, "Para que sea positivo se espera un numero menor que 32"
    assert en_funcion <= 0, "Deberia de ser un numero negativo"