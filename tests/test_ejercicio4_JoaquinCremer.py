################
# Joaquín Cremer - @JoaquinCremer
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los tests del ejercicio 4

"""
import pytest
from src.ejercicio4 import suma_lenta


def test_suma_lenta_positivo():
    """
       Este test prueba el caso en el que el resultado de la suma de los dos numero es negativo
    """
    numero = 4
    otro_numero = 2
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado > 0, "El resultado debe ser un numero positivo"
    assert resultado == 6, "El resultado no es el esperado"
    pass

def test_suma_lenta_negativo():
    """
        Este test prueba el caso en el que el resultado es negativo
    """
    numero = 2
    otro_numero = -4
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado < 0, "El resultado debe ser un numero negativo"
    assert resultado == -2, "El resultado no es el esperado"
    pass
def test_suma_lenta_cero():
    """
        Este test prueba el caso en el que el resultado es 0
    """
    numero = 2
    otro_numero = -2
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == 0, "El resultado debe ser cero"
    
    pass
    