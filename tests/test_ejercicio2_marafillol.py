################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""TEST EJERCICIO 2
"""
from src.ejercicio2 import signo
def test_si_signo_es_cero():
    """Esta función verifica si la función signo funciona
    correctamente si número es neutro.
    """
    numero = 0
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == 0, "No se obtiene el resultado esperado."
def test_si_signo_es_positivo():
    """Esta función verifica si la función signo funciona
    correctamente si número es positivo.
    """
    numero = 4
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == 1, "No se obtiene el resultado esperado."
def test_si_signo_es_negativo():
    """Esta función verifica si la función signo funciona
    correctamente si número es negativo.
    """
    numero = -3
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == -1, "No se obtiene el resultado esperado."
def test_si_signo_es_decimal_y_negativo():
    """Esta función verifica si la función signo funciona
    correctamente si número es negativo y decimal.
    """
    numero = -1.7
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == -1, "No se obtiene el resultado esperado."
def test_si_signo_es_decimal_y_positivo():
    """Esta función verifica si la función signo funciona
    correctamente si número es positivo y decimal.
    """
    numero = 3.5
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == 1, "No se obtiene el resultado esperado."
    