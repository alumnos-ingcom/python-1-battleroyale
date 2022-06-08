################
# Joaquin Cremer - @Joaquín Cremer
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los tests del ejercicio 3.

"""
import pytest
from src.ejercicio3 import compara


def test_compara_mayor():
    """
       En este test prueba cuando el primer numero es mayor al segundo numero
    """
    numero = 5
    otro_numero = 1
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == 1, "El resultado no es el esperado"
    pass
def test_compara_menor():
    """
        Este test prueba el caso en el que el segundo numero ingresado es mayor al primero
    """
    numero = 1
    otro_numero = 5
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == -1, "El resultado no es el esperado"
    pass
def test_compara_iguales():
    """
        Este test prueba el caso en el que los dos numero ingresados son iguales
    """
    numero = 2
    otro_numero = 2
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == 0, "El resultado no es el esperado"
    pass
