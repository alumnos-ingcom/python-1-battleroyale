################
# Joaquin Cremer - @JoaquinCremer
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los test del ejercicio 2.

"""
import pytest
from src.ejercicio2 import signo

def test_signo_positivo():
    numero = 2
    resultado = signo(numero)
    assert isinstance(resultado, str), "El resultado debe ser una string"
    assert resultado == "positivo", "El resultado no es el esperado"
    pass

def test_signo_negativo():
    numero = -2
    resultado = signo(numero)
    assert isinstance(resultado, str), "El resultado debe ser una string"
    assert resultado == "negativo", "El resultado no es el esperado"
    pass    
def test_signo_cero():
    numero = 0
    resultado = signo(numero)
    assert isinstance(resultado, str), "El resultado debe ser una string"
    assert resultado == "cero", "El resultado no es el esperado"
    pass
