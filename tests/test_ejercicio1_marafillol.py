################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""TEST EJERCICIO 1
"""
from src.ejercicio1 import convertir_a_fahrenheit, convertir_a_centigrados
def test_convertir_a_fahrenheit_cero():
    """Esta función verifica si convertir_a_fahrenheit funciona correctamente.
    """
    centigrados = 0.0
    resultado = convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser un número decimal."
    assert resultado == 32.0, "No se obtiene el resultado esperado."
def test_convertir_a_fahrenheit_negativo_a_positivo():
    """Esta función verifica si convertir_a_fahrenheit funciona correctamente.
    """
    centigrados = -4.0
    resultado = convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser un número decimal."
    assert resultado == 24.8, "No se obtiene el resultado esperado."
def test_convertir_a_centigrados_cero():
    """Esta función verifica si convertir_a_centigrados funciona correctamente.
    """
    fahrenheit = 0.0
    resultado = convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser un número decimal."
    assert resultado == -17.77777777777778, "No se obtiene el resultado esperado."
def test_convertir_a_centigrados_iguales():
    """Esta función verifica si convertir_a_fahrenheit funciona correctamente.
    """
    centigrados = -40.0
    resultado = convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser un número decimal."
    assert resultado == -40.0, "No se obtiene el resultado esperado."
def test_convertir_a_fahrenheit_iguales():
    """Esta función verifica si convertir_a_fahrenheit funciona correctamente.
    """
    centigrados = -40.0
    resultado = convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser un número decimal."
    assert resultado == -40.0, "No se obtiene el resultado esperado."
    