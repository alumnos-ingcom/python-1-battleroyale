################
# Joaquín Cremer - @JoaquinCremer
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los tests del ejercicio 5
"""
import pytest
from src.ejercicio5 import division_lenta



def test_division_lenta():
    """
       Una breve descripción del caso de prueba aplicado a la función
    """
    dividendo = 10
    divisor = 5
    resultado_cociente, resultado_resto = division_lenta(dividendo, divisor)
    assert isinstance(resultado_cociente, int), "El cociente debe ser un numero entero"
    assert isinstance(resultado_resto, int), "El resto debe ser un numero entero"
    assert resultado_cociente == 2, "El resultado del cociente no es el esperado"
    assert resultado_resto == 0, "El resultado del resto no es el esperado"
    pass

