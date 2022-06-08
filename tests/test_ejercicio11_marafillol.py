################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""TEST EJERCICIO 11
"""
from src.ejercicio11 import es_multiplo
def test_es_multiplo_ambos_positivos_true():
    """Esta función verifica si es_multiplo funciona correctamente.
    """
    numero = 2
    multiplo = 4
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_multiplo_ambos_positivos_false():
    """Esta función verifica si es_multiplo funciona correctamente.
    """
    numero = 6
    multiplo = 37
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_es_multiplo_ambos_negativos():
    """Esta función verifica si es_multiplo funciona correctamente.
    """
    numero = -4
    multiplo = -8
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, str), "El resultado debe ser un string."
def test_es_multiplo_ambos_iguales():
    """Esta función evalúa si es_multiplo funciona correctamente.
    """
    numero = 3
    multiplo = 3
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_multiplo_ambos_uno():
    """Esta función evalúa si es_multiplo funciona correctamente.
    """
    numero = 1
    multiplo = 1
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_multiplo_ambos_cero():
    """Esta función evalúa si es_multiplo funciona correctamente.
    """
    numero = 0
    multiplo = 0
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, str), "El resultado debe ser un string."
