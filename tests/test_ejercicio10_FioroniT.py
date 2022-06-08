################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio10 import es_palindromo
"""
Esta función debe indicar si la palabra ingresada cumple las condiciones para ser un palíndromo
"""
def test_es_palindromo_true():
    texto = "Neuquen"
    resultado = es_palindromo(texto)
    assert isinstance(texto, str), "La palabra indicada debe ser de tipo string"
    assert isinstance(resultado, bool), "La salida debe retornar un valor booleano"
    resultado == True, "Si la palabra es un palíndromo el valor retornado es True"
def test_es_palindromo_false():
    texto = "Rio_Negro"
    resultado = es_palindromo(texto)
    assert isinstance(texto, str), "La palabra indicada debe ser de tipo string"
    assert isinstance(resultado, bool), "La salida debe retornar un valor booleano"
    resultado == False, "Si la palabra no es un palíndromo el valor retornado es False"