################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio1 import centigrados_a_fahrenheit, fahrenheit_a_centigrados

"""
En este test se va a probar la funcionalidad del programa de conversion centigrados-fahrenheit.
"""


def test_centigrados_a_fahrenheit_positivo():
    """
    Esta función prueba los valores de entrada positivos y corrobora que los datos de salida sean los apropiados
    """
    centigrados = 20
    resultado = centigrados_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser tipo float"
    assert resultado == 68.0, "El resultado no es lo esperado"
    
def test_centigrados_a_fahrenheit_negativo():
    """
    Esta función prueba los valores de entrada negativos y corrobora que los datos de salida sean los apropiados
    """
    centigrados = -20
    resultado = centigrados_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser tipo float"
    assert resultado == -4.0, "El resultado no es lo esperado"
    
def test_fahrenheit_a_centigrados_positivo():
    """
    Esta función prueba los valores de entrada positivos y corrobora que los datos de salida sean los apropiados
    """
    fahrenheit = 50
    resultado = fahrenheit_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser tipo float"
    assert resultado == 10.0, "El resultado no es lo esperado"

def test_fahrenheit_a_centigrados_negativo():
    """
     Esta función prueba los valores de entrada negativos y corrobora que los datos de salida sean los apropiados
    """
    fahrenheit = -50
    resultado = fahrenheit_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser tipo float"
    assert resultado == -45.55555555555556, "El resultado no es lo esperado"