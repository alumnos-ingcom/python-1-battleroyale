################
# Joaquín Cremer - @JoaquinCremer
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
    Estos son los test para el ejercicio 10
"""
import pytest
from src.ejercicio10 import es_palindromo


def test_es_palindromo_true():
    """
       Este test prueba el caso en el que la palabra ingresada es palindromo
    """
    texto = "neuquen"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser booleano"
    assert resultado == True, "El resultado no es el esperado"
    pass

def test_es_palindromo_false():
    """
        Este test prueba el caso en el que la palabra ingresada no es palindromo
    """
    texto = "Hola"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser booleano"
    assert resultado == False, "El resultado no es el esperado"
    pass

