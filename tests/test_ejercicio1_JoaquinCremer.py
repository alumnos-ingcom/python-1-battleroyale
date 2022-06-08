################
# Joaquin Cremer - @Joaquín Cremer
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test de las funciones del ejercicio 1.
"""
import pytest
from src.ejercicio1 import convertir_a_fahrenheit, convertir_a_centigrados


def test_convertir_a_fahrenheit():
    """
       Una breve descripción del caso de prueba aplicado a la función
    """
    centigrados = 5
    resultado = convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser un numero"
    assert resultado == 41, "No se obtiene el resultado esperado"
    pass

def test_convertir_a_centigrados():
    fahrenheit = 5
    resultado = convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser un numero"
    assert resultado == -15, "No se obtiene el resultado esperado"
    pass