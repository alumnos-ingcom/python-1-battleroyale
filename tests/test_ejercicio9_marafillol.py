################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""TEST EJERCICIO 9
"""
from src.ejercicio9 import factores_primos
def test_factores_primos_positivo_un_digito():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero = 6
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (2, 3), "No se obtiene el resultado esperado."
def test_factores_primos_positivo_dos_digitos():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero = 15
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (3, 5), "No se obtiene el resultado esperado."
def test_factores_primos_positivo_tres_digitos():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero = 125
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (5, 5, 5), "No se obtiene el resultado esperado."
def test_factores_primos_es_uno():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero = 1
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (), "No se obtiene el resultado esperado."
def test_factores_primos_es_cero():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero = 0
    resultado=factores_primos(numero)
    assert isinstance(resultado, str), "El resultado debe ser un string."
def test_factores_primos_negativo():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero = -16
    resultado = factores_primos(numero)
    assert isinstance(resultado, str), "El resultado debe ser un string."
    