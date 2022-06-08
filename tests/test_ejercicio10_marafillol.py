################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""TEST EJERCICIO 10
"""
from src.ejercicio10 import es_palindromo
def test_es_palindromo_si_es_true():
    """Esta función verifica si es_palindromo funciona correctamente.
    """
    texto = "solos"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_palindromo_si_es_false():
    """Esta función verifica si es_palindromo funciona correctamente.
    """
    texto = "mara"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_es_palindromo_si_son_letras_iguales():
    """Esta función verifica si es_palindromo funciona correctamente.
    """
    texto = "zzz"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_palindromo_si_esta_en_minuscula_true():
    """Esta función verifica si es_palindromo funciona correctamente.
    """
    texto = "neuquen"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_palindromo_si_esta_en_mayuscula_true():
    """Esta función verifica si es_palindromo funciona correctamente.
    """
    texto= "NEUQUEN"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_palindromo_primera_letra_en_mayuscula_true():
    """Esta función verifica si es_palindromo funciona correctamente.
    """
    texto = "Neuquen"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_palindromo_si_esta_en_mayus_y_minus_true():
    """Esta función verifica si es_palindromo funciona correctamente.
    """
    texto = "NarrAN"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
    