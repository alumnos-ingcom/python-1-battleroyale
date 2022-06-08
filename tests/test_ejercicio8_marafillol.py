################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""TEST EJERCICIO 8
"""
from src.ejercicio8 import es_primo
def test_es_primo_siendo_positivo_no_primo():
    """Esta función evalúa si es_primo funciona correctamente.
    """
    numero = 6
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_es_primo_siendo_positivo_primo():
    """Esta función evalúa si es_primo funciona correctamente.
    """
    numero = 2
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_primo_siendo_negativo():
    """Esta función evalúa si es_primo funciona correctamente.
    """
    numero = -5
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_es_primo_siendo_uno():
    """Esta función evalúa si es_primo funciona correctamente.
    """
    numero = 1
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_es_primo_siendo_cero():
    """Esta función evalúa si es_primo funciona correctamente.
    """
    numero = 0
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
