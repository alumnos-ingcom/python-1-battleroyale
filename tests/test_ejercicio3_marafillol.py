################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""TEST EJERCICIO 3
"""
from src.ejercicio3 import compara
def test_comparar_si_el_primero_es_menor():
    """Esta función verifica si la función compara funciona correctamente.
    """
    numero = 2
    otro_numero = 3
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == -1, "No se obtiene el resultado esperado."
def test_comparar_si_el_primero_es_mayor():
    """Esta función verifica si la función compara funciona correctamente.
    """
    numero = 1
    otro_numero = -1
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == 1, "No se obtiene el resultado esperado."
def test_comparar_si_el_primero_es_igual():
    """Esta función verifica si la función compara funciona correctamente.
    """
    numero = 6
    otro_numero = 6
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == 0, "No se obtiene el resultado esperado."
def test_comparar_si_el_primero_es_decimal_y_mayor():
    """Esta función verifica si la función compara funciona correctamente.
    """
    numero = 5.5
    otro_numero = 2
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == 1, "No se obtiene el resultado esperado."
def test_comparar_si_el_primero_es_decimal_y_menor():
    """Esta función verifica si la función compara funciona correctamente.
    """
    numero = -10.8
    otro_numero = -5
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == -1, "No se obtiene el resultado esperado."
def test_comparar_si_el_primero_es_decimal_y_igual():
    """Esta función verifica si la función compara funciona correctamente.
    """
    numero = 4.3
    otro_numero = 4.3
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == 0, "No se obtiene el resultado esperado."
    