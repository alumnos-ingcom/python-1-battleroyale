################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio3 import compara

"""
En este test se va a probar la funcionalidad del programa de comparación de numeros
"""
def test_compara_numero_mayor():
    numero = 20
    otro_numero = -20
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un número de tipo entero"
    assert resultado == 1, "El resultado cuando numero > otro_numero debe ser 1"
def test_compara_numero_menor():
    numero = -20
    otro_numero = 20
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un número de tipo entero"
    assert resultado == -1, "El resultado cuando otro_numero > numero debe ser -1"
def test_compara_numero_iguales():
    numero = 20
    otro_numero = 20
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un número de tipo entero"
    assert resultado == 0, "El resultado cuando numero y otro_numero son iguales debe ser 0"
    